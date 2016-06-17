#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "FWCore/Framework/interface/ESHandle.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
#include "Geometry/Records/interface/CaloGeometryRecord.h"

#include "Dipho/Investigation/interface/CandidatePhoton.h"
#include "Dipho/Investigation/interface/PhotonIdUtils.h"

#include "DataFormats/EcalRecHit/interface/EcalRecHitCollections.h"
#include "DataFormats/HcalRecHit/interface/HcalRecHitCollections.h"

using namespace std;

struct CaloIsoParams {
  CaloIsoParams() {};
  CaloIsoParams(bool overlapRemoval, PFCandidate::ParticleType type, const vector<double> &vetos) :
    overlapRemoval_(overlapRemoval), type_(type), vetos_(vetos) {};

  bool overlapRemoval_;
  PFCandidate::ParticleType type_;
  vector<double> vetos_;
};

class CandidatePhotonProducer : public edm::EDProducer {
  public:
    explicit CandidatePhotonProducer(const edm::ParameterSet&);
    ~CandidatePhotonProducer();

  private:
    virtual void produce(edm::Event&, const edm::EventSetup&) override;

    edm::EDGetTokenT<vector<pat::Photon> > photonToken_;
    edm::EDGetTokenT<vector<reco::Vertex> > vertexToken_;
    edm::EDGetTokenT<vector<VertexCandidateMap> vertexCandidateMapToken_;
    edm::EDGetTokenT<double> rhoToken_;
    edm::EDGetTokenT<EcalRecHitCollection> ecalHitEBToken_;
    edm::EDGetTokenT<EcalRecHitCollection> ecalHitEEToken_;
    edm::EDGetTokenT<EcalRecHitCollection> ecalHitESToken_;

    PhotonIdUtils phoTools;
    edm::FileInPath phoIdMVAweightfileEB_, phoIdMVAweightfileEE_;

    bool useNonZsLazyTools_;
    bool verbose_;

};
