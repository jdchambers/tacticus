from __future__ import division, print_function, unicode_literals

    
class World(object):
    """
    Defines a world in which the units evolve. Includes things like terrain
    and obstacles, as well as caches and grids to manage objects.
    
    Initialize a world object from a map level loaded from files.
    """
    
    image = None #the picture to display

    def __init__(self,map):
        self.heightmap #height map
    
        self.gradientmap #gradient map
        
        self.platoons = []
        
    def add_platoon(self,platoon):
        self.platoons.append(platoon)