import FWCore.ParameterSet.Config as cms


## select events with at least one good PV
pvFilter = cms.EDFilter(
    "VertexSelector",
    src = cms.InputTag("offlinePrimaryVertices"),
    cut = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.Rho <= 2"),
    filter = cms.bool(True),   # otherwise it won't filter the events, just produce an empty vertex collection.
    )


## apply HBHE Noise filter
import CommonTools.RecoAlgos.HBHENoiseFilter_cfi
HBHENoiseFilter = CommonTools.RecoAlgos.HBHENoiseFilter_cfi.HBHENoiseFilter.clone()


## select events with high pfMET
pfMETSelector = cms.EDFilter(
    "CandViewSelector",
    src = cms.InputTag("pfMet"),
    cut = cms.string( "pt()>200" )
    )

pfMETCounter = cms.EDFilter(
    "CandViewCountFilter",
    src = cms.InputTag("pfMETSelector"),
    minNumber = cms.uint32(1),
    )

pfMETSelSeq = cms.Sequence(
			   pvFilter*
                           HBHENoiseFilter*
                           pfMETSelector*
                           pfMETCounter
                           )



## select events with high tcMET
tcMETSelector = cms.EDFilter(
    "CandViewSelector",
    src = cms.InputTag("tcMet"),
    cut = cms.string( "pt()>200" )
    )

tcMETCounter = cms.EDFilter(
    "CandViewCountFilter",
    src = cms.InputTag("tcMETSelector"),
    minNumber = cms.uint32(1),
    )

tcMETSelSeq = cms.Sequence(
			   pvFilter*
                           HBHENoiseFilter*
                           tcMETSelector*
                           tcMETCounter
                           )


## select events with high MET dependent on PF and Calo MET Conditions
CondMETSelector = cms.EDProducer(
   "CandViewShallowCloneCombiner",
   decay = cms.string("pfMet caloMetM"),
   cut = cms.string(" (daughter(0).pt > 200) || (daughter(0).pt/daughter(1).pt > 2 && daughter(1).pt > 150 ) || (daughter(1).pt/daughter(0).pt > 2 && daughter(0).pt > 150 )  " )
   )

CondMETCounter = cms.EDFilter(
    "CandViewCountFilter",
    src = cms.InputTag("CondMETSelector"),
    minNumber = cms.uint32(1),
    )

CondMETSelSeq = cms.Sequence(
                           pvFilter*
                           HBHENoiseFilter*
                           CondMETSelector*
                           CondMETCounter
                           )



## select events with PAT METs in MINIAODSIM - remember to keep the right branches in the cmsDriver
miniMETSelector = cms.EDFilter(
    "CandViewSelector",
    src = cms.InputTag("slimmedMETs"),
    cut = cms.string( "pt()>200" )
    )

miniMETCounter = cms.EDFilter(
    "CandViewCountFilter",
    src = cms.InputTag("miniMETSelector"),
    minNumber = cms.uint32(1),
    )

miniMETSelSeq = cms.Sequence(
                           HBHENoiseFilter*
                           miniMETSelector*
                           miniMETCounter
                           )


