import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#
# Questions 1 & 2 Analysis
#

# Create list of the batteries in each unique test case
t1 = ["B0005", "B0006", "B0007", "B0018"]
t2 = ["B0025", "B0026", "B0027", "B0028"]
t3 = ["B0029", "B0030", "B0031", "B0032"]
t4 = ["B0033", "B0034", "B0036"]
t5 = ["B0045", "B0046", "B0047", "B0048"]
test_cases = [t1, t2, t3, t4, t5]

# Look at each test case
case = 1
for test_case in test_cases:


    # Create lists to store data we are interested in for
    # the specific test case we are currently looking at
    time_elapsed = list()
    slope_list = list()

    # For each battery in the specific test case
    for battery in test_case:

        # Create lists to store important data
        voltage_data = list()
        time_data = list()

        # Create list of discharge files for the current battery
        files = list()
        dir_path = "data/batteries/" + battery + "/Discharge/"
        files = os.listdir(dir_path)

        # Get the total time elapsed to discharge a fresh new battery
        file_path1 = "data/batteries/" + battery + "/Discharge/" + files[0]
        file_data = np.loadtxt(file_path1, delimiter=",", skiprows=1)
        time_elapsed.append(file_data[-1,-1])

        # Look at the time elapsed for each consecutive charge/discharge cycle
        for file in files:

            # Store the data from that file in a np array
            file_path = "data/batteries/" + battery + "/Discharge/" + file
            file_data = np.loadtxt(file_path, delimiter=",", skiprows=1)

            # Grab the max voltage data and total time for this trial
            # and put it in the time and voltage list
            voltage_data.append(max(file_data[:, 0]))
            time_data.append(file_data[-1, -1])


        # Create line of best fit for the time to discharge data
        numbers = np.arange(0, len(time_data))
        slope, intercept = np.polyfit(numbers, time_data, deg=1)
        best_fit = numbers * slope + intercept

        # Place the slope into the list for this battery
        slope_list.append(abs(slope))


    # Find the average initial battery life for each battery in this test case
    average_init_duration = np.mean(time_elapsed)

    # Find the average time reduction for each battery in the test case
    average_slope = np.mean(slope_list)
    print(f"For Test Case {case}, battery life was: {average_init_duration.round(2)} "
          f"seconds and average time reduction was {average_slope.round(2)} seconds.")
    print(f"Average percent reduction was {((average_slope/average_init_duration) * 100).round(2)}%.\n")

    # Increment the test case we are looking at
    case += 1

    # Move on to next battery and repeat
