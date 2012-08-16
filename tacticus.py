#/usr/bin/env python
from __future__ import division, print_function, unicode_literals

from operator import setslice
import pyglet

import cocos
from cocos.director import director

import gameview


if __name__ == "__main__":

    pyglet.resource.path.append('data')
    pyglet.resource.reindex()
    #font.add_directory('data')

    # director init takes the same arguments as pyglet.window
    director.init( resizable=True, width=700, height=700 )
#    scene.add( BackgroundLayer(), z=0 )
    game = gameview.Game()
    
    keyboard = pyglet.window.key.KeyStateHandler()
    director.window.push_handlers(keyboard)
    director.show_FPS = True
    director.run( game )
