#include "Dipho/Investigation/interface/CandidatePhoton.h"

#include "DataFormats/EcalRecHit/interface/EcalRecHitCollections.h"
#include "RecoEcal/EgammaCoreTools/interface/EcalClusterLazyTools.h"

// FIXME:  Once OSUT3Analysis works with ROOT6, i.e., releases > CMSSW_7_4_5_ROOT5,
// then uncomment the following line:
// #include "OSUT3Analysis/AnaTools/interface/DataFormat.h"
// and remove these two lines:
#define INVALID_VALUE (numeric_limits<int>::min ())
#define IS_INVALID(x) (x <= INVALID_VALUE + 1)

CandidatePhoton::CandidatePhoton() :
  isSaturated_      (false),
  isLeRecovered_    (false),
  isNeighRecovered_ (false),
  isGain1_          (false),
  isGain6_          (false),
  isWeird_          (false)
{

}

CandidatePhoton::CandidatePhoton(const pat::Photon &photon) :
  pat::Photon(photon),
  isSaturated_      (false),
  isLeRecovered_    (false),
  isNeighRecovered_ (false),
  isGain1_          (false),
  isGain6_          (false),
  isWeird_          (false)
{

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
