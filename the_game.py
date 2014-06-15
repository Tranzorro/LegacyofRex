# imports go here for global values that the game can use at any time, anywhere in all code blocks.
import pygame, os
from tkinter import *
from math import exp, log
from eztext import *
import Characters
#from the_game_screen import *
#start the pygame engine here:
pygame.init()
clock = pygame.time.Clock()  # controls how fast the screen updates at max.
size = (800,750)  # width and hight
screen = pygame.display.set_mode(size)
pygame.display.set_caption("The Legacy of Rex")
font = pygame.font.Font (None, 25)
stat_font = pygame.font.Font (None, 25)
logo_font = pygame.font.Font ("C:/Windows/Fonts/impact.ttf", 80)
map_font = pygame.font.Font ("C:/Windows/Fonts/impact.ttf", 25)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
alpha1 = 1000
alpha2 = 1000
locationText = (10, 426)
txtbx = T_input(x=10, y=730, font=stat_font, maxlength=90, color=(white), prompt='>: ')
Player1 = Characters.Player()
Player1.name = "Lord of awesomness"
Player1.playerpos = "first"
Player2 = Characters.Jenny()
Player2.playerpos = "second"
Player3 = Characters.Evana()
Player3.playerpos = "third"
Player4 = Characters.Bonny()
Player4.playerpos = "fourth"
#this space is used for all global functions and variables to be used within all other code blocks, such as print_slow.
def update_stat_window():
	if Player1.playerpos or Player2.playerpos or Player3.playerpos or Player4.playerpos == "first":
		char_Name = stat_font.render("Name: {}" .format(Player1.name), True, white) #limit all names by 18 characters
		char_Health = stat_font.render("HP: {}" .format(Player1.hp), True, white)
		char_Defence = stat_font.render("Def: {}" .format(Player1.defence), True, white)
		char_Attack = stat_font.render("Atk: {}" .format(Player1.attack), True, white)
		char_Magic = stat_font.render("MP: {}" .format(Player1.mp), True, white)
		char_Sanity = stat_font.render("San: {}" .format(Player1.sanity), True, white)
		char_Stamina = stat_font.render("Sta: {}" .format(Player1.stamina), True, white)
		char_Status1 = stat_font.render("Status: {}" .format(Player1.statusailment1), True, white) #tox, bur, cur, pet, slw
		char_Status2 = stat_font.render("{}" .format(Player1.statusailment2), True, white) #ice, bli, zom, par, sho, ins
		char_Path = stat_font.render("Path: {}" .format(Player1.path), True, white)
		char_Head = stat_font.render("Head: {}" .format(Player1.equipment["Head"]), True, white) #limit item names for this slot to 22 characters
		char_Chest = stat_font.render("Chest: {}" .format(Player1.equipment["Chest"]), True, white) # limit names to 22
		char_Legs = stat_font.render("Legs: {}" .format(Player1.equipment["Legs"]), True, white) # limit names to 23
		char_Feet = stat_font.render("Feet: {}" .format(Player1.equipment["Feet"]), True, white) #limit names to 23
		char_LeftHand = stat_font.render("LHand: {}" .format(Player1.equipment["LHand"]), True, white) # limit names to 23
		char_RightHand = stat_font.render("RHand: {}" .format(Player1.equipment["RHand"]), True, white) # limit names to 23
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
	if Player1.playerpos or Player2.playerpos or Player3.playerpos or Player4.playerpos == "second":
		character_stats2 = stat_font.render("Name: {}" .format(Player2.name), True, white)
		character_stats2_a = stat_font.render("HP: {}" .format(Player2.hp), True, white)
		character_stats2_a_a = stat_font.render("Def: {}" .format(Player2.defence), True, white)
		character_stats2_a_b = stat_font.render("Atk: {}" .format(Player2.attack), True, white)
		character_stats2_b = stat_font.render("MP: {}" .format(Player2.mp), True, white)
		character_stats2_b_a = stat_font.render("San: {}" .format(Player2.sanity), True, white)
		character_stats2_b_b = stat_font.render("Sta: {}" .format(Player2.stamina), True, white)
		character_stats2_c = stat_font.render("Status: {}".format(Player2.statusailment1), True, white)
		character_stats2_c_a = stat_font.render("{}" .format(Player2.statusailment2), True, white)
		character_stats2_E = stat_font.render("Path: {}" .format(Player2.path), True, white)
		character_stats2_E_a = stat_font.render("Head: {}" .format(Player2.equipment["Head"]), True, white)
		character_stats2_E_b = stat_font.render("Chest: {}" .format(Player2.equipment["Chest"]), True, white)
		character_stats2_E_c = stat_font.render("Legs: {}" .format(Player2.equipment["Legs"]), True, white)
		character_stats2_E_d = stat_font.render("Feet: {}" .format(Player2.equipment["Feet"]), True, white)
		character_stats2_E_e = stat_font.render("LHand: {}" .format(Player2.equipment["LHand"]), True, white)
		character_stats2_E_f = stat_font.render("RHand: {}" .format(Player2.equipment["RHand"]), True, white)
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
	if Player1.playerpos or Player2.playerpos or Player3.playerpos or Player4.playerpos == "third":
		character_stats3 = stat_font.render("Name: {}" .format(Player3.name) , True, white)
		character_stats3_a = stat_font.render("HP: {}" .format(Player3.hp), True, white)
		character_stats3_a_a = stat_font.render("Def: {}" .format(Player3.defence), True, white)
		character_stats3_a_b = stat_font.render("Atk: {}" .format(Player3.attack), True, white)
		character_stats3_b = stat_font.render("MP: {}" .format(Player3.mp), True, white)
		character_stats3_b_a = stat_font.render("San: {}" .format(Player3.sanity), True, white)
		character_stats3_b_b = stat_font.render("Sta: {}" .format(Player3.stamina), True, white)
		character_stats3_c = stat_font.render("Status: {}" .format(Player3.statusailment1), True, white)
		character_stats3_c_a = stat_font.render("{}" .format(Player3.statusailment2), True, white)
		character_stats3_E = stat_font.render("Path: {}" .format(Player3.path), True, white)
		character_stats3_E_a = stat_font.render("Head: {}" .format(Player3.equipment["Head"]), True, white)
		character_stats3_E_b = stat_font.render("Chest: {}" .format(Player3.equipment["Chest"]), True, white)
		character_stats3_E_c = stat_font.render("Legs: {}" .format(Player3.equipment["Legs"]), True, white)
		character_stats3_E_d = stat_font.render("Feet: {}" .format(Player3.equipment["Feet"]), True, white)
		character_stats3_E_e = stat_font.render("LHand: {}" .format(Player3.equipment["LHand"]), True, white)
		character_stats3_E_f = stat_font.render("RHand: {}" .format(Player3.equipment["RHand"]), True, white)
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
	if Player1.playerpos or Player2.playerpos or Player3.playerpos or Player4.playerpos == "fourth":
		character_stats4 = stat_font.render("Name: {}" .format(Player4.name), True, white)
		character_stats4_a = stat_font.render("HP: {}" .format(Player4.hp), True, white)
		character_stats4_a_a = stat_font.render("Def: {}" .format(Player4.defence), True, white)
		character_stats4_a_b = stat_font.render("Atk: {}" .format(Player4.attack), True, white)
		character_stats4_b = stat_font.render("MP: {}" .format(Player4.mp), True, white)
		character_stats4_b_a = stat_font.render("San: {}" .format(Player4.sanity), True, white)
		character_stats4_b_b = stat_font.render("Sta: {}" .format(Player4.stamina), True, white)
		character_stats4_c = stat_font.render("Status: {}" .format(Player4.statusailment1), True, white)
		character_stats4_c_a = stat_font.render("{}" .format(Player4.statusailment2), True, white)
		character_stats4_E = stat_font.render("Path: {}" .format(Player4.path), True, white)
		character_stats4_E_a = stat_font.render("Head: {}" .format(Player4.equipment["Head"]), True, white)
		character_stats4_E_b = stat_font.render("Chest: {}" .format(Player4.equipment["Chest"]), True, white)
		character_stats4_E_c = stat_font.render("Legs: {}" .format(Player4.equipment["Legs"]), True, white)
		character_stats4_E_d = stat_font.render("Feet: {}" .format(Player4.equipment["Feet"]), True, white)
		character_stats4_E_e = stat_font.render("LHand: {}" .format(Player4.equipment["LHand"]), True, white)
		character_stats4_E_f = stat_font.render("RHand: {}" .format(Player4.equipment["RHand"]), True, white)
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

