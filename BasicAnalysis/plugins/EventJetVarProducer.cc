#ifndef EVENT_JET_VAR_PRODUCER
#define EVENT_JET_VAR_PRODUCER

#include "OSUT3Analysis/AnaTools/interface/EventVariableProducer.h"
#include "TLorentzVector.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "OSUT3Analysis/AnaTools/interface/DataFormat.h"
#include "OSUT3Analysis/AnaTools/interface/ValueLookupTree.h"
#include "OSUT3Analysis/AnaTools/interface/CommonUtils.h"
#include "DataFormats/VertexReco/interface/Vertex.h"

class EventJetVarProducer : public EventVariableProducer {
public:
  EventJetVarProducer (const edm::ParameterSet &);
  ~EventJetVarProducer ();

private:
  void AddVariables(const edm::Event &);
  edm::EDGetTokenT<vector<TYPE(jets)> > tokenJets_;
  edm::EDGetTokenT<vector<TYPE(mets)>  > tokenMets_;

  bool IsValidJet(const TYPE(jets) & jet);
};



EventJetVarProducer::EventJetVarProducer(const edm::ParameterSet &cfg) :
  EventVariableProducer(cfg)
{
  tokenJets_      = consumes<vector<TYPE(jets)> >      (collections_.getParameter<edm::InputTag> ("jets"));
  tokenMets_      = consumes<vector<TYPE(mets)> >      (collections_.getParameter<edm::InputTag> ("mets"));

}

EventJetVarProducer::~EventJetVarProducer() {}

bool
EventJetVarProducer::IsValidJet(const TYPE(jets) & jet){

  if (!(jet.pt() > 30))         return false;
  if (!(fabs(jet.eta()) < 4.5)) return false;
  if (!anatools::jetPassesTightLepVeto (jet)) return false;

  return true;
}


void
EventJetVarProducer::AddVariables (const edm::Event &event) {

  edm::Handle<vector<TYPE(jets)> > jets;
  if (!event.getByToken (tokenJets_, jets)) {
    clog << "ERROR:  Could not find jets collection." << endl;
    return;
  }

  edm::Handle<vector<TYPE(mets)> > mets;
  if (!event.getByToken (tokenMets_, mets)) {
    clog << "ERROR:  Could not find mets collection." << endl;
    return;
  }

  int nJets = 0;
  double dijetMaxDeltaPhi         = -999.;  // default is large negative value
  double deltaPhiMetJetLeading    =  999.;  // default is large positive value
  double deltaPhiMetJetSubleading =  999.;
  double ptJetLeading    = -999;
  double ptJetSubleading = -999;
  int idx1 = -1;
  for (const auto &jet1 : *jets) {
    idx1++;
    if (!IsValidJet(jet1)) continue;
    int idx2 = -1;
    if (jet1.pt() > ptJetSubleading) {
      double dPhi = fabs(deltaPhi(jet1, mets->at(0)));
      if (jet1.pt() > ptJetLeading) {
        ptJetSubleading = ptJetLeading;
        deltaPhiMetJetSubleading = deltaPhiMetJetLeading;
        ptJetLeading = jet1.pt();
        deltaPhiMetJetLeading = dPhi;
      } else {
        ptJetSubleading = jet1.pt();
        deltaPhiMetJetSubleading = dPhi;
      }
    }
    for (const auto &jet2 : *jets) {
      idx2++;
      if (idx2 <= idx1)              continue;  // Avoid double-counting.
      if (!IsValidJet(jet2)) continue;
      double dPhi = fabs(deltaPhi(jet1.phi(), jet2.phi()));
      if (dPhi > dijetMaxDeltaPhi) {
        dijetMaxDeltaPhi = dPhi;
      }
    }
    nJets++;
  }

  (*eventvariables)["nJets"]            = nJets;
  (*eventvariables)["dijetMaxDeltaPhi"] = dijetMaxDeltaPhi;
  (*eventvariables)["deltaPhiMetJetLeading"]     = deltaPhiMetJetLeading;
  (*eventvariables)["deltaPhiMetJetSubleading"]  = deltaPhiMetJetSubleading;

}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(EventJetVarProducer);


#endif
