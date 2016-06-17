import FWCore.ParameterSet.Config as cms

histograms = cms.PSet(
    inputCollection = cms.vstring("photons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("photonPt"),
            title = cms.string("photon Transverse Momentum; photon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("pt"),
        ),
	    cms.PSet (
            name = cms.string("photonEta"),
            title = cms.string("photon Pseudorapidity; photon #eta"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("eta"),
        ),
        cms.PSet (
            name = cms.string("hasConversionTracks"),
            title = cms.string("hasConversionTracks; "),
            binsX = cms.untracked.vdouble(4, -2, 2),
            inputVariables = cms.vstring("hasConversionTracks"),
        ),
	    cms.PSet (
            name = cms.string("photonEtaVsPhi"),
            title = cms.string("photon Pseudorapidity vs. Phi; photon #phi; photon #eta"),
            binsX = cms.untracked.vdouble(100, -3.14, 3.14),
            binsY = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("eta","phi"),
        ),
    )
)

invMassHistograms = cms.PSet(
    inputCollection = cms.vstring("photons", "photons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("diphotonInvmass"),
            title = cms.string("diphoton invariant mass; m_{#gamma#gamma}"),
            binsX = cms.untracked.vdouble(2000, 0, 2000),
            inputVariables = cms.vstring("invMass(photon, photon)"),
        ),
        cms.PSet (
            name = cms.string("diphotonInvmassVsHasConvTracks"),
            title = cms.string("diphoton invariant mass vs. hasConversionTracks; m_{#gamma#gamma}; "),
            binsX = cms.untracked.vdouble(2000, 0, 2000),
            binsY = cms.untracked.vdouble(4, -2, 2),
            inputVariables = cms.vstring("invMass(photon, photon)","photon.hasConversionTracks"),
        ),
    )
)
