#ifndef CANDIDATEPHOTON_H
#define CANDIDATEPHOTON_H

#include "DataFormats/EgammaCandidates/interface/Photon.h"
#include "DataFormats/PatCandidates/interface/Photon.h"
#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"

using namespace std;

class CandidatePhoton : public pat::Photon
{

  public:
    CandidatePhoton();
    CandidatePhoton(const pat::Photon &);

    virtual void ~CandidateTrack() {};

    const bool isSaturated() { return isSaturated_; };
    const bool isLeRecovered() { return isLeRecovered_; };
    const bool isNeighRecovered() { return isNeighRecovered_; };
    const bool isGain1() { return isGain1_; };
    const bool isGain6() { return isGain6_; };
    const bool isWeird() { return isWeird_; };

    template<class T> static void SetRecHitFlags(CandidatePhoton &pho, T &lazyTool);

  private:

    bool isSaturated_;
    bool isLeRecovered_;
    bool isNeighRecovered_;
    bool isGain1_;
    bool isGain6_;
    bool isWeird_;

};

#endif
