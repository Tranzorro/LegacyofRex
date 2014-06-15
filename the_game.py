# imports go here for global values that the game can use at any time, anywhere in all code blocks.
import pygame, os
from math import exp, log
from eztext import *
import Characters
#start the pygame engine here:
pygame.init()
clock = pygame.time.Clock()  # controls how fast the screen updates at max. Only global var for use of pygame.
#this space is used for all global functions and variables to be used within all other code blocks, such as print_slow.
# DO NOT USE GLOBAL VARIABLES!!! MAKE A FUNTION OR CLASS FOR THEM! how? figure that out.
class Game(): #contains all the necessary things to make the game run, mainly just exists to remove any and all global vars.
	size = (800,750)  # width and hight of the window.
	screen = pygame.display.set_mode(size) # creates the screen i think.
	pygame.display.set_caption("The Legacy of Rex") # this dictates what the window box will show for the program name.
	font = pygame.font.Font (None, 25) # this tells the game what font type and size to use.
	stat_font = pygame.font.Font (None, 25) # same as above.
	logo_font = pygame.font.Font ("C:/Windows/Fonts/impact.ttf", 80) # same as above.
	map_font = pygame.font.Font ("C:/Windows/Fonts/impact.ttf", 25) # same as above.
	black = (0,0,0)  # creates a variable color, used for altering the screen color, or text color.
	white = (255,255,255) # same as above.
	red = (255,0,0) # same as above.
	green = (0,255,0) # same as above.
	blue = (0,0,255) # same as above.
	txtbx = T_input(x=10, y=730, font=stat_font, maxlength=90, color=(white), prompt='>: ') # this is used for the eztext module.
	Player1 = Characters.Player()  # creates the character player1 which is the user at all times!
	Player1.name = "Lord of awesomness"  # player1's name after creation. must be below the line in which player1 was created to work!
	Player1.playerpos = "first"  # player 1's character stat window position for use in party placement. player 1 will always be first!
	Player2 = Characters.Jenny() # same as player 1, just a new variable for the second.
	Player2.playerpos = "second" # same as player 1, just a new variable for the second. 
	Player3 = Characters.Evana() # same as player 1, just a new variable for the third.
	Player3.playerpos = "third" # same as player 1, just a new variable for the third.
	Player4 = Characters.Bonny() # same as player 1, just a new variable for the fourth.
	Player4.playerpos = "fourth" # same as player 1, just a new variable for the fourth.

	def render_stats(): # contains all the character stat window info. including the actual window lines n stuff.
		if Game.Player1.playerpos or Game.Player2.playerpos or Game.Player3.playerpos or Game.Player4.playerpos == "first":
			char_Name = Game.stat_font.render("Name: {}" .format(Game.Player1.name), True, Game.white) # limit all names by 18 characters
			char_Health = Game.stat_font.render("HP: {}" .format(Game.Player1.hp), True, Game.white)
			char_Defence = Game.stat_font.render("Def: {}" .format(Game.Player1.defence), True, Game.white)
			char_Attack = Game.stat_font.render("Atk: {}" .format(Game.Player1.attack), True, Game.white)
			char_Magic = Game.stat_font.render("MP: {}" .format(Game.Player1.mp), True, Game.white)
			char_Sanity = Game.stat_font.render("San: {}" .format(Game.Player1.sanity), True, Game.white)
			char_Stamina = Game.stat_font.render("Sta: {}" .format(Game.Player1.stamina), True, Game.white)
			char_Status1 = Game.stat_font.render("Status: {}" .format(Game.Player1.statusailment1), True, Game.white) # tox, bur, cur, pet, slw
			char_Status2 = Game.stat_font.render("{}" .format(Game.Player1.statusailment2), True, Game.white) # ice, bli, zom, par, sho, ins
			char_Path = Game.stat_font.render("Path: {}" .format(Game.Player1.path), True, Game.white)
			char_Head = Game.stat_font.render("Head: {}" .format(Game.Player1.equipment["Head"]), True, Game.white) # limit item names for this slot to 22 characters
			char_Chest = Game.stat_font.render("Chest: {}" .format(Game.Player1.equipment["Chest"]), True, Game.white) # limit names to 22
			char_Legs = Game.stat_font.render("Legs: {}" .format(Game.Player1.equipment["Legs"]), True, Game.white) # limit names to 23
			char_Feet = Game.stat_font.render("Feet: {}" .format(Game.Player1.equipment["Feet"]), True, Game.white) # limit names to 23
			char_LeftHand = Game.stat_font.render("LHand: {}" .format(Game.Player1.equipment["LHand"]), True, Game.white) # limit names to 23
			char_RightHand = Game.stat_font.render("RHand: {}" .format(Game.Player1.equipment["RHand"]), True, Game.white) # limit names to 23
			Game.screen.blit(char_Name, [15, 15]) # x, y
			Game.screen.blit(char_Health, [15, 30]) # x, y
			Game.screen.blit(char_Defence, [100, 30]) # x, y
			Game.screen.blit(char_Attack, [185, 30])
			Game.screen.blit(char_Magic, [15, 45]) # x, y
			Game.screen.blit(char_Sanity, [100, 45]) # x, y
			Game.screen.blit(char_Stamina, [185, 45])
			Game.screen.blit(char_Status1, [15, 60]) # x, y
			Game.screen.blit(char_Status2, [15, 75]) # x, y
			Game.screen.blit(char_Path, [15, 90]) # x, y
			Game.screen.blit(char_Head, [15, 105]) # x, y
			Game.screen.blit(char_Chest, [15, 120]) # x, y
			Game.screen.blit(char_Legs, [15, 135]) # x, y
			Game.screen.blit(char_Feet, [15, 150]) # x, y
			Game.screen.blit(char_LeftHand, [15, 165]) # x, y
			Game.screen.blit(char_RightHand, [15, 180]) # x, y
		if Game.Player1.playerpos or Game.Player2.playerpos or Game.Player3.playerpos or Game.Player4.playerpos == "second":
			character_stats2 = Game.stat_font.render("Name: {}" .format(Game.Player2.name), True, Game.white)
			character_stats2_a = Game.stat_font.render("HP: {}" .format(Game.Player2.hp), True, Game.white)
			character_stats2_a_a = Game.stat_font.render("Def: {}" .format(Game.Player2.defence), True, Game.white)
			character_stats2_a_b = Game.stat_font.render("Atk: {}" .format(Game.Player2.attack), True, Game.white)
			character_stats2_b = Game.stat_font.render("MP: {}" .format(Game.Player2.mp), True, Game.white)
			character_stats2_b_a = Game.stat_font.render("San: {}" .format(Game.Player2.sanity), True, Game.white)
			character_stats2_b_b = Game.stat_font.render("Sta: {}" .format(Game.Player2.stamina), True, Game.white)
			character_stats2_c = Game.stat_font.render("Status: {}".format(Game.Player2.statusailment1), True, Game.white)
			character_stats2_c_a = Game.stat_font.render("{}" .format(Game.Player2.statusailment2), True, Game.white)
			character_stats2_E = Game.stat_font.render("Path: {}" .format(Game.Player2.path), True, Game.white)
			character_stats2_E_a = Game.stat_font.render("Head: {}" .format(Game.Player2.equipment["Head"]), True, Game.white)
			character_stats2_E_b = Game.stat_font.render("Chest: {}" .format(Game.Player2.equipment["Chest"]), True, Game.white)
			character_stats2_E_c = Game.stat_font.render("Legs: {}" .format(Game.Player2.equipment["Legs"]), True, Game.white)
			character_stats2_E_d = Game.stat_font.render("Feet: {}" .format(Game.Player2.equipment["Feet"]), True, Game.white)
			character_stats2_E_e = Game.stat_font.render("LHand: {}" .format(Game.Player2.equipment["LHand"]), True, Game.white)
			character_stats2_E_f = Game.stat_font.render("RHand: {}" .format(Game.Player2.equipment["RHand"]), True, Game.white)
			Game.screen.blit(character_stats2, [274, 15])
			Game.screen.blit(character_stats2_a, [274, 30]) # x, y
			Game.screen.blit(character_stats2_a_a, [359, 30])
			Game.screen.blit(character_stats2_a_b, [444, 30])
			Game.screen.blit(character_stats2_b, [274, 45]) # x, y
			Game.screen.blit(character_stats2_b_a, [359, 45])
			Game.screen.blit(character_stats2_b_b, [444, 45])
			Game.screen.blit(character_stats2_c, [274, 60]) # x, y
			Game.screen.blit(character_stats2_c_a, [274, 75]) # x, y
			Game.screen.blit(character_stats2_E, [274, 90]) # x, y
			Game.screen.blit(character_stats2_E_a, [274, 105]) # x, y
			Game.screen.blit(character_stats2_E_b, [274, 120]) # x, y
			Game.screen.blit(character_stats2_E_c, [274, 135]) # x, y
			Game.screen.blit(character_stats2_E_d, [274, 150]) # x, y
			Game.screen.blit(character_stats2_E_e, [274, 165]) # x, y
			Game.screen.blit(character_stats2_E_f, [274, 180]) # x, y
		if Game.Player1.playerpos or Game.Player2.playerpos or Game.Player3.playerpos or Game.Player4.playerpos == "third":
			character_stats3 = Game.stat_font.render("Name: {}" .format(Game.Player3.name) , True, Game.white)
			character_stats3_a = Game.stat_font.render("HP: {}" .format(Game.Player3.hp), True, Game.white)
			character_stats3_a_a = Game.stat_font.render("Def: {}" .format(Game.Player3.defence), True, Game.white)
			character_stats3_a_b = Game.stat_font.render("Atk: {}" .format(Game.Player3.attack), True, Game.white)
			character_stats3_b = Game.stat_font.render("MP: {}" .format(Game.Player3.mp), True, Game.white)
			character_stats3_b_a = Game.stat_font.render("San: {}" .format(Game.Player3.sanity), True, Game.white)
			character_stats3_b_b = Game.stat_font.render("Sta: {}" .format(Game.Player3.stamina), True, Game.white)
			character_stats3_c = Game.stat_font.render("Status: {}" .format(Game.Player3.statusailment1), True, Game.white)
			character_stats3_c_a = Game.stat_font.render("{}" .format(Game.Player3.statusailment2), True, Game.white)
			character_stats3_E = Game.stat_font.render("Path: {}" .format(Game.Player3.path), True, Game.white)
			character_stats3_E_a = Game.stat_font.render("Head: {}" .format(Game.Player3.equipment["Head"]), True, Game.white)
			character_stats3_E_b = Game.stat_font.render("Chest: {}" .format(Game.Player3.equipment["Chest"]), True, Game.white)
			character_stats3_E_c = Game.stat_font.render("Legs: {}" .format(Game.Player3.equipment["Legs"]), True, Game.white)
			character_stats3_E_d = Game.stat_font.render("Feet: {}" .format(Game.Player3.equipment["Feet"]), True, Game.white)
			character_stats3_E_e = Game.stat_font.render("LHand: {}" .format(Game.Player3.equipment["LHand"]), True, Game.white)
			character_stats3_E_f = Game.stat_font.render("RHand: {}" .format(Game.Player3.equipment["RHand"]), True, Game.white)
			Game.screen.blit(character_stats3, [15, 224])
			Game.screen.blit(character_stats3_a, [15, 239]) # x, y
			Game.screen.blit(character_stats3_a_a, [100, 239])
			Game.screen.blit(character_stats3_a_b, [185, 239])
			Game.screen.blit(character_stats3_b, [15, 254]) # x, y
			Game.screen.blit(character_stats3_b_a , [100, 254]) # x, y
			Game.screen.blit(character_stats3_b_b, [185, 254])
			Game.screen.blit(character_stats3_c, [15, 269]) # x, y
			Game.screen.blit(character_stats3_c_a, [15, 284]) # x, y
			Game.screen.blit(character_stats3_E, [15, 299]) # x, y
			Game.screen.blit(character_stats3_E_a, [15, 314]) # x, y
			Game.screen.blit(character_stats3_E_b, [15, 329]) # x, y
			Game.screen.blit(character_stats3_E_c, [15, 344]) # x, y
			Game.screen.blit(character_stats3_E_d, [15, 359]) # x, y
			Game.screen.blit(character_stats3_E_e, [15, 374]) # x, y
			Game.screen.blit(character_stats3_E_f, [15, 389]) # x, y
		if Game.Player1.playerpos or Game.Player2.playerpos or Game.Player3.playerpos or Game.Player4.playerpos == "fourth":
			character_stats4 = Game.stat_font.render("Name: {}" .format(Game.Player4.name), True, Game.white)
			character_stats4_a = Game.stat_font.render("HP: {}" .format(Game.Player4.hp), True, Game.white)
			character_stats4_a_a = Game.stat_font.render("Def: {}" .format(Game.Player4.defence), True, Game.white)
			character_stats4_a_b = Game.stat_font.render("Atk: {}" .format(Game.Player4.attack), True, Game.white)
			character_stats4_b = Game.stat_font.render("MP: {}" .format(Game.Player4.mp), True, Game.white)
			character_stats4_b_a = Game.stat_font.render("San: {}" .format(Game.Player4.sanity), True, Game.white)
			character_stats4_b_b = Game.stat_font.render("Sta: {}" .format(Game.Player4.stamina), True, Game.white)
			character_stats4_c = Game.stat_font.render("Status: {}" .format(Game.Player4.statusailment1), True, Game.white)
			character_stats4_c_a = Game.stat_font.render("{}" .format(Game.Player4.statusailment2), True, Game.white)
			character_stats4_E = Game.stat_font.render("Path: {}" .format(Game.Player4.path), True, Game.white)
			character_stats4_E_a = Game.stat_font.render("Head: {}" .format(Game.Player4.equipment["Head"]), True, Game.white)
			character_stats4_E_b = Game.stat_font.render("Chest: {}" .format(Game.Player4.equipment["Chest"]), True, Game.white)
			character_stats4_E_c = Game.stat_font.render("Legs: {}" .format(Game.Player4.equipment["Legs"]), True, Game.white)
			character_stats4_E_d = Game.stat_font.render("Feet: {}" .format(Game.Player4.equipment["Feet"]), True, Game.white)
			character_stats4_E_e = Game.stat_font.render("LHand: {}" .format(Game.Player4.equipment["LHand"]), True, Game.white)
			character_stats4_E_f = Game.stat_font.render("RHand: {}" .format(Game.Player4.equipment["RHand"]), True, Game.white)
			Game.screen.blit(character_stats4, [274, 224])
			Game.screen.blit(character_stats4_a, [274, 239]) # x, y
			Game.screen.blit(character_stats4_a_a, [359, 239])
			Game.screen.blit(character_stats4_a_b, [444, 239])
			Game.screen.blit(character_stats4_b, [274, 254]) # x, y
			Game.screen.blit(character_stats4_b_a, [359, 254])
			Game.screen.blit(character_stats4_b_b, [444, 254])
			Game.screen.blit(character_stats4_c, [274, 269]) # x, y
			Game.screen.blit(character_stats4_c_a, [274, 284]) # x, y
			Game.screen.blit(character_stats4_E, [274, 299]) # x, y
			Game.screen.blit(character_stats4_E_a, [274, 314]) # x, y
			Game.screen.blit(character_stats4_E_b, [274, 329]) # x, y
			Game.screen.blit(character_stats4_E_c, [274, 344]) # x, y
			Game.screen.blit(character_stats4_E_d, [274, 359]) # x, y
			Game.screen.blit(character_stats4_E_e, [274, 374]) # x, y
			Game.screen.blit(character_stats4_E_f, [274, 389]) # x, y
		# stat window 1
		pygame.draw.rect(Game.screen, Game.white, [5, 5, 260, 200], 2) # this will be the character stats window rectangle. this will hole 4 character stat slots.
		# stat window 2
		pygame.draw.rect(Game.screen, Game.white, [264, 5, 260, 200], 2) # 2nd spot character window
		# stat window 3
		pygame.draw.rect(Game.screen, Game.white, [5, 214, 260, 200], 2) # 3rd spot character window
		# stat window 4
		pygame.draw.rect(Game.screen, Game.white, [264, 214, 260, 200], 2) # 4th spot character window

	def render_map(): # contains the rendering of the map window, and the game logo name thing.
		logo = Game.logo_font.render("LEGACY", True, Game.white)
		logo_1 = Game.logo_font.render("OF", True, Game.white)
		logo_2 = Game.logo_font.render("REX", True, Game.white)
		Game.screen.blit(logo,[550, -10])
		Game.screen.blit(logo_1,[620,60])
		Game.screen.blit(logo_2,[600, 130])
		pygame.draw.rect(Game.screen, Game.white, [534, 214, 260, 200], 2)
		map_text = Game.map_font.render ("No map installed yet.", True, Game.white)
		map_text1 = Game.map_font.render ("Sorry!", True, Game.white)
		Game.screen.blit(map_text,[540, 218])
		Game.screen.blit (map_text1,[540, 240])

	def render_info(): # contains the large info window on bottom of screen, which is supposed to scroll when it exceeds the visual text limit.
		tbx = pygame.sprite.RenderPlain(textBox())
		tbx.draw(Game.screen)
		pygame.draw.rect(Game.screen, Game.white,  [5, 424, 790, 300], 2 )  # this is the rectangle at [x, y, width, hight] locations. the last digit is the thickness of the lines
		#game_text = font.render("if you see this, you are doing it wrong! this needs to be a scrolling test window!", True, white)
		#screen.blit(game_text, [15, 427]) # this will show the text above as indicated.

	def print_slow(): # a function intended to let the in game text have a speed in which it reveals itself, instead of being instantaneous.
		for letter in str:
			sys.stdout.write(letter)
			sys.stdout.flush()
			time.sleep(0.01) 

	def Time_of_day(): # this dictates how time passes in the game, and allows for special events to occur if the time is right!
		Time = ["Morning", "Afternoon", "Evening", "Night"] # this list holds the different times of day/night
		# insert code to make a working clock that changes the time of day in the game, in both millitary and standard time.

