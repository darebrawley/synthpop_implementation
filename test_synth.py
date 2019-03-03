# %load_ext autoreload
# %autoreload 2
from synthpop.recipes.starter2 import Starter
from synthpop.synthesizer import synthesize_all, enable_logging
import os
import pandas as pd
enable_logging()

# setting API Key
os.environ["CENSUS"] = "d95e144b39e17f929287714b0b8ba9768cecdc9f"
starter = Starter(os.environ["CENSUS"], "NC", "Mecklenburg County")
ind = pd.Series(["37", "119", "005706", "4"], index=["state", "county", "tract", "block group"])
output = synthesize_all(starter, indexes=[ind])
output.to_csv("data/test_synth_output.csv")
