import items, enemies, actions, world



class MapTile:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def intro_text(self):
		raise NotImplementedError()
	
	def modify_player(self, player):
		raise NotImplementedError()
	
	def adjacent_moves(self):
		"""Returns all moves for adjacent tile"""
		moves = []
		if world.tile_exists(self.x + 1, self.y):
			moves.append(actions.MoveEast())
		if world.tile_exists(self.x - 1, self.y):
			moves.append(actions.MoveWest())
		if world.tile_exists(self.x, self.y + 1):
			moves.append(actions.MoveSouth())
		if world.tile_exists(self.x, self.y - 1):
			moves.append(actions.MoveNorth())
		return moves
	
	def available_actions(self):
		"""Returns available actions in the room for abstract room"""
		moves = self.adjacent_moves()
		moves.append(actions.ViewInventory())
		moves.append(actions.Info())
		moves.append(actions.Suicide())
		moves.append(actions.ShowLevel())
		moves.append(actions.ShowHealth())
		moves.append(actions.DevLevelUp())
		moves.append(actions.Heal())
		
		return moves

class StartingRoom(MapTile):
	def intro_text(self):
		return """
		You find yourself in the parlour of a Victorian summer house, walls decaying in the frigid winds of winter.
		"""
	
	def modify_player(self, player):
		#Room has no action on player
		pass

class LeaveParlourRoom(MapTile):
	def intro_text(self):
		return """
		A large red door creaks open...
		... dust trails underneath as the cool morning air hits your face! Freedom!
		
		A Winner Is You!
		"""
	
	def modify_player(self, player):
		player.victory = True

class LootRoom(MapTile):
	def __init__(self, x, y, item):
		self.item = item
		self.instanceCollected = [False] * len(self.item)
		super().__init__(x, y)
		
	def add_loot(self, player):
		for i in range(len(self.item)):
			if self.instanceCollected[i] == False:
				player.inventory.append(self.item[i])
				print("You picked up the {}. Thats nice.\n".format(self.item[i].name))
				self.instanceCollected[i] = True
	
	def modify_player(self, player):
		self.add_loot(player)
		
class CoveredLootRoom(LootRoom):
	def __init__(self, x, y, item, tile):
		self.item = item
		self.tile = tile
		super().__init__(x, y)
		
	def add_loot(self, player):
		player.inventory.append(self.item)
	
	def modify_fromTile(self, tile):
		if self.tile.is_covered:
			tile.is_covered = false
	
	def modify_player(self, player):
		self.add_loot(player)
		self.modify_fromTile(self.tile)

class EnemyRoom(MapTile):
	def __init__(self, x, y, enemy):
		self.enemy = enemy
		super().__init__(x, y)
		
	def modify_player(self, player):
		if self.enemy.is_alive():
			player.hp = player.hp - self.enemy.dealt
			print("{}".format(self.enemy.wpn.description))
			print("The {} does {} damage. You have {} HP remaining.".format(self.enemy.name, self.enemy.dealt, player.hp))
	def available_actions(self):
		if self.enemy.is_alive():
			return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy), actions.Heal()]
		else:
			return self.adjacent_moves()

"""class EncounterRoom(MapTile):
	def __init__(self, x, y, enemies):
		self.enemies = enemies
		super.__init__(x, y)
		
	def modify_player(self, player):
		alive_enemies = enemy_initiative = []
		player_initiatve = player.initiative_roll()
		for enemy in range(len(self.enemies):
			alive_enemies.append(1)
			enemy_initiative.append(self.enemies[enemy].initiative_roll())
		while len(alive_enemies) > 0:
			for enemy in range(len(self.enemies)):
				if self.enemies[enemy].is_alive() and self.enemies[enemy].initiative_roll() > player.initiative_roll():
					player.hp = player.hp - self.enemies[enemy].dealt
					print("The {} hits you for {} with their {}! You have {} HP left!".format(self.enemies[enemy].name, self.enemies[enemy].dealt, self.enemies[enemy].weapon, player.hp))"""
					
		

class SecretTunnelEnemyRoom(EnemyRoom):
	def __init__(self, x, y, enemy, is_covered):
		self.is_covered = is_covered
		super().__init__(x, y, enemy)
	
	def modify_player(self, player):
		if self.enemy.is_alive():
			player.hp = player.hp - self.enemy.damage
			print("The {} dows {} damage. You have {} HP remaining.".format(self.enemy.name, self.enemy.damage, player.hp))

class ParlourHallway(MapTile):
	def intro_text(self):
		return """
		An unremarkable hallway. Candles dot the walls, filling the air with the smell of melting tallow.
		Doors mark the walls at intervals, you try all the handles as you walk past.
		"""
	
	def modify_player(self, player):
		#Room has no action on the player
		pass

class ParlourHallwayBend(MapTile):
	def intro_text(self):
		return """
		At first you were concerned that the walls were closing in on you, but really they're just turning. An unremarkable candle lit hallway with a bend in it.
		"""
		
	def modify_player(self, player):
		#Room Has no action on player
		pass

