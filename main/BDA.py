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
for i in range (25, 33):
    test_battery = i
    metadata_path = "data/metadata.csv"
    df = pd.read_csv(metadata_path, header=0)
    battery_names = np.unique(df['battery_id'])
    dir_path = "data/batteries/" + battery_names[test_battery] + "/Discharge/"
    files = os.listdir(dir_path)

    voltage_data = list()
    time_data = list()
    for file in files:
        file_path = "data/batteries/" + battery_names[test_battery] + "/Discharge/" + file
        file_data = np.loadtxt(file_path, delimiter=",", skiprows=1)
        voltage_data.append(max(file_data[:,0]))
        time_data.append(file_data[-1,-1])


    #plt.title("Max Voltage per Cycle of " + battery_names[test_battery])
    #plt.plot(voltage_data, label="Volts [V]")
    #plt.legend()
    #plt.show()

    numbers = np.arange(0,len(time_data))
    slope, intercept = np.polyfit(numbers, time_data, deg=1)
    best_fit = numbers*slope + intercept
    plt.title("Time to Discharge per Cycle of " + battery_names[test_battery] + str(i))
    plt.plot(time_data, label="Time [s]")
    plt.plot(best_fit, label="Linear Approx")
    plt.legend()
    plt.show()