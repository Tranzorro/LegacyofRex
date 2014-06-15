
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
		self.sanity = 100
		self.stamina = 100
		self.statusailment1 = ""
		self.statusailment2 = ""
		self.path = "roflstomper"
		self.playerpos = None
		self.equipment = {"Head": "empty", "Chest": "empty", "Legs": "empty", "Feet": "empty", "LHand": "bare hand", "RHand": "bare hand"}



class Player(Creature):  #player class, all stats the player has and actions are held here. inherits from creature class.
	def __init__(self):
		Creature.__init__(self)

		self.name = "this is player"
		self.hp = 10
		self.mp = 5
		self.attack = 3
		self.defence = 2
		self.mattack = 5
		self.mdefence = 5
		self.sanity = 100
		self.stamina = 100
		self.path = "Adventurer"
		self.playerpos = None
		self.statusailment1 = ""
		self.statusailment2 = ""
		self.equipment = {"Head":"boobs", "Chest": "bra", "Legs": "strapon", "Feet": "flippers", "LHand": "bare hand", "RHand": "bare hand"}
		self.inventory = []


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
	def __init__(self):
		Creature.__init__(self)
		self.standing = "neutral"
		self.name = "Larck"
		self.hp= 6000
		self.attack = 500
		self.defence = 500
		self.atkchoice = 100
		self.runchoice = 0
		self.level = "?"
		self.sanity = 100
		self.stamina = 100
		self.path = "Beast_Whisperer"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}
		self.inventory = []


class Irene(Creature):
	def __init__(self):
		Creature.__init__(self)
		self.name = "Irene"
		self.hp = 400
		self.standing = "neutral"
		self.attack = 50
		self.defence = 50
		self.atkchoice = 100
		self.runchoice = 0
		self.sanity = 100
		self.stamina = 100
		self.path = "Fighter"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}
		self.inventory = []

class Silvia(Creature):
	def __init__(self):
		Creature.__init__(self)
		self.name = "Silvia"
		self.hp = 400
		self.standing = "neutral"
		self.attack = 50
		self.defence = 50
		self.atkchoice = 100
		self.runchoice = 0
		self.sanity = 100
		self.stamina = 100
		self.path = "Mage"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}
		self.inventory = []

class Bonny(Creature):
	def __init__(self):
		Creature.__init__(self)
		self.name = "Bonny"
		self.hp = 400
		self.standing = "neutral"
		self.attack = 50
		self.defence = 50
		self.atkchoice = 100
		self.runchoice = 0
		self.sanity = 100
		self.stamina = 100
		self.path = "Fighter"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}
		self.inventory = []

class Evana(Creature):
	def __init__(self):
		Creature.__init__(self)
		self.name = "Evana"
		self.hp = 400
		self.standing = "neutral"
		self.attack = 50
		self.defence = 50
		self.atkchoice = 100
		self.runchoice = 0
		self.sanity = 100
		self.stamina = 100
		self.path = "Healer"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}
		self.inventory = []

class Stella(Creature):
	def __init__(self):
		Creature.__init__(self)
		self.name = "Stella"
		self.hp = 400
		self.standing = "neutral"
		self.attack = 50
		self.defence = 50
		self.atkchoice = 100
		self.runchoice = 0
		self.sanity = 100
		self.stamina = 100
		self.path = "Brawler"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}
		self.inventory = []

class Jenny(Creature):
	def __init__(self):
		Creature.__init__(self)
		self.name = "Jenny"
		self.hp = 400
		self.standing = "neutral"
		self.attack = 50
		self.defence = 50
		self.atkchoice = 100
		self.runchoice = 0
		self.sanity = 100
		self.stamina = 100
		self.path = "Ninja"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}
		self.inventory = []

class Lilly(Creature):
	def __init__(self):
		Creature.__init__(self)
		self.name = "Lilly"
		self.hp = 400
		self.standing = "neutral"
		self.attack = 50
		self.defence = 50
		self.atkchoice = 100
		self.runchoice = 0
		self.sanity = 100
		self.stamina = 100
		self.path = "Thief"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}
		self.inventory = []

class Shawn(Creature):
	def __init__(self):
		Creature.__init__(self)
		self.name = "Shawn"
		self.hp = 200
		self.standing = "neutral"
		self.attack = 50
		self.defence = 50
		self.atkchoice = 100
		self.runchoice = 0
		self.sanity = 100
		self.stamina = 100
		self.path = "Hunter"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}
		self.inventory = []

