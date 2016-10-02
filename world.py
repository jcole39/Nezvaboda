import enemies

_world = {}
starting_position = (0, 0)
#Obviously when building the procedural world generation it will be done in this file. This is temporary as to build the core of the engine.
def load_tiles():
	"""Parses a file that describes the world space into the _world object"""
	with open('resources/map.txt', 'r') as f:
		rows = f.readlines()
	x_max = len(rows[0].split('\t')) #Assumes all rows use same number of tabs
	for y in range(len(rows)):
		cols = rows[y].split('\t')
		for x in range(x_max):
			tile_name = cols[x].replace('\n', '')
			if tile_name == 'StartingRoom':
				global starting_position
				starting_position = (x, y)
			_world[(x,y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)
			# Remember the above statement for all future python programs that require external resources or maps. This is very important stuff.
def tile_exists(x,y):
	return _world.get((x,y))