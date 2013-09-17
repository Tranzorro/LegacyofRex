#this .py has all the areas to visit.
#we will start with the woods, and work our way to the cities.
#country is not added as class due to inability to leave country.
#the user will have decisions based on exploring, and other interactions.
import LORdeath
import LORplayerstats

class Woods():

	def woodsStart():
			print ("You cannot see anything, you open your eyes to find you are alone, surrounded by trees.\n you are quite tired, and as you wake up, you notice that you have no clue where you are.")
			return Woods.woodshome

	def woodshome():
		print ('You are in the woods. The area looks safe, for now... This is where you first woke up.\n this area is home to the largest tree around.')
		print ('options')
		print ('explore, look, smell, touch, eat, inventory, take, talk')
		user = input("> ")
		if user.lower() == "explore":
			print ('you wish to explore, where do you want to explore? here, or go somewhere else?')
			print ('places you can explore from your current position: north, south, east, west, here')
			user = input("> ")
			if user.lower() == "here":
				print ("You wander about the woods at random and find the sight to be rather pleasant.")
				print ("Your feet make the leaves and sticks crack with every step you take as you take")
				print ("in your surroundings. As you go deeper and deeper into the woods, you manage")
				print ("to stumble across an old tree, one that seems to be much older and much larger")
				print ("than all the other trees. upon this trees surface you note it has a rather oddly")
				print ("shaped knot hole in the middle of its large trunk. in some ways it may look like a")
				print ("face in the surface of the tree, but thats silly, trees don't have faces!")
				return Woods.woodshome
			elif user.lower() == "north":
				return Woods.woodsN1
			elif user.lower() == "east":
				return Woods.woodsE1
			elif user.lower() == "south":
				return Woods.woodsS1
			elif user.lower() == "west":
				return Woods.woodsW1
			else:
				print ("Hmmm... nope. Don't know that one, try again.")
				return Woods.woodshome
		elif user.lower() == "look":
			print ("what do you wish to look at? yourself? or the surroundings?")
			user = input("> ")
			if user.lower() == "surroundings":
				print ("you look at the largest tree in the area, and see that it's rather old looking. you could swear")
				print ("it has a face on it, but it's a tree... why would it have a face? do you think it would talk to you")
				print ("if you tried to talk to it? it seems to have quite a bit of life to it, as its leaves are all full of")
				print ("bright green colors. the branches even have a few flowers growing off them. its really quite beautiful.")
				return Woods.woodshome
			elif user.lower() == "self":
				print ("you attempt to look at yourself, but there is nothing reflective enough to see yourself in! try to locate some")
				print ("water, or a place with a mirror to see yoruself.")
				return Woods.woodshome
		elif user.lower() == "smell":
			print ("what do you want to smell? yourself? or your surroundings?")
			user = input("> ")
			if user.lower() == "self":
				print ("You take a whiff of yourself with a big snort! phew! you stink! you could use a bath!")
				return Woods.woodshome
			elif user.lower() == "surroundings":
				print ("you breath in deeply, taking in the fresh air of your surroundings. You pick up the smell")
				print ("of pine needles, Tall grass, Flower pollen, and maybe a hint of droppings nearby from some")
				print ("native creature who roams these parts.")
				return Woods.woodshome
		elif user.lower() == "touch" or user.lower() == "feel":
			print ("what would you like to touch? yourself? your surroundings?")
			user = input("> ")
			if user.lower() == "self":
				print ("you begin to feel yourself all over... you can feel the fur on your skin,")
				print ("your protruding muzzle, your pointy ears, your fluffy tail that swishes")
				print ("behind you with exitement as you seem to enjoy this.. maybe a little too much...")
				return Woods.woodshome
			elif user.lower() == "surroundings":
				print (" You take your hand to the ground and feel the leaves that crunch in your grip.")
				print ("The twigs are rather brittle in this part of the woods. any more brittle and they")
				print ("would disintigrate from hitting the ground! you go to a nearby tree and feel its")
				print ("bark coating, feeling the coursness of the fiber armor these old trees have worn")
				print ("for ages, and hopefully many more to come. you stand still for a moment to take ")
				print ("in the wind as it blows through your fur. it feels nice. gentle. a little brisk though.")
				print ("you think you should find a warm place to stay for the night, you don't want to catch")
				print ("your death out  here!")
				return Woods.woodshome
		elif user.lower() == "eat":
			print ("what do you want to taste or eat? yourself? some food you might have, an object laying around?")
			user = input("> ")
			if user.lower() == "self":
				print ("You give yourself a lick on the back of your hand... you taste aweful!")
				print ("Though i'm sure other hungry creatures might not care when they are hungry enough...")
				return Woods.woodshome
			elif user.lower() == "food":
				print ("You don't have anything to eat yet. try looking around or buying some!")
				return Woods.woodshome
			elif user.lower() == "object":
				print ("You pick up a stick and lick it, it tastes... horrible. but full of fiber! you think you saw a catterpillar on it...")
				print (" but it's nowhere to be found now. though your tongue seems to feel rather odd and tingly...")
				return Woods.woodshome
		elif user.lower() == "inventory" or user.lower() == "bag":
			print ("You don't have an inventory yet! sorry, have to put that in still... damned lazy coder!")
			return Woods.woodshome
		elif user.lower() == "take":
			print ("Can't take anything yet! no inventory to put it into! coder, get your ass on that!")
			return Woods.woodshome
		elif user.lower() == "talk":
			print ("who do you want to talk to? yourself? or someone else? or someTHING else?")
			user = input("> ")
			if user.lower() == "self":
				print ("You want to talk to yoruself? what are you, crazy? you aren't insane enough to talk to yourself yet.")
				return Woods.woodshome
			elif user.lower() == "tree":
				print ("You walk up to the biggest oldest tree around, and say 'Hello', it doesn't respond to you... Go figure.")
				return Woods.woodshome
		else:
			print ("Hmmmm nope, try something else.")
			return Woods.woodshome
		
	def darkwoods():
		print ('you are in the darkwoods. i have yet to add anything here yet.\n try going to another place!')
		print ('options')
		
	def woodsN1():
		print ("You follow your internal compass... it seems the woods go deeper and deeper. You think you can see a clearing")
		print ("ahead, but it's still rather far.")
		print ('options')
		print ('explore')
		user = input("> ")
		if user.lower() == "explore":
			print ("where would you like to explore? here? or somewhere else? you can go north, east, south, and west.")
			user = input("> ")
			if user.lower() == "north":
				return Woods.woodsN2
			elif user.lower() == "east":
				return Woods.woodsNE1_1
			elif user.lower() == "south":
				return Woods.woodshome
			elif user.lower() == "west":
				return Woods.woodsNW1_1
			elif user.lower() == "here":
				print ("You wander about and find nothing of interest. all the trees look the same here.")
				return Woods.woodsN1

	def woodsN2():
			print ("you tripped on a stick and smashed your head on a rock.")
