import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#
# Basic Discharge Analysis
# Look at elementary statistics from each battery
# Including max charge voltage and total discharge time
#

# Create list of every battery in entire dataset
metadata_path = "data/metadata.csv"
df = pd.read_csv(metadata_path, header=0)
battery_names = np.unique(df['battery_id'])

for test_battery in battery_names:

    # Create list to store data we are interested in for
    # the specific battery we are currently looking at
    voltage_data = list()
    time_data = list()

    # Create list containing file name of each discharge
    # csv data for the specific battery we are looking at
    dir_path = "data/batteries/" + test_battery + "/Discharge/"
    files = os.listdir(dir_path)

    # Look at each discharge data file
    for file in files:

        # Store the data from that file in a np array
        file_path = "data/batteries/" + test_battery + "/Discharge/" + file
        file_data = np.loadtxt(file_path, delimiter=",", skiprows=1)

        # Grab the max voltage data and total time for this trial
        # and put it in the time and voltage list
        voltage_data.append(max(file_data[:,0]))
        time_data.append(file_data[-1,-1])

    # Create line of best fit for the time to discharge data
    numbers = np.arange(0,len(time_data))
    slope, intercept = np.polyfit(numbers, time_data, deg=1)
    best_fit = numbers*slope + intercept

    print(f"Lifetime reduction per cycle (seconds): {abs(slope)}")

    # Plot the max voltage per cycle and time to discharge per cycle
    # For the current battery we are looking at
    fig, axs = plt.subplots(1,2, figsize =(15,5))

    axs[0].set_title("Max Voltage per Cycle of " + test_battery)
    axs[0].plot(voltage_data, label="Volts [V]")
    axs[0].legend()
    axs[1].set_title("Time to Discharge per Cycle of " + test_battery)
    axs[1].plot(time_data, label="Time [s]")
    axs[1].plot(best_fit, label="Linear Approx")
    axs[1].legend()
    plt.tight_layout()
    plt.show()

    # Move on to next battery and repeat
