import pandas as pd
import numpy as np
import os
import shutil


# Create Dataframe with all metadata data
file_path = "data/metadata.csv"
df = pd.read_csv(file_path, header=0)

# Create list of each battery name
battery_names = np.unique(df['battery_id'])

# Create folders to store battery data
try:
    os.mkdir ("data/batteries")
except:
    print("Directories already created.")


# Look at each unique Battery ID
for id in battery_names:

    # Store csv file names in the dictionary
    data = df[df['battery_id'] == id]           # Create sub-dataframe for current unique Battery ID
    csv_array = data['filename'].to_numpy()     # Grab all csv file names

    # Create sub-directory for the current unique Battery ID
    try:
        os.mkdir("data/batteries/" + id)
    except:
        print("Sub-directory already created.")

    # Move each associated csv files into new subdirectory
    file_dir = "data/data/"
    move_to = "data/batteries/" + id
    for file in csv_array:
        shutil.move(file_dir + file, move_to)
