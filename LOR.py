#this imports the data from the other files to allow the game to function.
import LORplayerstats
import LORplaces
import LORcollectables
import LORcast
import LORprices
import sys
import random
import os

os.system("color 0E") #green text. type "color /?" for color id's
#this is the warning label. adult content will be added into this game!.. eventually...
print ("WARNING")
print()
print()
print()
print ("This game contains adult material not suited for children!")
print ("by continueing past this point you agree that you take full responsibility in knowing your own laws")
print ("and that we take no responsibility whatsoever if you get in trouble for being an idiot.")
print ("legal jargon stuff.")
print ("TL;DR adult game! if you are underaged, GTFO! otherwise, enjoy the game!")
print()
print()
print()
print()
print ("would you like to play 'Legacy of Rex'? Yes or no?")


#everything after this line will be stats, and character info based on decisions.
#IE: character's class, they follow a path to decide to be paladin or dark knight.
#other stats include hp, mp, stamina, strength, speed, intilect, stealth, and so on.
#this will be the area that imports from other .py's and calls their functions within.
#let's start with assigning the characters base stats at level 1!


#contains all the areas to visit.

	

#    class Map:
#            def __init__(self):
#                    self.locations = {}
#                    self.places = {}
#            def addPlace(self, name, coord, handle):
#                    """Add a place to the map."""
#                    self.locations[coord] = handle
#                    self.places[name] = coord
#            def getPlace(self, coord):
#                    """Find a place by it's given coordinate."""
#                    return self.locations[coord]
#            def findPlace(self, name):
#                    """Find a place by it's given name."""
#                    return self.locations[self.places[name]]
#            def seekCoord(self, handle):
#                    """Find a coord by a handle object."""
#                    for _coord, _handle in self.locations.iteritems():
#                            if( _handle == handle ):
#                                    return _coord





