import pandas as pd
import numpy as np
import os
import shutil

# November 13, 2024
# Bloom, Hamilton

root_path = "data/batteries/"
metadata_path = "data/metadata.csv"
df = pd.read_csv(metadata_path, header=0)
battery_names = np.unique(df['battery_id'])

for battery in battery_names:
    try:
        os.mkdir(root_path + battery + "/Impedance/")
        os.mkdir(root_path + battery + "/Charge/")
        os.mkdir(root_path + battery + "/Discharge/")
    except:
        print("Sub-directory already created")

    data = df[df['battery_id'] == battery]

    idf = data[data['type'] == 'impedance']
    cdf = data[data['type'] == 'charge']
    ddf = data[data['type'] == 'discharge']

    icsv = idf['filename'].to_numpy()
    ccsv = cdf['filename'].to_numpy()
    dcsv = ddf['filename'].to_numpy()

    try:
        for csv in icsv:
            shutil.move(root_path + battery + "/" + csv, root_path + battery + "/Impedance/")
        for csv in ccsv:
            shutil.move(root_path + battery + "/" + csv, root_path + battery + "/Charge/")
        for csv in dcsv:
            shutil.move(root_path + battery + "/" + csv, root_path + battery + "/Discharge/")
    except:
        print("Files already moved.")

    
    