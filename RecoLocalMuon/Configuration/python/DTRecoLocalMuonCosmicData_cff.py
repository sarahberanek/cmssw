Traceback (most recent call last):
  File "/afs/cern.ch/cms/sw/slc4_ia32_gcc345/cms/cmssw/CMSSW_2_1_0_pre4/src/FWCore/ParameterSet/python/cfg2py.py", line 10, in ?
    print cmsParse.dumpCff(fileInPath)
  File "/afs/cern.ch/cms/sw/slc4_ia32_gcc345/cms/cmssw/CMSSW_2_1_0_pre4/python/FWCore/ParameterSet/parseConfig.py", line 1607, in dumpCff
    compressedValues = _getCompressedNodes(fileName, 0, values)
  File "/afs/cern.ch/cms/sw/slc4_ia32_gcc345/cms/cmssw/CMSSW_2_1_0_pre4/python/FWCore/ParameterSet/parseConfig.py", line 1366, in _getCompressedNodes
    raise pp.ParseFatalException(s,loc,"the process contains the error \n"+str(e))
FWCore.ParameterSet.parsecf.pyparsing.ParseFatalException: the process contains the error 
Unable to find file 'CMSSW/EventFilter/DTRawToDigi/data/dtunpacker.cfi' using the search path ${'CMSSW_SEARCH_PATH'} 
/build1/bellan/21X/CMSSW_2_1_0_pre4/src:/build1/bellan/21X/CMSSW_2_1_0_pre4/share:/afs/cern.ch/cms/sw/slc4_ia32_gcc345/cms/cmssw/CMSSW_2_1_0_pre4/src:/afs/cern.ch/cms/sw/slc4_ia32_gcc345/cms/cmssw/CMSSW_2_1_0_pre4/share:/afs/cern.ch/cms/sw/slc4_ia32_gcc345/cms/data-CondCore-SQLiteData/24:/afs/cern.ch/cms/sw/slc4_ia32_gcc345/cms/data-FastSimulation-MaterialEffects/20:/afs/cern.ch/cms/sw/slc4_ia32_gcc345/cms/data-FastSimulation-PileUpProducer/21:/afs/cern.ch/cms/sw/slc4_ia32_gcc345/cms/data-Geometry-CaloTopology/19-cms:/afs/cern.ch/cms/sw/slc4_ia32_gcc345/cms/data-MagneticField-Interpolation/22:/afs/cern.ch/cms/sw/slc4_ia32_gcc345/cms/data-RecoMuon-MuonIdentification/19-cms:/afs/cern.ch/cms/sw/slc4_ia32_gcc345/cms/data-RecoParticleFlow-PFBlockProducer/19-cms:/afs/cern.ch/cms/sw/slc4_ia32_gcc345/cms/data-RecoParticleFlow-PFTracking/22:/afs/cern.ch/cms/sw/slc4_ia32_gcc345/cms/data-RecoTracker-RingESSource/19-cms:/afs/cern.ch/cms/sw/slc4_ia32_gcc345/cms/data-RecoTracker-RoadMapESSource/19-cms:/afs/cern.ch/cms/sw/slc4_ia32_gcc345/cms/data-SimG4CMS-Calo/19-cms:/afs/cern.ch/cms/sw/slc4_ia32_gcc345/cms/data-Validation-EcalDigis/19-cms:/afs/cern.ch/cms/sw/slc4_ia32_gcc345/cms/data-Validation-EcalHits/19-cms:/afs/cern.ch/cms/sw/slc4_ia32_gcc345/cms/data-Validation-EcalRecHits/19-cms:/afs/cern.ch/cms/sw/slc4_ia32_gcc345/cms/data-Validation-Geometry/19-cms:/afs/cern.ch/cms/sw/slc4_ia32_gcc345/cms/data-Validation-HcalHits/19-cms (at char 0), (line:1, col:1)
