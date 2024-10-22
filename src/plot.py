import matplotlib.pyplot as plt
import numpy as np

temps = np.loadtxt("temperature.csv", delimiter=",")
pos = np.loadtxt("position.csv", delimiter=",")
time = np.loadtxt("time.csv", delimiter=",")

for i in range(temps.shape[0]):
    plt.plot(pos, temps[i, :])

plt.show()