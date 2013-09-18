import cmd
from room import get_room
import textwrap
import shutil
import tempfile

class Game(cmd.Cmd):
	def __init__(self):
		cmd.Cmd.__init__(self)

		self.dbfile = tempfile.mktemp()
		shutil.copyfile("game.db", self.dbfile)

		self.loc = get_room(41, self.dbfile)
		self.printroom()

	def move(self, dir):
		newroom = self.loc._neighbor(dir)
		if newroom is None:
			print ("sorry, can't go that way.")
		else:
			self.loc = get_room(newroom, self.dbfile)
			self.printroom()

		if newroom == 82 or 83 or 84:
			print ("sorry, have nothing made for this location yet, so you died from a random flying boulder with a splat!")
			self.dead

	def printroom(self):
		print(self.loc.name)
		print("")
		for line in textwrap.wrap(self.loc.description, 72):
			print(line)

	def do_up(self, args):
		"""go up"""
		self.move('up')

	def do_down(self, args):
		"""go down"""
		self.move('down')

	def do_north(self, args):
		"""go north"""
		self.move('north')

	def do_east(self, args):
		"""go east"""
		self.move('east')

	def do_south(self, args):
		"""go south"""
		self.move('south')

	def do_west(self, args):
		"""go west"""
		self.move('west')

	def do_quit(self, args):
		"""leaves the game"""
		print("goodbye")
		return True

	def do_save(self, args):
		"""saves the game"""
		shutil.copyfile(self.dbfile, args)
		print ("The game was saved to {0}".format(args))

	def dead(self):
		"""you died, this is game over!"""
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
			self.do_quit

if __name__ == "__main__":
	g = Game()
	g.cmdloop()