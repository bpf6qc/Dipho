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
        conversionSafeElectronVeto,
        #cutDiphotonInvmassSkim
    )
)

eleVetoSkimSelection = copy.deepcopy(basicSkimSelection)
eleVetoSkimSelection.name = cms.string("eleVetoSkimSelection")
addCuts(eleVetoSkimSelection.cuts, [conversionSafeElectronVeto])

###########################
# N-1 skims
###########################

basicSkimNoPt = copy.deepcopy(basicSkimSelection)
basicSkimNoPt.name = cms.string("basicSelectionNoPtCuts")
removeCuts(basicSkimNoPt.cuts, [cutPhotonPt75])

basicSkimNoEta = copy.deepcopy(basicSkimSelection)
basicSkimNoEta.name = cms.string("basicSelectionNoEtaCuts")
removeCuts(basicSkimNoEta.cuts, [cutPhotonEta])

basicSkimNoHoverE = copy.deepcopy(basicSkimSelection)
basicSkimNoHoverE.name = cms.string("basicSelectionNoHoverECuts")
removeCuts(basicSkimNoHoverE.cuts, [hOverE])

basicSkimNoSigmaIetaIeta = copy.deepcopy(basicSkimSelection)
basicSkimNoSigmaIetaIeta.name = cms.string("basicSelectionNoSigmaIetaIetaCuts")
removeCuts(basicSkimNoSigmaIetaIeta.cuts, [looseSigmaIetaIeta])

basicSkimNoChHadIso = copy.deepcopy(basicSkimSelection)
basicSkimNoChHadIso.name = cms.string("basicSelectionNoChHadIsoCuts")
removeCuts(basicSkimNoChHadIso.cuts, [looseChargedHadronIso])

basicSkimNoNeutralHadIso = copy.deepcopy(basicSkimSelection)
basicSkimNoNeutralHadIso.name = cms.string("basicSelectionNoNeutralHadIsoCuts")
removeCuts(basicSkimNoNeutralHadIso.cuts, [looseNeutralHadronIso])

basicSkimNoPhotonIso = copy.deepcopy(basicSkimSelection)
basicSkimNoPhotonIso.name = cms.string("basicSelectionNoPhotonIsoCuts")
removeCuts(basicSkimNoPhotonIso.cuts, [loosePhotonIso])

basicSkimNoVeto = copy.deepcopy(basicSkimSelection)
basicSkimNoVeto.name = cms.string("basicSelectionNoVet")
removeCuts(basicSkimNoVeto.cuts, [conversionSafeElectronVeto])

basicSkimNoIso = copy.deepcopy(basicSkimSelection)
basicSkimNoIso.name = cms.string("basicSelectionNoIsoCuts")
isoCutsToRemove = [
    looseChargedHadronIso,
    looseNeutralHadronIso,
    loosePhotonIso,
]
removeCuts(basicSkimNoIso.cuts, isoCutsToRemove)

###########################
# Specific eta channels
###########################

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
