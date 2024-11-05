import matplotlib.pyplot as plt
import numpy as np

temps = np.loadtxt("./out/temperature.csv", delimiter=",")
pos = np.loadtxt("./out/position.csv", delimiter=",")
time = np.loadtxt("./out/time.csv", delimiter=",")
max_temp = np.max(temps)
min_temp = np.min(temps)
min_pos = np.min(pos)
max_pos = np.max(pos)

plt.rcParams["figure.dpi"] = 300

r = np.linspace(0, 0.1, 1000)
plt.plot(r, (1e6*(0.1**2 - r**2)) / (4 * 10), label="Theoretical Steady State")
plt.plot(pos, temps[-1, :], label=f"CN Steady State")

plt.xlim((0, 0.1))
plt.ylim((0, 250))
plt.xlabel("Radial Position [m]")
plt.ylabel("Temperature [K]")
plt.legend()

plt.show()
