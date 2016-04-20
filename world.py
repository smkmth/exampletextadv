_world = {}
starting_position = (0,0)

def load_tiles():
    """Parses a file that describes a world space into the world object"""
    with open('resources/map.txt' , 'r') as f:#open map.txt in read mode because we dont want to edit the map.txt file
        rows = f.readlines()#readlines breaks the document into single lines
    x_max = len(rows[0].split('\t'))#assumes all rows  contain the same number of tabs
    for y in range (x_max):
        tile_name = cols[x].replace('\n', '')
        if tile_name == 'StartingRoom':
            global starting_position
            starting_position = (x,y)
        world[(x,y)] = None if tile_name == '' else getattr( import ('tiles'),tile name) (x,y)

def tile_exists(x,y):
    return world.get((x,y))




        
