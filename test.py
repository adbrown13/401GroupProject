#!/usr/bin/python

import Tkinter
import tkMessageBox
import sound
import idk
import random


def mainloop():
	top = Tkinter.Tk()
	top.title("Experiment")

	var ="Choose the type of file you want to view"
	label = Tkinter.LabelFrame(top, text=var, font=("Helvetica",25)) #, relief=Tkinter.RAISED)
	label.pack(fill="both", expand="yes")


	w, h = top.winfo_screenwidth(), top.winfo_screenheight()
	#top.overrideredirect(1)
	top.geometry("%dx%d+0+0" % (w/2, h/2))

	type_of_file_to_play = random.choice(["1","2","3"])

	if(type_of_file_to_play == "1"):
		sound.run_audio
	#audiobutton = Tkinter.Button(label, text="Audio", font=("Helvetica",15), command = sound.run_audio)
	#audiobutton.pack(fill=Tkinter.BOTH, expand=1)

	if(type_of_file_to_play == "2"):
		sound.run_muted
	#videobutton = Tkinter.Button(label, text="Video", font=("Helvetica",15), command = sound.run_muted)
	#videobutton.pack(fill=Tkinter.BOTH, expand=1)

	if(type_of_file_to_play == "2"):
		sound.run_all
	#avbutton = Tkinter.Button(label, text="Audio-Video", font=("Helvetica",15), command = sound.run_all)
	#avbutton.pack(fill=Tkinter.BOTH, expand=1)


	top.mainloop()
if __name__=='__main__':
	mainloop()
