import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *
from Configuration.Generator.Pythia8PowhegEmissionVetoSettings_cfi import *



externalLHEProducer = cms.EDProducer('ExternalLHEProducer',
    args = cms.vstring('/afs/cern.ch/user/t/tmu/public/MC_samples/HZZ_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz'),
    nEvents = cms.untracked.uint32(5000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh'),
    generateConcurrently = cms.untracked.bool(True),
)


generator = cms.EDFilter(
    "Pythia8ConcurrentHadronizerFilter",
                         maxEventsToPrint = cms.untracked.int32(1),
                         pythiaPylistVerbosity = cms.untracked.int32(1),
                         filterEfficiency = cms.untracked.double(1.0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(13000.),
                         PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        pythia8PSweightsSettingsBlock,
        pythia8PowhegEmissionVetoSettingsBlock,
        processParameters = cms.vstring(
              '23:mMin = 0.05',
              '24:mMin = 0.05',
              '25:m0 = 125.0',
              '25:onMode = off',
              '25:onIfMatch = 24 -24', #H->z z
              '23:onMode = off', # disable all Z decay modes
              '23:onIfAny = 1 2 3 4 5 6 7 8 11 13 15', # enable only Z->ll and Z->qq
            'ResonanceDecayFilter:filter = on',
            'ResonanceDecayFilter:exclusive = off', #off: require at least the specified number of daughters, on: require exactly the specified number of daughters
             'ResonanceDecayFilter:mothers = 25,24,23', #? TBC! list of mothers not specified -> count all particles in hard process+resonance decays 
            'ResonanceDecayFilter:eMuAsEquivalent = on', #on: treat electrons and muons as equivalent
            'ResonanceDecayFilter:daughters = 24,24,11,11,11,11',
          ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'pythia8PSweightsSettings',
                                    'processParameters',
#                                    'pythia8PowhegEmissionVetoSettingsBlock',
                                    )
        )
                         )


ProductionFilterSequence = cms.Sequence(generator)