#			print ("you can go north, east, south, or west.")
			return LORdeath.Death
			"""if user.lower() == "north":
				return Woods.woodsN3()
			elif user.lower() == "east":
				return Woods.woodsNE1_2()
			elif user.lower() == "south":
				return Woods.woodsN1()
			elif user.lower() == "west":
				return Woods.woodsNW1_2()"""

	def woodsN3():
		print ("got nuthin here. go somewhere else... sorry.")
		print ("you can go north east south and west.")
		user = input("> ")
		if user.lower() == "north":
			return Woods.woodsN4
		elif user.lower() == "east":
			return Woods.woodsNE1_3
		elif user.lower() == "south":
			return Woods.woodsN2
		elif user.lower() == "west":
			return Woods.woodsNW1_3

	def woodsN4():
		print ("aint got nuthin here. sorry. go somewhere else.")
		print ("west, east, or south.")
		user = input("> ")
		if user.lower() == "west":
			return Woods.woodsNW1_4
		elif user.lower() == "east":
			return Woods.woodsNE1_4
		elif user.lower() == "south":
			return Woods.woodsN3

	def woodsS1():
		print ("nothign here. go elsewhere...")
		print ("north south east or west bro.")
		user = input("> ")
		if user.lower() == "north":
			return Woods.woodshome
		elif user.lower() == "east":
			return Woods.woodsSE1_1
		elif user.lower() == "south":
			return Woods.woodsS2
		elif user.lower() == "west":
			return Woods.woodsSW1_1

	def woodsS2():
		print ("north east south or west bro")
		user = input("> ")
		if user.lower() == "north":
			return Woods.woodsS1
		elif user.lower() == "east":
			return Woods.woodsSE1_2
		elif user.lower() == "south":
			return Woods.woodsS3
		elif user.lower() == "west":
			return Woods.woodsSW1_2

	def woodsS3():
		print ("north east south or west")
		user = input("> ")
		if user.lower() == "north":
			return Woods.woodsS2
		elif user.lower() == "east":
			return Woods.woodsSE1_3
		elif user.lower() == "south":
			return Woods.woodsS4
		elif user.lower() == "west":
			return Woods.woodsSW1_3

	def woodsS4():
		print ("north east or west")
		user = input("> ")
		if user.lower() == "north":
			return Woods.woodsS3
		elif user.lower() == "east":
			return Woods.woodsSE1_4
		elif user.lower() == "west":
			return Woods.woodsSW1_4

	def woodsE1():
		print ("north east south or west")
		user = input("> ")
		if user.lower() == "north":
			return Woods.woodsNE1_1
		elif user.lower() == "east":
			return Woods.woodsE2
		elif user.lower() == "south":
			return Woods.woodsSE1_1
		elif user.lower() == "west":
			return Woods.woodshome

	def woodsE2():
		print ("north east south or west")
		user = input("> ")
		if user.lower() == "north":
			return Woods.woodsNE2_1
		elif user.lower() == "east":
			return Woods.woodsE3
		elif user.lower() == "south":
			return Woods.woodsSE2_1
		elif user.lower() == "west":
			return Woods.woodsE1

	def woodsE3():
		print ("north east south or west")
		user = input("> ")
		if user.lower() == "north":
			return Woods.woodsNE3_1
		elif user.lower() == "east":
			return Woods.woodsE4
		elif user.lower() == "south":
			return Woods.woodsSE3_1
		elif user.lower() == "west":
			return Woods.woodsE2

	def woodsE4():
		print ("north south west")
		user = input("> ")
		if user.lower() == "north":
			return Woods.woodsNE4_1
		elif user.lower() == "south":
			return Woods.woodsSE4_1
		elif user.lower() == "west":
			return Woods.woodsE3

	def woodsW1():
		print ("north east south or west")
		user = input("> ")
		if user.lower() == "north":
			return Woods.woodsNW1_1
		elif user.lower() == "east":
			return Woods.woodshome
		elif user.lower() == "south":
			return Woods.woodsSW1_1
		elif user.lower() == "west":
			return Woods.woodsW2

	def woodsW2():
		print ("north east south west")
		user = input("> ")
		if user.lower() == "north":
			return Woods.woodsNW2_1
		elif user.lower() == "east":
			return Woods.woodsW1
		elif user.lower() == "south":
			return Woods.woodsSW2_1
		elif user.lower() == "west":
			return Woods.woodsW3

	def woodsW3():
		print ("north east south or west")
		user = input("> ")
		if user.lower() == "north":
			return Woods.woodsNW3_1
		elif user.lower() == "east":
			return Woods.woodsW2
		elif user.lower() == "south":
			return Woods.woodsSW3_1
		elif user.lower() == "west":
			return Woods.woodsW4

	def woodsW4():
		print ("north east south")
		user = input("> ")
		if user.lower() == "north":
			return Woods.woodsNW4_1
		elif user.lower() == "east":
			return Woods.woodsW3
		elif user.lower() == "south":
			return Woods.woodsSW4_1

	def woodsNE1_1():
		print ("north east south west")
		user = input("> ")
		if user.lower() == "north":
			return Woods.woodsNE1_2
		elif user.lower() == "east":
			return Woods.woodsNE2_1
		elif user.lower() == "south":
			return Woods.woodsE1
		elif user.lower() == "west":
			return Woods.woodsN1

	def woodsNE1_2():
		print ("north east south west")
		user = input("> ")
		if user.lower() == "north":
			return Woods.woodsNE1_3
		elif user.lower() == "east":
			return Woods.woodsNE2_2
		elif user.lower() == "south":
			return Woods.woodsNE1_1
		elif user.lower() == "west":
			return Woods.woodsN2 

	def woodsNE1_3():
		print ("north east south west")
		user = input("> ")
		if user.lower() == "north":
			return Woods.woodsNE1_4
		elif user.lower() == "east":
			return Woods.woodsNE2_3
		elif user.lower() == "south":
			return Woods.woodsNE1_2
		elif user.lower() == "west":
			return Woods.woodsN3

	def woodsNE1_4():
		print ("east south west")
		user = input("> ")
		if user.lower() == "east":
			return Woods.woodsNE2_4
		elif user.lower() == "south":
			return Woods.woodsNE1_3
		elif user.lower() == "west":
			return Woods.woodsN4

	def woodsNE2_1():
		print ("north east south or west")
		user = input("> ")
		if user.lower() == "north":
			return Woods.woodsNE2_2
		elif user.lower() == "east":
			return Woods.woodsNE3_2
		elif user.lower() == "south":
			return Woods.woodsE2
		elif user.lower() == "west":
			return Woods.woodsNE1_1

	def woodsNE2_2():
		print ("north east south or west")
		user = input("> ")
		if user.lower() == "north":
			return Woods.woodsNE2_3
		elif user.lower() == "east":
			return Woods.woodsNE3_2
		elif user.lower() == "south":
			return Woods.woodsNE2_1
		elif user.lower() == "west":
			return Woods.woodsNE1_2

	def woodsNE2_3():
		print ("north east south or west")
		user = input("> ")
		if user.lower() == "north":
			return Woods.woodsNE2_4
		elif user.lower() == "east":
			return Woods.woodsNE3_4
		elif user.lower() == "south":
			return Woods.woodsNE2_2
		elif user.lower() == "west":
			return Woods.woodsNE1_3

	def woodsNE2_4():
		print ("east south or west")
		user = input("> ")
		if user.lower() == "east":
			return Woods.woodsNE3_4
		elif user.lower() == "south":
			return Woods.woodsNE2_3
		elif user.lower() == "west":
			return Woods.woodsNE1_4

	def woodsNE3_1():
		print ("north east south or west")
		user = input("> ")
		if user.lower() == "north":
			return Woods.woodsNE3_2
		elif user.lower() == "east":
			return Woods.woodsNE4_1
		elif user.lower() == "south":
			return Woods.woodsE3
		elif user.lower() == "west":
			return Woods.woodsNE2_1

	def woodsNE3_2():
		print ("north east south or west")
		user = input("> ")
		if user.lower() == "north":
			return Woods.woodsNE3_3
		elif user.lower() == "east":
			return Woods.woodsNE4_2
		elif user.lower() == "south":
			return Woods.woodsNE3_1
		elif user.lower() == "west":
			return Woods.woodsNE2_2

	def woodsNE3_3():
		print ("north east south or west")
		user = input("> ")
		if user.lower() == "north":
			return Woods.woodsNE3_4
		elif user.lower() == "east":
			return Woods.woodsNE4_3
		elif user.lower() == "south":
			return Woods.woodsNE3_2
		elif user.lower() == "west":
			return Woods.woodsNE2_3

	def woodsNE3_4():
		print ("east south or west")
		user = input("> ")
		if user.lower() == "east":
			return Woods.woodsNE4_4
		elif user.lower() == "south":
			return Woods.woodsNE3_3
		elif user.lower() == "west":
			return Woods.woodsNE2_4

	def woodsNE4_1():
		print ("north south or west")
		user = input("> ")
		if user.lower() == "north":
			return Woods.woodsNE4_2
		elif user.lower() == "south":
			return Woods.woodsE4
		elif user.lower() == "west":
			return Woods.woodsNE3_1

	def woodsNE4_2():
		print ("north south or west")
		user = input("> ")
		if user.lower() == "north":
			return Woods.woodsNE4_3
		elif user.lower() == "south":
			return Woods.woodsNE4_1
		elif user.lower() == "west":
			return Woods.woodsNE3_2

	def woodsNE4_3():
		print ("north south or west")
		user = input("> ")
		if user.lower() == "north":
			return Woods.woodsNE4_4
		elif user.lower() == "south":
			return Woods.woodsNE4_2
		elif user.lower() == "west":
			return Woods.woodsNE3_3

	def woodsNE4_4():
		print ("south or west")
		user = input("> ")
		if user.lower() == "south":
			return Woods.woodsNE4_3
		elif user.lower() == "west":
			return Woods.woodsNE3_4

	def woodsNW1_1():
		print ("north east south or west")
		user = input("> ")
		if user.lower() == "north":
			return Woods.woodsNW1_2
		elif user.lower() == "east":
			return Woods.woodsN1
		elif user.lower() == "south":
			return Woods.woodsW1
		elif user.lower() == "west":
			return Woods.woodsNW2_1

	def woodsNW1_2():
		print ("north east south or west")
		user = input("> ")
		if user.lower() == "north":
			return Woods.woodsNW1_2
		elif user.lower() == "east":
			return Woods.woodsN2
		elif user.lower() == "south":
			return Woods.woodsNW1_1
		elif user.lower() == "west":
			return Woods.woodsNW2_2

	def woodsNW1_3():
		print ("nothing here but death")
		return death()

	def woodsNW1_4():
		print ("nothing here but death")
		return death()

	def woodsNW2_1():
		print ("nothing here but death")
		return death()

	def woodsNW2_2():
		print ("nothing here but death")
		return death()

	def woodsNW2_3():
		print ("nothing here but death")
		return death()

	def woodsNW2_4():
		print ("nothing here but death")
		return death()

	def woodsNW3_1():
		print ("nothing here but death")
		return death()

	def woodsNW3_2():
		print ("nothing here but death")
		return death()

	def woodsNW3_3():
		print ("nothing here but death")
		return death()

	def woodsNW3_4():
		print ("nothing here but death")
		return death()

	def woodsNW4_1():
		print ("nothing here but death")
		return death()

	def woodsNW4_2():
		print ("nothing here but death")
		return death()

	def woodsNW4_3():
		print ("nothing here but death")
		return death()

	def woodsNW4_4():
		print ("nothing here but death")
		return death()

	def woodsSE1_1():
		print ("nothing here but death")
		return death()

	def woodsSE1_2():
		print ("nothing here but death")
		return death()

	def woodsSE1_3():
		print ("nothing here but death")
		return death()

	def woodsSE1_4():
		print ("nothing here but death")
		return death()

	def woodsSE2_1():
		print ("nothing here but death")
		return death()

	def woodsSE2_2():
		print ("nothing here but death")
		return death()

	def woodsSE2_3():
		print ("nothing here but death")
		return death()

	def woodsSE2_4():
		print ("nothing here but death")
		return death()

	def woodsSE3_1():
		print ("nothing here but death")
		return death()

	def woodsSE3_2():
		print ("nothing here but death")
		return death()

	def woodsSE3_3():
		print ("nothing here but death")
		return death()

	def woodsSE3_4():
		print ("nothing here but death")
		return death()

	def woodsSE4_1():
		print ("nothing here but death")
		return death()

	def woodsSE4_2():
		print ("nothing here but death")
		return death()

	def woodsSE4_3():
		print ("nothing here but death")
		return death()

	def woodsSE4_4():
		print ("nothing here but death")
		return death()

	def woodsSW1_1():
		print ("nothing here but death")
		return death()

	def woodsSW1_2():
		print ("nothing here but death")
		return death()

	def woodsSW1_3():
		print ("nothing here but death")
		return death()

	def woodsSW1_4():
		print ("nothing here but death")
		return death()

	def woodsSW2_1():
		print ("nothing here but death")
		return death()

	def woodsSW2_2():
		print ("nothing here but death")
		return death()

	def woodsSW2_3():
		print ("nothing here but death")
		return death()

	def woodsSW2_4():
		print ("nothing here but death")
		return death()

	def woodsSW3_1():
		print ("nothing here but death")
		return death()

	def woodsSW3_2():
		print ("nothing here but death")
		return death()

	def woodsSW3_3():
		print ("nothing here but death")
		return death()

	def woodsSW3_4():
		print ("nothing here but death")
		return death()

	def woodsSW4_1():
		print ("nothing here but death")
		return death()

	def woodsSW4_2():
		print ("nothing here but death")
		return death()

	def woodsSW4_3():
		print ("nothing here but death")
		return death()

	def woodsSW4_4():
		print ("nothing here but death")
		return death()

