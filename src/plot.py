import matplotlib.pyplot as plt
import numpy as np

temps = np.loadtxt("./out/temperature.csv", delimiter=",")
pos = np.loadtxt("./out/position.csv", delimiter=",")
time = np.loadtxt("./out/time.csv", delimiter=",")
max_temp = np.max(temps)
min_temp = np.min(temps)
min_pos = np.min(pos)
max_pos = np.max(pos)


for i in range(temps.shape[0]):
    plt.plot(pos, temps[i, :], label=f"{time[i]:.3f}")

plt.xlim((min_pos, max_pos))
plt.ylim((min_temp, max_temp))
plt.xlabel("Radial Position [m]")
plt.ylabel("Temperature [K]")
plt.legend(bbox_to_anchor=(1, 1), title="Time [s]")

plt.show()
