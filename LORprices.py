# dictionaries for items, armor, weapons, and pricing. lets start with basic items.
# these items will not be organized by what they apply to, simply the data will be there.
# if possible i can call the item with its value and assign it to its class and other data as need it.
#prices for common: 0-5 uncommon: 5-10 rare: 10-30 epic: 30-60 legendary: 60-200 event: 500-1000
item_price = {
"moss":1,
"rock":1,
"damaged blade":2,
"broken chest piece":3,
"broken leg piece":3,
"broken boots":3,
"piece of string":1,
"patch of fur":2,
"tossed newspaper":1,
"mushroom":3,
"mud":1,
"twig":1,
"leafs":1,
"sugar cube":2,
"apple seed":2,
"half eaten carrot":1,
"chunky vomit":5,
"damp cloth":2,
"dusty rag":1,
"rat tail":5,
"old cup":3,
"broken wand":5,
"waterlogged book":5,
"shiney object":5,
"dried blood":5,
"napkin":1,
"torn shirt":2,
"torn pants":2,
"rotting flesh":5,
"decayed bones":5,
"blade of grass":1,
"pretty flower":2,
"dead fly":1,
"insect wings":2,
"juicy apple":5,
"ripe pear":5,
"ripe banana":5,
"juicy orange":5,
"tangled plant root":2,
"ginger":3,
"wheat":3,
"broken glass":1,
"some old junk":1,
"dead bird":1,
"handfull of manuer":2,
"pen":2,
"quil":3,
"empty ink bottle":5,
"dried paint chip":1,
"piece of rust":2,
"old hat":5,
"scratched monicle":3,
"lock of hair":2,
"rope":4,
"wooden idol":5,
"statue fragment":2,
"burnt wood":1,
"tree bark":1,
"singed paper":1,
"key":5,
"hilt":7,
"scabbard":7,
"broken helm":5,
"piece of leather":3,
"chunk of coal":5,
"broken gauntlet":3,
"old knife":3,
"newt tail":3,
"salt":3,
"squishy eye ball":3,
"lizard claw":3,
"ear lobe":3,
"nasty finger":3,
"fine sand":5,
"urine sample":3,
"ink sack":3,
"still beating heart":5,
"liver":3,
"slimey organs":3,
"bottle of bile":3,
"thermometer":5,
"toad oil":3,
"grease":3,
"gun powder":3,
"leaky tear duct":5,
"shriveled gecko":3,
"creature tongue":3,
"brain matter":5,
"jewel setting":7,
"small ring":5,
"large ring":5,
"wooden bowl":3,
"pestle":5,
"morter":5,
"rusty pot":5,
"shiney kettle":5,
"slice of bacon":90,
"coffee bean":5,
"watermelon":5,
"squash":5,
"slice of half eaten pie":5,
"slice of half eaten cake":5,
"crumbly cookie":3,
"old wallet":3,
"moldy book":5,
"dried leather":5,
"piece of tin":3,
"piece of copper":3,
"pocket lint":1,
"ball of yarn":2,
"fluffy wool":2,
"towel":2,
"creepy hand":3,
"rusty dagger":5,
"rusty short sword":5,
"rusty axe":5,
"rusty chain whip":5,
"rusty spear":5,
"rusty helm":5,
"rusty legging":5,
"rusty chest piece":5,
"rusty gloves":5,
"rusty boots":5,
"rusty arrow":5,
"chipped dinner plate":1,
"half a loaf of soggy bread":2,
"bamboo stick":2,
"'smiling' frog head":3,
"odd key":5,
"glowing shard":10,
"pearl shard":10,
"amber":10,
"gold nugget":10,
"topaz":10,
"aquamarine":10,
"jade":10,
"silver nugget":10,
"iron":10,
"titanium":10,
"ruby":10,
"sapphire":10,
"emerald":10,
"cobalt":10,
"onix":10,
"diamond":10,
"tiger's eye":10,
"steel dagger":5,
"steel short sword":5,
"steel longsword":5,
"steel axe":5,
"steel spear":5,
"steel club":5,
"steel knuckles":5,
"steel katana":5,
"steel arrow":5,
"'angry' wart":5,
"flimsy sheet metal":5,
"live craw fish":2,
"wett stone":2,
"jester's stick":3,
"bell balls":1,
"fancy key":5,
"slippery slug":5,
"wiggly worm":5,
"slithering snake":5,
"peeping chick":5,
"mad moth":5,
"prety butterfly wings":5,
"crushed wings":5,
"ice cube":5,
"small pepper":5,
"large pepper":5,
"half a cake":5,
"half a pie":5,
"yummy cookie":5,
"loaf of bread":5,
"fancy cup":7,
"fancy bowl":7,
"fancy dinner plate":7,
"glowing flower":7,
"glowing mushroom":7,
"glowing rock":7,
"shiney ring":7,
"shiney monical":7,
"pircing stud":7,
"glass cutter":7,
"cat ears":7,
"giant seed":7,
"pointy stick":7,
"glowing orb":7,
"blazing gem":7,
"cold gem":7,
"tingly gem":7,
"whisteling gem":7,
"heavy gem":7,
"soaked gem":7,
"floating gem":7,
"laughing hilt":7,
"hot scabbard":7,
"cold blade":7,
"tinlgy guard":7,
"bloodsoaked tassle":7,
"pulsating jewel":7,
"floating straps":7,
"stick":7,
"juicy steak recipe":7,
"easter egg basket":7,
"full pie":6,
"full cake":6,
"giant cookie":5,
"gold statue idol":5,
"shiney plaque":1,
"store discount ticket":1,
"friendship gifts":1,
"heroic trophies":1,
"hot rock":1,
"hot flower":1,
"hot mushroom":1,
"cold rock":1,
"cold mushroom":1,
"cold flower":1,
"tingly rock":1,
"tingly flower":1,
"tingly mushroom":1,
"whisteling rock":1,
"whisteling flower":1,
"whisteling mushroom":1,
"heavy rock":1,
"heavy flower":1,
"heavy mushroom":1,
"soaked rock":1,
"soaked flower":1,
"soaked mushroom":1,
"jester's hat":1,
"jester's chest piece":1,
"jester's pants":1,
"jester's boots":1,
"jester's gloves":1,
"pointy object":1,
"telescope":1,
"apple":1,
"orange":1,
"pear":1,
"squash":1,
"banana":1,
"grapes":1,
"glass of milk":1,
"glass of whine":1,
"glass of water":1,
"glass of beer":1,
"jar of honey":1,
"jar of oil":1,
"jar of jelly":1,
"jar of tree sap":1,
"plate of cake":1,
"plate of pie":1,
"sammich":1,
"walnut":1,
"buttered toast":1,
"chicken fillet":1,
"fish fillet":1,
"spaghetti":1,
"soup":1,
"pumpkin pie":1,
"turkey dinner":1,
"fruit cake":1,
"glass of lemonade":1,
"glass of orange juice":1,
"muffin":1,
"donut":1,
"truffles":1,
"waffles":1,
"potions":1,
"infusions":1,
"candles":1,
"ointments":1,
"remedies":1,
}

armor_price = {
"singing armor":1,
"molten phoenix armor":1,
"wrath armor":1,
"morph armor":1,
"giants armor":1,
"tsunami armor":1,
"cursed armor":1,
"demon armor":1,
"angel armor":1,
"beast armor":1,
"magic armor":1,
"shadow armor":1,
"gravity armor":1,
"steampunk god armor":1,
"maids uniform":1,
"butler suit":1,
"fancy tie":1,
"top hat":1,
"artemis' hooded cloak":1,
"Henguls' cursed rings":1,
"chain armor":1,
"half plate armor":1,
"full plate armor":1,
"scale armor":1,
"glowing earring":1,
"cloth armor":1,
"vanity armor":1,
"piercings":1,
}

weapon_price = {
"cursed sword":1,
"immortals sword":1,
"incendiary weapons":1,
"lunar hammer":1,
"crystal morph stick":1,
"rubber chicken weapon":1,
"holloween scepter of souls":1,
"christmas spear of bone chilling":1,
"lucky whip of coins":1,
"4th of july exploding sword":1,
"lit candlestick staff":1,
"blacksmithing hammer":1,
"tailors threading needle":1,
"mining pick":1,
"jester's 'balls'":1,
}