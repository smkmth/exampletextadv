import items, enemies

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def intro_text(self):
    raise NotImplementedError()

class StartingRoom(MapTile):
    def intro_text(self):
        return """
        You find yourself in a cave with a flickering tourch on the wall.
        You can make out four paths. each equally as dark and foreboding.
        """
    def modfiy_player(self,player):
        #room has no action on player
        pass

class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.iitem = item
        super().__init__(x,y)

    def add_loot(self,player):
        player.inventory.append(self.item)

    def modify_player(self,player):
        self.add_loot(player)
class EnemyRoom(MapTile):
    def __init__(self, x, y,enemy):
        self.enemy =enemey
        super().__init__(x,y)

    def modify_player(self,the_player):
        if self.senemy.is_alive():
            the_player.hp = the_player.hp -self.enemy.damage
            print("Enemy does {} damage. You have {} hp remaining.".format(self.enemy.damage,the_player.hp))

class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x,y, enemies.GiantSpider())

    def intro_text(self):
        if self.enemy.is_allive():
            return """
            A giant spider jumps down from its web in front of you!
            
            """
        else:
            return """
            The corpse of a dead spider rots on the ground.
            """
class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x,y, items.Dagger())

    def intro_text(self):
        return """
        You notice somthing shiney in the corner; its a dagger!
        You pick it up.

This constructor 

        """





    
            

    





