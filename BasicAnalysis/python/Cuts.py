import FWCore.ParameterSet.Config as cms
import copy
from OSUT3Analysis.Configuration.cutUtilities import *

# https://twiki.cern.ch/twiki/bin/view/CMS/CutBasedPhotonIdentificationRun2#SPRING15_selections_25_ns

massOn750pm10 = cms.PSet(
    inputCollection = cms.vstring("photons", "photons"),
    cutString = cms.string("fabs( invMass( photon, photon ) - 750) < 10"),
    numberRequired = cms.string(">= 1")
)

massOn750pm25 = cms.PSet(
    inputCollection = cms.vstring("photons", "photons"),
    cutString = cms.string("fabs( invMass( photon, photon ) - 750) < 25"),
    numberRequired = cms.string(">= 1")
)

massOn750pm50 = cms.PSet(
    inputCollection = cms.vstring("photons", "photons"),
    cutString = cms.string("fabs( invMass( photon, photon ) - 750) < 50"),
    numberRequired = cms.string(">= 1")
)

massOff750pm10 = cms.PSet(
    inputCollection = cms.vstring("photons", "photons"),
    cutString = cms.string("fabs( invMass( photon, photon ) - 750) >= 10"),
    numberRequired = cms.string(">= 1")
)

massOff750pm25 = cms.PSet(
    inputCollection = cms.vstring("photons", "photons"),
    cutString = cms.string("fabs( invMass( photon, photon ) - 750) >= 25"),
    numberRequired = cms.string(">= 1")
)

massOff750pm50 = cms.PSet(
    inputCollection = cms.vstring("photons", "photons"),
    cutString = cms.string("fabs( invMass( photon, photon ) - 750) >= 50"),
    numberRequired = cms.string(">= 1")
)

#########
# H/E
#########

hOverE = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("hadTowOverEm < 0.05"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("H/E")
)

###################
# sigma ieta ieta
###################

looseSigmaIetaIeta = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("(isEB && full5x5_sigmaIetaIeta < 0.0102) || (isEE && full5x5_sigmaIetaIeta < 0.0274)"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("Loose #sigma_{i#eta i#eta}")
)

mediumSigmaIetaIeta = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("(isEB && full5x5_sigmaIetaIeta < 0.0102) || (isEE && full5x5_sigmaIetaIeta < 0.0268)"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("Medium #sigma_{i#eta i#eta}")
)

tightSigmaIetaIeta = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("(isEB && full5x5_sigmaIetaIeta < 0.0100) || (isEE && full5x5_sigmaIetaIeta < 0.0268)"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("Tight #sigma_{i#eta i#eta}")
)

###################
# chHadIso
###################

looseChargedHadronIso = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("(isEB && chargedHadronIso < 3.32) || (isEE && chargedHadronIso < 1.97)"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("Loose charged hadron isolation")
)

mediumChargedHadronIso = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("(isEB && chargedHadronIso < 1.37) || (isEE && chargedHadronIso < 1.10)"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("Medium charged hadron isolation")
)

tightChargedHadronIso = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("(isEB && chargedHadronIso < 0.76) || (isEE && chargedHadronIso < 0.56)"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("Tight charged hadron isolation")
)

###################
# neutralHadIso
###################

looseNeutralHadronIso = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("(isEB && max(0.0, neutralHadronIso - rho*Aeff_neutralHadron) < 1.92 + 0.014*pt + 0.000019*pt*pt) || \
                            (isEE && max(0.0, neutralHadronIso - rho*Aeff_neutralHadron) < 11.86 + 0.0139*pt + 0.000025*pt*pt)"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("Loose neutral hadron isolation")
)

mediumNeutralHadronIso = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("(isEB && max(0.0, neutralHadronIso - rho*Aeff_neutralHadron) < 1.06 + 0.014*pt + 0.000019*pt*pt) || \
                            (isEE && max(0.0, neutralHadronIso - rho*Aeff_neutralHadron) < 2.69 + 0.0139*pt + 0.000025*pt*pt)"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("Medium neutral hadron isolation")
)

tightNeutralHadronIso = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("(isEB && max(0.0, neutralHadronIso - rho*Aeff_neutralHadron) < 0.97 + 0.014*pt + 0.000019*pt*pt) || \
                            (isEE && max(0.0, neutralHadronIso - rho*Aeff_neutralHadron) < 2.09 + 0.0139*pt + 0.000025*pt*pt)"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("Tight neutral hadron isolation")
)

###################
# photonIso
###################

loosePhotonIso = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("(isEB && max(0.0, photonIso - rho*Aeff_photon) < 0.81 + 0.0053*pt) || \
                            (isEE && max(0.0, photonIso - rho*Aeff_photon) < 0.83 + 0.0034*pt)"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("Loose photon isolation")
)

mediumPhotonIso = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("(isEB && max(0.0, photonIso - rho*Aeff_photon) < 0.28 + 0.0053*pt) || \
                            (isEE && max(0.0, photonIso - rho*Aeff_photon) < 0.39 + 0.0034*pt)"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("Medium photon isolation")
)

tightPhotonIso = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("(isEB && max(0.0, photonIso - rho*Aeff_photon) < 0.08 + 0.0053*pt) || \
                            (isEE && max(0.0, photonIso - rho*Aeff_photon) < 0.16 + 0.0034*pt)"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("Tight photon isolation")
)

###################
# electron veto
###################

pixelSeedVeto = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.vstring("! hasPixelSeed"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("Pixel seed veto")
)

conversionSafeElectronVeto = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("passElectronVeto"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("Coversion-safe electron veto")
)

cutPhotonPt75 = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("pt > 75"),
    numberRequired = cms.string(">= 2")
)

cutPhotonEta = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("fabs(superCluster.eta) < 2.5 && (fabs(superCluster.eta) < 1.4442 || fabs(superCluster.eta) > 1.566)"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string("ECAL fiducial region (eta)")
)

cutPhotonEtaEBEE = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("fabs(superCluster.eta) < 1.4442"),
    numberRequired = cms.string("== 1"),
    alias = cms.string("Barrel-endcap")
)

cutPhotonEtaEBEB = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("fabs(superCluster.eta) < 1.4442"),
    numberRequired = cms.string("== 2"),
    alias = cms.string("Barrel-barrel")
)

cutPhotonEtaEEEE = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("fabs(superCluster.eta) > 1.566"),
    numberRequired = cms.string("== 2"),
    alias = cms.string("Endcap-endcap")
)

cutDiphotonInvmassSkim = cms.PSet(
    inputCollection = cms.vstring("photons", "photons"),
    cutString = cms.string("invMass ( photon, photon ) > 230"),
    numberRequired = cms.string(">= 1")
)

cutDiphotonInvmassEBEE = cms.PSet(
    inputCollection = cms.vstring("photons", "photons"),
    cutString = cms.string("invMass ( photon, photon ) > 230"),
    numberRequired = cms.string(">= 1")
)

cutDiphotonInvmassEBEB = cms.PSet(
    inputCollection = cms.vstring("photons", "photons"),
    cutString = cms.string("invMass ( photon, photon ) > 320"),
    numberRequired = cms.string(">= 1")
)

cutDiphotonInvmassEEEE = cms.PSet(
    inputCollection = cms.vstring("photons", "photons"),
    cutString = cms.string("invMass ( photon, photon ) > 320"),
    numberRequired = cms.string(">= 1")
)