class Plains():

	def plains():
		print ('you are in the plains. i have yet to add anything here yet.\n try going to another place!')
		print ('options')

	def sandstorm():
		print ('you enter the sandstorm, you are lost! i have yet to add anything here yet.\n try going to another place!')
		print ('options')

class Hills():

	def hills():
		print ('you are in the hills. i have yet to add anything here yet.\n try going to another place!')
		print ('options')

	def hut():
		print ('you are at a hut. i have yet to add anything here yet.\n try going to another place!')
		print ('options')

class Fields():

	def fields():
		print ('you are in the fields! i have yet to add anything here yet.\n try going to another place!')
		print ('options')

	def cave():
		print ('you arrive at the cave! i have yet to add anything here yet.\n try going to another place!')
		#goto cave

	def river():
		print ('you arrive at the river. i have yet to add anything here yet.\n try going to another place!')
		print ('options')

class Mountain():

	def mountain():
		print ('you arrive at the mountains. i have yet to add anything here yet.\n try going to another place!')
		print ('options')

	def peaks():
		print ('you have scaled the mountains and find the peaks! i have yet to add anything here yet.\n try going to another place!')
		print ('options')
		
	def volcano():
		print ('you arrive at a very hot volcano. i have yet to add anything here yet.\n try going to another place!')
		print ('options')

