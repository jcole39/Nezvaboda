from player import Player

class Action():
	def __init__(self, method, name, hotkey, **kwargs):
		self.method = method
		self.hotkey = hotkey
		self.name = name
		self.kwargs = kwargs
		
	def __str__(self):
		return "{}: {}".format(self.hotkey, self.name)

class DevAction(Action):
	pass

class MoveNorth(Action):
	def __init__(self):
		super().__init__(method=Player.move_north, name='Move north', hotkey='w')

class MoveSouth(Action):
	def __init__(self):
		super().__init__(method=Player.move_south, name='Move south', hotkey='s')

class MoveEast(Action):
	def __init__(self):
		super().__init__(method=Player.move_east, name='Move east', hotkey='d')

class MoveWest(Action):
	def __init__(self):
		super().__init__(method=Player.move_west, name='Move west', hotkey='a')

class ViewInventory(Action):
	def __init__(self):
		super().__init__(method=Player.print_inventory, name='View Inventory', hotkey='e')

class Attack(Action):
	def __init__(self, enemy):
		super().__init__(method=Player.attack, name="Attack", hotkey='a', enemy=enemy)

class Heal(Action):
	def __init__(self):
		super().__init__(method=Player.heal, name="Heal", hotkey='h')

class Flee(Action):
	def __init__(self, tile):
		super().__init__(method=Player.flee, name="Flee", hotkey='f', tile=tile)

class GiveXp(Action):
	def __init__(self, xp):
		super().__init__(method=Player.give_xp, name="Give exp", hotkey='dv_givexp', xp=xp)

class Suicide(DevAction):
	def __init__(self):
		super().__init__(method=Player.suicide, name="Kill Self DEV", hotkey="kill")
		
class DevLevelUp(DevAction):
	def __init__(self):
		super().__init__(method=Player.levelup, name="Levelup DEV", hotkey="dv_lvl")

class ShowHealth(Action):
	def __init__(self):
		super().__init__(method=Player.showHealth, name="Show player health", hotkey="dv_showHealth")

class ShowLevel(Action):
	def __init__(self):
		super().__init__(method=Player.show_level, name="Show level and exp.", hotkey="c")

class Info(Action):
	def __init__(self):
		super().__init__(method=Player.info, name="Information", hotkey="i")
