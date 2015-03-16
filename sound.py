import sys, time, pyglet
import vote

def run_audio( soundFileName ):
    
    window = pyglet.window.Window(width=600, height=600)
    pleaseListenImage = pyglet.image.load('Resources/PleaseListen.jpg').get_texture()

    soundPlayer = pyglet.media.Player()
    soundPlayer.volume=10

    def next_song(dt):
        soundPlayer.pause()
        window.close()
        voting = vote.App(soundFileName)
        pyglet.app.exit()

    @window.event 
    def on_draw(): 
        window.clear()
        pleaseListenImage.blit(0,0)

    soundFile = pyglet.media.load( soundFileName )
    soundPlayer.queue( soundFile )
    
    soundPlayer.play()
    pyglet.clock.schedule_once(next_song, soundPlayer.source.duration-0.25)
    pyglet.app.run()
    return

def run_muted( fileName ):

    window = pyglet.window.Window(width=800, height=600) 
    player = pyglet.media.Player() 
    player.volume=0
    
    MediaLoad = pyglet.media.load(fileName) 
    player.queue(MediaLoad)
    player.play()

    def on_eos(dt):
        player.pause()
        window.close()
        voting = vote.App(soundFileName)
        pyglet.app.exit()
        
    @window.event 
    def on_draw(): 
        window.clear()
        if player.source and player.source.video_format: 
            player.get_texture().blit(0,0)
    
    pyglet.clock.schedule_once(on_eos, player.source.duration-0.25)
    pyglet.app.run()
    return

def run_all( fileName ):
    window = pyglet.window.Window(width=800, height=600) 
    player = pyglet.media.Player() 
    player.volume=10

    MediaLoad = pyglet.media.load(fileName)
    player.queue(MediaLoad)
    player.play()

    def on_eos(dt):
        player.pause()
        window.close()
        voting = vote.App(soundFileName)
        pyglet.app.exit()
        
    @window.event 
    def on_draw(): 
        window.clear() 
        if player.source and player.source.video_format: 
            player.get_texture().blit(0,0)
    
    pyglet.clock.schedule_once(on_eos, player.source.duration-0.25)
    pyglet.app.run()
    return


if __name__ == '__main__':
    if (len(sys.argv) == 1):
        #default to sound recorded during tour
        fname = "new.avi"
    else:
        fname = sys.argv[1]
    main( )
