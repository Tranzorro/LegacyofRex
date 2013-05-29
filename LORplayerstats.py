#stats to use when making the stats class / functions / methods.

class player_stats():  #stats you have

	def __init__(self, name):

		pass


	def name(self):  #the name of the character you are

		self.name = "Rex"

	def description():  #the characters description after you look at yourself in a reflection.

		pass

	def level():  #your level

		level = 1

	def spells():  #spells you can obtain

		base_spells = [rock_toss, scorch, gust, water_ball]
		learnable_spells = [fire[fire_ball, meteor, fire_pillar, engulf], water[water_whip, flood, tsunami, whirlpool], ice[icicle, freeze, hailstorm, crystalize], air[burst, tornado, wind_scythe, pressure_wave], earth[boulder_crush, sinkhole, earthquake, liquify_ground], electric[shock, bolt, lightning_storm, disrupting_blast], gravity[lift, compress, crush, shift], time[slow, forward, halt, rewind]]
		high_path_spells = []

	def path():  #paths your character can achieve, 1 path only, and 1 highpath after that.

		print ("you are %d") % (current_path)

		current_path = path[adventurer]

		path = {adventurer:'an adventurer',
		knight:'a knight',
		thief:'a thief',
		healer:'a healer',
		mage:'a mage',
		archer:'an archer',
		fighter:'a fighter',
		summoner:'a summoner',
		rider:'a rider',
		tamer:'a tamer'}

		high_path = {paladin:'a paladin',
		shadow_lord:'a shadow_lord',
		ninja:'a ninja',
		pirate:'a pirate',
		priest:'a priest',
		druid:'a druid',
		archmage:'an archmage',
		battlemage:'a battlemage',
		hunter:'a hunter',
		sniper:'a sniper',
		brawler:'a brawler',
		martial_artist:'a marthial_artist',
		angel_caller:'an angel_caller',
		demon_caller:'a demon_caller',
		jouster:'a jouster',
		dragoon:'a dragoon',
		beast_whisperer:'a beast_whisperer',
		beast_master:'a beast_master'}

	def adventurer():    # basic *pathless* stats. every new game starts as this

		weapon_prof = [common, uncommon]
		armor_prof = [common, uncommon]
		spells = player_stats.spells(base_spells)

	def knight():    # likes the sword and board. high attack and defense.

		knight_affinity = []

		if knight_affinity <= 30:
			player_stats.path.current_path = knight

		hp = hp + 30
		strength = strength + 30
		defense = defense + 30
		attack = attack + 30
		resistance = resistance + 5
		crit = crit + 5

	def thief():    # likes to steal, hide, and assassinate. good with knives.

		thief_affinity = []

		if thief_affinity <= 30:
			player_stats.path.current_path = thief

	def healer():    # likes to stay alive, hp regens faster, can cast healing spells, and buffs to defend self or party memebers.

		healer_affinity = []

		if healer_affinity <= 30:
			player_stats.path.current_path = healer

	def mage():   # likes magic, uses spells more often in combat, high magic power.

		mage_affinity = []

		if mage_affinity <= 30:
			player_stats.path.current_path = mage

		spells = spells + player_stats.spells(learnable_spells)

	def archer():   # likes ranged attacks. good with bows and guns.

		archer_affinity = []

		if archer_affinity <= 30:
			player_stats.path.current_path = archer

	def fighter():    # likes barehanded fighting. best with gloves and close ranged weapons.

		fighter_affinity = []

		if fighter_affinity <= 30:
			player_stats.path.current_path = fighter

	def summoner():    # calls on others to aid in the fight. summons cost life points and require a special item to summon someone.

		summoner_affinity = []

		if summoner_affinity <= 30:
			player_stats.path.current_path = summoner

	def rider():   #does battle while riding a mount. best with spears.

		rider_affinity = []

		if rider_affinity <= 30:
			player_stats.path.current_path = rider

	def tamer():   #relies on wild creatures to aid in battle, can make enemies cross over to your side for a little while. only works with beasts, not people.

		tamer_affinity = []

		if tamer_affinity <= 30:
			player_stats.path.current_path = tamer

	def paladin():  # high path of the knight. higher defense. can cast healing magic and best against undead.

		paladin_affinity = []

		if paladin_affinity <= 100:
			player_stats.path.current_path = paladin

	def shadow_lord():   #high path of kinght. higher attack. can cast dark margic, and best against followers of the light.

		shadow_lord_affinity = []

		if shadow_lord_affinity <= 100:
			player_stats.path.current_path = shadow_lord

	def ninja():  # high path of the thief. higher speed, evasion and perception. best for assassinations.

		ninja_affinity = []

		if ninja_affinity <= 100:
			player_stats.path.current_path = ninja

	def pirate():   # high path of the thief, higher attack in melee and ranged. merchantile + 10, allowing to haggle for bargains.

		pirate_affintiy = []

		if pirate_affinity <= 100:
			player_stats.path.current_path = pirate

	def priest():   # high path of the healer. casts spells of protections, best for support.

		priest_affinity = []

		if priest_affinity <= 100:
			player_stats.path.current_path = priest

	def druid():   # high path of the healer. cast natural based magics, best for attack with little support.

		druid_affinity = []

		if druid_affinity <= 100:
			player_stats.path.current_path = druid

	def archmage():   # high path of the mage. casts only spells, best for attack. higher mp.

		archmage_affinity = []

		if archmage_affinity <= 100:
			player_stats.path.current_path = archmage

	def battlemage():  # high path of the mage. casts blood magic, uses hp for great damage. higher mp, but hp regen is low.

		battlemage_affinity = []

		if battlemage_affinity <= 100:
			player_stats.path.current_path = battlemage

	def hunter():   # high path of archer, can track nearby enemies and avoid suprise attacks.

		hunter_affinity = []

		if hunter_affinity <= 100:
			player_stats.path.current_path = hunter

	def sniper():   # high path of the archer, best with guns. can attack with precision, good for support.

		sniper_affinity = []

		if sniper_affinity <= 100:
			player_stats.path.current_path = sniper

	def brawler():   #high path of the fighter. higher strength and speed.

		brawler_affinity = []

		if brawler_affinity <= 100:
			player_stats.path.current_path = brawler

	def martial_artist():    # high path of the fighter, higher speed, strength and evasion. best for light armor users.

		martial_artist_affinity = []

		if martial_artist_affinity <= 100:
			player_stats.path.current_path = martial_artist

	def angel_caller():    # high path of the summoner. higher hp, can heal party, and deal heavy damage to followers of the darkness.

		angel_caller_affinity = []

		if angel_caller_affinity <= 100:
			player_stats.path.current_path = angel_caller

	def demon_caller():   # high path of the summoner. higher hp, and attack. deal great damage against followers of the light.

		demon_caller_affinity = []

		if demon_caller_affinity <= 100:
			player_stats.path.current_path = demon_caller

	def jouster():   #high path of the rider. best with javelin and spear. higher attack and speed.

		jouster_affinity = []

		if jouster_affinity <= 100:
			player_stats.path.current_path = jouster

	def dragoon():   # high path of the rider, higher attack, speed, and can ride dragons, uses longswords and crossbows rather than polearms.

		dragoon_affinity = []

		if dragoon_affinity <= 100:
			player_stats.path.current_path = dragoon

	def beast_whisperer():  # high path of the tamer, can avoid beast battles and tame the beasts to aid you even outside battle as your pet. can only keep 1 creature as pet at any given time.

		beast_whisperer_affinity = []

		if beast_whisperer_affinity <= 100:
			player_stats.path.current_path = beast_whisperer

	def beast_master():  # forces creature to submit to your will during battle. basically evil tamer.

		beast_master_affinity = []

		if beast_master_affinity <= 100:
			player_stats.path.current_path = beast_master

	def equipped():   #stuff you are wearing currently on what slots.

		left_hand = []
		left_finger_1 = []
		left_finger_2 = []
		left_finger_3 = []
		left_finger_4 = []
		left_finger_5 = []
		right_hand = []
		right_finger_1 = []
		right_finger_2 = []
		right_finger_3 = []
		right_finger_4 = []
		right_finger_5 = []
		left_wrist = []
		right_wrist = []
		head = []
		lip = []
		tongue = []
		nose = []
		ears = []
		neck = []
		torso = []
		legs = []
		feet = []
		left_toe_1 = []
		left_toe_2 = []
		left_toe_3 = []
		left_toe_4 = []
		right_toe_1 = []
		right_toe_2 = []
		right_toe_3 = []
		right_toe_4 = []
		tail = []
		back = []

	def inventory(): #stuff in your inventory currently

		inventory = []

	def currency():  # money you currently have

		money = [0]

	def combat():   #battle stats

		hp = 10      # health points
		mp = 10      # magic points
		strength = 1   # modifier to add onot attack damage, also dictates what weapons you may or may not weild. and objects you can or cannot carry
		speed = 1      # how fast you can travel, and a modifier for evasion. 
		intillect = 1  # modifier to add magic points, and dictates what spells you may or may not learn and or use.
		dexterity = 1  # governs your ability to be stealthy, speedy, and overall flexible to overcome obsticles you would othersie not be able to overcome.
		defense = 1    # distates how much damage you can mitigate. and what armors you may or may not be able to use.
		attack = 2     # how much base damage you will deal when unarmed. strength adds onto this.
		resistance = 0  # how much risistance you have against status ailments.
		evade = 2       # chance of dodging an attack. speed adds to this.
		crit = 1        # chance to hit twice as hard from your attack + strength.

	def interaction():  #stats that affect your abilities during exploration and interaction

		sanity = 100    # for every point of sanity lost, you gain a mental problem. mostly illusions and inability to cope with people.
		perception = 1  # higher the better, lets you spot things around you would normally miss, and increases chance of random discoveries.
		luck = 1        # increases drop rate of better quality items in battle, and also random discoveries of objects laying around.
		stamina = 10    # your energy to complete a task, fight, travel, most everything takes stamina. regens fairly fast, but when very tired, sleep and it will replenish to full.

	def social():   #stats that affect your social outcomes.

		merchantile = 1  #ability to gamble, and haggle. the higher, the better chance at succeeding.
		charisma = 30    # increases chance of people liking you more, and can affect haggling.

	def reputation():  #stats that will affect who will be nice or kill you

		Larck = []
		Irene = []
		Silvia = []
		Bonny = []
		Evana = []
		Stella = []
		Jenny = []
		Lilly = []
		Shawn = []
		Zeru = []
		Travis = []
		Michelle = []
		Devan = []
		Valendras = []
		Hengul = []
		Dustin = []
		Artemis = []
		Sally = []
		Mousegirl = []
		Euna = []

	def location():    # stat that changes depending on where you are and where you were.

		location = []   #where you are now
		previous = []   # where you were before now

	def visits():    # stats that affect what unlocks events after certain amounts of visits to certain places has been reached.

		woods = []
		plains = []
		fields = []
		hills = []
		mountains = []
		peaks = []
		volcano = []
		dark_woods = []
		sea = []
		depths = []
		Hadistrom = []
		Verona = []
		Gorbin = []
		Hiorin = []
		Binkertink = []
		lake = []
		sky = []
		underground = []
		Cave = []
		hills_hut = []
		river = []
		cave_main_hall = []
		cave_your_bedroom = []
		cave_girls_bedroom = []
		cave_dining_hall = []
		cave_treasury = []
		cave_bathing_room = []
		cave_medical_room = []
		binkertink_docks = []
		binkertink_port = []
		binkertink_house = []
		binkertink_inn = []
		binkertink_jeweler = []
		binkertink_arena = []
		binkertink_streets = []
		binkertink_front_gate = []
		hadistrom_front_gate = []
		hiorin_blacksmith = []
		hiorin_house = []
		hiorin_tower = []
		hiorin_library = []
		hiorin_alchemist = []
		hiorin_inn = []
		hiorin_bank = []
		hiorin_castle = []
		hiorin_other_dimension = []
		hiorin_streets = []
		hiorin_front_gates = []
		gorbin_tavern = []
		gorbin_streets = []
		verona_tailor = []
		verona_house = []
		verona_bar = []
		verona_streets = []