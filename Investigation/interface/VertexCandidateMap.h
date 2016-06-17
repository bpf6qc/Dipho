#ifndef VertexCandidateMap_h
#define VertexCandidateMap_h

#include "DataFormats/Common/interface/Ptr.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
#include <string>
#include <iostream>

using namespace std;

typedef pair<edm::Ptr<reco::Vertex>, edm::Ptr<pat::PackedCandidate> > VertexCandidatePair;
typedef vector<VertexCandidatePair> VertexCandidateMap;

struct compare_by_vtx {
  bool operator() (const VertexCandidatePair &left, const VertexCandidatePair &right ) { return (left.first < right.first); }
};

struct compare_with_vtx {
  bool operator() (const VertexCandidatePair &left, const edm::Ptr<reco::Vertex> &right) { return (left.first < right); }
  bool operator() (const edm::Ptr<reco::Vertex> &left, const VertexCandidatePair &right) { return(left < right.first); }
};

struct compare_by_cand {
  bool operator() (const VertexCandidatePair &left, const VertexCandidatePair &right) { return (left.second < right.second); }
};

struct compare_with_cand {
  bool operator() (const VertexCandidatePair &left, const edm::Ptr<pat::PackedCandidate> &right) { return (left.second < right); }
  bool operator() (const edm::Ptr<pat::PackedCandidate> &left, const VertexCandidatePair &right) { return (left < right.second); }
};

void print_track_count(const VertexCandidateMap &theMap, string s) {

  int nvtx = -1;
  int ntrk = 0;
  edm::Ptr<reco::Vertex> current_vtx;

  for(auto current_pair = theMap.begin(); current_pair != theMap.end(); current_pair++) {
    if(current_vtx != current_pair->first) {
      if(nvtx >= 0) cout << " " << s << ": Vertex " << nvtx << " had " << ntrk << " candidates" << endl;
      nvtx++;
      ntrk = 0;
      current_vtx = current_pair->first;
    }
    cout << "   " << s << ": Vertex " << nvtx << " trk " << ntrk << " pt eta charge dz " << current_pair->second->pt() << " " << current_pair->second->eta()
         << " " << current_pair->second->charge()
         << " " << current_pair->second->dz( current_pair->first->position() ) << endl;
    ntrk++;
  }
}

#endif
