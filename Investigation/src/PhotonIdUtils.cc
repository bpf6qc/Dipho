#include "Dipho/Investigation/interface/PhotonIdUtils.h"

#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Candidate/interface/Candidate.h"

#include "Geometry/CaloTopology/interface/CaloTopology.h"
#include "RecoEcal/EgammaCoreTools/interface/EcalClusterTools.h"

PhotonIdUtils::PhotonIdUtils(OverlapRemovalAlgo *algo) :
  overlapAlgo_(algo),
  removeOverlappingCandidates_(true),
  deltaPhiRotation_(0.)
{}

PhotonIdUtils::~PhotonIdUtils() {};

bool PhotonIdUtils::vetoPackedCand(const pat::Photon &photon, const edm::Ptr<pat::PackedCandidate> &pfcand) {
  edm::RefVector<pat::PackedCandidateCollection> associated = photon.associatedPackedPFCandidates();

  int nass = 0;
  for(unsigned int i = 0; i < associated.size(); i++) {
    edm::Ptr<pat::PackedCandidate> associatedPtr = edm::refToPtr(associated[i]);
    if(associatedPtr == pfcand) {
      nass++;
      break;
    }
  }

  return (nass > 0);
}

flash PhotonIdUtils::pfIsoChgWrtVtx(const edm::Ptr<pat::Photon> &photon,
                                    const edm::Ptr<reco::Vertex> vtx,
                                    const VertexCandidateMap vtxcandmap,
                                    float coneSize, float coneVetoBarrel, float coneVetoEndcap,
                                    float ptMin) {

  float isovalue = 0;
  float coneVeto = 0;
  if(photon->isEB()) coneVeto = coneVetoBarrel;
  else if(photon->isEE()) coneVeto = coneVetoEndcap;

  math::XYZVector SCdirection(photon->superCluster()->x() - vtx->x(),
                              photon->superCluster()->y() - vtx->y(),
                              photon->superCluster()->z() - vtz->z());

  auto mapRange = equal_range(vtxcandmap.begin(), vtxcandmap.end(), vtx, compare_with_vtx());
  if(mapRange.first == mapRange.second) return -1.;

  for(auto pair_iter = mapRange.first; pair_iter != mapRange.second; pair_iter++) {
    edm::Ptr<pat::PackedCandidate> pfcand = pair_iter->second;

    if(abs(pfcand->pdfId()) == 11 || abs(pfcand->pdgId()) == 13) continue; //J. Tao not e/mu

    if(removeOverlappingCandidates_ &&
       ((overlapAlgo_ == 0 && vetoPackedCand(*photon, pfcand)) || ((overlapAlgo_ != 0 && (*overlapAlgo_)(*photon, pfcand)))) {
         continue;
    }

    if(pfcand->pt() < ptMin) continue;
    float dRTkToVtx = deltaR(pfcand->momentum().Eta(), pfcand->momentum().Phi(),
                             SCdirection.Eta(), SCdirection.Phi() + deltaPhiRotation_);

    if(dRTkToVtx > coneSize || dRTkToVtx < coneVeto) continue;

    isoValue += pfcand->pt();
  }

  return isovalue;
}

map<edm::Ptr<reco::Vertex>, float> PhotonIdUtils::pfIsoChgWrtAllVtx(const edm::Ptr<pat::Photon> &photon,
                                                                    const vector<edm::Ptr<reco::Vertex> > &vertices,
                                                                    float coneSize, float coneVetoBarrel, float coneVetoEndcap,
                                                                    float ptMin) {

  map<edm::Ptr<reco::Vertex>, float> isomap;
  isomap.clear();

  for(unsigned int i = 0; i < vertices.size(); i++) {
    float iso = pfIsoChgWrtVtx(photon, vertices[i], vtxcandmap, coneSize, coneVetoBarrel, coneVetoEndcap, ptMin);
    isomap.insert(make_pair(vertices[i], iso));
  }

}

float PhotonIdUtils::pfIsoChgWrtWorstVtx(map<edm::Ptr<reco::Vertex>, float> &vtxIsoMap) {

  float MaxValueMap = -1000;
  float itValue = 0;

  for(map<edm::Ptr<reco::Vertex>, float>::iterator it = vtxIsoMap.begin(); it != vtxIsoMap.end(); it++) {
    itValue = it->second;
    if(itValue > MaxValueMap) MaxValueMap = itValue;
  }

  return MaxValueMap;
}

float PhotonIdUtils::pfCaloIso(const edm::Ptr<pat::Photon> &photon,
                               const vector<edm::Ptr<pat::PackedCandidate> > &pfcandidates,
                               float dRMax,
                               float dRVetoBarrel,
                               float dRVetoEndcap,
                               float etaStripBarrel,
                               float etaStripEndcap,
                               float minEnergyBarrel,
                               float minEnergyEndcap,
                               reco::PFCandidate::ParticleType type,
                               const reco::Vertex *vtx) {

  static reco::PFCandidate helper;
  int pdgId = helper.translateTypeToPdgId(type);

  float dRVeto = 99;
  float maxetaStrip = 99;

  if(photon->isEB()) {
    dRVeto = dRVetoBarrel;
    maxetaStrip = etaStripBarrel;
  }
  else if(photon->isEE()) {
    dRVeto = dRVetoEndcap;
    maxetaStrip = etaStripEndcap;
  }

  for(size_t ipf = 0; ipf < pfcandidates.size(); ipf++) {
    edm::Ptr<pat::PackedCandidate> pfcand = pfcandidates[ipf];

    if(pfcand->pdgId() != pdgId) continue;
    if(photon->isEB() && fabs(pfcand->pt()) < minEnergyBarrel) continue;
    if(photon->isEE() && fabs(pfcand->energy()) < minEnergyEndcap) continue;

    if(removeOverlappingCandidates_ && vetoPackedCand(*photon, pfcand)) continue;

    double vx, vy, vz;

    if(vtx) {
      vx = vtx->x();
      vy = vtx->y();
      vz = vtx->z();
    }
    else {
      math::XYZPoint pfcandvtx = pfcand->vertex();
      vx = pfcandvtx.x();
      vy = pfcandvtx.y();
      vz = pfcandvtx.z();
    }

    math::XYZVector SCdirectionWrtCandVtx(photon->superCluster->x() - vx,
                                          photon->superCluster->y() - vy,
                                          photon->superCluster->z() - vz);

    float dEta = fabs(SCdirectionWrtCandVtx.Eta() - pfcand->momentum().Eta());
    float dR = deltaR(SCdirectionWrtCandVtx.Eta(), SCdirectionWrtCandVtx.Phi(), pfcand->momentum.Eta(), pfcand->momentum.Phi());

    if(dEta < maxetaStrip) continue;
    if(dR < dRVeto || dR > dRMax) continue;

    isoValue += pfcand->pt();
  }

  return isoValue;
}

void PhotonIdUtils::setupMVA(const string &xmlfilenameEB, const string &xmlfilenameEE) {

  // **** bdt 2015 EB ****

  string mvamethod = "BDT";

  phoIdMva_EB_ = make_shared<TMVA::Reader>("!Color:Silent");

  phoIdMva_EB_->AddVariable("SCRawE",             &phoIdMva_SCRawE_);
  phoIdMva_EB_->AddVariable("r9",                 &phoIdMva_R9_);
  phoIdMva_EB_->AddVariable("sigmaIetaIeta",      &phoIdMva_covIEtaIEta_);
  phoIdMva_EB_->AddVariable("etaWidth",           &phoIdMva_EtaWidth_);
  phoIdMva_EB_->AddVariable("phiWidth",           &phoIdMva_PhiWidth_);
  phoIdMva_EB_->AddVariable("covIEtaIPhi",        &phoIdMva_covIEtaIPhi_);
  phoIdMva_EB_->AddVariable("s4",                 &phoIdMva_S4_);
  phoIdMva_EB_->AddVariable("phoIso03",           &phoIdMva_pfPhoIso03_);
  phoIdMva_EB_->AddVariable("chgIsoWrtChosenVtx", &phoIdMva_pfChgIso03_);
  phoIdMva_EB_->AddVariable("chgIsoWrtWorstVtx",  &phoIdMva_pfChgIso03worst_);
  phoIdMva_EB_->AddVariable("scEta",              &phoIdMva_ScEta_);
  phoIdMva_EB_->AddVariable("rho",                &phoIdMva_rho_);
  phoIdMva_EB_->BookMVA(mvamethod.c_str(), xmlfilenameEB);

  // **** bdt 2015 EE ****

  phoIdMva_EE_ = make_shared<TMVA::Reader>("!Color:Silent");

  phoIdMva_EE_->AddVariable("SCRawE",             &phoIdMva_SCRawE_);
  phoIdMva_EE_->AddVariable("r9",                 &phoIdMva_R9_);
  phoIdMva_EE_->AddVariable("sigmaIetaIeta",      &phoIdMva_covIEtaIEta_);
  phoIdMva_EE_->AddVariable("etaWidth",           &phoIdMva_EtaWidth_);
  phoIdMva_EE_->AddVariable("phiWidth",           &phoIdMva_PhiWidth_);
  phoIdMva_EE_->AddVariable("covIEtaIPhi",        &phoIdMva_covIEtaIPhi_);
  phoIdMva_EE_->AddVariable("s4",                 &phoIdMva_S4_);
  phoIdMva_EE_->AddVariable("phoIso03",           &phoIdMva_pfPhoIso03_);
  phoIdMva_EE_->AddVariable("chgIsoWrtChosenVtx", &phoIdMva_pfChgIso03_);
  phoIdMva_EE_->AddVariable("chgIsoWrtWorstVtx",  &phoIdMva_pfChgIso03worst_);
  phoIdMva_EE_->AddVariable("scEta",              &phoIdMva_ScEta_);
  phoIdMva_EE_->AddVariable("rho",                &phoIdMva_rho_);
  phoIdMva_EE_->AddVariable("esEffSigmaRR",       &phoIdMva_ESEffSigmaRR_);
  phoIdMva_EE_->BookMVA( mvamethod.c_str(), xmlfilenameEE);
}

float PhotonIdUtils::computeMVAWrtVtx(CandidatePhoton &photon,
                                      const edm::Ptr<reco::Vertex> &vtx,
                                      const double rho,
                                      const double correctedEtaWidth) {

  phoIdMva_SCRawE_          = photon.superCluster()->rawEnergy();
  phoIdMva_R9_              = photon.full5x5_r9();
  phoIdMva_S4_              = photon.s4();
  phoIdMva_covIEtaIEta_     = photon.full5x5_sigmaIetaIeta();
  phoIdMva_EtaWidth_        = (correctedEtaWidth == 0.) ? photon.superCluster()->etaWidth() : correctedEtaWidth;
  phoIdMva_PhiWidth_        = photon.superCluster()->phiWidth();
  phoIdMva_covIEtaIPhi_     = photon.sieip();
  phoIdMva_pfPhoIso03_      = photon.pfPhoIso03();
  phoIdMva_pfChgIso03_      = photon.pfChgIso03WrtVtx(vtx);
  phoIdMva_pfChgIso03worst_ = photon.pfChgIsoWrtWorstVtx03();
  phoIdMva_ScEta_           = photon.superCluster()->eta();
  phoIdMva_rho_             = rho; // we don't want to add the event-based rho as flashgg::photon member
  phoIdMva_ESEffSigmaRR_    = photon.esEffSigmaRR();

  phoIdMva = (photon.isEB()) ? phoIdMva_EB_ : phoIdMva_EE_;

  float mvavalue = phoIdMva->EvaluateMVA("BDT");
  return mvavalue;
}

map<edm::Ptr<reco::Vertex>, float> PhotonIdUtils::computeMVAWrtAllVtx(CandidatePhoton &photon,
                                                                      const vector<edm::Ptr<reco::Vertex> > &vertices,
                                                                      const double rho) {
  map<edm::Ptr<reco::Vertex>, float> mvamap;
  mvamap.clear();

  for(insigned int i = 0; i < vertices.size(); i++) {
    edm::Ptr<reco::Vertex> vertex = vertices[i];
    float MVAperVtx = computeMVAWrtVtx(photon, vertex, rho);
    mvamap.insert(make_pair(vertex, MVAperVtx));
  }

  return mvamap;
}

CandidatePhoton PhotonIdUtils::pho4MomCorrection(edm::Ptr<CandidatePhoton> &photon, edm::Ptr<reco::Vertex> vtx) {

  float vtx_X = vtx->x();
  float vtx_Y = vtx->y();
  float vtx_Z = vtx->z();

  float sc_X = photon->superCluster()->x();
  float sc_Y = photon->superCluster()->y();
  float sc_Z = photon->superCluster()->z();

  math::XYZVector vtx_Pos(vtx_X, vtx_Y, vtx_Z);
  math::XYZVector sc_Pos(sc_X, sc_Y, sc_Z);

  math::XYZVector direction = sc_Pos - vtx_Pos;
  math::XYZVector p = direction.Unit() * photon->energy();
  math::XYZTLorentzVector corrected_p4(p.x(), p.y(), p.z(), photon->energy());

  CandidatePhoton p4CorrPho = *photon;
  p4CorrPho.setP4(corrected_p4);

  return p4CorrPho;
}

void PhotonIdUtils::recomputeNonZsClusterShapes(reco::Photon &pho, noZS::EcalClusterLazyTools &tools) {

  reco::SuperClusterRef scRef = pho.superCluster();

  float maxXtal = tools.eMax(*(scRef->seed()));

  //Change these to consider severity level of hits
  float e1x5 = tools.e1x5(*(scRef->seed()));
  float e2x5 = tools.e2x5Max(*(scRef->seed()));
  float e3x3 = tools.e3x3(*(scRef->seed()));
  float e5x5 = tools.e5x5(*(scRef->seed()));
  vector<float> cov = tools.covariances(*(scRef->seed()));
  vector<float> locCov = tools.localCovariances(*(scRef->seed()));

  reco::Photon::ShowerShape showerShape;
  showerShape.e1x5 = e1x5;
  showerShape.e2x5 = e2x5;
  showerShape.e3x3 = e3x3;
  showerShape.e5x5 = e5x5;
  showerShape.maxEnergyXtal = maxXtal;
  showerShape.sigmaIetaIeta = sqrt(locCov[0]);
  showerShape.sigmaEtaEta = sqrt(cov[0]);

  pho.full5x5_setShowerShapeVariables(showerShape);

}

void PhotonIdUtils::recomputeNonZsClusterShapes(reco::Photon &pho, const EcalRecHitCollection *ebRecHits, const EcalRecHitCollection *eeRecHits, const CaloTopology *topology) {

  noZS::EcalClusterTools tools;

  reco::SuperClusterRef scRef = pho.superCluster();

  int subdetId = scRef->seed()->hitsAndFractions()[0].first.subdetId();
  const EcalRecHitCollection *hits = (subdetId == EcalBarrel) ? ebRecHits : eeRecHits;

  float e1x5 = noZS::EcalClusterTools::e1x5(*(scRef->seed()), &(*hits), &(*topology));
  float e2x5 = noZS::EcalClusterTools::e2x5Max(*(scRef->seed()), &(*hits), &(*topology));
  float e3x3 = noZS::EcalClusterTools::e3x3(*(scRef->seed()), &(*hits), &(*topology));
  float e5x5 = noZS::EcalClusterTools::e5x5(*(scRef->seed()), &(*hits), &(*topology));
  vector<float> locCov = noZS::EcalClusterTools::localCovariances(*(scRef->seed()), &(*hits), &(*topology));

  reco::Photon::ShowerShape showerShape;
  showerShape.e1x5 = e1x5;
  showerShape.e2x5 = e2x5;
  showerShape.e3x3 = e3x3;
  showerShape.e5x5 = e5x5;
  showerShape.maxEnergyXtal = maxXtal;
  showerShape.sigmaIetaIeta = sqrt(locCov[0]);

  pho.full5x5_setShowerShapeVariables(showerShape);

}

template<class T> static void PhotonIdUtils::SetRecHitFlags(CandidatePhoton &pho, T &lazyTool) {
  DetId seed = (pho.superCluster()->seed()->hitsAndFractions())[0].first;
  bool isBarrel = seed.subdetId() == EcalBarrel;
  const EcalRecHitCollection * rechits = isBarrel ? lazyTool.getEcalEBRecHitCollection() : lazyTool.getEcalEERecHitCollection()

  unsigned short nSaturated = 0, nLeRecovered = 0, nNeighRecovered = 0, nGain1 = 0, nGain6 = 0, nWeird = 0;
  auto matrix5x5 = lazyTool.matrixDetId(seed, -2, +2, -2, 2);

  for(auto & deId : matrix5x5) {
    auto rh = rechits->find(deId);
    if(rh != rechits->end()) {
      nSaturated += rh->checkFlag(EcalRecHit::kSaturated);
      nLeRecovered += rh->checkFlag(EcalRecHit::kLeadingEdgeRecovered);
      nNeighRecovered += rh->checkFlag(EcalRecHit::kNeighborsRecovered);
      nGain1 += rh->checkFlag(EcalRecHit::kHasSwitchToGain1);
      nGain6 += rh->checkFlag(EcalRecHit::kHasSwitchToGain6);
      nWeird += rh->checkFlag(EcalRecHit::kWeird) || rh->checkFlag(EcalRecHit::kDiWeird);
    }
  }

  if(isSaturated)      pho.isSaturated_ = true;
  if(isLeRecovered)    pho.isLeRecovered_ = true;
  if(isNeighRecovered) pho.isNeighRecovered_ = true;
  if(isGain1)          pho.isGain1_ = true;
  if(isGain6)          pho.isGain6_ = true;
  if(isWeird)          pho.isWeird_ = true;
}
