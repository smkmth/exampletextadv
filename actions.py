import player

class Action():
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs #kwargs is an expandable argument which can account for more then one argument

    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)
    
class MoveNorth(Action):
    def __init__(self):
        super(MoveNorth,self).__init__(method=Player.move_north, name = 'Move north', hotkey = 'n')
                             
class MoveSouth(Action):
    def __init__(self):
        super(MoveSouth,self).__init__(method=Player.move_south, name = 'Move south', hotkey = 's')
        #this calls the Parent class 

class MoveEast(Action):
    def __init__(self):
        super(MoveEast,self).__init__(method=Player.move_east, name = 'Move east', hotkey = 'e')

class MoveWest(Action):
    def __init__(self):
        super(MoveWest,self).__init__(method=Player.move_west, name = 'Move west', hotkey = 'w')
        
class ViewInventory(Action):
    """Prints the players inventory"""
    def __init__(self):
        super(ViewInventory,self).__init__(method=Player.print_inventory, name ='View inventory', hotkey = 'i')

class Flee(Action):
    def __init__(self,tile):
        super().__init__(method= Player.flee, name ='Flee', hotkey = 'f', tile = tile)
                                           

class Attack(Action):
    def __init__(self,enemy):
            super(Attack,self).__init__(method=Player.attack, name='Attack', hotkey = 'a', enemy = enemy)

                

        
