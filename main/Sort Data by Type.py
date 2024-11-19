import pandas as pd
import numpy as np
import os
import shutil

# Create list of all unique Battery ID's
root_path = "data/batteries/"
metadata_path = "data/metadata.csv"
df = pd.read_csv(metadata_path, header=0)
battery_names = np.unique(df['battery_id'])

# Look at each unique battery
for battery in battery_names:

    # Create directories for the impedance, charging, and discharging data
    try:
        os.mkdir(root_path + battery + "/Impedance/")
        os.mkdir(root_path + battery + "/Charge/")
        os.mkdir(root_path + battery + "/Discharge/")
    except:
        print("Sub-directory already created")

    # Create sub-dataframe for the current unique battery
    data = df[df['battery_id'] == battery]

    #impedence, charge, discharge sub-dataframe
    idf = data[data['type'] == 'impedance']
    cdf = data[data['type'] == 'charge']
    ddf = data[data['type'] == 'discharge']

    # create list of corresponding csv files
    icsv = idf['filename'].to_numpy()
    ccsv = cdf['filename'].to_numpy()
    dcsv = ddf['filename'].to_numpy()

    # Move csv files to correct sub-directory
    try:
        for csv in icsv:
            shutil.move(root_path + battery + "/" + csv, root_path + battery + "/Impedance/")
        for csv in ccsv:
            shutil.move(root_path + battery + "/" + csv, root_path + battery + "/Charge/")
        for csv in dcsv:
            shutil.move(root_path + battery + "/" + csv, root_path + battery + "/Discharge/")
    except:
        print("Files already moved.")

# Repeat for next battery
