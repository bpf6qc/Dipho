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

onMassSelection_pm10 = copy.deepcopy(basicSkimSelection)
onMassSelection_pm10.name = cms.string("onMassSelection_pm10")
addCuts(onMassSelection_pm10.cuts, [massOn750pm10])

offMassSelection_pm10 = copy.deepcopy(basicSkimSelection)
offMassSelection_pm10.name = cms.string("offMassSelection_pm10")
addCuts(offMassSelection_pm10.cuts, [massOff750pm10])

onMassSelection_pm25 = copy.deepcopy(basicSkimSelection)
onMassSelection_pm25.name = cms.string("onMassSelection_pm25")
addCuts(onMassSelection_pm25.cuts, [massOn750pm25])

offMassSelection_pm25 = copy.deepcopy(basicSkimSelection)
offMassSelection_pm25.name = cms.string("offMassSelection_pm25")
addCuts(offMassSelection_pm25.cuts, [massOff750pm25])

onMassSelection_pm50 = copy.deepcopy(basicSkimSelection)
onMassSelection_pm50.name = cms.string("onMassSelection_pm50")
addCuts(onMassSelection_pm50.cuts, [massOn750pm50])

offMassSelection_pm50 = copy.deepcopy(basicSkimSelection)
offMassSelection_pm50.name = cms.string("offMassSelection_pm50")
addCuts(offMassSelection_pm50.cuts, [massOff750pm50])
