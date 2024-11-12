import math
import numpy as np
import pandas as pd
import scipy

import kagglehub

# Download latest version
path = kagglehub.dataset_download("patrickfleith/nasa-battery-dataset")

#File Selection
files = [""]
fileselect = files[]
path = "../../../data/" + fileselect
data = np.genfromtxt(path, delimiter=',')

