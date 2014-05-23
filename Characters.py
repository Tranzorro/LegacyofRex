
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
		self.status = None
		self.path = "Adventurer"
		self.playerpos = None
		self.equipment = {"Head": "empty", "Chest": "empty", "Legs": "empty", "Feet": "empty", "LHand": "bare hand", "RHand": "bare hand"}

		def update_stat_window():
			pass


class Player(Creature):  #player class, all stats the player has and actions are held here. inherits from creature class.
	def __init__(self):
		Creature.__init__(self)

		self.name = "this is player"
		self.hp = "wut"
		self.mp = "wut"
		self.attack = "wut"
		self.defence = "wut"
		self.mattack = "wut"
		self.mdefence = "wut"
		self.sanity = "wut"
		self.stamina = "wut"
		self.status = "i r dumb"
		self.path = "Adventurer"
		self.playerpos = None
		self.equipment = {"Head":"", "Chest": "", "Legs": "", "Feet": "", "LHand": "", "RHand": ""}

	def update_stat_window(self):
		if self.playerpos == "first":
			char_Name = stat_font.render("Name: " + Player1.name, True, white) #limit all names by 18 characters
			char_Health = stat_font.render("HP: " + Player1.hp, True, white)
			char_Defence = stat_font.render("Def: " + Player1.defence, True, white)
			char_Attack = stat_font.render("Atk: " + Player1.attack, True, white)
			char_Magic = stat_font.render("MP: " + Player1.mp, True, white)
			char_Sanity = stat_font.render("San: " + Player1.sanity, True, white)
			char_Stamina = stat_font.render("Sta: " + Player1.stamina, True, white)
			char_Status1 = stat_font.render("Status: tox, bur, cur, pet, slw", True, white)
			char_Status2 = stat_font.render("ice, bli, zom, par, sho, ins", True, white)
			char_Path = stat_font.render("Path: " + Player1.path, True, white)
			char_Head = stat_font.render("Head: " + Player1.equipment["Head"], True, white) #limit item names for this slot to 22 characters
			char_Chest = stat_font.render("Chest: " + Player1.equipment["Chest"], True, white) # limit names to 22
			char_Legs = stat_font.render("Legs: " + Player1.equipment["Legs"], True, white) # limit names to 23
			char_Feet = stat_font.render("Feet: " + Player1.equipment["Feet"], True, white) #limit names to 23
			char_LeftHand = stat_font.render("LHand: " + Player1.equipment["LHand"], True, white) # limit names to 23
			char_RightHand = stat_font.render("RHand: " + Player1.equipment["RHand"], True, white) # limit names to 23
			screen.blit(char_Name, [15, 15]) #x, y
			screen.blit(char_Health, [15, 30]) # x, y
			screen.blit(char_Defence, [100, 30]) #x, y
			screen.blit(char_Attack, [185, 30])
			screen.blit(char_Magic, [15, 45]) # x, y
			screen.blit(char_Sanity, [100, 45]) #x, y
			screen.blit(char_Stamina, [185, 45])
			screen.blit(char_Status1, [15, 60]) # x, y
			screen.blit(char_Status2, [15, 75]) # x, y
			screen.blit(char_Path, [15, 90]) # x, y
			screen.blit(char_Head, [15, 105]) # x, y
			screen.blit(char_Chest, [15, 120]) # x, y
			screen.blit(char_Legs, [15, 135]) # x, y
			screen.blit(char_Feet, [15, 150]) # x, y
			screen.blit(char_LeftHand, [15, 165]) # x, y
			screen.blit(char_RightHand, [15, 180]) # x, y
		elif self.playerpos == "second":
			character_stats2 = stat_font.render("Name: " + Player2.name, True, white)
			character_stats2_a = stat_font.render("HP: " + Player2.hp, True, white)
			character_stats2_a_a = stat_font.render("Def: " + Player2.defence, True, white)
			character_stats2_a_b = stat_font.render("Atk: " + Player2.attack, True, white)
			character_stats2_b = stat_font.render("MP: " + Player2.mp, True, white)
			character_stats2_b_a = stat_font.render("San: " + Player2.sanity, True, white)
			character_stats2_b_b = stat_font.render("Sta: " + Player2.stamina, True, white)
			character_stats2_c = stat_font.render("Status: tox, bur, cur, pet, slw", True, white)
			character_stats2_c_a = stat_font.render("ice, bli, zom, par, sho, ins", True, white)
			character_stats2_E = stat_font.render("Path: " + Player2.path, True, white)
			character_stats2_E_a = stat_font.render("Head: " + Player2.equipment["Head"], True, white)
			character_stats2_E_b = stat_font.render("Chest: " + Player2.equipment["Chest"], True, white)
			character_stats2_E_c = stat_font.render("Legs: " + Player2.equipment["Legs"], True, white)
			character_stats2_E_d = stat_font.render("Feet: " + Player2.equipment["Feet"], True, white)
			character_stats2_E_e = stat_font.render("LHand: " + Player2.equipment["LHand"], True, white)
			character_stats2_E_f = stat_font.render("RHand: " + Player2.equipment["RHand"], True, white)
			screen.blit(character_stats2, [274, 15])
			screen.blit(character_stats2_a, [274, 30]) # x, y
			screen.blit(character_stats2_a_a, [359, 30])
			screen.blit(character_stats2_a_b, [444, 30])
			screen.blit(character_stats2_b, [274, 45]) # x, y
			screen.blit(character_stats2_b_a, [359, 45])
			screen.blit(character_stats2_b_b, [444, 45])
			screen.blit(character_stats2_c, [274, 60]) # x, y
			screen.blit(character_stats2_c_a, [274, 75]) # x, y
			screen.blit(character_stats2_E, [274, 90]) # x, y
			screen.blit(character_stats2_E_a, [274, 105]) # x, y
			screen.blit(character_stats2_E_b, [274, 120]) # x, y
			screen.blit(character_stats2_E_c, [274, 135]) # x, y
			screen.blit(character_stats2_E_d, [274, 150]) # x, y
			screen.blit(character_stats2_E_e, [274, 165]) # x, y
			screen.blit(character_stats2_E_f, [274, 180]) # x, y
		elif slef.playerpos == "third":
			character_stats3 = stat_font.render("Name: " + Player3.name , True, white)
			character_stats3_a = stat_font.render("HP: " + Player3.hp, True, white)
			character_stats3_a_a = stat_font.render("Def: " + Player3.defence, True, white)
			character_stats3_a_b = stat_font.render("Atk: " + Player3.attack, True, white)
			character_stats3_b = stat_font.render("MP: " + Player3.mp, True, white)
			character_stats3_b_a = stat_font.render("San: " + Player3.sanity, True, white)
			character_stats3_b_b = stat_font.render("Sta: " + Player3.stamina, True, white)
			character_stats3_c = stat_font.render("Status: tox, bur, cur, pet, slw", True, white)
			character_stats3_c_a = stat_font.render("ice, bli, zom, par, sho, ins", True, white)
			character_stats3_E = stat_font.render("Path: " + Player3.path, True, white)
			character_stats3_E_a = stat_font.render("Head: " + Player3.equipment["Head"], True, white)
			character_stats3_E_b = stat_font.render("Chest: " + Player3.equipment["Chest"], True, white)
			character_stats3_E_c = stat_font.render("Legs: " + Player3.equipment["Legs"], True, white)
			character_stats3_E_d = stat_font.render("Feet: " + Player3.equipment["Feet"], True, white)
			character_stats3_E_e = stat_font.render("LHand: " + Player3.equipment["LHand"], True, white)
			character_stats3_E_f = stat_font.render("RHand: " + Player3.equipment["RHand"], True, white)
			screen.blit(character_stats3, [15, 224])
			screen.blit(character_stats3_a, [15, 239]) # x, y
			screen.blit(character_stats3_a_a, [100, 239])
			screen.blit(character_stats3_a_b, [185, 239])
			screen.blit(character_stats3_b, [15, 254]) # x, y
			screen.blit(character_stats3_b_a , [100, 254]) #x, y
			screen.blit(character_stats3_b_b, [185, 254])
			screen.blit(character_stats3_c, [15, 269]) # x, y
			screen.blit(character_stats3_c_a, [15, 284]) # x, y
			screen.blit(character_stats3_E, [15, 299]) # x, y
			screen.blit(character_stats3_E_a, [15, 314]) # x, y
			screen.blit(character_stats3_E_b, [15, 329]) # x, y
			screen.blit(character_stats3_E_c, [15, 344]) # x, y
			screen.blit(character_stats3_E_d, [15, 359]) # x, y
			screen.blit(character_stats3_E_e, [15, 374]) # x, y
			screen.blit(character_stats3_E_f, [15, 389]) # x, y
		elif self.playerpos == "fourth":
			character_stats4 = stat_font.render("Name: " + Player4.name, True, white)
			character_stats4_a = stat_font.render("HP: " + Player4.hp, True, white)
			character_stats4_a_a = stat_font.render("Def: " + Player4.defence, True, white)
			character_stats4_a_b = stat_font.render("Atk: " + Player4.attack, True, white)
			character_stats4_b = stat_font.render("MP: " + Player4.mp, True, white)
			character_stats4_b_a = stat_font.render("San: " + Player4.sanity, True, white)
			character_stats4_b_b = stat_font.render("Sta: " + Player4.stamina, True, white)
			character_stats4_c = stat_font.render("Status: tox, bur, cur, pet, slw", True, white)
			character_stats4_c_a = stat_font.render("ice, bli, zom, par, sho, ins", True, white)
			character_stats4_E = stat_font.render("Path: " + Player4.path, True, white)
			character_stats4_E_a = stat_font.render("Head: " + Player4.equipment["Head"], True, white)
			character_stats4_E_b = stat_font.render("Chest: " + Player4.equipment["Chest"], True, white)
			character_stats4_E_c = stat_font.render("Legs: " + Player4.equipment["Legs"], True, white)
			character_stats4_E_d = stat_font.render("Feet: " + Player4.equipment["Feet"], True, white)
			character_stats4_E_e = stat_font.render("LHand: " + Player4.equipment["LHand"], True, white)
			character_stats4_E_f = stat_font.render("RHand: " + Player4.equipment["RHand"], True, white)
			screen.blit(character_stats4, [274, 224])
			screen.blit(character_stats4_a, [274, 239]) # x, y
			screen.blit(character_stats4_a_a, [359, 239])
			screen.blit(character_stats4_a_b, [444, 239])
			screen.blit(character_stats4_b, [274, 254]) # x, y
			screen.blit(character_stats4_b_a, [359, 254])
			screen.blit(character_stats4_b_b, [444, 254])
			screen.blit(character_stats4_c, [274, 269]) # x, y
			screen.blit(character_stats4_c_a, [274, 284]) # x, y
			screen.blit(character_stats4_E, [274, 299]) # x, y
			screen.blit(character_stats4_E_a, [274, 314]) # x, y
			screen.blit(character_stats4_E_b, [274, 329]) # x, y
			screen.blit(character_stats4_E_c, [274, 344]) # x, y
			screen.blit(character_stats4_E_d, [274, 359]) # x, y
			screen.blit(character_stats4_E_e, [274, 374]) # x, y
			screen.blit(character_stats4_E_f, [274, 389]) # x, y


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
		self.status = None
		self.path = "Adventurer"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}


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
		self.status = None
		self.path = "Adventurer"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}

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
		self.status = None
		self.path = "Adventurer"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}

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
		self.status = None
		self.path = "Adventurer"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}

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
		self.status = None
		self.path = "Adventurer"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}

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
		self.status = None
		self.path = "Adventurer"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}

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
		self.status = None
		self.path = "Adventurer"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}

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
		self.status = None
		self.path = "Adventurer"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}

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
		self.status = None
		self.path = "Adventurer"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}

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
		self.status = None
		self.path = "Adventurer"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}

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
		self.status = None
		self.path = "Adventurer"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}

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
		self.status = None
		self.path = "Adventurer"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}

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
		self.status = None
		self.path = "Adventurer"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}

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
		self.status = None
		self.path = "Adventurer"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}

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
		self.status = None
		self.path = "Adventurer"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}

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
		self.status = None
		self.path = "Adventurer"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}

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
		self.status = None
		self.path = "Adventurer"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}

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
		self.status = None
		self.path = "Adventurer"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}

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
		self.status = None
		self.path = "Adventurer"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}

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
		self.status = None
		self.path = "Adventurer"
		self.playerpos = None
		self.equipment = {"Head":" ", "Chest": " ", "Legs": " ", "Feet": " ", "LHand": " ", "RHand": " "}