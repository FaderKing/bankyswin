__author__ = "Destiny Kefas"
__author__ = "Aiden Ogbuagu"

from panda3d.core import loadPrcFileData

currentBuild = "XLR Prototype V0.0.2a"

confVars = f"""
win-size 1280 720
window-title {currentBuild}
show-frame-rate-meter 1
"""
loadPrcFileData("", confVars)

from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import PandaNode,NodePath,Camera,TextNode 

class Game(ShowBase):
    def __init__(self):
        super().__init__()

        self.font1 = loader.loadFont("Fonts/main_regular.ttf")
        self.font2 = loader.loadFont("Fonts/main_italic.ttf")

        self.addInfo(0.95, "dtk is coding small small")
        self.addTitle(currentBuild)

    def addInfo(self, pos, msg):
        return OnscreenText(
	        text=msg,
	        style=1, 
	        fg=(1,1,1,1),
	        pos=(-1.76, pos),
	        align=TextNode.ALeft, 
	        scale = .05, 
	        font = self.font1, 
	        mayChange=True
        )
    
    def addTitle(self, text):
        return OnscreenText(
	        text=text,
	        style=1,
	        fg=(1,1,1,1),
	        pos=(1.3,-0.95),
	        align=TextNode.ARight, 
	        scale = .07, 
	        font = self.font1
    )
    
game =Game()
game.run()