class ParlourHallwayT(MapTile):
	def intro_text(self):
		return """
		You arrive at a three way intersection of decrepit hallways.
		"""
	
	def modify_player(self, player):
		pass
		
class SpectreObservatory(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, enemies.Spectre())
	
	def intro_text(self):
		if self.enemy.is_alive():
			return """
			As you open the double doors just a hair, a harsh copper smell fills the air, and a loud hiss rings out from the center of the gargantuan observatory. A howling Spectre zooms overtop the desks and telescopes as the windows shatter and glass falls all around.
			"""
		else:
			return """
			You open the double doors, the copper smell finally having faded. The observatory is in disarray, papers tossed every which way. Almost all of the desks have deep, bloody scratches in them. Turning, you notice that even the walls are littered with ragged scarlet scrawls.
			"""
			
class ZombieHallway(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, enemies.Zombie())
		
	def intro_text(self):
		if self.enemy.is_alive():
			return """
			As you creep down the hallway, the flicker of candle light reveals a hunched over figure, heaving in the distance. It turns and faces you, its sunken eyes glinting as it smells you. The decaying corpse sprints at you, its footsteps thundering down the hall!"""
		else:
			return """
			As you walk down the hallway, the smell of rot cuts into your nose. Let's hope this one stays dead."""
			
class WretchedZombieBathroom(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, enemies.WretchedZombie())
	
	def intro_text(self):
		if self.enemy.is_alive():
			return """
			Ah finally, a bathroom! You wisely check under the stalls before you pick a seat. As you finish up, you wash your hands in the still running sink and look at yourself in the mirror. Your reflection is muddled, eyes melting into your nose, nose melting into your mouth. A great feeling of dread washes over you as you spy something else horrifying in the mirror. Groaning behind you, an exceptionally decayed corpse takes a swing at you from behind!"""
		else:
			return """
			The bathroom. Not much here but a rotting corpse and the mirrors. You dare not look at them again, lest your horrible reflection accost you again."""
	
class BatHallway(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, enemies.AngryBat())
		
	def intro_text(self):
		if self.enemy.is_alive():
			return """
			As you walk down the hallway, a clicking noise behind you tells you that something has been upset by your presence. A dark, darting shape drifts over your head to deeper down the hallway."""
		else:
			return """
			An unremarkable hallway with candles dotting the wall at set intervalls. You try the doors but everything is locked. A dead bat lies on the ground."""
			
class ZombieCellar(SecretTunnelEnemyRoom):
	#MUST DECLARE AND CARRY OVER IF COVERED FOR THIS ROOM.
	def __init__(self, x, y, enemy, is_covered):
		super().__init__(x, y, enemies.Zombie(), true)
	
	
	def intro_text(self):
		if self.enemy.is_alive() and self.is_covered:
			return """
			Creaking carefully down the stairs, you arrive to a musky cellar, filled with dusty wine bottles and, to your great surprise, a shambling member of the undead! A tuft of trash covers a vent in the wall.
			"""
		elif self.enemy.is_alive() and self.is_covered == false:
			return """
			Creaking carefully down the stairs, you arrive to a musky cellar, filled with dusty wine bottles and, to your great surprise, a shambling member of the undead! An exposed vent in the wall leads south, but it really shouldn't.
			"""
		elif self.enemy.is_alive() == false and self.is_covered:
			return """
			Creaking carefully down the stairs, you arrive to the musky cellar, a few wine bottles knocked off from your scuffle. There is a rotting corpse on the ground, and it looks like it is going to stay that way.
			"""
		else:
			return """
			Creaking carefully down the stairs, you arrive to the musky cellar, a few wine bottles knocked off from your scuffle. There is a rotting corpse on the ground, and it looks like it is going to stay that way. There is an exposed vent in the corner, leading south.
			"""

class FindRockRoom(LootRoom):
	def __init__(self, x, y):
		super().__init__(x, y, [items.Rock(), items.Pike()])
	
	def intro_text(self):
		return """
		A great room filled with empty, broken display cases sits saddened by its past grandeur. The offending rock sits in the biggest of the displays, along with the pike it is holding.
		"""
		
class FindHealingPotionRoom(LootRoom):
	def __init__(self, x, y):
		super().__init__(x, y, [items.HealingPotion(), items.HealingPotion()])
		
	def intro_text(self):
		return """
		You enter a small room, red and white wallpaper adorns the dirty edges of a metal box in the wall. Approaching carefully, you pry the front face off to reveal a pair of healing potions. A medical pack! Just what you need.
		"""
		
class FindScimtarRoom(CoveredLootRoom):
	def __init__(self, x, y):
		super().__init__(x, y, items.Scimtar(), tiles.ZombieCellar())
	
	def intro_text(self):
		
		return """
		Peeling back the vent leads into a tiny, secluded room built into the side of the house. A sheath in the corner looks interesting, you pick it up.
		"""
		