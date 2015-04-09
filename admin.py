#!/usr/bin/python

import Tkinter
import tkMessageBox
import locale
locale.setlocale(locale.LC_ALL, '')
import avi


def mainloop():
	top = Tkinter.Tk()


	top.title("Admin Mode")

	var ="Make the movies"
	label = Tkinter.LabelFrame(top, text=var, font=("Helvetica",25)) #, relief=Tkinter.RAISED)
	label.pack(fill="both", expand="yes")


	w, h = top.winfo_screenwidth(), top.winfo_screenheight()
	#top.overrideredirect(1)
	top.geometry("%dx%d+0+0" % (w/2, h/2))




	def popup():
		top.destroy()

	audiobutton = Tkinter.Button(label, text="Make movie", font=("Helvetica",15), command = avi.makeAvi)
	audiobutton.pack(fill=Tkinter.BOTH, expand=1)


	top.mainloop()
if __name__=='__main__':
	mainloop()
