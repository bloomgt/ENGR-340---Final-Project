import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
#
# Basic Discharge Analysis
#
# November 13, 2024
# Bloom, Hamilton
#

#test_battery = 15
metadata_path = "data/metadata.csv"
df = pd.read_csv(metadata_path, header=0)
battery_names = np.unique(df['battery_id'])


print(len(battery_names))

for test_battery in battery_names:
    voltage_data = list()
    time_data = list()
    dir_path = "data/batteries/" + test_battery + "/Discharge/"
    files = os.listdir(dir_path)
    for file in files:
        file_path = "data/batteries/" + test_battery + "/Discharge/" + file
        file_data = np.loadtxt(file_path, delimiter=",", skiprows=1)
        voltage_data.append(max(file_data[:,0]))
        time_data.append(file_data[-1,-1])


    numbers = np.arange(0,len(time_data))
    slope, intercept = np.polyfit(numbers, time_data, deg=1)
    print(f"Lifetime reduction per cycle (seconds): {abs(slope)}")
    best_fit = numbers*slope + intercept


    fig, axs = plt.subplots(1,2, figsize =(15,5))

    axs[0].set_title("Max Voltage per Cycle of " + battery_names[test_battery])
    axs[0].plot(voltage_data, label="Volts [V]")
    axs[0].legend()
    axs[1].set_title("Time to Discharge per Cycle of " + battery_names[test_battery])
    axs[1].plot(time_data, label="Time [s]")
    axs[1].plot(best_fit, label="Linear Approx")
    axs[1].legend()
    plt.tight_layout()
    plt.show()

dummy = 1