from pygame import *
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
font = pygame.font.Font (None, 25)
stat_font = pygame.font.Font (None, 25)
logo_font = pygame.font.Font ("C:/Windows/Fonts/impact.ttf", 80)
map_font = pygame.font.Font ("C:/Windows/Fonts/impact.ttf", 25)
#everything in this file controles what shows up on the screen.
class Screen_stats():
	def __init__(self):
		self.Name = stat_font.render("Name: " + self.name , True, white) #limit all names by 18 characters
		self.Hp = stat_font.render("HP: " + "this should ", True, white)
		self.Mp = stat_font.render("MP: " + "100", True, white)
		self.Def = stat_font.render("Def: " + "1", True, white)
		self.Atk = stat_font.render("Atk: " + "3", True, white)
		self.San = stat_font.render("San: " + "100", True, white)
		self.Sta = stat_font.render("Sta: " + "100", True, white)
		self.Status1 = stat_font.render("Status: " + "tox" + "bur" + "cur" + "pet" + "slw", True, white)
		self.Status2 = stat_font.render("ice" + "bli" + "zom" + "par" + "sho" + "ins", True, white)
		self.Path = stat_font.render("Path: " + "theif", True, white)
		self.Head = stat_font.render("Head: " + "Headpiece of epicness", True, white) #limit item names for this slot to 22 characters
		self.Chest = stat_font.render("Chest: " + "Chestpiece of epicness", True, white) # limit names to 22
		self.Legs = stat_font.render("Legs: " + "Legplates of epicness", True, white) # limit names to 23
		self.Feet = stat_font.render("Feet: " + "Boots of asskicking", True, white) #limit names to 23
		self.Lhand = stat_font.render("Lhand: " + "fist of fisting", True, white) # limit names to 23
		self.Rhand = stat_font.render("Rhand: " + "fist of fisting", True, white) # limit names to 23
class ScreenText():


class Player1(self,Screen_stats):
	def __init__(self):
		def __init__(Base_stats):

class Player2(self,Screen_stats):

class Player3(self,Screen_stats):

class Player4(self,Screen_stats):
