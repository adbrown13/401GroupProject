from Tkinter import *
import tkFileDialog
import tkMessageBox
import datetime

class App:
 
    def __init__(self, filename,audio,mode):
        self.master = Tk()
        
        self.filename = filename
        self.audio = audio
        self.mode = mode
        #call start to initialize to create the UI elemets
        self.start()
 
    def start(self):
        self.master.title("Voting")
        self.now = datetime.datetime.now()
 
        #CREATE A TEXT/LABEL

        label01 = "The gender of the speaker is:"
        Label(self.master, text=label01).grid(row=0, column=0, sticky=W)
 
 
        #CREATE RADIO BUTTONS
        RADIO_BUTTON = [
            ("Man", "M"),
            ("Woman","W"),
            ("Can't decide","C")
        ]
 
        #initialize a variable to store the selected value of the radio buttons
        #set it to A by default
        self.radio_var = StringVar(master=self.master)
        self.radio_var.set("M")
 
        #create a loop to display the RADIO_BUTTON
        i=0
        for text, item in RADIO_BUTTON:
            #setup each radio button. variable is set to the self.radio_var
            #and the value is set to the "item" in the for loop
            self.radio = Radiobutton(self.master, text=text, variable=self.radio_var, value=item)
            self.radio.grid(row=1, column=i)
            i += 1

        #create a variable with text
        label02 = "How masculine-feminine is this speaker? (Enter a number)"
        Label(self.master, text=label02).grid(row=2, column=0, sticky=W)

        #Feminintiy entry
        self.fem = Entry(self.master)
        self.fem["width"] = 10
        self.fem.focus_set()
        self.fem.grid(row=3,column=0)

        if(self.audio == 1):
            label03 = "How natural does this speaker's voice sound? (Enter a number)"
            Label(self.master, text=label03).grid(row=4, column=0, sticky=W)

            #Naturalness entry
            self.natty = Entry(self.master)
            self.natty["width"] = 10
            self.natty.focus_set()
            self.natty.grid(row=5,column=0)
 
        #button to save data to csv
        self.submit = Button(self.master, text="Continue", command=self.start_processing, fg="red")
        self.submit.grid(row=6, column=0)
        
        self.master.wait_window()
    def start_processing(self):
        if (self.mode):
            f = open('data.csv', 'a')
            filename = self.filename.split("/")
            if(self.audio == 1):
                f.write(filename[1] + ',' +  self.audio + ',' + self.radio_var.get() + ',' +  self.fem.get() + ',' + self.natty.get() + '\n')
            else:
                f.write(filename[1] + ',' +  self.audio + ',' + self.radio_var.get() + ',' +  self.fem.get() + '\n')
            f.close()
            self.master.destroy()