import FWCore.ParameterSet.Config as cms

# This cfi contains everything needed to use the VolumeBased magnetic
# field engine version 1103l

from MagneticField.GeomBuilder.cmsMagneticFieldXML_1103l_cfi import *

# avoid interference with EmptyESSource in uniformMagneticField.cfi
es_prefer_magfield = cms.ESPrefer("XMLIdealGeometryESSource","magfield")


ParametrizedMagneticFieldProducer = cms.ESProducer("ParametrizedMagneticFieldProducer",
    version = cms.string('OAE_1103l_071212'),
    parameters = cms.PSet(
        BValue = cms.string('3_8T')
    ),
    label = cms.untracked.string('parametrizedField')
)


VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducer",
    useParametrizedTrackerField = cms.bool(True),
    label = cms.untracked.string(''),
    version = cms.string('grid_1103l_090216_3_8t'),
    debugBuilder = cms.untracked.bool(False),
    cacheLastVolume = cms.untracked.bool(True),
    scalingVolumes = cms.vint32(),
    scalingFactors = cms.vdouble()
)


