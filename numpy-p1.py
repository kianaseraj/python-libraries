
import numpy as np
import matplotlib.pyplot as plt
N_run = 100
N = 100_000
pos = np.random.uniform(-1, 1, size=(N_run, N, 2))
dist = np.sum(pos**2, axis=2)
num_inside = np.sum(dist <= 1, axis=1)
pi_estimate = 4 * num_inside / N
print(pi_estimate)
plt.hist(pi_estimate)
plt.show()
