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
basicSkimNoVeto.name = cms.string("basicSelectionNoVeto")
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

#################################################################################
# Specific mass channels -- take basicSkimSelection as input
#################################################################################

onMassSelectionPM10 = copy.deepcopy(basicSkimSelection)
onMassSelectionPM10.name = cms.string("onMassSelectionPM10")
addCuts(onMassSelectionPM10.cuts, [massOn750p10, massOn750m10])

offMassSelectionPM10 = copy.deepcopy(basicSkimSelection)
offMassSelectionPM10.name = cms.string("offMassSelectionPM10")
addCuts(offMassSelectionPM10.cuts, [massOff750p10, massOff750m10])

onMassSelectionPM25 = copy.deepcopy(basicSkimSelection)
onMassSelectionPM25.name = cms.string("onMassSelectionPM25")
addCuts(onMassSelectionPM25.cuts, [massOn750p25, massOn750m25])

offMassSelectionPM25 = copy.deepcopy(basicSkimSelection)
offMassSelectionPM25.name = cms.string("offMassSelectionPM25")
addCuts(offMassSelectionPM25.cuts, [massOff750p25, massOff750m25])

onMassSelectionPM50 = copy.deepcopy(basicSkimSelection)
onMassSelectionPM50.name = cms.string("onMassSelectionPM50")
addCuts(onMassSelectionPM50.cuts, [massOn750p50, massOn750m50])

offMassSelectionPM50 = copy.deepcopy(basicSkimSelection)
offMassSelectionPM50.name = cms.string("offMassSelectionPM50")
addCuts(offMassSelectionPM50.cuts, [massOff750p50, massOff750m50])