def render_stats():
	update_stat_window()

def print_slow():
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.01)

def Time_of_day(): #this dictates how time passes in the game, and allows for special events to occur if the time is right!
	Time = ["Morning", "Afternoon", "Evening", "Night"] #this list holds the different times of day/night
	#insert code to make a working clock that changes the time of day in the game, in both millitary and standard time. 

class textBox(pygame.sprite.Sprite):                                #I don't understand how most of this works, all I know is that I got it working... a little.
    #A textbox to see what we are doing in the game
	def __init__(self, position = locationText,                        ##locationText is a variable holding the default location of the text
			size = [790, 300], alpha = alpha2,                ##alpha2 is normally 150
			color = (255,255,255), scrollPosition = 0,
			textSize = 25):
		pygame.sprite.Sprite.__init__(self)
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
		self.text = "this text should pop up if you did it correctly. let's see if we can get you scrolling!"
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

	def update(self, mouseXY):            ##The update occurs every time the mouse is down on the textbox, and the arguments are the mouse's coordenates
		pygame.sprite.Sprite.update(self)
		if len(self.text) != 0 and self.rect.collidepoint(mouseXY) == True:
			mouseY = mouseXY[1] - locationText[1]
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

#loop until the user clicks the close button.
done = False
#:::::::::::::::::::MAIN PROGRAM LOOP::::::::::::::::::::
while not done:
	#ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
	events = pygame.event.get()
	for event in events: #user did something
		if event.type == QUIT:  #if user clicked close
			done = True #changes while condition to make it end, and exit loop.
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				done = True
	txtbx.update (events)

	#ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT


	#ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
	#ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT


	#ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
	screen.fill(black)

	#make a line of code to make boxes to hold text in by "drawing lines"
	tbx = pygame.sprite.RenderPlain(textBox())
	tbx.draw(screen)
	pygame.draw.rect(screen, white,  [5, 424, 790, 300], 2 )  # this is the rectangle at [x, y, width, hight] locations. the last digit is the thickness of the lines
	#game_text = font.render("if you see this, you are doing it wrong! this needs to be a scrolling test window!", True, white)
	#screen.blit(game_text, [15, 427]) # this will show the text above as indicated.



	#character stat windows
	#stat window 1
	pygame.draw.rect(screen, white, [5, 5, 260, 200], 2) # this will be the character stats window rectangle. this will hole 4 character stat slots.
	#stat window 2
	pygame.draw.rect(screen, white, [264, 5, 260, 200], 2) # 2nd spot character window
	#stat window 3
	pygame.draw.rect(screen, white, [5, 214, 260, 200], 2) # 3rd spot character window
	#stat window 4
	pygame.draw.rect(screen, white, [264, 214, 260, 200], 2) # 4th spot character window
	render_stats()


	logo = logo_font.render("LEGACY", True, white)
	logo_1 = logo_font.render("OF", True, white)
	logo_2 = logo_font.render("REX", True, white)
	screen.blit(logo,[550, -10])
	screen.blit(logo_1,[620,60])
	screen.blit(logo_2,[600, 130])

	pygame.draw.rect(screen, white, [534, 214, 260, 200], 2)
	map_text = map_font.render ("No map installed yet.", True, white)
	map_text1 = map_font.render ("Sorry!", True, white)
	screen.blit(map_text,[540, 218])
	screen.blit (map_text1,[540, 240])

	#input box
	txtbx.draw(screen)

	pygame.display.flip()
	#ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT


	#Limit to 30 fps
	clock.tick(30)
pygame.quit()