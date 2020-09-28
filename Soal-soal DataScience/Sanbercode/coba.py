import matplotlib.pyplot as plt
import numpy as np

rng = np.random.RandomState(42)
x = 20 * rng.rand(50)
y = x**2 + 2 * x + - 1 + rng.randn(50)

# data yang akan di prediksi
x_new = np.arange(20, 30, 0.5)

fig, ax = plt.subplots(figsize=(12, 6))
ax.scatter(x, y)
ax.set_xlabel('X-Value')
ax.set_ylabel('Y-Value')
plt.show()