class textBox(pygame.sprite.Sprite):  # I don't understand how most of this works, all I know is that I got it working... a little.
	#A textbox to see what we are doing in the game
	locationText = (10, 426) # start location of the large game info text.
	alpha1 = 1000 # sets the alpha for the large info screen window background / text.
	alpha2 = 1000 # same as above.
	def __init__(self, position = locationText,                        ##locationText is a variable holding the default location of the text
			size = [790, 300], alpha = alpha2,                ##alpha2 is normally 150
			color = (255,255,255), scrollPosition = 0,
			textSize = 25):
		pygame.sprite.Sprite.__init__(self)
		self.locationText = locationText, locationText = (10,426) # start location of the large game info text.
		#self.alpha1 = alpha1 # sets the alpha for the large info screen window background / text.
		#self.alpha2 = alpha2 # same as above.
		self.position = position
		self.size = size
		self.textSize = textSize
		self.alpha = alpha
		self.scrollColor = color
		self.interSpace = 1
		self.ScrollY = 0
		self.sensitiveSpace = 1
		self.maxLines = int(self.size[1] / (self.textSize + 4)) - 1
		self.font = pygame.font.Font (None, 25) #pygame.font.SysFont("Times New Roman", self.textSize, True)        ##The font used to draw the text in the textbox
		self.scrollPosition = pygame.rect.Rect(self.size[0] - 10, self.ScrollY, 10, 20)
		self.text = "This text will only show because I'm hardcoded into the box... Figure out a way to make me a variable that can be replaced with a new value! Also, this is a bigass line of text in the code, but this should be sparsed rather neatly on screen automagically! If not, then something is wrong. See if you can scroll with this shit! If not, you may have blocked a part of the code that makes that work! Otherwise, you will need to do some critical thinking and hope to your brain that you can figure this shit out! I should be relatively close to scrolling length by now right? Maybe? Perhaps now? No? Well then I'll have to keep pounding out some random jibberish and hope I reach the length needed to actually scroll! Why so many exlamation points? Am I yelling, or just emphasizing something? What am I asking you for, I'm just a bunch of words in the code, don't answer me. Dumbass. I'm still not long enough to scroll yet... Think I need some new material. Mary had a little lamb, the doctor fainted. Haha! Get it? Cuz' Mary had a.. well you should get it... If you aren't a total idiot."
		self.set_text(self.text)
		self.update(pygame.mouse.get_pos())

	def __createText__(self):
		self.rect = pygame.rect.Rect(self.position, self.size)
		self.image = pygame.surface.Surface(self.size)
		self.image.fill(pygame.color.Color(0,0,0))
		self.image.set_alpha(self.alpha)
		pygame.draw.rect(self.image, self.scrollColor, pygame.rect.Rect(self.scrollPosition), 0)
		pos = int(self.ScrollY / self.interSpace)
		for lineNumber in range(len(self.text)):
			if lineNumber < (self.maxLines * (pos + 1)) + 1 and lineNumber >= self.maxLines * pos:
				self.image.blit(self.font.render(self.text[lineNumber], True, (255, 255, 255)),
					pygame.rect.Rect((0, ((lineNumber - (self.maxLines * pos))*(self.textSize + 5)) + 5),(770, 11)))              

	def set_text(self, text):
		if text != "" or text != []:
			self.text = text.split("\n")
			wasSplit = False
			while (wasSplit == False):
				for line in range(len(self.text)):
					teImg = self.font.render(self.text[line], True, (255, 255, 255))
					if teImg.get_width() > self.size[0] - 10:
						isOfSize = False
						i = 0
						while(isOfSize == False):
							temImg = self.font.render(self.text[line][:len(self.text[line]) - i], True, (255, 255, 255))
							if temImg.get_width() <= self.size[0] - 10 and self.text[line][len(self.text[line]) - i] == " ":
								self.text.insert(line + 1, self.text[line][len(self.text[line]) - i:])
								self.text[line] = self.text[line][:len(self.text[line]) - i]
								isOfSize = True
								break
							i += 1
				wasSplit = True
				for line in range(len(self.text)):
					temImg = self.font.render(self.text[line], True, (0, 0, 0))
					if temImg.get_width() > self.size[0] - 10:
						wasSplit = False
						break
			self.set_position(0)
			self.__createText__()

	def set_position(self, newPosition):
		self.ScrollY = newPosition
		self.scrollPosition = pygame.rect.Rect(self.size[0] - 10, self.ScrollY, 10, 20)

	"""def update(self, mouseXY):            ##The update occurs every time the mouse is down on the textbox, and the arguments are the mouse's coordenates
		pygame.sprite.Sprite.update(self)
		if len(self.text) != 0 and self.rect.collidepoint(mouseXY) == True:
			mouseY = mouseXY[1] - self.locationText[1]
			if mouseY < 0: mouseY = 0
			numSteps = (len(self.text) / self.maxLines)
			if numSteps == 0:
				self.interSpace = 1
				self.sensitiveSpace = 1
				self.set_position(0)
				self.__createText__()
			else:
				self.interSpace = 20 + ((self.size[1] - ((numSteps + 1) * 20))/(numSteps))
				self.sensitiveSpace = self.size[1]/numSteps
				for step in range(numSteps):
					if step == 0:
						newPos = int(self.sensitiveSpace/2)
						self.set_position(0)
					else:
						newPos = int((self.sensitiveSpace * (step))+self.sensitiveSpace/2)
					if mouseY >= newPos:
						self.set_position(step*self.interSpace)
				if mouseY >= int((self.sensitiveSpace * (numSteps-1))+self.sensitiveSpace/2):
					self.set_position(self.size[1] - 20)
				self.__createText__() 
# """
# the main program loop:::::::::::::::
Game.screen.fill(Game.black)
# loop until the user clicks the close button.
done = False # game ending variable. when True, the game will end.
#:::::::::::::::::::MAIN PROGRAM LOOP::::::::::::::::::::
while not done:
	events = pygame.event.get()
	for event in events: # user did something
		if event.type == QUIT:  # if user clicked close
			done = True # changes while condition to make it end, and exit loop.
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				done = True
	# ORGANIZE THIS IN A WAY THAT DOESN'T CAUSE THE GAME TO EAT YOUR CPU. IT RUNS TOO MANY LOOPS TO RENDER EVERYTHING CONSTANTLY.
	Game.txtbx.update (events) # this lets the input box show what you are typing in real time. should this fail to clear during the use of backspace, you have somehow broken it by moving this exact line someplace it shouldn't be!
	Game.render_info() # shows all in game info in real time
	Game.render_stats() # character stat windows
	Game.render_map() # shows the logo of the game, and the map of where you are. only shows true map once you get one in game.
	Game.txtbx.draw(Game.screen) # shows the input box to type in at bottom of screen
	pygame.display.flip() # finally displays everything above.
	clock.tick(30) # Limit to 30 fps
pygame.quit()