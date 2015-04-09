"""The avi File is responsible for the conversion of c3d to avi
"""
import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import cnames
from matplotlib import animation
import btk
#################################
def makeAvi():
	#Read in the file
	reader = btk.btkAcquisitionFileReader()  
	reader.SetFilename("monologue3.c3d")
	acq = reader.GetOutput()                 
	acq.Update()                             
	data = np.empty((3, acq.GetPointFrameNumber(), 1))
	for i in range(0, acq.GetPoints().GetItemNumber()):
		label = acq.GetPoint(i).GetLabel()
		data = np.dstack((data, acq.GetPoint(label).GetValues().T))
	data = data.T
	data = np.delete(data, 0, axis=0)  
	data[data==0] = np.NaN            
	dat = data[:, :, :]
	freq = acq.GetPointFrequency()
	fig = plt.figure()
	ax = fig.add_axes([0, 0, 1, 1], projection='3d')
	pts = []
	stick_lines=[]
	stick_defines = [
	    (0, 2),
	    (0, 5),
	    (1, 2),
	    (1, 5),
	    (2, 3),
	    (3, 4),
	    (3,11),
	    (4, 13),
	    (4, 11),
	    (11,13),
	    (5, 6),
	    (6, 7),
	    (6,12),
	    (7, 12),
	    (7, 14),
	    (12,14),
	    (8, 9),
	    (9, 10),
	    (10, 8)
	]
	for i in range(dat.shape[0]):
		pts += ax.plot([], [], [], 'o')
	for i in stick_defines:
		stick_lines += ax.plot([], [], [], '-k')
	ax.set_xlim3d([np.nanmin(dat[:, :, 0]), np.nanmax(dat[:, :, 	0])])
	ax.set_ylim3d([np.nanmin(dat[:, :, 1]), np.nanmax(dat[:, :, 1])])
	ax.set_zlim3d([np.nanmin(dat[:, :, 2]), np.nanmax(dat[:, :, 2])])
	ax.view_init(30, 180)

	def animate(i):
	    for  pt, xi in zip( pts, dat):
	        x, y, z = xi[:i].T
	        pt.set_data(x[-1:], y[-1:])
	        pt.set_3d_properties(z[-1:])
	    for stick_line, (sp, ep) in zip(stick_lines, stick_defines):
	        stick_line._verts3d = dat[[sp,ep], i, :].T
	    fig.canvas.draw()
	    return  pts + stick_lines
	
	Writer=animation.writers['ffmpeg']
	writer=Writer(fps=freq)
	anim = animation.FuncAnimation(fig, func=animate,  	frames=dat.shape[1], blit=True, repeat='False')
	
	#plt.show()

	anim.save('walk5.avi',writer=writer)
	os.system('ffmpeg -i walk5.avi -i 024CartoonDescriptionDemo.wav new.avi')
	