class Sea():

	def sea():
		print ('you are at the sea. i have yet to add anything here yet.\n try going to another place!')
		print ('options')

	def depths():
		print ('you swim down inot the depths. its dark here... i have yet to add anything here yet.\n try going to another place!')
		print ('options')
		
class Cave():

	def main_hall():
		print ("you enter tha cave's main hall. where do you wana go from here? i have yet to add anything here yet.\n try going to another place!")
		print ('options')
		
	def your_bedroom():
		print ('you touch the wall and it dissapears, revealing your very rundown and basic looking room. i have yet to add anything here yet.\n try going to another place!')
		print ('options')
		
	def girls_bedroom():
		print ('you follow the girl to wall and she touches it, the wall vanishes and the room inside reveals itself. i have yet to add anything here yet.\n try going to another place!')
		print ('options')

	def dining_hall():
		print ('you enter the dining hall. you see a large rectangular table with many seats. i have yet to add anything here yet.\n try going to another place!')
		print ('options')
		
	def treasury():
		print ("you arrive at the dragon's treasury room. its filled with piles of gold and silver, many different reare and unknown objects on pedistals. i have yet to add anything here yet.\n try going to another place!")
		print ('options')
		
	def bathing_room():
		print ('you enter the bathing room. all you see is the wall torches and a pillar in the room that is in the center of a large empty round hole in the floor, lined with tiled stones. i have yet to add anything here yet.\n try going to another place!')
		print ('options')
		
	def medical_room():
		print ('you enter the medical room. there are plenty of beds and floor pads to lay on, there is medical equipment all over the place. i have yet to add anything here yet.\n try going to another place!')
		print ('options')

