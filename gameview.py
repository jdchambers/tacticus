from __future__ import division, print_function, unicode_literals

#pyglet
from pyglet.window import key

# cocos2d related
from cocos.layer import Layer, ColorLayer, ScrollingManager
from cocos.scene import Scene

import cocos
import pyglet

class GameController(Layer):

    is_event_handler = True     #: enable pyglet's events

    def __init__(self,gamescene):
        super(GameController, self).__init__()
        self.scene=gamescene

    def on_key_press (self, key, modifiers):
        """This function is called when a key is pressed.
        'key' is a constant indicating which key was pressed.
        'modifiers' is a bitwise or of several constants indicating which
            modifiers are active at the time of the press (ctrl, shift, capslock, etc.)
        """
        scr = self.scene.scroller
        print(scr.fx,scr.fy)
        scr.set_focus(scr.fx+20, scr.fy+20)

    def on_key_release (self, key, modifiers):
        """This function is called when a key is released.
    
        'key' is a constant indicating which key was pressed.
        'modifiers' is a bitwise or of several constants indicating which
            modifiers are active at the time of the press (ctrl, shift, capslock, etc.)
    
        Constants are the ones from pyglet.window.key
        """
        pass

class ImageLayer(cocos.layer.ScrollableLayer):
    def __init__(self,filename):
        super(ImageLayer, self).__init__()
        self.img = pyglet.resource.image(filename)

    def draw( self ):
        self.img.blit(0,0)

class Game( Scene):
    """
    Return a Scene containing the active game layers
    
    """

    def __init__(self):
        """
        DUMMY MAP FOR NOW
        """
        super(Game,self).__init__()
        
        self.scroller = ScrollingManager()
        
        bg = ColorLayer(172,144,255,255)
        self.add( bg, z=0, name="background" )
        
        test_layer = cocos.tiles.load('testcard.xml')['testmap']
        self.scroller.add(test_layer)


                
        #This loads a cocos2d XML format map
        #map = ImageLayer('test2.png')
        #scroller.add(map, z=1, name='map')
        
        self.add(self.scroller,z=1)
        
        inputlayer = GameController(self)
        self.add(inputlayer, z=5)
        
    def build_layers(self):
        pass
