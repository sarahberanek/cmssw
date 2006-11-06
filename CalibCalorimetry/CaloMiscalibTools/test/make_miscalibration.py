#!/usr/bin/env python2
import commands,string,time,thread,random,math,sys

#global variables
MINRES=0.02
SEED=-1
ENDCAPSINGLE=0
NPOINT=3
eta=[]
eta_ev=[]
res=[]
#
eta.append((0.+0.261)/2)
eta.append((0.957+0.783)/2)
eta.append((1.479+1.305)/2)

# events/crystal/fb


def miscalibecal(lumi,endcap,z,etaindex,phiindex,randval):
    global MINRES,ENDCAPSINGLE,NPOINT
    if endcap:
        modindex=etaindex
        crysindex=phiindex
    #return a random factor according to  eta
    if lumi==0:
        if randval==1:
            return random.gauss(1,MINRES)
#            return 1.0
        else:
            return MINRES
    if endcap != 1:
        # from AN 
        #0.000 0.261         6.19 0.12
        #0.783 0.957        10.7 0.27
        #1.305 1.479        15.0 0.42
        # get eta from etaindex
        etacur=(etaindex-0.5)*0.0174
        eta_ev.append(300./5*lumi)   
        eta_ev.append(270./5*lumi)
        eta_ev.append(170./5*lumi) 
        res.append(math.sqrt(6.19**2/eta_ev[0]+0.12**2))
        res.append(math.sqrt(10.7**2/eta_ev[1]+0.27**2))
        res.append(math.sqrt(15**2/eta_ev[2]+0.42**2))
        # extrapolation
        
        for ieta in range(0,NPOINT):
            if eta[ieta]> etacur:
                break
        indexmin=ieta-1
        indexmax=ieta
        # in case there are no more points left
        if(indexmin<0):
            indexmin=indexmin+1
            indexmax=indexmax+1
        # now real extrapolation
        real_res=res[indexmin]+(etacur-eta[indexmin])*(res[indexmax]-res[indexmin])/(eta[indexmax]-eta[indexmin])
        real_res=real_res/100
        if real_res>MINRES:
            real_res=MINRES
        if randval==1:
            return random.gauss(1,real_res)
        else:
            return real_res
    if endcap:
        if ENDCAPSINGLE==0:
            # first time called, we have to derive it from last barrel
            ENDCAPSINGLE=miscalibecal(lumi,0,1,85,1,0)
        if randval==1:
            return random.gauss(1,ENDCAPSINGLE)
        else:
            return ENDCAPSINGLE

    
def miscalibhcal(lumi,det,etaindex,phiindex,depth,randval):
    global MINRES,NPOINT
    #return a random factor according to  eta
    if lumi==0:
        if randval==1:
            return random.gauss(1,MINRES)
#            return 1.0
        else:
            return MINRES
    



#main
if len(sys.argv)==1:
    print 'Usage: '+sys.argv[0]+' <ecalbarrel|ecalendcap|HCAL> <lumi> <filename> [MINRES=0.02] [SEED=random]'
    print '       put lumi=0 for precalibration values (random at MINRES)'
    sys.exit(1)

ecalbarrel=0
ecalendcap=0
hcal=0

if sys.argv[1]=='ecalbarrel':
    #endcap=0
    ecalbarrel=1
elif sys.argv[1]=='ecalendcap':
    #endcap=1
    ecalendcap=1
elif sys.argv[1]=='HCAL':
    hcal=1
else:
    print 'please specify one of <barrel|endcap|HCAL>'
    sys.exit(1)

#if ecalendcap==1:
#    ne_z=[]
#    ne_mod=[]
#    ne_xtal=[]
#    necells=0

if hcal==1:

# read valid hcal cells
    hcalcell=open('valid_hcalcells.txt','r')
    hcal_det=[]
    hcal_eta=[]
    hcal_phi=[]
    hcal_depth=[]
    hcalcells=0

    for line in hcalcell:
        hcalcells=hcalcells+1
        curr_list=line.split()
        hcal_det.append(string.atoi(curr_list[0]))
        hcal_eta.append(string.atoi(curr_list[1]))
        hcal_phi.append(string.atoi(curr_list[2]))
        hcal_depth.append(string.atoi(curr_list[3]))
    hcalcell.close()
    print 'Read ',hcalcells,' valid cells for hcal'


# read non existing cells file, not needed anymore
#    necell=open('non_existing_cell_endcap','r')

