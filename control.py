# pyglet related
import pyglet
from pyglet.window import key

# cocos2d related
from cocos.layer import Layer
from cocos.scene import Scene

# tetrico related
from constants import *

__all__ = ['GameCtrl']

#
# Controller ( MVC )
#

class GameCtrl( Layer ):

    is_event_handler = True #: enable pyglet's events

    def __init__(self, model):
        super(GameCtrl,self).__init__()

        self.used_key = False
        self.paused = True

        self.model = model
        self.elapsed = 0

    def on_key_press(self, k, m ):
        if self.paused:
            return False

        if self.used_key:
            return False

        return False

    def on_text_motion(self, motion):
        if self.paused:
            return False

        if self.used_key:
            return False

        return False

    def pause_controller( self ):
        '''removes the schedule timer and doesn't handler the keys'''
        self.paused = True
        self.unschedule( self.step )

    def resume_controller( self ):
        '''schedules  the timer and handles the keys'''
        self.paused = False
        self.schedule( self.step )

    def step( self, dt ):
        '''updates the engine'''
        self.elapsed += dt

    def draw( self ):
        '''draw the map and the block'''
        self.used_key = False
