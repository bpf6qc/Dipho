import FWCore.ParameterSet.Config as cms
import copy

from Dipho.Investigation.Cuts import * # Put all the individual cuts in this file

##########################
##### Preselection   #####
##########################

basicSelection = cms.PSet(
    name = cms.string("BasicSelection"),
    triggers = triggersDipho,
    cuts = cms.PSet(
        #cutGoodPV,
        cutPhotonPt75,
        cutPhotonEta,
    )
)

ebeeSelection = copy.deepcopy(basicSelection)
ebeeSelection.name = cms.string("ebeeSelection")
ebeeCuts = [
    cutPhotonEtaEBEE,
    cutDiphotonInvmassEBEE,
]
addCuts(ebeeSelection.cuts, ebeeCuts)

eebebSelection = copy.deepcopy(basicSelection)
eebebSelection.name = cms.string("ebebSelection")
ebebCuts = [
    cutPhotonEtaEBEE,
    cutDiphotonInvmassEBEB,
]
addCuts(ebebSelection.cuts, ebebCuts)
