
# %load_ext autoreload
# %autoreload 2
from synthpop.recipes.starter2 import Starter
from synthpop.synthesizer import synthesize_all, enable_logging
import os
import pandas as pd
enable_logging()

# setting API Key
os.environ["CENSUS"] = "d95e144b39e17f929287714b0b8ba9768cecdc9f"

def synthesize_counties(counties):
    for county in counties:
        starter = Starter(os.environ["CENSUS"], "RI", county)
        synthesize_all(starter)
hh = synthesize_counties(["Kent County"])
hh.to_csv("output.csv")
