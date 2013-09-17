#stats to use when making the stats class / functions / methods.

class BaseStats:  #stats every npc has

	def __init__(self):

		self.name = ""
		self.description = "i look like something."  #description of pc/npc when looking at reflection/ npc
		self.spells = ['rock_toss', 'scorch', 'gust', 'water_ball']
		self.allignment = None
		self.abilities = []   # list of special moves you can perform
		self.current_path = None
		self.affinities = {}  # list of affinities you have gained
		self.affinities = {"knight":0, "thief":0, "healer":0, "mage":0, "archer":0, "fighter":0, "summoner":0, "rider":0, "tamer":0, "paladin":0, "shadow_lord":0,
		"ninja":0, "pirate":0, "priest":0, "druid":0, "archmage":0, "battlemage":0, "hunter":0, "sniper":0, "brawler":0, "martial_artist":0, "angel_caller":0,
		"demon_caller":0, "jouster":0, "dragoon":0, "beast_whisperer":0, "beast_master":0}
		self.inventory = []
		self.equipment = []
		self.item_drop = []
		self.currency = 0
		# battle stats VVVVV
		self.hp = 0      # health points
		self.mp = 0      # magic points
		self.strength = 0   # modifier to add onot attack damage, also dictates what weapons you may or may not weild. and objects you can or cannot carry
		self.speed = 0      # how fast you can travel, and a modifier for evasion. 
		self.intillect = 0  # modifier to add magic points, and dictates what spells you may or may not learn and or use.
		self.dexterity = 0  # governs your ability to be stealthy, speedy, and overall flexible to overcome obsticles you would othersie not be able to overcome.
		self.defense = 0    # distates how much damage you can mitigate. and what armors you may or may not be able to use.
		self.attack = 0     # how much base damage you will deal when unarmed. strength adds onto this.
		self.resistance = 0  # how much risistance you have against status ailments.
		self.evade = 0       # chance of dodging an attack. speed adds to this.
		self.crit = 0        # chance to hit twice as hard from your attack + strength.
		# exploration stats VVVVV
		self.sanity = 0    # for every point of sanity lost, you gain a mental problem. mostly illusions and inability to cope with people.
		self.perception = 0  # higher the better, lets you spot things around you would normally miss, and increases chance of random discoveries.
		self.luck = 0        # increases drop rate of better quality items in battle, and also random discoveries of objects laying around.
		self.stamina = 0    # your energy to complete a task, fight, travel, most everything takes stamina. regens fairly fast, but when very tired, sleep and it will replenish to full.
		# social stats VVVVV
		self.merchantile = 0  #ability to gamble, and haggle. the higher, the better chance at succeeding.
		self.charisma = 0    # increases chance of people liking you more, and can affect haggling.
		# equipment VVVVV
		self.left_hand = None
		self.left_finger_1 = None
		self.left_finger_2 = None
		self.left_finger_3 = None
		self.left_finger_4 = None
		self.left_finger_5 = None
		self.right_hand = None
		self.right_finger_1 = None
		self.right_finger_2 = None
		self.right_finger_3 = None
		self.right_finger_4 = None
		self.right_finger_5 = None
		self.left_wrist = None
		self.right_wrist = None
		self.head = None
		self.lip = None
		self.tongue = None
		self.nose = None
		self.ears = None
		self.neck = None
		self.torso = None
		self.legs = None
		self.feet = None
		self.left_toe_1 = None
		self.left_toe_2 = None
		self.left_toe_3 = None
		self.left_toe_4 = None
		self.right_toe_1 = None
		self.right_toe_2 = None
		self.right_toe_3 = None
		self.right_toe_4 = None
		self.tail = None
		self.back = None
		# visits VVVVV
		self.woods = 0
		self.plains = 0
		self.fields = 0
		self.hills = 0
		self.mountains = 0
		self.peaks = 0
		self.volcano = 0
		self.dark_woods = 0
		self.sea = 0
		self.depths = 0
		self.Hadistrom = 0
		self.Verona = 0
		self.Gorbin = 0
		self.Hiorin = 0
		self.Binkertink = 0
		self.lake = 0
		self.sky = 0
		self.underground = 0
		self.Cave = 0
		self.hills_hut = 0
		self.river = 0
		self.cave_main_hall = 0
		self.cave_your_bedroom = 0
		self.cave_girls_bedroom = 0
		self.cave_dining_hall = 0
		self.cave_treasury = 0
		self.cave_bathing_room = 0
		self.cave_medical_room = 0
		self.binkertink_docks = 0
		self.binkertink_port = 0
		self.binkertink_house = 0
		self.binkertink_inn = 0
		self.binkertink_jeweler = 0
		self.binkertink_arena = 0
		self.binkertink_streets = 0
		self.binkertink_front_gate = 0
		self.hadistrom_front_gate = 0
		self.hiorin_blacksmith = 0
		self.hiorin_house = 0
		self.hiorin_tower = 0
		self.hiorin_library = 0
		self.hiorin_alchemist = 0
		self.hiorin_inn = 0
		self.hiorin_bank = 0
		self.hiorin_castle = 0
		self.hiorin_other_dimension = 0
		self.hiorin_streets = 0
		self.hiorin_front_gates = 0
		self.gorbin_tavern = 0
		self.gorbin_streets = 0
		self.verona_tailor = 0
		self.verona_house = 0
		self.verona_bar = 0
		self.verona_streets = 0		

		self.learnable_spells = [fire[fire_ball, meteor, fire_pillar, engulf], water[water_whip, flood, tsunami, whirlpool], ice[icicle, freeze, hailstorm, crystalize], air[burst, tornado, wind_scythe, pressure_wave], earth[boulder_crush, sinkhole, earthquake, liquify_ground], electric[shock, bolt, lightning_storm, disrupting_blast], gravity[lift, compress, crush, shift], time[slow, forward, halt, rewind]]
		self.high_path_spells = []



	AffinityStats = {
	"knight":(30,30,30,30,5,5), #likes sword and board. balanced def and att
	"thief":(), # likes to steal, hide, and assassinate. good with knives.
	"healer":(), # likes to stay alive, hp regens faster, can cast healing spells, and buffs to defend self or party memebers.
	"mage":(), # likes magic, uses spells more often in combat, high magic power.
	"archer":(), # likes ranged attacks. good with bows and guns.
	"fighter":(), # likes barehanded fighting. best with gloves and close ranged weapons.
	"summoner":(), # calls on others to aid in the fight. summons cost life points and require a special item to summon someone.
	"rider":(), #does battle while riding a mount. best with spears.
	"tamer":(), #relies on wild creatures to aid in battle, can make enemies cross over to your side for a little while. only works with beasts, not people.
	"paladin":(), # high path of the knight. higher defense. can cast healing magic and best against undead.
	"shadow_lord":(), #high path of kinght. higher attack. can cast dark margic, and best against followers of the light.
	"ninja":(), # high path of the thief. higher speed, evasion and perception. best for assassinations.
	"pirate":(), # high path of the thief, higher attack in melee and ranged. merchantile + 10, allowing to haggle for bargains.
	"priest":(), # high path of the healer. casts spells of protections, best for support.
	"druid":(), # high path of the healer. cast natural based magics, best for attack with little support.
	"archmage":(), # high path of the mage. casts only spells, best for attack. higher mp.
	"battlemage":(), # high path of the mage. casts blood magic, uses hp for great damage. higher mp, but hp regen is low.
	"hunter":(), # high path of archer, can track nearby enemies and avoid suprise attacks.
	"sniper":(), # high path of the archer, best with guns. can attack with precision, good for support.
	"brawler":(), #high path of the fighter. higher strength and speed.
	"martial_artist":(), # high path of the fighter, higher speed, strength and evasion. best for light armor users.
	"angel_caller":(), # high path of the summoner. higher hp, can heal party, and deal heavy damage to followers of the darkness.
	"demon_caller":(), # high path of the summoner. higher hp, and attack. deal great damage against followers of the light.
	"jouster":(), #high path of the rider. best with javelin and spear. higher attack and speed.
	"dragoon":(), # high path of the rider, higher attack, speed, and can ride dragons, uses longswords and crossbows rather than polearms.
	"beast_whisperer":(), # high path of the tamer, can avoid beast battles and tame the beasts to aid you even outside battle as your pet. can only keep 1 creature as pet at any given time.
	"beast_master":()} # forces creature to submit to your will during battle. basically evil tamer.
	#statDiff = BaseStats.AffinityStats["knight"]
	#self.hp += statDiff[0]
	#self.strength += statDiff[1]
	#self.defense += statDiff[2]
	#self.attack += statDiff[3]
	#self.resistance += statDiff[4]
	#self.crit += statDiff[5]

	def checkAffinity(self, affinity):
		return False

	def checkAffinities(self):
		for x in self.affinities.keys:
			if(self.checkAffinity(x)):
				break

