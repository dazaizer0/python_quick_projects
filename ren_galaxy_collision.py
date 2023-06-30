# studied and rewritten from matplotlib-examples
import numpy as np
import matplotlib.pyplot as plt


def lorenz(xyz, *, s=10, r=28, b=2.667):
    x, y, z = xyz
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return np.array([x_dot, y_dot, z_dot])


dt = 0.008
num_steps = 16000

xyz_s = np.empty((num_steps + 1, 3))
xyz_s[0] = (0., 1., 1.05)
for i in range(num_steps):
    xyz_s[i + 1] = xyz_s[i] + lorenz(xyz_s[i]) * dt

ax = plt.figure().add_subplot(projection='3d')

ax.plot(*xyz_s.T, lw=0.5)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("galaxy collision")

plt.show()
