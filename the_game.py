# imports go here for global values that the game can use at any time, anywhere in all code blocks.
import pygame, os
from math import exp, log
from eztext import *
from Characters import *
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
txtbx = T_input(x=10, y=730, font=stat_font, maxlength=90, color=(white), prompt='>: ')
Player1 = Player()
Player1.name = "Lord of awesomness"
Player1.playerpos = "first"
Player2 = Evana()
Player2.playerpos = "second"
Player3 = Irene()
Player3.playerpos = "third"
Player4 = Silvia()
Player4.playerpos = "fourth"
#this space is used for all global functions and variables to be used within all other code blocks, such as print_slow.
def render_stats():
	Player1.update_stat_window()
	Player2.update_stat_window()
	Player3.update_stat_window()
	Player4.update_stat_window()

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

	pygame.draw.rect(screen, white,  [5, 424, 790, 300], 2 )  # this is the rectangle at [x, y, width, hight] locations. the last digit is the thickness of the lines
	game_text = font.render("you will see this scrolling around in this window at some point!", True, white)
	screen.blit(game_text, [15, 427]) # this will show the text above as indicated.

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