from player import Player
from env import server
from env import Map
from env import Music
from env import Mode
from menu import Main
#TODO: Other Imports go here

#The Game Element itself
class Game():
    
    def __init__(self):
        #This will be the default time
        #that the game will start counting from
        #on the first start up.
        
        Time = (12, 6)
        lastTime = Time
        
        #List of all Game modes
        STORY_MODE = Mode.gamemode('SM')
        BATTLEFRONT = Mode.gamemode('BF')
        DOMINION = Mode.gamemode('D')
        CO_OP = Mode.gamemode('CO')
        
        GM = [STORY_MODE, CO_OP, DOMINION, BATTLEFRONT]
        
    def start(self, GMVal):
        if menu.controlVal == 'KEYBOARD_AND_MOUSE':
            Player.controls = 'KB'
            #Player.controls = CNTRLS[0]
            if GMVal == 1:
                GM[0].start()
                	
            elif GMVal == 2:
                GM[1].start()
                
            elif GMVal == 3:
                GM[2].start()
                
            elif GMVal == 4:
                GM[3].start()
                
            else:
                GM[0].start()
                
        elif menu.controlVal == 'GAME_CONTROLLER':
            Player.controls = 'GC'
            #Player.controls = CNTRLS[1]
                if GMVal == 1:
                GM[0].start()
                	
            elif GMVal == 2:
                GM[1].start()
                
            elif GMVal == 3:
                GM[2].start()
                
            elif GMVal == 4:
                GM[3].start()
                
            else:
                GM[0].start()
        else:
            #Set Value to default (Keyboard & Mouse)
            Player.controls = 'KB'
                if GMVal == 1:
                GM[0].start()
                	
            elif GMVal == 2:
                GM[1].start()
                
            elif GMVal == 3:
                GM[2].start()
                
            elif GMVal == 4:
                GM[3].start()
                
            else:
                GM[0].start()
        #Spawn Announcements   
        server.add(Player)
        server.announce(Player)
        
        #Start BGM
        Music.BGM.start()
        
        #Start Day/Night Cycle
        #from the previously saved time
        #Map.startDNC(lastTime)
        
        world.AI.start()
        player.start()
        world.start()
        
    def pause(self):
        player.pause()
        world.pause()
        
    def end(self):
        world.stop()
        player.stop()
        
