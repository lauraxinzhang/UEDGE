import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('NSTX_limiter.dat')
print np.shape(data)

plt.plot(data[:, 0], data[:, 1])
plt.show()
