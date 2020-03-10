#!/usr/bin/python
__author1__ = "FaderDev"
__author2__ = ""
__license__ = """
Simplified BSD (BSD 2-Clause) License.
See License.txt or http://opensource.org/licenses/BSD-2-Clause for more info
"""
# Panda3D imports
# Character Assets should be stored in the format:"character1"-where 1 is the Character No.
from direct.actor.Actor import Actor

class Player():
    def __init__(self, charId, charNr, UsrName):
        #self.Multiplayer = False
        self.charId = charId
        self.UsrName = username
        self.controls = 'KB'
        charPath = "characters/character{}/".format(charNr)
        self.character = Actor(
            charPath + "char", {
                "Idle":charPath + "idle",
                "walk":charPath + "walk",
                "sprint":charPath + "sprint",
                "jump":charPath + "jump",
                "jump_f":charPath + "jump_f",
                "crouch":charPath + "    crouch",
                "sneak_f":charPath + "sneak_f",
                "crouch_idle":charPath + "crouch_idle"
            })
            
    self.character.setH(90)
    self.character.reparentTo(render)
    self.character.hide()
    
    self.inventory = []
    self.hotbar = []
    
    self.forwardButton = KeyboardButton.asciiKey('w')
    self.sprintButton = KeyboardButton.asciiKey('Shift')
    self.jumpButton = KeyboardButton.asciiKey('Space')
    self.crouchButton = KeyboardButton.asciiKey('c')
    #self.JumpButton = KeyboardButton.asciiKey('')
    #self.Button = KeyboardButton.asciiKey('')


    def start(self, startPos):
        #if Multiplayer==
        self.character.setPos(startPos)
        self.character.show()
 
    def stop(self):
        self.character.hide()

    def equip(self, ItemID):
        self.inventory.append(ItemID)
        print(str(self.UsrName) + " has equipped " + str(ItemID))
        
    def wield(self, ItemID):
        if len(self.hotbar) >= 2:
            raise ValueError('Hotbar Full!')
        else:
            self.hotbar.append(ItemID)

    def discard(self, ItemID):
        self
        