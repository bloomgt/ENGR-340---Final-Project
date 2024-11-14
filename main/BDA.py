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


    plt.title("Max Voltage per Cycle of " + test_battery)
    plt.plot(voltage_data, label="Volts [V]")
    plt.legend()
    plt.show()

    numbers = np.arange(0,len(time_data))
    slope, intercept = np.polyfit(numbers, time_data, deg=1)
    print(f"Lifetime reduction per cycle (seconds): {abs(slope)}")
    best_fit = numbers*slope + intercept
    plt.title("Time to Discharge per Cycle of " + test_battery)
    plt.plot(time_data, label="Time [s]")
    plt.plot(best_fit, label="Linear Approx")
    plt.legend()
    plt.show()