class Zeru(Creature):
	def __init__(self):
		Creature.__init__(self)
		self.name = "Zeru"
		self.hp = 100
		self.standing = "neutral"
		self.attack = 50
		self.defence = 50
		self.atkchoice = 100
		self.runchoice = 0
		self.sanity = 100
		self.stamina = 100
		self.path = "Archer"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}
		self.inventory = []

class Travis(Creature):
	def __init__(self):
		Creature.__init__(self)
		self.name = "Travis"
		self.hp = 300
		self.standing = "neutral"
		self.attack = 50
		self.defence = 50
		self.atkchoice = 100
		self.runchoice = 0
		self.sanity = 100
		self.stamina = 100
		self.path = "Mage"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}
		self.inventory = []

class Michelle(Creature):
	def __init__(self):
		Creature.__init__(self)
		self.name = "Michelle"
		self.hp = 300
		self.standing = "neutral"
		self.attack = 50
		self.defence = 50
		self.atkchoice = 100
		self.runchoice = 0
		self.sanity = 100
		self.stamina = 100
		self.path = "Pirate"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}
		self.inventory = []

class Devan(Creature):
	def __init__(self):
		Creature.__init__(self)
		self.name = "Devan"
		self.hp = 100
		self.standing = "neutral"
		self.attack = 50
		self.defence = 50
		self.atkchoice = 100
		self.runchoice = 0
		self.sanity = 100
		self.stamina = 100
		self.path = "Fighter"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}
		self.inventory = []

class Valendras(Creature):
	def __init__(self):
		Creature.__init__(self)
		self.name = "Valendras"
		self.hp = 10000
		self.standing = "neutral"
		self.attack = 50
		self.defence = 50
		self.atkchoice = 100
		self.runchoice = 0
		self.sanity = 100
		self.stamina = 100
		self.path = "Shadow_Lord"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}
		self.inventory = []

class Hengul(Creature):
	def __init__(self):
		Creature.__init__(self)
		self.name = "Hengul"
		self.hp = 8000
		self.standing = "neutral"
		self.attack = 50
		self.defence = 50
		self.atkchoice = 100
		self.runchoice = 0
		self.sanity = 100
		self.stamina = 100
		self.path = "Battlemage"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}
		self.inventory = []

class Dustin(Creature):
	def __init__(self):
		Creature.__init__(self)
		self.name = "Dustin"
		self.hp = 700
		self.standing = "neutral"
		self.attack = 50
		self.defence = 50
		self.atkchoice = 100
		self.runchoice = 0
		self.sanity = 100
		self.stamina = 100
		self.path = "Brawler"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}
		self.inventory = []

class Artemis(Creature):
	def __init__(self):
		Creature.__init__(self)
		self.name = "Artemis"
		self.hp = 3000
		self.standing = "neutral"
		self.attack = 50
		self.defence = 50
		self.atkchoice = 100
		self.runchoice = 0
		self.sanity = 100
		self.stamina = 100
		self.path = "Archmage"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}
		self.inventory = []

class Sally(Creature):
	def __init__(self):
		Creature.__init__(self)
		self.name = "Sally"
		self.hp = 400
		self.standing = "neutral"
		self.attack = 50
		self.defence = 50
		self.atkchoice = 100
		self.runchoice = 0
		self.sanity = 100
		self.stamina = 100
		self.path = "Sniper"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}
		self.inventory = []

class Mousegirl(Creature):
	def __init__(self):
		Creature.__init__(self)
		self.name = "Mousegirl"
		self.hp = 100
		self.standing = "neutral"
		self.attack = 50
		self.defence = 50
		self.atkchoice = 100
		self.runchoice = 0
		self.sanity = 100
		self.stamina = 100
		self.path = "Tamer"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}
		self.inventory = []

class Euna(Creature):
	def __init__(self):
		Creature.__init__(self)
		self.name = "Euna"
		self.hp = 1000
		self.standing = "neutral"
		self.attack = 50
		self.defence = 50
		self.atkchoice = 100
		self.runchoice = 0
		self.sanity = 100
		self.stamina = 100
		self.path = "???"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}
		self.inventory = []

class Empty(Creature): #for a placeholder on the screen when the party is empty. nothing more. if this class is ever used to actually do anything, you broke it!
	def __init__(self):
		Creature.__init__(self)
		self.name = ""
		self.hp = ""
		self.attack = ""
		self.defence = ""
		self.mp = ""
		self.sanity = ""
		self.stamina = ""
		self.statusailment1 = ""
		self.statusailment2 = ""
		self.playerpos = None
		self.path = ""
		self.equipment = {"Head":"", "Chest":"", "Legs":"", "Feet":"", "LHand":"", "RHand":""}