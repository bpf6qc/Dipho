import FWCore.ParameterSet.Config as cms
import copy
from OSUT3Analysis.Configuration.cutUtilities import *

tightHoverE = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("hadTowOverEm < 0.05"),
    numberRequired = cms.string(">= 2")
)

tightSigmaIetaIeta = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("(isEB && full5x5_sigmaIetaIeta < 0.0100) || (isEE && full5x5_sigmaIetaIeta < 0.0268)"),
    numberRequired = cms.string(">= 2")
)

tightChargedHadronIso = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("(isEB && chargedHadronIso < 0.76) || (isEE && chargedHadronIso < 0.56)"),
    numberRequired = cms.string(">= 2")
)

tightNeutralHadronIso = cms.PSet(
    inputCollection = cms.vstring("photons", "rho"),
    cutString = cms.string("(fabs(photon.superCluster.eta) < 1.0 && max(0.0, photon.neutralHadronIso - rho.rho*0.0599) < 0.97 + 0.014*photon.pt + 0.000019*photon.pt*photon.pt) || \
                            (fabs(photon.superCluster.eta) >= 1.0 && fabs(photon.superCluster.eta) < 1.479 && max(0.0, photon.neutralHadronIso - rho.rho*0.0819) < 0.97 + 0.014*photon.pt + 0.000019*photon.pt*photon.pt) || \
                            (fabs(photon.superCluster.eta) >= 1.479 && fabs(photon.superCluster.eta) < 2.0 && max(0.0, photon.neutralHadronIso - rho.rho*0.0696) < 2.09 + 0.0139*photon.pt + 0.000025*photon.pt*photon.pt) || \
                            (fabs(photon.superCluster.eta) >= 2.0 && fabs(photon.superCluster.eta) < 2.2 && max(0.0, photon.neutralHadronIso - rho.rho*0.0360) < 2.09 + 0.0139*photon.pt + 0.000025*photon.pt*photon.pt) || \
                            (fabs(photon.superCluster.eta) >= 2.2 && fabs(photon.superCluster.eta) < 2.3 && max(0.0, photon.neutralHadronIso - rho.rho*0.0360) < 2.09 + 0.0139*photon.pt + 0.000025*photon.pt*photon.pt) || \
                            (fabs(photon.superCluster.eta) >= 2.3 && fabs(photon.superCluster.eta) < 2.4 && max(0.0, photon.neutralHadronIso - rho.rho*0.0462) < 2.09 + 0.0139*photon.pt + 0.000025*photon.pt*photon.pt) || \
                            (fabs(photon.superCluster.eta) >= 2.4 && max(0.0, photon.neutralHadronIso - rho.rho*0.0656) < 2.09 + 0.0139*photon.pt + 0.000025*photon.pt*photon.pt)"),
    numberRequired = cms.string(">= 2")
)

tightPhotonIso = cms.PSet(
    inputCollection = cms.vstring("photons", "rho"),
    cutString = cms.string("(fabs(photon.superCluster.eta) < 1.0 && max(0.0, photon.photonIso - rho.rho*0.1271) < 0.08 + 0.0053*photon.pt) || \
                            (fabs(photon.superCluster.eta) >= 1.0 && fabs(photon.superCluster.eta) < 1.479 && max(0.0, photon.photonIso - rho.rho*0.1101) < 0.08 + 0.0053*photon.pt) || \
                            (fabs(photon.superCluster.eta) >= 1.479 && fabs(photon.superCluster.eta) < 2.0 && max(0.0, photon.photonIso - rho.rho*0.0756) < 0.16 + 0.0034*photon.pt) || \
                            (fabs(photon.superCluster.eta) >= 2.0 && fabs(photon.superCluster.eta) < 2.2 && max(0.0, photon.photonIso - rho.rho*0.1175) < 0.16 + 0.0034*photon.pt) || \
                            (fabs(photon.superCluster.eta) >= 2.2 && fabs(photon.superCluster.eta) < 2.3 && max(0.0, photon.photonIso - rho.rho*0.1498) < 0.16 + 0.0034*photon.pt) || \
                            (fabs(photon.superCluster.eta) >= 2.3 && fabs(photon.superCluster.eta) < 2.4 && max(0.0, photon.photonIso - rho.rho*0.1857) < 0.16 + 0.0034*photon.pt) || \
                            (fabs(photon.superCluster.eta) >= 2.4 && max(0.0, photon.photonIso - rho.rho*0.2183) < 0.16 + 0.0034*photon.pt)"),
    numberRequired = cms.string(">= 2")
)

conversionSaveElectronVeto = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("passElectronVeto"),
    numberRequired = cms.string(">= 2")
)

###########################

cutPhotonPt75 = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("pt > 75"),
    numberRequired = cms.string(">= 2")
)

cutPhotonEta = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("fabs(superCluster.eta) < 2.5 && (fabs(superCluster.eta) < 1.4442 || fabs(superCluster.eta) > 1.566)"),
    numberRequired = cms.string(">= 2")
)

cutPhotonEtaEBEE = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("fabs(superCluster.eta) < 1.4442"),
    numberRequired = cms.string("== 1")
)

cutPhotonEtaEBEB = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("fabs(superCluster.eta) < 1.4442"),
    numberRequired = cms.string("== 2")
)

cutDiphotonInvmassEBEE = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("invMass ( photon, photon ) > 230"),
    numberRequired = cms.string(">= 1")
)

cutDiphotonInvmassEBEB = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("invMass ( photon, photon ) > 320"),
    numberRequired = cms.string(">= 1")
)

###########################

tightDiphotonSelection = cms.PSet(
    name = cms.string("tightDiphotonSelection"),
    triggers = cms.vstring("HLT_DoublePhoton_60"),
    cuts = cms.PSet(
        cutPhotonPt75,
        cutPhotonEta,
        tightHoverE,
        tightSigmaIetaIeta,
        tightChargedHadronIso,
        tightNeutralHadronIso,
        tightPhotonIso,
        conversionSaveElectronVeto
    )
)

ebeeSelection = copy.deepcopy(tightDiphotonSelection)
ebeeSelection.name = cms.string("ebeeSelection")
ebeeCuts = [
    cutPhotonEtaEBEE,
    cutDiphotonInvmassEBEE,
]
addCuts(ebeeSelection.cuts, ebeeCuts)

eebebSelection = copy.deepcopy(tightDiphotonSelection)
eebebSelection.name = cms.string("ebebSelection")
ebebCuts = [
    cutPhotonEtaEBEE,
    cutDiphotonInvmassEBEB,
]
addCuts(ebebSelection.cuts, ebebCuts)