#    for line in necell:
#        necells=necells+1
#        curr_list=line.split()
#        ne_z.append(string.atoi(curr_list[0]))
#        ne_mod.append(string.atoi(curr_list[1]))
#        ne_xtal.append(string.atoi(curr_list[2]))
#    necell.close()
#    print 'Read ',necells,' non-existing cells for endcap'

    
lumi=string.atof(sys.argv[2])

if hcal==1:
    print 'lumi dependence not yet implemented for HCAL'

if lumi<0:
    print 'lumi = '+str(lumi)+' not valid'
    sys.exit(1)
    
fileout=sys.argv[3]

if len(sys.argv)>=5:
    MINRES=string.atof(sys.argv[4])

print 'Using minimal resolution: '+str(MINRES)

if len(sys.argv)>=6:
    SEED=string.atoi(sys.argv[5])
    print 'Using fixed seed for random generation: '+str(SEED)
    random.seed(SEED)
    
# now open file
xmlfile=open(fileout,'w')
# write header
xmlfile.write('<?xml version="1.0" ?>\n')
xmlfile.write('\n')
xmlfile.write('<CalibrationConstants>\n')
if ecalbarrel==1:
    xmlfile.write('  <EcalBarrel>\n')
elif ecalendcap==1:
    xmlfile.write('  <EcalEndcap>\n')
elif hcal==1:
    xmlfile.write('  <Hcal>\n')


count=0
if ecalbarrel==1 or ecalendcap==1:

    # define ranges
    mineta=1
    minphi=1
    if ecalbarrel==1:
        maxeta=85
        maxphi=360
    else:
        maxeta=100
        maxphi=100
    
    for zindex in (-1,1):
        for etaindex in range(mineta,maxeta+1):
            for phiindex in range(minphi,maxphi+1):
                miscal_fac=miscalibecal(lumi,ecalendcap,zindex,etaindex,phiindex,1)
                # create line:
                if ecalbarrel==1:
                    if zindex==-1:
                        line='        <Cell eta_index="'+str(-etaindex)+'" phi_index="'+str(phiindex)+'" scale_factor="'+str(miscal_fac)+'"/>\n'
                        xmlfile.write(line)
                        count=count+1
                    else:
                        line='        <Cell eta_index="'+str(+etaindex)+'" phi_index="'+str(phiindex)+'" scale_factor="'+str(miscal_fac)+'"/>\n'
                        xmlfile.write(line)
                        count=count+1
                else:
                    goodxtal=1
                    line='        <Cell x_index="'+str(etaindex)+'" y_index="'+str(phiindex)+'" z_index="'+str(zindex)+'" scale_factor="'+str(miscal_fac)+'"/>\n'
                    xmlfile.write(line)
                    count=count+1
                    
############################## HERE HCAL    
if hcal==1:
    mindet=1
    maxdet=4
    mineta=-63
    maxeta=63
    minphi=0
    maxphi=127
    mindepth=1
    maxdepth=4
    for cell in range(0,hcalcells):
        detindex=hcal_det[cell]
        etaindex=hcal_eta[cell]
        phiindex=hcal_phi[cell]
        depthindex=hcal_depth[cell]
#    for detindex in range(mindet,maxdet+1):
#        for etaindex in range(mineta,maxeta+1):
#            for phiindex in range(minphi,maxphi+1):
#                for depthindex in range(mindepth,maxdepth+1):
        miscal_fac=miscalibhcal(lumi,detindex,etaindex,phiindex,depthindex,1)
        line='        <Cell det_index="'+str(detindex)+'" eta_index="'+str(etaindex)+'" phi_index="'+str(phiindex)+'" depth_index="'+str(depthindex)+'" scale_factor="'+str(miscal_fac)+'"/>\n'
        xmlfile.write(line)
        count=count+1




# write footer
if ecalbarrel==1:
    xmlfile.write('  </EcalBarrel>\n')
elif ecalendcap==1:
    xmlfile.write('  </EcalEndcap>\n')
elif hcal==1:
    xmlfile.write('  </Hcal>\n')

xmlfile.write('</CalibrationConstants>\n')
xmlfile.close()
print 'File '+fileout+' written with '+str(count)+' lines'
#print miscalibecal(5,0,1,85,1,0)
#print miscalibecal(5,1,-1,10,1,0)
#print miscalibecal(5,1,-1,10,1,1)
#print miscalibecal(5,1,-1,10,1,1)
