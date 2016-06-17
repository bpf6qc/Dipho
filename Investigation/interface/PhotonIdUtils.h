#ifndef PHOTONIDUTILS_H
#define PHOTONIDUTILS_H

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Common/interface/Ptr.h"
//#include "DataFormats/Common/interface/PtrVector.h"
#include "DataFormats/Common/interface/RefToPtr.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidateFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"

#include "Dipho/Investigation/interface/CandidatePhoton.h"
#include "Dipho/Investigation/interface/VertexCandidateMap.h"

#include "DataFormats/EcalRecHit/interface/EcalRecHitCollections.h"
#include "RecoEcal/EgammaCoreTools/interface/EcalClusterLazyTools.h"
/// class EcalRecHitCollection;
class CaloTopology;

#include <TMVA/Reader.h>

using namespace std;

class OverlapRemovalAlgo {
  public:
    virtual bool operator() (const pat::Photon &photon, const edm::Ptr<pat::PackedCandidate> &pfcand) = 0;
};

class PhotonIdUtils {
  public:
    PhotonIdUtils(OverlapRemovalAlgo * algo = 0);
    ~PhotonIdUtils();

    void initialize();

    float pfIsoChgWrtVtx(const edm::Ptr<pat::Photon> &,
                         const edm::Ptr<reco::Vertex>,
                         const flashgg::VertexCandidateMap,
                         float, float, float, float);
    map<edm::Ptr<reco::Vertex>, float> pfIsoChgWrtAllVtx(const edm::Ptr<pat::Photon> &,
                                                         const vector<edm::Ptr<reco::Vertex> > &,
                                                         const VertexCandidateMap,
                                                         float, float, float, float);

    float pfIsoChgWrtWorstVtx(map<edm::Ptr<reco::Vertex>, float> &);

    float pfCaloIso(const edm::Ptr<pat::Photon> &,
                    const vector<edm::Ptr<pat::PackedCandidate> > &,
                    float, float, float, float, float, float, float,
                    reco::PFCandidate::ParticleType, const reco::Vertex *vtx = 0);

    void setupMVA(const string &, const string &);
    float computeMVAWrtVtx(CandidatePhoton &, const edm::Ptr<reco::Vertex> &, const double, const double etaWidth = 0);

    static CandidatePhoton pho4MomCorrection(edm::Ptr<CandidatePhoton> &, edm::Ptr<reco::Vertex>);

    math::XYZTLorentzVector pho4MomCorrectionTLVector(edm::Ptr<CandidatePhoton> &, edm::Ptr<reco::Vertex>);

    static bool vetoPackedCand(const pat::Photon &photon, const edm::Ptr<pat::PackedCandidate> &pfcand);

    map<edm::Ptr<reco::Vertex>, float> computeMVAWrtAllVtx(CandidatePhoton &, const vector<edm::Ptr<reco::Vertex> > &, const double);

    shared_ptr<TMVA::Reader> phoIdMva;

    void removeOverlappingCandidates( bool x ) { removeOverlappingCandidates_ = x; };
    void deltaPhiRotation( double x ) { deltaPhiRotation_ = x; };

    static void recomputeNonZsClusterShapes(reco::Photon &pho, noZS::EcalClusterLazyTools &tools);
    static void recomputeNonZsClusterShapes(reco::Photon &pho,
                                            const EcalRecHitCollection *ebRecHits, const EcalRecHitCollection *eeRecHits,
                                            const CaloTopology *topology );

    template<class T> static void fillExtraClusterShapes(CandidatePhoton &pho, T &lazyTool) {
      const reco::CaloClusterPtr seed_clu = pho.superCluster()->seed();
      const reco::SuperClusterRef super_clu = pho.superCluster();

      vector<float> viCov = lazyTool.localCovariances(*seed_clu);

      pho.setSipip( viCov[2] );
      pho.setSieip( viCov[1] );
      pho.setE2nd( lazyTool.e2nd( *seed_clu ) );
      pho.setE2x5right( lazyTool.e2x5Right( *seed_clu ) );
      pho.setE2x5left( lazyTool.e2x5Left( *seed_clu ) );
      pho.setE2x5top( lazyTool.e2x5Top( *seed_clu ) );
      pho.setE2x5bottom( lazyTool.e2x5Bottom( *seed_clu ) );
      pho.setE2x5max( lazyTool.e2x5Max( *seed_clu ) );
      pho.setEright( lazyTool.e2x5Right( *seed_clu ) );
      pho.setEleft( lazyTool.e2x5Left( *seed_clu ) );
      pho.setEtop( lazyTool.e2x5Top( *seed_clu ) );
      pho.setEbottom( lazyTool.e2x5Bottom( *seed_clu ) );
      pho.setE1x3( lazyTool.e1x3( *seed_clu ) );
      pho.setS4( lazyTool.e2x2( *seed_clu ) / lazyTool.e5x5( *seed_clu ) );
      pho.setESEffSigmaRR( lazyTool.eseffsirir( *super_clu ) );
    }

    template<class T> static void SetRecHitFlags(CandidatePhoton &pho, T &lazyTool);

  private:

    OverlapRemovalAlgo *overlapAlgo_;
    bool removeOverlappingCandidates_;
    double deltaPhiRotation_;

    float phoIdMva_SCRawE_;
    float phoIdMva_R9_;
    float phoIdMva_covIEtaIEta_;
    float phoIdMva_PhiWidth_;
    float phoIdMva_EtaWidth_;
    float phoIdMva_covIEtaIPhi_;
    float phoIdMva_S4_;
    float phoIdMva_pfPhoIso03_;
    float phoIdMva_pfChgIso03_;
    float phoIdMva_pfChgIso03worst_;
    float phoIdMva_ScEta_;
    float phoIdMva_rho_;
    float phoIdMva_ESEffSigmaRR_;

    shared_ptr<TMVA::Reader> phoIdMva_EB_;
    shared_ptr<TMVA::Reader> phoIdMva_EE_;
};

#endif
