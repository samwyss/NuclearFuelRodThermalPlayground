import matplotlib.pyplot as plt
import numpy as np
from numpy.ma.core import shape

temps = np.loadtxt("./out/temperature.csv", delimiter=",")
pos = np.loadtxt("./out/position.csv", delimiter=",")
time = np.loadtxt("./out/time.csv", delimiter=",")
max_temp = np.max(temps)
min_temp = np.min(temps)
min_pos = np.min(pos)
max_pos = np.max(pos)

plt.rcParams["figure.dpi"] = 300

fig, ax = plt.subplots(figsize=(8,6), dpi=300)

r = np.linspace(0, 0.1, 1000)
plt.plot(r, (1e6 * 0.1 / (2 * 100) + 1e6 * 0.1**2 / (4 * 10) * (1-(r/0.1)**2)), "k", label="Theory SS")

for i in range(temps.shape[0]):
    plt.plot(pos, temps[i, :], ".", label=f"t={time[i]/3600:.1f} [h]")

plt.xlim((0, 0.1))
plt.ylim((0, 800))
plt.xlabel("Radial Position [m]")
plt.ylabel("Temperature [K]")
plt.legend()

plt.show()
