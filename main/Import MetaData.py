import pandas as pd
import numpy as np


file_path = path_to_dir + metadata_path

df = pd.read_csv(file_path, header=0)

battery_names = np.unique(df['battery_id'])

dict = {}

for id in battery_names:
    data = df[df['battery_id'] == id]
    dict[id] = data['filename'].to_numpy()
