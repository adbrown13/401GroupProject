#!/usr/bin/python

import Tkinter
import tkMessageBox
import sound

import random

def mainloop():
	top = Tkinter.Tk()
	top.title("Experiment")

	def run_video():
                top.withdraw()
                sound.run_muted()
                top.deiconify()
	def run_audiovideo():
                top.withdraw()
                sound.run_all()
                top.deiconify()
	def run_audio():
                top.withdraw()
                sound.run_audio()
                top.deiconify()

	var ="Choose the type of file you want to view"
	label = Tkinter.LabelFrame(top, text=var, font=("Helvetica",25)) #, relief=Tkinter.RAISED)
	label.pack(fill="both", expand="yes")


	w, h = top.winfo_screenwidth(), top.winfo_screenheight()
	#top.overrideredirect(1)
	top.geometry("%dx%d+0+0" % (w/2, h/2))

	type_of_file_to_play = random.choice(["1","2","3"])

	#if(type_of_file_to_play == "1"):
	#	sound.run_audio()
	audiobutton = Tkinter.Button(label, text="Audio", font=("Helvetica",15), command = run_audio)
	audiobutton.pack(fill=Tkinter.BOTH, expand=1)

	#if(type_of_file_to_play == "2"):
	#	sound.run_muted()
	videobutton = Tkinter.Button(label, text="Video", font=("Helvetica",15), command = run_video)
	videobutton.pack(fill=Tkinter.BOTH, expand=1)

	#if(type_of_file_to_play == "3"):
	#	sound.run_all()
	avbutton = Tkinter.Button(label, text="Audio-Video", font=("Helvetica",15), command = run_audiovideo)
	avbutton.pack(fill=Tkinter.BOTH, expand=1)


	top.mainloop()
if __name__=='__main__':
	mainloop()
