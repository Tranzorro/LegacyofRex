#deaths and all the ways you can die.
import sys
import os
#contains all the ways to die and relays the specific way you died when you die.
def Death():
		print ("      _____          _____        ______  _______        ______   ")
		print ("  ___|\    \     ___|\    \      |      \/       \   ___|\     \  ")
		print (" /    /\    \   /    /\    \    /          /\     \ |     \     \ ")
		print ("|    |  |____| |    |  |    |  /     /\   / /\     ||     ,_____/|")
		print ("|    |    ____ |    |__|    | /     /\ \_/ / /    /||     \--'\_|/")
		print ("|    |   |    ||    .--.    ||     |  \|_|/ /    / ||     /___/|  ")
		print ("|    |   |_,  ||    |  |    ||     |       |    |  ||     \____|\ ")
		print ("|\ ___\___/  /||____|  |____||\____\       |____|  /|____ '     /|")
		print ("| |   /____ / ||    |  |    || |    |      |    | / |    /_____/ |")
		print (" \|___|    | / |____|  |____| \|____|      |____|/  |____|     | /")
		print ("   \( |____|/    \(      )/      \(          )/       \( |_____|/ ")
		print ("    '   )/        '      '        '          '         '    )/    ")
		print ("        '                                                   '     ")
		print ("                                                                  ")
		print ("        _____     ____      ____      ______        _____         ")
		print ("   ____|\    \   |    |    |    | ___|\     \   ___|\    \        ")
		print ("  /     /\    \  |    |    |    ||     \     \ |    |\    \       ")
		print (" /     /  \    \ |    |    |    ||     ,_____/||    | |    |      ")
		print ("|     |    |    ||    |    |    ||     \--'\_|/|    |/____/       ")
		print ("|     |    |    ||    |    |    ||     /___/|  |    |\    \       ")
		print ("|\     \  /    /||\    \  /    /||     \____|\ |    | |    |      ")
		print ("| \_____\/____/ || \ ___\/___ / ||____ '     /||____| |____|      ")
		print (" \ |    ||    | / \ |   ||   | / |    /_____/ ||    | |    |      ")
		print ("  \|____||____|/   \|___||___|/  |____|     | /|____| |____|      ")
		print ("     \(    )/        \(    )/      \( |_____|/   \(     )/        ")
		print ("      '    '          '    '        '    )/       '     '         ")
		print ("                                         '                        ")
		print ("you have died.")
		print ("play again?")
		user = input("> ")
		if user.lower() == "yes":
			return LOR.Game()
		elif user.lower() == "no":
			os.system('cls')
			sys.exit()