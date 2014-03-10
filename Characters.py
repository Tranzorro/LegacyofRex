
class Creature:  #base class for all livign things in the game, other classes inherit from this one.
	def __init__(self):

		self.name = "[You missed an override in the names here. D: check for the existance of a self.name in the monsters class!]"
		self.hp = 0
		self.mp = 0
		self.attack = 0
		self.defence = 0
		self.mattack = 0
		self.mdefence = 0
		self.atkchoice = 0
		self.runchoice = 0
		self.standing = "neutral"
		self.level = str(0)

class Player(Creature):  #player class, all stats the player has and actions are held here. inherits from creature class.
	def __init__(self):
		Creature.__init__(self)

		self.name = "Lord of Awesomeness"
		self.hp = 10
		self.mp = 10
		self.attack = 7
		self.defence = 3
		self.mattack = 4
		self.mdefence = 2

class CommonEnemy(Creature):
	#normal common enemy AI that only does basic fight tactics
	def __init__(self):
		Creature.__init__(self)

class Rare(Creature):  #rare creatures will have special unique battle mechanics as opposed to common monsters. rare fights do not have the standard tactics
	#enemies that are hardly ever found, but have higher understanding of battle. rewards are quite generous compared to common fights
	def __init__(self):
		Creature.__init__(self)

class Gremlin(CommonEnemy):  #gremlin enemy class, very weak baddie
	def __init__(self):
		CommonEnemy.__init__(self)

		self.name = "Gremlin"
		self.hp = 2
		self.attack = 4
		self.defence = 1
		self.atkchoice = 100
		self.runchoice = 10

class Kobold(CommonEnemy): #Kobold enemy class, another weenie baddie
	def __init__(self):
		CommonEnemy.__init__(self)

		self.name = "Kobold"
		self.hp = 3
		self.attack = 2
		self.defence = 2
		self.atkchoice = 100
		self.runchoice = 20

class Wolf(CommonEnemy): #wolf enemy class, a slighty stronger enemy meant to be able to actually kill the player.
	def __init__(self):
		CommonEnemy.__init__(self)

		self.name = "Wolf"
		self.hp = 7
		self.attack = 10
		self.defence = 5
		self.atkchoice = 100
		self.runchoice = 5

class Minotaur(CommonEnemy):
	def __init__(self):
		CommonEnemy.__init__(self)

		self.name = "Minotaur"
		self.hp = 250
		self.attack = 70
		self.defence = 20
		self.atkchoice = 100
		self.runchoice = 5

class Harpy(CommonEnemy):
		def __init__(self):
		CommonEnemy.__init__(self)

		self.name = "Harpy"
		self.hp = 50
		self.attack = 35
		self.defence = 35
		self.atkchoice = 100
		self.runchoice = 5

class Ram(CommonEnemy):
	def __init__(self):
		CommonEnemy.__init__(self)

		self.name = "Ram"
		self.hp = 25
		self.attack = 18
		self.defence = 30
		self.atkchoice = 100
		self.runchoice = 5


class Larck(Creature):
	self.standing = "neutral"
	self.name = "Larck"
	self.hp= 6000
	self.attack = 500
	self.defence = 500
	self.atkchoice = 100
	self.runchoice = 0
	self.level = "?"

class Irene(Creature):
	self.name = "Irene"
	self.hp = 400
	self.standing = "neutral"
	self.attack = 50
	self.defence = 50
	self.atkchoice = 100
	self.runchoice = 0

class Silvia(Creature):
	self.name = "Silvia"
	self.hp = 400
	self.standing = "neutral"
	self.attack = 50
	self.defence = 50
	self.atkchoice = 100
	self.runchoice = 0

class Bonny(Creature):
	self.name = "Bonny"
	self.hp = 400
	self.standing = "neutral"
	self.attack = 50
	self.defence = 50
	self.atkchoice = 100
	self.runchoice = 0

class Evana(Creature):
	self.name = "Evana"
	self.hp = 400
	self.standing = "neutral"
	self.attack = 50
	self.defence = 50
	self.atkchoice = 100
	self.runchoice = 0

class Stella(Creature):
	self.name = "Stella"
	self.hp = 400
	self.standing = "neutral"
	self.attack = 50
	self.defence = 50
	self.atkchoice = 100
	self.runchoice = 0

class Jenny(Creature):
	self.name = "Jenny"
	self.hp = 400
	self.standing = "neutral"
	self.attack = 50
	self.defence = 50
	self.atkchoice = 100
	self.runchoice = 0

class Lilly(Creature):
	self.name = "Lilly"
	self.hp = 400
	self.standing = "neutral"
	self.attack = 50
	self.defence = 50
	self.atkchoice = 100
	self.runchoice = 0

class Shawn(Creature):
	self.name = "Shawn"
	self.hp = 200
	self.standing = "neutral"
	self.attack = 50
	self.defence = 50
	self.atkchoice = 100
	self.runchoice = 0

class Zeru(Creature):
	self.name = "Zeru"
	self.hp = 100
	self.standing = "neutral"
	self.attack = 50
	self.defence = 50
	self.atkchoice = 100
	self.runchoice = 0

class Travis(Creature):
	self.name = "Travis"
	self.hp = 300
	self.standing = "neutral"
	self.attack = 50
	self.defence = 50
	self.atkchoice = 100
	self.runchoice = 0

class Michelle(Creature):
	self.name = "Michelle"
	self.hp = 300
	self.standing = "neutral"
	self.attack = 50
	self.defence = 50
	self.atkchoice = 100
	self.runchoice = 0

class Devan(Creature):
	self.name = "Devan"
	self.hp = 100
	self.standing = "neutral"
	self.attack = 50
	self.defence = 50
	self.atkchoice = 100
	self.runchoice = 0

class Valendras(Creature):
	self.name = "Valendras"
	self.hp = 10000
	self.standing = "neutral"
	self.attack = 50
	self.defence = 50
	self.atkchoice = 100
	self.runchoice = 0

class Hengul(Creature):
	self.name = "Hengul"
	self.hp = 8000
	self.standing = "neutral"
	self.attack = 50
	self.defence = 50
	self.atkchoice = 100
	self.runchoice = 0

class Dustin(Creature):
	self.name = "Dustin"
	self.hp = 700
	self.standing = "neutral"
	self.attack = 50
	self.defence = 50
	self.atkchoice = 100
	self.runchoice = 0

class Artemis(Creature):
	self.name = "Artemis"
	self.hp = 3000
	self.standing = "neutral"
	self.attack = 50
	self.defence = 50
	self.atkchoice = 100
	self.runchoice = 0

class Sally(Creature):
	self.name = "Sally"
	self.hp = 400
	self.standing = "neutral"
	self.attack = 50
	self.defence = 50
	self.atkchoice = 100
	self.runchoice = 0

class Mousegirl(Creature):
	self.name = "Mousegirl"
	self.hp = 100
	self.standing = "neutral"
	self.attack = 50
	self.defence = 50
	self.atkchoice = 100
	self.runchoice = 0

class Euna(Creature):
	self.name = "Euna"
	self.hp = 1000
	self.standing = "neutral"
	self.attack = 50
	self.defence = 50
	self.atkchoice = 100
	self.runchoice = 0