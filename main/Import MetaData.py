import pandas as pd
import numpy as np
import kagglehub

# Download latest version
path = kagglehub.dataset_download("patrickfleith/nasa-battery-dataset")
data = np.genfromtxt(path, delimiter=',')


