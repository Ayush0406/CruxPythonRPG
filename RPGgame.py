class Character:
	def __init__(self, damage, health, name):
		self.damage = damage
		self.health = health
		self.name = name
		
	def attack(self, enemy):
		ememy.health -= self.damage
		if enemy.health <= 0:
			print "%r KILLED", enemy.name
			
	def take_damage(self, damage):
		self.health -= damage
		if self.health <= 0:
			print "%r is dead", self.name

class Hero(Character):
	def __init__(self, damage = 10, health = 30, name = "Hero"):
		super(Hero, self).__init__(damage, health, name)
		max_health = 50
	
	def rest(self):
		self.health += self.damage
		if self.health >= max_health:
			self.health = max_health
			print (self.name + ' health full')
	
	
class Monster(Character):
	def __init__(self, damage, health, name):
		super(Monster, self).__init__(damage, health, name)


class Goblin(Monster):
	def __init__(self, damage = 5, health = 10, name = 'Goblin'):
		super(Goblin, self).__init__(damage, health, name)
		

class Orc(Monster):
	def __init__(self, damage = 10, health = 20, name = 'Orc'):
		super(Orc, self).__init__(damage, health, name)
	
