import matplotlib.pyplot as plt
import numpy as np

temps = np.loadtxt("./out/temperature.csv", delimiter=",")
pos = np.loadtxt("./out/position.csv", delimiter=",")
time = np.loadtxt("./out/time.csv", delimiter=",")

for i in range(temps.shape[0]):
    plt.plot(pos, temps[i, :])

plt.show()