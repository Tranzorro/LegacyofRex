#deaths and all the ways you can die.

#contains all the ways to die and relays the specific way you died when you die.

def death():
	print ("you have died.")
	print ("play again?")
	user = input("> ")
	if user.lower() == "yes":
		return Game()
	elif user.lower() == "no":
		sys.exit()