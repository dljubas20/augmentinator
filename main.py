from typing import Final

import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib as mpl
import augment as ag

import os

NUM_OF_ROTATIONS : Final[int] = 4

def fn(dir):
    for root, subdirs, files in os.walk(dir):
        if len(files) != 0:
            for f in files:
                ag.rotateImg(os.path.join(root, os.path.basename(f)), NUM_OF_ROTATIONS)

if os.path.isdir("new") == False:
        os.mkdir("new")

fn("lfw")