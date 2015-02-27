import sys, wave, contextlib, math, time, pyglet
from PIL import Image, ImageTk
from Tkinter import Tk, Label, BOTH, Toplevel
from ttk import Frame, Style


class audioOnly(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("Please Listen")
        self.pack(fill=BOTH, expand=1)
        
        style = Style()
        style.configure("Tframe", background="#333")
        
        #Put in a "Please Listen" picture
        listen = Image.open("Resources/PleaseListen.jpg")
        listenImg = ImageTk.PhotoImage(listen)
        soundLabel = Label(self, image=listenImg)
        soundLabel.image = listenImg
        soundLabel.place(x=20, y=20)


#Get the duration of the sound clip
def getWavDuration( fname ):
    with contextlib.closing(wave.open(fname, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return int(math.ceil(duration*1000))

#Get wav file frequency.  Use to get frequency before playing
#Wrong frequency can result in differently-pitched voices
def getFreq( fname ):
    with contextlib.closing(wave.open(fname, 'r')) as f:
        return f.getframerate()

def main( soundFileName ):
    root = Toplevel()
    
    root.geometry( "640x640+300+200" ) #20 pixel buffer on each side
    #root.overrideredirect(1) #remove top toolbar
    
    window = audioOnly(root)

    soundPlayer = pyglet.media.Player()
    soundFile = pyglet.media.load( soundFileName )
    soundPlayer.queue( soundFile )
    soundPlayer.play()
    
    #After the music ends, remove the screen
    root.after(int(soundFile.duration*1000),root.destroy)
    root.mainloop()

if __name__ == '__main__':
    if (len(sys.argv) == 1):
        #default to sound recorded during tour
        fname = "new.avi"
    else:
        fname = sys.argv[1]
    main( fname )
