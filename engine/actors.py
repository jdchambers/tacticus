from __future__ import division, print_function, unicode_literals

from cocos.cocosnode import CocosNode
from cocos.euclid import Vector2, Point2
import math
import itertools

from util import *

"""
Abstract Actors in the game world
Units are in M, these values are transformed to work in pixels for rendering
"""

class Actor(CocosNode):
    """
    The base Actor class
    For pretty much anything that isn't the base map - things which can interact.
    (anything which doesn't interact is just decoration and therefore has no 
    impact in the game simulation engine)
    The basic actor is a 0-D point with position (inherited from CocosNode),
    velocity, and acceleration. As a shortcut, has a "movable" property, this
    is the same as having velocity and acceleration permanently set to 0
    
    """
    
    def __init__(self):
        self.velocity = Vector2(0,0)
        self.acceleration = Vector2(0,0)
    
    def __repr__(self):
        return 'Actor @ (%.2f, %.2f)'%(self.x, self.y)
        
        
class Warrior(Actor):
    """
    The basic fighting unit. Moves around.
    Most behaviours are done by Actions which control it's behaviour.
    This allows us to use the Event system
    """
    radius = 0.4 #size of warrior
    def __init__(self,x,y):
        self.sight = 80 #how far warrior can see
        self.x = x
        self.y = y
        
        super(Warrior,self).__init__()
    
    def __repr__(self):
        return 'Warrior @ (%.2f, %.2f)'%(self.x, self.y)
    
class PathDriver(object):
    """
    Make an actor follow a path defined by a series of points
    """
    pass
    
    
    
def grid_formation(no_units, cols=5, spacing = 1):
    """
    grid with given number of units, columns, and spacing between units
    """
    no_units = cols if no_units < cols else no_units
    rows = int(math.ceil(no_units/cols))
    targets = []
    for i in xrange(0,int(cols)):
        for j in xrange(0,rows):
            targets.append( Point2(i*spacing,j*spacing) )
    return targets


class Platoon(object):
    """
    One platoon of warriors
    Manages formations etc.
    
    default formation: grid
    
    """
    
    def __init__(self, size = 20, type='default'):
        """
        Generate a platoon with a given number of units of a given type
        
        TODO just does Warrior for now
        """
        self.units = []
        self.team = PLAYER
        
        self.formation = grid_formation(size, spacing = 3*Warrior.radius)
        for p in self.formation:
            self.units.append(Warrior(p.x,p.y))
        
        self.leader = self.units[0] #first unit added is leader at local origin point of platoon
    
    def __repr__(self):
        return 'Platoon: %d units. Leader at (%f, %f )' %(len(self.units), self.leader.x, self.leader.y)
     