import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib as mpl

import os

def fn(dir):
    num_of_files = 0
    for root, subdirs, files in os.walk(dir):
        if len(files) != 0:
            num_of_files += len(files)

    return num_of_files

fn("lfw")