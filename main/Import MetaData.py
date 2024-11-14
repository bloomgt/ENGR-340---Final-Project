import pandas as pd
import numpy as np
import os
import shutil

file_path = "data/metadata.csv"

file_path = path_to_dir + metadata_path

df = pd.read_csv(file_path, header=0)

battery_names = np.unique(df['battery_id'])

dict = {}

try:
    os.mkdir ("data/batteries")
except:
    print("Directories already created.")

for id in battery_names:
    data = df[df['battery_id'] == id]
    csv_array = data['filename'].to_numpy()
    dict[id] = csv_array
    try:
        os.mkdir("data/batteries/" + id)
    except:
        print()
    file_dir = "data/data/"
    move_to = "data/batteries/" + id
    for file in csv_array:
        shutil.move(file_dir + file, move_to)
