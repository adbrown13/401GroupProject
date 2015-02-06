import btk
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import numpy as np
import matplotlib.pyplot as plt
#set up 
reader = btk.btkAcquisitionFileReader()  
reader.SetFilename("walk5.c3d")
acq = reader.GetOutput()                 
acq.Update()                             

#get data
data = np.empty((3, acq.GetPointFrameNumber(), 1))
for i in range(0, acq.GetPoints().GetItemNumber()):
    label = acq.GetPoint(i).GetLabel()
    data = np.dstack((data, acq.GetPoint(label).GetValues().T))
data = data.T
data = np.delete(data, 0, axis=0)  
data[data==0] = np.NaN            
dat = data[:, 130:340, :]
freq = acq.GetPointFrequency()
plt.rcParams['toolbar'] = 'None'
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1], projection='3d')
#ax.view_init(10, 150)
pts = []
for i in range(dat.shape[0]):
    pts += ax.plot([], [], [], 'o')

ax.set_xlim3d([np.nanmin(dat[:, :, 0]), np.nanmax(dat[:, :, 0])])
ax.set_ylim3d([np.nanmin(dat[:, :, 1])-400, np.nanmax(dat[:, :, 1])+400])
ax.set_zlim3d([np.nanmin(dat[:, :, 2]), np.nanmax(dat[:, :, 2])])


# animation function
def animate(i):
    for pt, xi in zip(pts, dat):
        x, y, z = xi[:i].T
        pt.set_data(x[-1:], y[-1:])
        pt.set_3d_properties(z[-1:])   
    return pts

# Animation object
anim = animation.FuncAnimation(fig, func=animate, frames=dat.shape[1], interval=1000/freq, blit=False, repeat=False)
plt.ioff()
plt.show()

