import FWCore.ParameterSet.Config as cms
import copy
from OSUT3Analysis.Configuration.cutUtilities import *

from Dipho.BasicAnalysis.Cuts import *

###########################

basicSkimSelection = cms.PSet(
    name = cms.string("basicSkimSelection"),
    triggers = cms.vstring("HLT_DoublePhoton60_v"),
    cuts = cms.VPSet(
        cutPhotonPt75,
        cutPhotonEta,
        hOverE,
        looseSigmaIetaIeta,
        looseChargedHadronIso,
        looseNeutralHadronIso,
        loosePhotonIso,
        #cutDiphotonInvmassSkim
    )
)

ebeeSkimSelection = copy.deepcopy(basicSkimSelection)
ebeeSkimSelection.name = cms.string("ebeeSkimSelection")
ebeeCuts = [
    cutPhotonEtaEBEE,
]
addCuts(ebeeSkimSelection.cuts, ebeeCuts)

ebebSkimSelection = copy.deepcopy(basicSkimSelection)
ebebSkimSelection.name = cms.string("ebebSkimSelection")
ebebCuts = [
    cutPhotonEtaEBEB,
]
addCuts(ebebSkimSelection.cuts, ebebCuts)

eeeeSkimSelection = copy.deepcopy(basicSkimSelection)
eeeeSkimSelection.name = cms.string("eeeeSkimSelection")
eeeeCuts = [
    cutPhotonEtaEEEE,
]
addCuts(eeeeSkimSelection.cuts, eeeeCuts)
