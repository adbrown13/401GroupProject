#!/usr/bin/python

import Tkinter
import tkMessageBox
import sound
import time
import randomfilechooser

import random

def mainloop():
	top = Tkinter.Tk()
	top.title("Experiment")
	mediaFileNames = randomfilechooser.chooseRandomFile()
	print mediaFileNames

	def run_video(mode):
                top.withdraw()
                for i in mediaFileNames:
                        sound.run_muted(i,mode)
                        time.sleep(2)
                top.deiconify()
	def run_audiovideo(mode):
                top.withdraw()
                for i in mediaFileNames:
                        sound.run_all(i,mode)
                        time.sleep(2)
                top.deiconify()
	def run_audio(mode):
                top.withdraw()
                for i in mediaFileNames:
                        sound.run_audio(i,mode)
                        time.sleep(2)
                top.deiconify()

	var ="Choose the type of file you want to view"
	label = Tkinter.LabelFrame(top, text=var, font=("Helvetica",25)) #, relief=Tkinter.RAISED)
	label.pack(fill="both", expand="yes")

#######FULL SCREEN
	pad=3
	top._geom='200x200+0+0'
	top.geometry("{0}x{1}+0+0".format(
		top.winfo_screenwidth()-pad, top.winfo_screenheight()-pad))
          
	def toggle_geom(top,event):
		geom=top.winfo_geometry()
		print(geom,top._geom)
		top.geometry(top._geom)
		top._geom=geom
#######FULL SCREEN

	def run_normal():
		type_of_file_to_play = ["1","2","3"]
		random.shuffle(type_of_file_to_play)

		for i in type_of_file_to_play:
			if(i == "1"):
				run_video(1)
			if(i == "2"):
				run_audiovideo(1)
			if(i == "3"):
				run_audio(1)

	def run_practice():
		type_of_file_to_play = ["1","2","3"]
		random.shuffle(type_of_file_to_play)

		for i in type_of_file_to_play:
			if(i == "1"):
				run_video(0)
			if(i == "2"):
				run_audiovideo(0)
			if(i == "3"):
				run_audio(0)

	audiobutton1 = Tkinter.Button(label, text="Practice", font=("Helvetica",15), command = run_practice)
	audiobutton1.pack(fill=Tkinter.BOTH, expand=1)

	audiobutton2 = Tkinter.Button(label, text="Start", font=("Helvetica",15), command = run_normal)
	audiobutton2.pack(fill=Tkinter.BOTH, expand=1)
	"""
	if(type_of_file_to_play == "1"):
	#	sound.run_audio()
	audiobutton = Tkinter.Button(label, text="Audio", font=("Helvetica",15), command = run_audio)
	audiobutton.pack(fill=Tkinter.BOTH, expand=1)

	if(type_of_file_to_play == "2"):
	#	sound.run_muted()
		videobutton = Tkinter.Button(label, text="Video", font=("Helvetica",15), command = run_video)
		videobutton.pack(fill=Tkinter.BOTH, expand=1)
	
	if(type_of_file_to_play == "3"):
	#	sound.run_all()
		avbutton = Tkinter.Button(label, text="Audio-Video", font=("Helvetica",15), command = run_audiovideo)
		avbutton.pack(fill=Tkinter.BOTH, expand=1)
	"""

	top.mainloop()
if __name__=='__main__':
	mainloop()
