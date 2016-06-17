from OSUT3Analysis.Configuration.configurationOptions import *
from Dipho.BasicAnalysis.miniAODV2Samples import *

config_file = "protoConfig_cfg.py"

intLumi = 2590.0 # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/595

InputCondorArguments = {'request_memory': '2048MB', 'request_cpus': '1'}

datasetsData = [
    'DoubleEG_2015D'
]

datasets = datasetsData
