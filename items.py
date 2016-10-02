class Item():
	"""The Base Class for all Items"""
	def __init__(self, name, description, value):
		self.name = name
		self.description = description
		self.value = value
	
	def __str__(self):
		"""Sets the value returned by print()ing"""
		return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class HealingItem(Item):
	def __init__(self, name, description, value, healing_ammt):
		self.healing_ammt = healing_ammt
		super().__init__(name, description, value)
		
	def __str__(self):
		return "{}\n=====\n{}\n\Value: {}\nHealing Ammount: {}".format(self.name, self.description, self.value, self.healing_ammt)


##### HEALING ITEMS #####


class HealingPotion(HealingItem):
	def __init__(self):
		super().__init__(name="Healing Potion", description="A cylindrical vial of pulsating red goo. It really is best all in one go, not to sip. Has a label with 50 scrawled in shakey handwriting.", value=100, healing_ammt=50)

class MinorHealingPotion(HealingItem):
	def __init__(self):
		super().__init__(name="Minor Healing Potion", description="An obtuse angled vial of blue liquid. Faint aroma of wheatgrass. Probably best to shoot. Has a label with 25 scrawled in shakey handwriting.", value=50, healing_ammt=25)
		
		
##### ECONOMIC ITEMS #####

class Gold(Item):
	def __init__(self, amt):
		self.amt = amt
		super().__init__(name="Gold", description="A round coin with {} chiseled into the front and back.".format(str(self.amt)), value=self.amt*10000)
		
class Silver(Item):
	def __init__(self, amt):
		self.amt = amt
		super().__init__(name="Silver", description="A squarish coin with {} chiseled into the front and back.".format(str(self.amt)), value=self.amt*100)
		
class Copper(Item):
	def __init__(self, amt):
		self.amt = amt
		super().__init__(name="Copper", description="A round coin with a square hole directly in the center. It has {} chiseled around the front and back rims.".format(str(self.amt)), value=self.amt)
		
##### EDIBLE ITEMS ######

class Apple(Item):
	def __init__(self, color):
		self.color = color
		super().__init__(name="{} Apple".format(str(self.color)), description="A juicy looking {} apple. Looks tasty.".format(str(self.color)),value=5)
	""" Probably want to create an edible class and inherit from that later """

class Weapon(Item):
	def __init__(self, name, description, value, damage):
		self.damage = damage
		super().__init__(name, description, value)
		
	def __str__(self):
		return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
	
class EnemyWeapon(Item):
	def __init__(self, name, description, value):
		super().__init__(name, description, value)
	def __str__(self):
		return "{}\n=====\n{}\nValue: {}\nThis is an enemy weapon. Wonder how you found it?".format(self.name, self.description, self.value)
		
		
##### PLAYER WEAPONS


class Rock(Weapon):
	def __init__(self):
		super().__init__(name="Rock", description="A shard of granite, looks almost sharp enough to slash with.", value=0, damage=14)

class Scimtar(Weapon):
	def __init__(self):
		super().__init__(name="Scimtar", description="A glistening edge follows the razor all along its curved side. A sickly scimtar.", value=25, damage=30)

class Pike(Weapon):
	def __init__(self):
		super().__init__(name="Pike", description="A long, slender, and heavy weapon. Perfect for perforation at a distance.", value=20, damage=40)

class FingerCannon(Weapon):
	def __init__(self):
		super().__init__(name="Finger Cannon", description="An ancient technique known as 'finger pistols'. Bang!", value=0, damage=500)
		
class Fists(Weapon):
	def __init__(self):
		super().__init__(name="Fists", description="An ancient technique, known as 'box-hing'. Your scrawny fists can't do much.", value=0, damage=10)


##### ENEMY WEAPONS

		
class ZombieSlash(EnemyWeapon):
	def __init__(self):
		super().__init__(name="Zombie Slash", description="The Zombie slashes at you with its decaying fists!", value=0)
		
class SpectreBlast(EnemyWeapon):
	def __init__(self):
		super().__init__(name="Spectre Blast", description="The Spectre screeches and launches charged ectoplasm from its fingertips!", value=0)
		
class BatSlash(EnemyWeapon):
	def __init__(self):
		super().__init__(name="Bat Slash", description="The Bat swings down and slashes at your face!", value=0)
		
class WraithBlast(EnemyWeapon):
	def __init__(self):
		super().__init__(name="Wraith Blast", description="The Wraith utters a low, gurgling chant as dark energy bundles in its hands before it shoots out at you like needles!", value=0)