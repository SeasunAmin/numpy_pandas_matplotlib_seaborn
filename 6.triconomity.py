import numpy as np
import matplotlib.pyplot as plt

sin = np.sin(180)
print(sin)

sin = np.sin(90)
print(sin)

x_sin = np.arange(0,3)
y_sin = np.arange(4,7)

plt.plot(x_sin,y_sin)
plt.show()