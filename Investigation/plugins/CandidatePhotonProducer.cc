#include "Dipho/Investigation/interface/CandidatePhoton.h"
#include "Dipho/Investigation/interface/CandidatePhotonProducer.cc"

#include "DataFormats/VertexReco/interface/Vertex.h"
#include "RecoEcal/EgammaCoreTools/interface/EcalClusterLazyTools.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

using namespace std;

CandidatePhotonProducer::CandidatePhotonProducer(const edm::ParameterSet& iConfig) :
  photonToken_       (consumes<vector<pat::Photon> >(iConfig.getParameter<edm::InputTag>("photons"))),
  vertexToken_       (consumes<vector<reco::Vertex> >(iConfig.getParameter<edm::InputTag>("vertices"))),
  vertexCandidateMapToken_ (consumes<vector<VertexCandidateMap>(iConfig.getParameter<edm::InputTag>("vertexCandidateMapTag"))),
  rhoToken_ (consumes<double>(iConfig.getParameter<edm::InputTag>("rhoFixedGridCollection"))),
  ecalHitEBToken_    (consumes<EcalRecHitCollection>(iConfig.getParameter<edm::InputTag>("reducedBarrelRecHitCollection"))),
  ecalHitEEToken_    (consumes<EcalRecHitCollection>(iConfig.getParameter<edm::InputTag>("reducedEndcapRecHitCollection"))),
  ecalHitESToken_    (consumes<EcalRecHitCollection>(iConfig.getParameter<edm::InputTag>("reducedPreshowerRecHitCollection"))),
  useNonZsLazyTools_ (iConfig.getParameter<bool>("useNonZsLazyTools"))
{

  phoIdMVAweightfileEB_ = iConfig.getParameter<edm::FileInPath>("photonIdMVAweightfile_EB");
  phoIdMVAweightfileEE_ = iConfig.getParameter<edm::FileInPath>("photonIdMVAweightfile_EE");
  phoTools_.setupMVA(phoIdMVAweightfileEB_.fullPath(), phoIdMVAweightfileEE_.fullPath());

  produces<vector<CandidatePhoton> >();

  verbose_ = false;

}

CandidatePhotonProducer::~CandidatePhotonProducer() {
}

void CandidatePhotonProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {

  edm::Handle<vector<pat::Photon> > photons;
  iEvent.getByToken(photonsToken_, photons);

  edm::Handle<vector<reco::Vertex> > vertices;
  iEvent.getByToken(vertexToken_, vertices);

  // VertexCandidateMap?

  edm::Handle<double> rhohandle;
  iEvent.getByToken(rhoToken_, rhoHandle);

  PhotonIdUtils phoTools;

  const double rhoFixedGrd = *(rhoHandle.product());
  const reco::Vertex *neutVtx = useVtx0ForNeutralIso_ ? &vertices->at(0) : 0;

  EcalClusterLazyTools zsLazyTool(iEvent, iSetup, ecalHitEBToken_, ecalHitEEToken_, ecalHitESToken_);
  noZS::EcalClusterLazyTools noZsLazyTool(iEvent, iSetup, ecalHitEBToken_, ecalHitEEToken_, ecalHitESToken_);

  for(unsigned int i = 0; i < photons->size(); i++) {
    Ptr<pat::Photon> pp = photons->ptrAt(i);
    CandidatePhoton cand = CandidatePhoton(*pp);

    if(useNonZsLazyTools_) phoTools.SetRecHitFlags(cand, noZsLazyTool);
    else phoTools.SetRecHitFlags(cand, zsLazyTool);

    map<edm::Ptr<reco::Vertex>, float> mvamap = phoTools.computeMVAWrtAllVtx(cand, vertices->ptrs(), rhoFixedGrd);
    cand.SetPhoIdMvaD(mvamap);

  }


}
