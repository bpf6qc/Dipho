import FWCore.ParameterSet.Config as cms
import copy
from OSUT3Analysis.Configuration.cutUtilities import *

##############################
##### Triggers           #####
##############################

triggersDipho = cms.vstring("HLT_DoublePhoton_60")

##########################
##### List of cuts   #####
##########################

cutGoodPV = cms.PSet(
    inputCollection = cms.vstring("primaryvertices"),
    cutString = cms.string("isValid > 0 && ndof >= 4"),
    numberRequired = cms.string(">= 1")
)

#########################
##### Photon cuts   #####
#########################

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

#############################
##### More photon cuts  #####
#############################

cutPhotonConvSafeEleVeto = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("passElectronVeto"),
    numberRequired = cms.string(">= 2")
)

cutPhotonChHadIso = cms.PSet(
    inputCollection = cms.vstring("photons"),
    cutString = cms.string("chargedHadronIso < 5"),
    numberRequired = cms.string(">= 2")
)

cutPhotonPhotonIso = cms.PSet(
    inputCollection = cms.vstring("photons", ""),
    cutString = cms.string("(fabs(superCluster.eta) < 0.9 && 2.5 + photonIso - )")
)
