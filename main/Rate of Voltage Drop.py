import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#
# Question 3 Analysis
#
#

# Create list of every battery in entire dataset
metadata_path = "data/metadata.csv"
df = pd.read_csv(metadata_path, header=0)
battery_names = np.unique(df['battery_id'])

#For each battery
for test_battery in battery_names:

    # Keep track of cycle count, updated at the end of the loop
    cycle = 1

    # Create list containing file name of each discharge
    # csv data for the specific battery we are looking at
    dir_path = "data/batteries/" + test_battery + "/Discharge/"
    files = os.listdir(dir_path)

    # Look at each discharge data file
    for file in files:

        # Create list to store data we are interested in for
        # the specific battery we are currently looking at
        voltage_data = list()
        time_data = list()

        # Store the data from that file in a np array
        file_path = "data/batteries/" + test_battery + "/Discharge/" + file
        file_data = np.loadtxt(file_path, delimiter=",", skiprows=1)

        # Grab the max voltage data and total time for this trial
        # and put it in the time and voltage list
        voltage_data = file_data[:,0]
        time_data = file_data[:,-1]

        # Create a directory for the Rate of Voltage Drop Plots
        file_dir = "data/analysis/ROVD Plot/" + test_battery
        try:
            os.mkdir(file_dir)
        except:
            print("Sub-directory already created")


        # Plot the battery voltage over time of discharging
        # For the current battery we are looking at and save
        plt.clf()
        plt.title("Voltage Drop over Time of " + test_battery + " Cycle: " + str(cycle))
        plt.plot( time_data, voltage_data, label="Volts [V]")
        plt.legend()
        plt.savefig(file_dir + "/ Cycle " + str(cycle) + "-ROVD.jpeg")

        # Increment cycle count
        cycle += 1

    # Move on to next battery and repeat
