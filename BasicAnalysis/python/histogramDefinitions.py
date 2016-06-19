import FWCore.ParameterSet.Config as cms

histograms = cms.PSet(
    inputCollection = cms.vstring("photons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("photonPt"),
            title = cms.string("photon Transverse Momentum; photon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(1000, 0, 5000),
            inputVariables = cms.vstring("pt"),
        ),
	    cms.PSet (
            name = cms.string("photonEta"),
            title = cms.string("photon Pseudorapidity; photon #eta"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("eta"),
        ),
        cms.PSet (
            name = cms.string("photonHoverE"),
            title = cms.string("photon H/E; photon H/E"),
            binsX = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring("hadTowOverEm"),
        ),
        cms.PSet (
            name = cms.string("photonSigmaIetaieta"),
            title = cms.string("photon #sigma_{i#eta i#eta}; photon #sigma_{i#eta i#eta}"),
            binsX = cms.untracked.vdouble(1000, 0, 1),
            inputVariables = cms.string("full5x5_sigmaIetaIeta"),
        ),
        cms.PSet (
            name = cms.string("photonChargedHadronIso"),
            title = cms.string("photon ChargedHadronIso; photon chHadIso"),
            binsX = cms.untracked.vdouble(500, -5, 20),
            inputVariables = cms.string("chargedHadronIso"),
        ),
        cms.PSet (
            name = cms.string("photonNeutralHadronIso"),
            title = cms.string("photon NeutralHadronIso; photon nHadIso"),
            binsX = cms.untracked.vdouble(500, -5, 20),
            inputVariables = cms.string("neutralHadronIso - rho*Aeff_neutralHadron"),
        ),
        cms.PSet (
            name = cms.string("photonNeutralHadronIsoNoRhoSub"),
            title = cms.string("photon NeutralHadronIso no rho subtraction; photon nHadIso (no rho sub)"),
            binsX = cms.untracked.vdouble(500, -5, 20),
            inputVariables = cms.string("neutralHadronIso"),
        ),
        cms.PSet (
            name = cms.string("photonNHadIsoVsPt"),
            title = cms.string("photon NeutralHadronIso vs Pt; photon nHadIso; photon Pt"),
            binsX = cms.untracked.vdouble(500, -5, 20),
            binsY = cms.untracked.vdouble(1000, 0, 5000),
            inputVariables = cms.string("neutralHadronIso - rho*Aeff_neutralHadron", "pt"),
        ),
        cms.PSet (
            name = cms.string("rho"),
            title = cms.string("rho; #rho"),
            binsX = cms.untracked.vdouble(500, 0, 500),
            inputVariables = cms.string("rho"),
        ),
        cms.PSet (
            name = cms.string("photonPhotonIso"),
            title = cms.string("photon PhotonIso; photon nHadIso"),
            binsX = cms.untracked.vdouble(500, -5, 20),
            inputVariables = cms.string("photonIso - rho*Aeff_photon"),
        ),
        cms.PSet (
            name = cms.string("photonPhotonIsoNoRhoSub"),
            title = cms.string("photon PhotonIso no rho subtraction; photon photonIso (no rho sub)"),
            binsX = cms.untracked.vdouble(500, -5, 20),
            inputVariables = cms.string("photoniso"),
        ),
        cms.PSet (
            name = cms.string("photonPhotonIsoVsPt"),
            title = cms.string("photon PhotonIso vs Pt; photon photonIso; photon Pt"),
            binsX = cms.untracked.vdouble(500, -5, 20),
            binsY = cms.untracked.vdouble(1000, 0, 5000),
            inputVariables = cms.string("photonIso - rho*Aeff_photon", "pt"),
        ),
        cms.PSet (
            name = cms.string("photonPassConvSafeEleVeto"),
            title = cms.string("passConvSafeEleVeto; pass veto"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.string("passElectronVeto"),
        ),
        cms.PSet (
            name = cms.string("photonHasPixelSeed"),
            title = cms.string("hasPixelSeed; has pixel seed"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.string("hasPixelSeed"),
        ),
        cms.PSet (
            name = cms.string("ecalIso"),
            title = cms.string("ecalIso; ecalIso"),
            binsX = cms.untracked.vdouble(500, -5, 20),
            inputVariables = cms.string("ecalIso"),
        ),
        cms.PSet (
            name = cms.string("hcalIso"),
            title = cms.string("hcalIso; hcalIso"),
            binsX = cms.untracked.vdouble(500, -5, 20),
            inputVariables = cms.string("hcalIso"),
        ),
        cms.PSet (
            name = cms.string("caloIso"),
            title = cms.string("caloIso; caloIso"),
            binsX = cms.untracked.vdouble(500, -10, 40),
            inputVariables = cms.string("caloIso"),
        ),
        cms.PSet (
            name = cms.string("trackIso"),
            title = cms.string("trackIso; trackIso"),
            binsX = cms.untracked.vdouble(500, -5, 20),
            inputVariables = cms.string("trackIso"),
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

MetHistograms = cms.PSet(
    inputCollection = cms.vstring("mets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("metPt"),
            title = cms.string("E_{T}^{miss}; E_{T}^{miss}"),
            binsX = cms.untracked.vdouble(400, 0, 2000),
            inputVariables = cms.vstring("pt"),
        ),
    ),
)

EventVariableHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("nJets"),
            title = cms.string(";Number of jets"),
            binsX = cms.untracked.vdouble(15, 0.0, 15.0),
            inputVariables = cms.vstring("nJets"),
        ),
        cms.PSet (
            name = cms.string("dijetMaxDeltaPhi"),
            title = cms.string("Maximum #Delta#Phi between two jets;#Delta#Phi_{max}(jet pairs)"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            inputVariables = cms.vstring("dijetMaxDeltaPhi"),
        ),
        cms.PSet (
            name = cms.string("deltaPhiMetJetLeading"),
            title = cms.string("#Delta#Phi(E_{T}^{miss},leading jet);#Delta#Phi(E_{T}^{miss},leading jet)"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            inputVariables = cms.vstring("deltaPhiMetJetLeading"),
        ),
        cms.PSet (
            name = cms.string("deltaPhiMetJetSubleading"),
            title = cms.string("#Delta#Phi(E_{T}^{miss},subleading jet);#Delta#Phi(E_{T}^{miss},subleading jet)"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            inputVariables = cms.vstring("deltaPhiMetJetSubleading"),
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
