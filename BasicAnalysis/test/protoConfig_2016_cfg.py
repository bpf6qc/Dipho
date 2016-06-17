import FWCore.ParameterSet.Config as cms
import OSUT3Analysis.DBTools.osusub_cfg as osusub
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *
import glob

data_global_tag = '80X_dataRun2_Prompt_v8'
mc_global_tag = '80X_mcRun2_asymptotic_2016_v3'

################################################################################
##### Set up the 'process' object ##############################################
################################################################################

process = cms.Process ('OSUAnalysis')

# how often to print a log message
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

# Use the following block for the Calo calculation.
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, mc_global_tag, '')
if osusub.batchMode and (osusub.datasetLabel in types) and (types[osusub.datasetLabel] == "data"):
    print "using global tag " + data_global_tag + "..."
    process.GlobalTag = GlobalTag(process.GlobalTag, data_global_tag, '')
else:
    print "using global tag " + mc_global_tag + "..."


# input source when running interactively
# ---------------------------------------
process.source = cms.Source ("PoolSource",
    #bypassVersionCheck = cms.untracked.bool (True),
    skipBadFiles = cms.untracked.bool (True),
    fileNames = cms.untracked.vstring (
        "root://cmsxrootd-site2.fnal.gov:1092//store/data/Run2015D/DoubleEG/MINIAOD/16Dec2015-v2/00000/FED54E49-83A6-E511-AB65-0CC47A4C8ED8.root",
        #"root://xrootd.rcac.purdue.edu//store/user/wulsin/SingleMuon/Run2015D-16Dec2015-v1-DisappTrks-v1/160131_105005/0000/miniAODWithCandidateTracks_1.root",
    ),
)

# Uncomment the following if you need access to collections in AOD. N.B.: since
# the data ntuples are not ancestors of the AOD files, this requires special
# modifications to IOPool/Input. Even after these modifications, saving skims
# for data will not work.

# addSecondaryFiles (process.source)

# Add all files in a directory:
# dirname = "condor/isoTrkSelection/MET_2015D/IsoTrkSelection/"
# for f in glob.glob(dirname + "skim*.root"):
#     process.source.fileNames.extend(cms.untracked.vstring('file:' + f))


# process.source.eventsToProcess = cms.untracked.VEventRange (
#     "1:60:53",
# )

# output histogram file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)

# number of events to process when running interactively
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (100)
)

################################################################################
##### Set up the 'collections' map #############################################
################################################################################

from OSUT3Analysis.AnaTools.osuAnalysis_cfi import collectionMap  # miniAOD

################################################################################
##### Set up weights to be used in plotting and cutflows  ######################
################################################################################

weights = cms.VPSet ()

################################################################################
##### Set up any user-defined variable producers ###############################
################################################################################

variableProducers = []
#variableProducers.append("LifetimeWeightProducer")
#variableProducers.append("PrimaryVtxVarProducer")
#variableProducers.append("EventJetVarProducer")

################################################################################
##### Import the channels to be run ############################################
################################################################################

from Dipho.BasicAnalysis.EventSelections import *

################################################################################
##### Import the histograms to be plotted ######################################
################################################################################

from Dipho.BasicAnalysis.histogramDefinitions import *
phist = cms.VPSet(histograms, invMassHistograms)

################################################################################
##### Sets of channels to be run simultaneously over a single skim. ############
################################################################################

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels(process, [basicSkimSelection], phist, weights, [], collectionMap, variableProducers, True)

################################################################################
##### Debugging options
################################################################################
# uncomment to produce a full python configuration log file
#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()

#process.Tracer = cms.Service("Tracer")