class Sky():

	def sky():
		print ('you go high into the sky. you can see quite far from up here! i have yet to add anything here yet.\n try going to another place!')
		print ('options')
		#goto anywhere

class Binkertink_City():

	def the_docks():
		print ('you arrive at the docks. i have yet to add anything here yet.\n try going to another place!')
		print ('options')
		
	def the_port():
		print ('you arrive at the port. i have yet to add anything here yet.\n try going to another place!')
		print ('options')

	def house():
		print ('you are at an empty house. i have yet to add anything here yet.\n try going to another place!')
		print ('options')
		
	def Inn():
		print ('you arrive at the local INN! i have yet to add anything here yet.\n try going to another place!')
		print ('options')
		
	def Jeweler():
		print ('you find a shop labeled "jeweler", yet it seems to be closed. i have yet to add anything here yet.\n try going to another place!')
		print ('options')
		
	def Arena():
		print ('you find a large building that seems to have large metal gates and flags all over. its locked. i have yet to add anything here yet.\n try going to another place!')
		print ('options')
		
	def streets():
		print ('you walk onto the streets of the city, where would you liek to go from here? i have yet to add anything here yet.\n try going to another place!')
		print ('options')
		
	def front_gate():
		print ('you arrive at the front gate of the city Binkertink. i have yet to add anything here yet.\n try going to another place!')
		print ('options')

