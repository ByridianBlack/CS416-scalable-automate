import sys
import os
from matplotlib import pyplot as plt
import numpy as np

names = ["naive_counter.png", "naive_counter_plus.png", "atomic_counter.png", "scalable_counter.png"]

def write_data():
    
    number_of_threads = 0
    for x in range(4):
        for y in range(6):
            number_of_threads = pow(2, y)
            if x == 0:
                os.system("./naive_counter " + str(number_of_threads) + " >> datafile.txt")
            elif x == 1:
                os.system("./naive_counter_plus " + str(number_of_threads) + " >> datafile.txt")
            elif x == 2:
                os.system("./atomic_counter " + str(number_of_threads) + " >> datafile.txt")
            elif x == 3:
                os.system("./scalable_counter " + str(number_of_threads) + " >> datafile.txt")          

def read_and_plot():
    
    x_axis = [1,2,4,8,16,32]
    y_axis = []


    with open("datafile.txt", "r") as NFILE:
        number_of_threads = 0
        for x in range(4):
            for y in range(6):
                # number_of_threads = pow(2, y)
                line = NFILE.readline()
                # x_axis.append(number_of_threads)
                y_axis.append(int(line.split(" ")[-2]))
                NFILE.readline()
                NFILE.readline()
            plt.scatter(x_axis, sorted(y_axis))
            plt.plot(np.unique(x_axis), np.poly1d(np.polyfit(x_axis, sorted(y_axis), 1))(np.unique(x_axis)))
            plt.xlabel("Number of Threads")
            plt.ylabel("Running Time (ms)")
            plt.savefig("./"+str(names[x]))
            plt.close()
            y_axis = []


# write_data()
read_and_plot()