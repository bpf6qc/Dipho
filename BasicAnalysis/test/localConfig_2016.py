from OSUT3Analysis.Configuration.configurationOptions import *
from Dipho.BasicAnalysis.miniAODV2Samples import *

config_file = "protoConfig_2016_cfg.py"

intLumi = 2596.910 # Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON.txt

InputCondorArguments = {'request_memory': '2048MB', 'request_cpus': '1'}

datasetsData = [
    'DoubleEG_2016B',
]

datasets = datasetsData