class Hadistrom_City():

	def front_gate():
		print ('you arrive at the front gate of Hadistrom City! i have yet to add anything here yet.\n try going to another place!')
		print ('options')

class Hiorin_city():

	def blacksmith():
		print ('you find a shop labeled "Blacksmith", but it seems to be closed. i have yet to add anything here yet.\n try going to another place!')
		print ('options')
		
	def house():
		print ('you arrive at an abandoned home. i have yet to add anything here yet.\n try going to another place!')
		print ('options')
		
	def tower():
		print ('you locate the largest building around, the Tower. i have yet to add anything here yet.\n try going to another place!')
		print ('options')
		
	def library():
		print ('you enter the library, its full of books and information! i have yet to add anything here yet.\n try going to another place!')
		print ('options')
		
	def Alchemist():
		print ('you locate a shop nearby called "Alchemist", though it seems to be closed. i have yet to add anything here yet.\n try going to another place!')
		print ('options')
		
	def Inn():
		print ('you found the local INN, you enter and find there are plenty of random citizens drinking and wandering about. i have yet to add anything here yet.\n try going to another place!')
		print ('options')
		
	def Bank():
		print ('you enter the bank, lots of peopel are here, you walk into a line to wait your turn to be serviced. i have yet to add anything here yet.\n try going to another place!')
		print ('options')
		
	def castle():
		print ('you arrive at the castle. two guards stand at attention at all times here. i have yet to add anything here yet.\n try going to another place!')
		print ('options')
		
	def other_dimension():
		print ('you walk through the portal and enter a strange new place. the sky and the ground are both one. you see nothing but empty space and a strange starry pattern across the entirety of the area. i have yet to add anything here yet.\n try going to another place!')
		print ('options')
		
	def streets():
		print ('you wander the streets. where would you like to go from here? i have yet to add anything here yet.\n try going to another place!')
		print ('options')

	def front_gates():
		
		pass

