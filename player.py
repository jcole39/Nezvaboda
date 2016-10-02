import random
import items, world, enemies

class Player():
	def __init__(self):
		self.inventory = [items.Gold(15), items.Fists()] #DECLARE STARTING ITEMS HERE
		self.level = random.randint(1,3)
		self.exp = 0
		self.currentWeapon = ''
		self.strength = random.randint(1,10)
		self.intellect = random.randint(1,10)
		self.discipline = random.randint(1,10)
		self.summoning = random.randint(1,10)
		self.maxhp = 45 + (self.strength * self.discipline) * (self.level * 0.65)
		self.hp = self.maxhp
		self.location_x, self.location_y = world.starting_position
		self.victory = False
		self.lastDirection = ''
		self.lastAction = ''
		self.hpRegen = (random.randint(1,20) + (self.maxhp / 10)) * (self.discipline * 0.65)
		
		# For Pissing Contests
		self.bestEnemyKilled = enemies.EmptyEnemy()
	
	def is_alive(self):
		return self.hp > 0
		
	def check_if_best_kill(self, enemy):
		return enemy.maxhp > self.bestEnemyKilled.maxhp
	
	def initiative_roll(self):
		return random.randint(1,20) + self.discipline
	
	def levelup(self):
		self.level += 1
		self.hp = 45 + (self.strength * self.discipline) * (self.level * 0.65 * 4)
		print("You just reached level {}! You have {} exp.".format(self.level, self.exp))
	
	def show_level(self):
		print("You are level {} with {} exp.".format(self.level, self.exp))
		
	def give_xp(self, xp):
		if (self.level * 0.65) * 1000 < self.exp + xp:
			self.exp = (self.exp + xp) - ((self.level * 0.65) * 1000)
			self.levelup()
		else:
			self.exp += xp
	
	def suicide(self):
		self.hp = -1
	
	def print_inventory(self):
		for item in self.inventory:
			print(item, '\n')

	#BEGIN CODING PLAYER ACTIONS
	def move(self, dx, dy):
		self.location_x += dx
		self.location_y += dy
		print(world.tile_exists(self.location_x, self.location_y).intro_text())
	
	def move_north(self):
		self.move(dx=0, dy=-1)
		self.lastDirection = 'north'
	
	def move_south(self):
		self.move(dx=0, dy=1)
		self.lastDirection = 'south'
	
	def move_east(self):
		self.move(dx=1, dy=0)
		self.lastDirection = 'east'
	
	def move_west(self):
		self.move(dx=-1, dy=0)
		self.lastDirection = 'west'
	
	def attack(self, enemy):
		best_weapon = None
		max_dmg = 0
		for i in self.inventory:
			if isinstance(i, items.Weapon):
				if i.damage > max_dmg:
					max_dmg = i.damage
					best_weapon = i
		dealt = best_weapon.damage + random.randint(int(self.strength/2), self.strength)*2
		enemy.hp -= dealt
		print("You use {} against {} and dealt {} damage!".format(best_weapon.name, enemy.name, dealt))
		
		if enemy.is_alive():
			print("{} HP is {}.".format(enemy.name, enemy.hp))
			
		else:
			reward = enemy.xpReward * (self.level * 0.65)
			self.give_xp(reward)
			print("You killed {} and got {} exp!".format(enemy.name, reward))
			if self.check_if_best_kill(enemy):
				self.bestEnemyKilled = enemy
			
	def heal(self):
		best_hi = None
		max_hp_res = 0
		for i in self.inventory:
			if isinstance(i, items.HealingItem):
				if i.healing_ammt > max_hp_res:
					max_hp_res = i.healing_ammt
					best_hi = i
		if best_hi == None:
			print("\nNo health items found! Best of luck!")
			pass
		else:
			healed = best_hi.healing_ammt + random.randint(int(self.discipline/2), self.discipline)*20
			if self.hp + healed > self.maxhp:
				self.hp = self.maxhp
				self.inventory.remove(best_hi)
			else:
				self.hp += healed
				self.inventory.remove(best_hi)
			print("Healed you right up! You're at {} HP.".format(self.hp))
			
	def do_action(self, action, **kwargs):
		action_method = getattr(self, action.method.__name__)
		self.lastAction = action.method.__name__
		if action_method:
			action_method(**kwargs)
	
	def info(self):
		print(world.tile_exists(self.location_x, self.location_y).intro_text())
	
	def showHealth(self):
		print(self.hp)
	
	def flee(self, tile):
		#Moves player to random adjacent tile
		available_moves = tile.adjacent_moves()
		r = random.randint(0, len(available_moves))
		self.do_action(available_moves[r])
		