class Player(BaseStats):
	def __init__(self):
		BaseStats.__init__(self)
		self.name = "Rex"
		self.current_path = "adventurer"
		self.hp = 50
		self.mp = 10
		self.strength = 2   # modifier to add onto attack damage, also dictates what weapons you may or may not weild. and objects you can or cannot carry
		self.speed = 2      # how fast you can travel, and a modifier for evasion. 
		self.intillect = 2  # modifier to add magic points, and dictates what spells you may or may not learn and or use.
		self.dexterity = 2  # governs your ability to be stealthy, speedy, and overall flexible to overcome obsticles you would othersie not be able to overcome.
		self.defense = 2    # distates how much damage you can mitigate. and what armors you may or may not be able to use.
		self.attack = 2     # how much base damage you will deal when unarmed. strength adds onto this.
		self.resistance = 0  # how much risistance you have against status ailments.
		self.evade = 10       # chance of dodging an attack. speed adds to this.
		self.crit = 5        # chance to hit twice as hard from your attack + strength.
		self.sanity = 100    # for every point of sanity lost, you gain a mental problem. mostly illusions and inability to cope with people.
		self.perception = 20  # higher the better, lets you spot things around you would normally miss, and increases chance of random discoveries.
		self.luck = 5        # increases drop rate of better quality items in battle, and also random discoveries of objects laying around.
		self.stamina = 100    # your energy to complete a task, fight, travel, most everything takes stamina. regens fairly fast, but when very tired, sleep and it will replenish to full.
		self.merchantile = 20  #ability to gamble, and haggle. the higher, the better chance at succeeding.
		self.charisma = 20    # increases chance of people liking you more, and can affect haggling.
		self.reputation["Larck"] = 0
		self.reputation["Irene"] = 0
		self.reputation["Silvia"] = 0
		self.reputation["Bonny"] = 0
		self.reputation["Evana"] = 0
		self.reputation["Stella"] = 0
		self.reputation["Jenny"] = 0
		self.reputation["Lilly"] = 0
		self.reputation["Shawn"] = 0
		self.reputation["Zeru"] = 0
		self.reputation["Travis"] = 0
		self.reputation["Michelle"] = 0
		self.reputation["Devan"] = 0
		self.reputation["Valendras"] = 0
		self.reputation["Hengul"] = 0
		self.reputation["Dustin"] = 0
		self.reputation["Artemis"] = 0
		self.reputation["Sally"] = 0
		self.reputation["Mousegirl"] = 0
		self.reputation["Euna"] = 0