# imports go here for global values that the game can use at any time, anywhere in all code blocks.
import pygame
from math import exp, log
import os
from eztext import *
#start the pygame engine here:
pygame.init()
clock = pygame.time.Clock()  # controls how fast the screen updates at max.
size = (800,750)  # width and hight
screen = pygame.display.set_mode(size)
pygame.display.set_caption("The Legacy of Rex")
#some screen colors:
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
font = pygame.font.Font (None, 25)
stat_font = pygame.font.Font (None, 25)
logo_font = pygame.font.Font ("C:/Windows/Fonts/impact.ttf", 80)
map_font = pygame.font.Font ("C:/Windows/Fonts/impact.ttf", 25)
#boxes for holding yoru text will be listed here. try to keep only 3:
txtbx = T_input(x=10, y=730, font=stat_font, maxlength=90, color=(white), prompt='>: ')
#this space is used for all global functions and variables to be used within all other code blocks, such as print_slow.
def print_slow():
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.01)

def Time_of_day(): #this dictates how time passes in the game, and allows for special events to occur if the time is right!
	Time = ["Morning", "Afternoon", "Evening", "Night"] #this list holds the different times of day/night
	#insert code to make a working clock that changes the time of day in the game, in both millitary and standard time. 
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
	txtbx.update (events)

	#ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT


	#ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
	#ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT


	#ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
	screen.fill(black)

	#make a line of code to make boxes to hold text in by "drawing lines"

	pygame.draw.rect(screen, white,  [5, 424, 790, 300], 2 )  # this is the rectangle at [x, y, width, hight] locations. the last digit is the thickness of the lines
	game_text = font.render("you will see this scrolling around in this window at some point!", True, white)
	screen.blit(game_text, [15, 427]) # this will show the text above as indicated.

	#character stat windows
	#stat window 1
	pygame.draw.rect(screen, white, [5, 5, 260, 200], 2) # this will be the character stats window rectangle. this will hole 4 character stat slots.
	character_stats1 = stat_font.render("Name: lord of awesomness" , True, white) #limit all names by 18 characters
	character_stats1_a = stat_font.render("HP: 100", True, white)
	character_stats1_a_a = stat_font.render("Def: 1", True, white)
	character_stats1_a_b = stat_font.render("Atk: 3", True, white)
	character_stats1_b = stat_font.render("MP: 100", True, white)
	character_stats1_b_a = stat_font.render("San: 100", True, white)
	character_stats1_b_b = stat_font.render("Sta: 100", True, white)
	character_stats1_c = stat_font.render("Status: tox, bur, cur, pet, slw", True, white)
	character_stats1_c_a = stat_font.render("ice, bli, zom, par, sho, ins", True, white)
	character_stats1_E = stat_font.render("Path: theif", True, white)
	character_stats1_E_a = stat_font.render("Head: Headpiece of epicness", True, white) #limit item names for this slot to 22 characters
	character_stats1_E_b = stat_font.render("Chest: Chestpiece of epicness", True, white) # limit names to 22
	character_stats1_E_c = stat_font.render("Legs: Legplates of epicness", True, white) # limit names to 23
	character_stats1_E_d = stat_font.render("Feet: Boots of asskicking", True, white) #limit names to 23
	character_stats1_E_e = stat_font.render("Lhand: fist of fisting", True, white) # limit names to 23
	character_stats1_E_f = stat_font.render("Rhand: fist of fisting", True, white) # limit names to 23
	screen.blit(character_stats1, [15, 15]) #x, y
	screen.blit(character_stats1_a, [15, 30]) # x, y
	screen.blit(character_stats1_a_a, [100, 30]) #x, y
	screen.blit(character_stats1_a_b, [185, 30])
	screen.blit(character_stats1_b, [15, 45]) # x, y
	screen.blit(character_stats1_b_a , [100, 45]) #x, y
	screen.blit(character_stats1_b_b, [185, 45])
	screen.blit(character_stats1_c, [15, 60]) # x, y
	screen.blit(character_stats1_c_a, [15, 75]) # x, y
	screen.blit(character_stats1_E, [15, 90]) # x, y
	screen.blit(character_stats1_E_a, [15, 105]) # x, y
	screen.blit(character_stats1_E_b, [15, 120]) # x, y
	screen.blit(character_stats1_E_c, [15, 135]) # x, y
	screen.blit(character_stats1_E_d, [15, 150]) # x, y
	screen.blit(character_stats1_E_e, [15, 165]) # x, y
	screen.blit(character_stats1_E_f, [15, 180]) # x, y

	#stat window 2
	pygame.draw.rect(screen, white, [264, 5, 260, 200], 2) # 2nd spot character window
	character_stats2 = stat_font.render("Name: mira" , True, white)
	character_stats2_a = stat_font.render("HP: 100", True, white)
	character_stats2_a_a = stat_font.render("Def: 1", True, white)
	character_stats2_a_b = stat_font.render("Atk: 3", True, white)
	character_stats2_b = stat_font.render("MP: 100", True, white)
	character_stats2_b_a = stat_font.render("San: 100", True, white)
	character_stats2_b_b = stat_font.render("Sta: 100", True, white)
	character_stats2_c = stat_font.render("Status: tox, bur, cur, pet, slw", True, white)
	character_stats2_c_a = stat_font.render("ice, bli, zom, par, sho, ins", True, white)
	character_stats2_E = stat_font.render("Path: Knight", True, white)
	character_stats2_E_a = stat_font.render("Head: Headpiece of epicness", True, white)
	character_stats2_E_b = stat_font.render("Chest: Chestpiece of epicness", True, white)
	character_stats2_E_c = stat_font.render("Legs: Legplates of epicness", True, white)
	character_stats2_E_d = stat_font.render("Feet: Boots of asskicking", True, white)
	character_stats2_E_e = stat_font.render("Lhand: fist of fisting", True, white)
	character_stats2_E_f = stat_font.render("Rhand: fist of fisting", True, white)
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


	#stat window 3
	pygame.draw.rect(screen, white, [5, 214, 260, 200], 2) # 3rd spot character window
	character_stats3 = stat_font.render("Name: Squeekers" , True, white)
	character_stats3_a = stat_font.render("HP: 100", True, white)
	character_stats3_a_a = stat_font.render("Def: 1", True, white)
	character_stats3_a_b = stat_font.render("Atk: 3", True, white)
	character_stats3_b = stat_font.render("MP: 100", True, white)
	character_stats3_b_a = stat_font.render("San: 100", True, white)
	character_stats3_b_b = stat_font.render("Sta: 100", True, white)
	character_stats3_c = stat_font.render("Status: tox, bur, cur, pet, slw", True, white)
	character_stats3_c_a = stat_font.render("ice, bli, zom, par, sho, ins", True, white)
	character_stats3_E = stat_font.render("Path: Druid", True, white)
	character_stats3_E_a = stat_font.render("Head: Headpiece of epicness", True, white)
	character_stats3_E_b = stat_font.render("Chest: Chestpiece of epicness", True, white)
	character_stats3_E_c = stat_font.render("Legs: Legplates of epicness", True, white)
	character_stats3_E_d = stat_font.render("Feet: Boots of asskicking", True, white)
	character_stats3_E_e = stat_font.render("Lhand: fist of fisting", True, white)
	character_stats3_E_f = stat_font.render("Rhand: fist of fisting", True, white)
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

	#stat window 4
	pygame.draw.rect(screen, white, [264, 214, 260, 200], 2) # 4th spot character window
	character_stats4 = stat_font.render("Name: your mother" , True, white)
	character_stats4_a = stat_font.render("HP: 100", True, white)
	character_stats4_a_a = stat_font.render("Def: 1", True, white)
	character_stats4_a_b = stat_font.render("Atk: 3", True, white)
	character_stats4_b = stat_font.render("MP: 100", True, white)
	character_stats4_b_a = stat_font.render("San: 100", True, white)
	character_stats4_b_b = stat_font.render("Sta: 100", True, white)
	character_stats4_c = stat_font.render("Status: tox, bur, cur, pet, slw", True, white)
	character_stats4_c_a = stat_font.render("ice, bli, zom, par, sho, ins", True, white)
	character_stats4_E = stat_font.render("Path: Beast Tamer", True, white)
	character_stats4_E_a = stat_font.render("Head: Headpiece of epicness", True, white)
	character_stats4_E_b = stat_font.render("Chest: Chestpiece of epicness", True, white)
	character_stats4_E_c = stat_font.render("Legs: Legplates of epicness", True, white)
	character_stats4_E_d = stat_font.render("Feet: Boots of asskicking", True, white)
	character_stats4_E_e = stat_font.render("Lhand: fist of fisting", True, white)
	character_stats4_E_f = stat_font.render("Rhand: fist of fisting", True, white)
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

	#logo location
	logo = logo_font.render("LEGACY", True, white)
	logo_1 = logo_font.render("OF", True, white)
	logo_2 = logo_font.render("REX", True, white)
	screen.blit(logo,[550, -10])
	screen.blit(logo_1,[620,60])
	screen.blit(logo_2,[600, 130])

	#additional info window/map. does not show map till you buy one!
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