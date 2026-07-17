#BEST FIT LINE WAS MADE BY ME, WORST FIT LINE AND UNCERTAINTIES IN THE GRAPH WAS MADE BY CLAUDE CODE FABLE 5

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

x = np.array([-10, -5, 0, 5, 10, 15, 20, 25, 30])
readings = np.array([
    [1346, 1365, 1349, 1348, 1349],
    [1340, 1341, 1343, 1342, 1345],
    [1328, 1331, 1337, 1333, 1340],
    [1323, 1326, 1336, 1325, 1334],
    [1319, 1317, 1333, 1324, 1330],
    [1313, 1311, 1331, 1313, 1325],
    [1308, 1304, 1326, 1311, 1321],
    [1302, 1302, 1328, 1308, 1319],
    [1297, 1295, 1332, 1304, 1328],
])
##5 repeat readings per temperature

y = readings.mean(axis=1)
yerr = readings.std(axis=1, ddof=1) / np.sqrt(readings.shape[1])
##error bar = standard error of the mean (sample SD / sqrt(n))

(m, c), cov = np.polyfit(x,y,1, cov=True)
#returns (m, b) @ deg order 1
#m, b means cmd[0], cmd[1]

r2 = 1 - np.sum((y - (m*x + c))**2) / np.sum((y - y.mean())**2)
##coefficient of determination of the best fit

m_max = ((y[-1] + yerr[-1]) - (y[0] - yerr[0])) / (x[-1] - x[0])
m_min = ((y[-1] - yerr[-1]) - (y[0] + yerr[0])) / (x[-1] - x[0])
c_max = (y[0] - yerr[0]) - m_max*x[0]
c_min = (y[0] + yerr[0]) - m_min*x[0]
dm = (m_max - m_min) / 2
##worst fits: steepest/shallowest lines through the first and last error bars
##dm = half the spread between the two worst-fit gradients

plt.scatter(x,y,color='blue')
plt.errorbar(x, y, yerr=yerr, fmt='none', ecolor='black', capsize=3,)
plt.plot(x, m*x + c, color='blue', lw = 2, label=f'Best fit: $B = {m:.3f}T + {c:.1f}$ ($R^2$ = {r2:.4f})')
plt.plot(x, m_max*x + c_max, color='red', lw = 1, ls='--')
plt.plot(x, m_min*x + c_min, color='green', lw = 1, ls='--')

ax = plt.gca()
ax.xaxis.set_major_locator(MultipleLocator(5))
ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_minor_locator(MultipleLocator(1))
ax.grid(which='major', lw=0.8)
ax.grid(which='minor', lw=0.3, alpha=0.5)
##fine minor grid (1 K x 1 uT) so worst fit can be read off manually
plt.legend()
plt.xlabel('Temperature ºC')
plt.ylabel('Mean Magnetic Flux Density µT (B)')
plt.title('Mean Magnetic Flux Density vs Temperature (T)')
plt.show()

