import random
import items

class Enemy:
	def __init__(self, name, xpReward, str, int, dis, sum, lvl, wpn):
		self.name = name
		self.strength = str
		self.intellect = int
		self.discipline = dis
		self.summoning = sum
		self.lvl = lvl
		self.xpReward = (xpReward + random.randint(self.lvl, self.lvl*4)) * 20
		# ON ENEMY CREATION CHOOSE CLASS BASED ON STATS
		# CHOOSE DAMAGE TYPE BASED ON STATS
		if self.strength >= self.intellect >= self.discipline >= self.summoning:
			self.enemy_class = 'Demon'
			self.damage = 2 + (self.strength * self.intellect) * (self.lvl * 0.65)
		elif self.intellect >= self.discipline >= self.summoning >= self.strength:
			self.enemy_class = 'Brainiac'
			self.damage = 2 + (self.discipline * self.intellect) * (self.lvl * 0.65)
		elif self.discipline >= self.summoning >= self.strength >= self.intellect:
			self.enemy_class = 'Corrupted'
			self.damage = 2 + (self.discipline * self.summoning) * (self.lvl * 0.65)
		elif self.summoning >= self.strength >= self.intellect >= self.discipline:
			self.enemy_class = 'Caster'
			self.damage = 2 + (self.strength * self.summoning) * (self.lvl * 0.65)
		else:
			self.enemy_class = 'Unassigned'
			self.damage = 2 + ((self.strength * self.summoning)*(self.intellect * self.discipline) * 0.5) * (self.lvl * 0.65)
		self.dealt = random.randint(1,20) + self.damage
		self.maxhp = 20 + (self.strength * self.discipline) * (self.lvl * 0.65)
		self.hp = self.maxhp
		self.wpn = wpn
	
	def is_alive(self):
		return self.hp > 0
	
	def initiative_roll(self):
		return random.randint(1,20) + self.discipline
		
		#### ADD IN THE STATS FOR EACH ENEMY!!!

class EmptyEnemy(Enemy):
	def __init__(self):
		super().__init__(name="Empty Enemy", xpReward=0, str=0,int=0,dis=0,sum=0,lvl=0,wpn=items.BatSlash())
		
class Zombie(Enemy):
	def __init__(self):
		super().__init__(name="Zombie", xpReward=40, str=3, int=1, dis=5, sum=3, lvl=2, wpn=items.ZombieSlash())
		
class WretchedZombie(Enemy):
	def __init__(self):
		super().__init__(name="Wretched Zombie", xpReward=140, str=4, int=2, dis=6, sum=4, lvl=4, wpn=items.ZombieSlash())

class AngryBat(Enemy):
	def __init__(self):
		super().__init__(name="Angry Bat", xpReward=10, str=1, int=1, dis=3, sum=2, lvl=1, wpn=items.BatSlash())
		
class Spectre(Enemy):
	def __init__(self):
		super().__init__(name="Spectre", xpReward=130, str=6, int=5, dis=3, sum=7, lvl=6, wpn=items.SpectreBlast())

class Wraith(Enemy):
	def __init__(self):
		super().__init__(name="Wraith", xpReward=500, str=5, int=3, dis=3, sum=6, lvl=8, wpn=items.WraithBlast())

