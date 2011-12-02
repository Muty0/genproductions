import FWCore.ParameterSet.Config as cms




source = cms.Source("EmptySource")

from Configuration.Generator.PythiaUEZ2Settings_cfi import *
from GeneratorInterface.ExternalDecays.TauolaSettings_cff import *

generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(0.1695),
    comEnergy = cms.double(7000.0),
    crossSection = cms.untracked.double(10.5),
    ExternalDecays = cms.PSet(
        Tauola = cms.untracked.PSet(
            TauolaPolar,
            TauolaDefaultInputCards
        ),
        parameterSets = cms.vstring('Tauola')
    ),
    UseExternalGenerators = cms.untracked.bool(True),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
         processParameters = cms.vstring('MSEL       =0      !User defined processes', 
                                         'MSUB(23)   =1      !WZ production',
                                         'CKIN(3)    =200.   ! min pt hat value'),

        # This is a vector of ParameterSet names to be read, in this order
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    )

)

ProductionFilterSequence = cms.Sequence(generator)

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    name = cms.untracked.string('$Source: /afs/cern.ch/project/cvs/reps/CMSSW/CMSSW/Configuration/GenProduction/python/WWtoAnything_TuneZ2_7TeV_pythia6_tauola_cff.py,v $'),
    annotation = cms.untracked.string('PYTHIA6-EWK WW at 7TeV')
)

