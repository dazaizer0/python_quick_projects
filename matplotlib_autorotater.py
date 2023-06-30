from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Set the axis labels
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

for angle in range(0, 360*4 + 1):

    angle_norm = (angle + 180) % 360 - 180
    _vrot = angle_norm

    ax.view_init(10, _vrot, 0)
    plt.title('Elevation: %d°, Azimuth: %d°, Roll: %d°' % (0, _vrot, 0))

    plt.draw()
    plt.pause(.001)