class Gorbin_Town():

	def Tavern():
		print ('you arrived at the local tavern. i have yet to add anything here yet.\n try going to another place!')
		print ('options')
		
	def underground():
		print ("you duck under some rocks and find a hole big enough to squeese through. you enter and see nothing. damn, it's dark here! i have yet to add anything here yet.\n try going to another place!")
		print ('options')
		
	def streets():
		print ('you wander the streets, where would you like to go from here? i have yet to add anything here yet.\n try going to another place!')
		print ('options')

class Verona():

	def tailor():
		print ('you found a shop labeled "Tailor", but it seems to be closed. i have yet to add anything here yet.\n try going to another place!')
		print ('options')
		
	def house():
		print ('you arrive at an abandoned home. i have yet to add anything here yet.\n try going to another place!')
		print ('options')
		
	def bar():
		print ('you arrive at the local bar, everyone is getting wasted here. i have yet to add anything here yet.\n try going to another place!')
		print ('options')
		
	def lake():
		print ('you arrive at the lake nearby the town. it seems calm and relaxign enough. there is a bench nearby that you take a seat on. i have yet to add anything here yet.\n try going to another place!')
		print ('options')
		
	def streets():
		print ('you wander the streets. where would you like to go from here? i have yet to add anything here yet.\n try going to another place!')
		print ('options')