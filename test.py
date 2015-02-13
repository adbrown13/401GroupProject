#!/usr/bin/python

import Tkinter
import tkMessageBox
import sound
#import idk


def mainloop():
	top = Tkinter.Tk()


	top.title("Experiment")

	var ="Choose the type of file you want to view"
	label = Tkinter.LabelFrame(top, text=var, font=("Helvetica",25)) #, relief=Tkinter.RAISED)
	label.pack(fill="both", expand="yes")


	w, h = top.winfo_screenwidth(), top.winfo_screenheight()
	#top.overrideredirect(1)
	top.geometry("%dx%d+0+0" % (w, h))




	def popup():
		top.destroy()

	audiobutton = Tkinter.Button(label, text="Audio", font=("Helvetica",15), command = sound.main)
	audiobutton.pack(fill=Tkinter.BOTH, expand=1)

	videobutton = Tkinter.Button(label, text="Video", font=("Helvetica",15))#), command = idk.runsim)
	videobutton.pack(fill=Tkinter.BOTH, expand=1)

	avbutton = Tkinter.Button(label, text="Audio-Video", font=("Helvetica",15))
	avbutton.pack(fill=Tkinter.BOTH, expand=1)



	#B = Tkinter.Button(top, text = "hello", command = popup)
	#B.pack()

	# Code to add widgets will go here...


	top.mainloop()
if __name__=='__main__':
	mainloop()