class Map():

	places = {
	'woodsStart': LORplaces.Woods.woodsStart,
	'woodshome': LORplaces.Woods.woodshome,
	'darkwoods': LORplaces.Woods.darkwoods,
	'woodsN1': LORplaces.Woods.woodsN1,
	'woodsN2': LORplaces.Woods.woodsN2,
	'woodsN3': LORplaces.Woods.woodsN3,
	'woodsN4': LORplaces.Woods.woodsN4,
	'woodsS1': LORplaces.Woods.woodsS1,
	'woodsS2': LORplaces.Woods.woodsS2,
	'woodsS3': LORplaces.Woods.woodsS3,
	'woodsS4': LORplaces.Woods.woodsS4,
	'woodsE1': LORplaces.Woods.woodsE1,
	'woodsE2': LORplaces.Woods.woodsE2,
	'woodsE3': LORplaces.Woods.woodsE3,
	'woodsE4': LORplaces.Woods.woodsE4,
	'woodsW1': LORplaces.Woods.woodsW1,
	'woodsW2': LORplaces.Woods.woodsW2,
	'woodsW3': LORplaces.Woods.woodsW3,
	'woodsW4': LORplaces.Woods.woodsW4,
	'woodsNE1_1': LORplaces.Woods.woodsNE1_1,
	'woodsNE1_2': LORplaces.Woods.woodsNE1_2,
	'woodsNE1_3': LORplaces.Woods.woodsNE1_3,
	'woodsNE1_4': LORplaces.Woods.woodsNE1_4,
	'woodsNE2_1': LORplaces.Woods.woodsNE2_1,
	'woodsNE2_2': LORplaces.Woods.woodsNE2_2,
	'woodsNE2_3': LORplaces.Woods.woodsNE2_3,
	'woodsNE2_4': LORplaces.Woods.woodsNE2_4,
	'woodsNE3_1': LORplaces.Woods.woodsNE3_1,
	'woodsNE3_2': LORplaces.Woods.woodsNE3_2,
	'woodsNE3_3': LORplaces.Woods.woodsNE3_3,
	'woodsNE3_4': LORplaces.Woods.woodsNE3_4,
	'woodsNE4_1': LORplaces.Woods.woodsNE4_1,
	'woodsNE4_2': LORplaces.Woods.woodsNE4_2,
	'woodsNE4_3': LORplaces.Woods.woodsNE4_3,
	'woodsNE4_4': LORplaces.Woods.woodsNE4_4,
	'woodsNW1_1': LORplaces.Woods.woodsNW1_1,
	'woodsNW1_2': LORplaces.Woods.woodsNW1_2,
 	'woodsNW1_3': LORplaces.Woods.woodsNW1_3,
 	'woodsNW1_4': LORplaces.Woods.woodsNW1_4,
 	'woodsNW2_1': LORplaces.Woods.woodsNW2_1,
 	'woodsNW2_2': LORplaces.Woods.woodsNW2_2,
 	'woodsNW2_3': LORplaces.Woods.woodsNW2_3,
 	'woodsNW2_4': LORplaces.Woods.woodsNW2_4,
 	'woodsNW3_1': LORplaces.Woods.woodsNW3_1,
 	'woodsNW3_2': LORplaces.Woods.woodsNW3_2,
 	'woodsNW3_3': LORplaces.Woods.woodsNW3_3,
 	'woodsNW3_4': LORplaces.Woods.woodsNW3_4,
 	'woodsNW4_1': LORplaces.Woods.woodsNW4_1,
 	'woodsNW4_2': LORplaces.Woods.woodsNW4_2,
 	'woodsNW4_3': LORplaces.Woods.woodsNW4_3,
 	'woodsNW4_4': LORplaces.Woods.woodsNW4_4,
 	'woodsSE1_1': LORplaces.Woods.woodsSE1_1,
	'woodsSE1_2': LORplaces.Woods.woodsSE1_2,
 	'woodsSE1_3': LORplaces.Woods.woodsSE1_3,
 	'woodsSE1_4': LORplaces.Woods.woodsSE1_4,
 	'woodsSE2_1': LORplaces.Woods.woodsSE2_1,
 	'woodsSE2_2': LORplaces.Woods.woodsSE2_2,
 	'woodsSE2_3': LORplaces.Woods.woodsSE2_3,
 	'woodsSE2_4': LORplaces.Woods.woodsSE2_4,
 	'woodsSE3_1': LORplaces.Woods.woodsSE3_1,
 	'woodsSE3_2': LORplaces.Woods.woodsSE3_2,
 	'woodsSE3_3': LORplaces.Woods.woodsSE3_3,
 	'woodsSE3_4': LORplaces.Woods.woodsSE3_4,
 	'woodsSE4_1': LORplaces.Woods.woodsSE4_1,
 	'woodsSE4_2': LORplaces.Woods.woodsSE4_2,
 	'woodsSE4_3': LORplaces.Woods.woodsSE4_3,
 	'woodsSE4_4': LORplaces.Woods.woodsSE4_4,
 	'woodsSW1_1': LORplaces.Woods.woodsSW1_1,
 	'woodsSW1_2': LORplaces.Woods.woodsSW1_2,
 	'woodsSW1_3': LORplaces.Woods.woodsSW1_3,
 	'woodsSW1_4': LORplaces.Woods.woodsSW1_4,
 	'woodsSW2_1': LORplaces.Woods.woodsSW2_1,
 	'woodsSW2_2': LORplaces.Woods.woodsSW2_2,
 	'woodsSW2_3': LORplaces.Woods.woodsSW2_3,
 	'woodsSW2_4': LORplaces.Woods.woodsSW2_4,
 	'woodsSW3_1': LORplaces.Woods.woodsSW3_1,
 	'woodsSW3_2': LORplaces.Woods.woodsSW3_2,
 	'woodsSW3_3': LORplaces.Woods.woodsSW3_3,
 	'woodsSW3_4': LORplaces.Woods.woodsSW3_4,
 	'woodsSW4_1': LORplaces.Woods.woodsSW4_1,
 	'woodsSW4_2': LORplaces.Woods.woodsSW4_2,
 	'woodsSW4_3': LORplaces.Woods.woodsSW4_3,
	'woodsSW4_4': LORplaces.Woods.woodsSW4_4,
	}

	def __init__(self, start_place):
		self.start_place = start_place

	def next_place(self, place_name):
		return Map.places.get(place_name)

	def enter_place(self):
		return self.next_place(self.start_place)


#runs the game
class Game(object):
	def __init__(self, place_map):
		self.place_map = place_map

	def play(self):
		next_place = Map.places["woodsStart"]

		while True:
			os.system('cls')
			print ("\n-----------------------------------------")
			next_place = next_place()
			#current_place = self.place_map.next_place(next_place_name)
			
	def help_and_quit():
		user = input("> ")
		if user.lower() == "exit" or user.lower() == "quit":
			sys.exit()
		elif user.lower() == "assist":
			print ("stuck? try using a basic verb: touch, feel, take, taste, eat, etc...some options are hidden! So try something new! HINT: it's a verb")



#renamed variables to run the game and load the map at its start point for a 
#new game.
lor_map = Map('woodsStart')
lor_game = Game(lor_map)

#waits for user input to start the game or quit the game.
user = input("> ")
if user.lower() == "yes":
	lor_game.play()
elif user.lower() == "no":
	os.system("cls")
	sys.exit()
else:
    print ("what? I'm not sure what you meant. Try something else perhaps? If you need help, type 'assist'.")


#use this to save a file or load a file for your progress
"""if user.lower() == "save":
	save progress to file
elif user.lower() == "load":
	load progress from file
else:
	print ("Sorry, try something else.") """