class Character:
	def __init__(self, damage, health, name):
		self.damage = damage
		self.health = health
		self.name = name
		
	def attack(self, enemy):
		ememy.take_damage(self.damage)
			
	def take_damage(self, damage):
		self.health -= damage
		if self.health <= 0:
			print "%r is dead", self.name

class Hero(Character):
	def __init__(self, damage = 10, health = 30, name = "Hero"):
		super(Hero, self).__init__(damage, health, name)
		max_health = 50
		self.xp = 0
		self.level = 1
		self.xplevels = [10, 20, 30, 40, 50 ,60]
		xp_to_next_level = xplevels[level-1]
		
	
	def rest(self):
		self.health += self.damage 
		if self.health >= max_health:
			self.health = max_health
			print (self.name + ' health full')
	
	def level_up(self):
		self.xp += 10
		if self.xp is self.xp_to_next_level:
			self.level += 1
			print "Congrats %s your level has increased to level %s" %(self.name, self.level)
			self.xp_to_next_level = self.xplevels[level-1]
			self.xp = 0
			
	def attack(self, enemy):
		super(Hero, self).attack(enemy)
		if enemy.health is 0:
			self.lvlup()
			
	def __str__(self):
		return 'Name: %s \n Health: %s \n Level: %s ' 
			
			
class Monster(Character):
	def __init__(self, damage, health, name):
		super(Monster, self).__init__(damage, health, name)
		
	def __str__(self):
		return "Name: %s \n Health: %s" %(sel.name, self.health)


class Goblin(Monster):
	def __init__(self, damage = 5, health = 10, name = 'Goblin'):
		super(Goblin, self).__init__(damage, health, name)
		

class Orc(Monster):
	def __init__(self, damage = 10, health = 20, name = 'Orc'):
		super(Orc, self).__init__(damage, health, name)
	
def explore():
	monstertype = random.choices([Goblin(), Orc(), None], [0.4, 0.1, 0.5], k = 1)
	return monstertype[0]
