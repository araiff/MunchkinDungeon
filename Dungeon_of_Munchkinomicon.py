#Munchkin text adventure
line = "-----------------------------------"
prompt = "> "
#global variables to keep track of progress
fairy = False
katana = False
#clear screen?
def introduction():
	print "\n\n\n\n\n\n\n\n*****************************"
	print "* Munchkins text adventure! *"
	print "*****************************\n"
	print "Welcome to the Dungeon of the Munchkinomicon. I am your GM, Python.\nLet's get started!",
	print "Just try not to die, ok?"

def username():
	print "Who are you?"
	return raw_input(prompt)

def death(name, reason):
	print "You died because %s. What did you think would happen?" % reason
	redo(name)
	
def redo(name):
	global fairy
	global katana
	print "Try again, %s?" % name
	tryagain = raw_input(prompt)
	if "yes" in tryagain or "Yes" in tryagain:
		if name == "Cthulu":
			username
		else:
			fairy = False
			katana = False
			
			entrance(name)
	else:
		print "Until next time..."
		exit(0)

def entrance(name):
	print line
	print "As you approach the cave entrance, you feel a sense of dread and terror unlike anything you've felt before. The door is blood red with gold trim in the shape of sinister eyes."
	print "Enter?"
	enter = raw_input(prompt)
	if "yes" in enter or "Yes" in enter:
		print "You open the door and enter the dungeon."
		room1(name)
	else:
		print "Probably a wise choice. You return to your life, but you'll always wonder what grand treasure lies behind those doors..."
		redo(name)

def room1(name):
	global fairy
	global katana
	print line
	print "There are two doors, a pink door and another blood red door."
	if not fairy:
		print "There are growling sounds behind the red door."
	print "What do you do?"
	door1 = raw_input(prompt)
	if "red" in door1:
		if "katana" in door1 and katana and not fairy:
			print line
			print "You raise your katana, unsure of what lies behind the red door."
			print "A rabid yorkshire terror attacks! %s uses Katana. It's super effective!" % name
			reddoor(name)
		elif fairy:
			print line
			print "You enter the room with a red door."
			reddoor(name)
		else:
			print line
			print "You slowly open the red door. The growling gets louder and something bites your ankle!"
			death(name, "you were mauled by a rabid yorkshire terror")
	elif "pink" in door1:
		if fairy:
			print line
			print "You open the pink door and tip the Fedora of Protection at the Sparkly Good Fairy."
			fairychamber(name)
		else:
			print line
			print "You confidently open the pink door and you hear magical sounds on the other side."
			print "You think to yourself, \"What could possibly go wrong?\", as you feel yourself start to shrink."
			death(name, "you were turned into a frog by the Sparkly Good Fairy")
	elif "search" in door1 and not katana:
		print line
		print "You look around the room and notice a treasure chest in one corner and a yellow rubber ducky in another."
		print "what do you do?"
		searchaction = raw_input(prompt)
		if "duck" in searchaction:
			print line
			print "You are cursed to live the rest of your life as Ernie on Sesame Street. You should know better than to pick up a duck in a dungeon."
			death(name, "you picked up a rubber ducky in a dungeon..")
		elif "chest" or "treasure" in searchaction:
			print line
			katana = True
			print "You find a katana and attach it to your belt just like you've seen all the characters in your favorite anime do."
			print "You return your attention to the red and pink doors."
			room1(name)
	elif "exit" in door1 and "dungeon" in door1:
		print "You cannot escape!"
		room1(name)
	else:
		print "Invalid action"
		room1(name)

def reddoor(name):
	global fairy
	global katana
	print line
	print "You are now in what looks like a broom closet."
	print "What do you do?"
	redaction = raw_input(prompt)
	if "search" in redaction or "loot" in redaction and not fairy:
		print "You notice that the yorkshire terror was wearing the Fedora of Protection."
		print "Take fedora?"
		take = raw_input(prompt)
		if "yes" in take or "ok" in take:
			print line
			print "You take the fedora and put it on. You feel protected from magical spells."
			fairy = True
			reddoor(name)
		elif "no" in take:
			print line
			print "You don't take the fedora. Your head feels cold."
			reddoor(name)
		else:
			print "Invalid response."
			reddoor(name)
	elif "search" in redaction and fairy:
		print "There are only brooms in closet."
	elif "leave" in redaction or "exit" in redaction:
		print line
		print "You leave the broom closet."
		room1(name)
	else:
		print "Invalid response."
		reddoor(name)

def fairychamber(name):
	print line
	print "You are in a pink room. You look to your left and notice the Sparkly Good Fairy casting a level 20 enchanting spell on you."
	print "What do you do?"
	fairychoice = raw_input(prompt)
	if "tip" in fairychoice and "fedora" in fairychoice:
		print line
		print "You tip your fedora at the incoming spell and deflect the spell back at the Sparkly Good Fairy."
		print "M'lady."
		print "The Sparkly Good Fairy turns into a frog upon impact, revealing stairs down to the inner chamber. It glows green."
		print "You fall into a trance and find yourself walking down the stairs"
		cthuluchamber(name)
	else:
		print line
		print "The Sparkly Good Fairy successfully hits you with a level 20 enchantment spell. You turn into a frog."
		print "Hint: This is a good tip!"
		death(name, "you were turned into a frog by the SGF")

def cthuluchamber(name):
	print line
	print "You are in a room that is glowing an eerie green. You see a blood red book on a pedestal. You hear a faint chanting and blue glowing script on a stone wall on the opposite side of the room."
	print "What do you do?"
	cthuluchoice = raw_input(prompt)
	if "book" in cthuluchoice:
		print "As you approach the book, you become consumed by it's power. The madness overtakes you and you are slowly transformed, turning pinker and sparklier..."
		death(name, "you became the Sparkly Good Fairy")
	elif "dragon" in cthuluchoice or "chant" in cthuluchoice or "blue" in cthuluchoice:
		print line
		print "As you approach the glowing blue text, the chanting grows louder and louder. You learn the chant that every dragonborn must know:"
		dragonborn = raw_input(prompt)
		if dragonborn == "fus ro dah" or dragonborn == "Fus Ro Dah":
			winner(name)
		else:
			print line
			print "You become overwhelmed by the power of the shout. Did you not understand the inscription? Perhaps you are not the dragonborn afterall..."
			print "Hint: Your unrelenting will can take you through."
			death(name, "the shout of dragons overwhelmed your feeble mind")
	elif "search" in cthuluchoice:
		cthuluchamber(name)
	else:
		print "Invalid action"
		cthuluchamber(name)

def winner(name):
	print line
	print "By using unrelenting force, you break the century-long hold that the Munchkinomicon has had on this dungeon."
	print "You exit the dungeon victorious, taking with you the dreadful book. You'll be able to get a king's ransom for it."
	print "\n\nCongratulations, %s!\n\n" % name
	redo(name)
	exit(0)
	
introduction()
name = username()
if name == "Cthulu":
	print "You are awake and you swallow the earth. This dungeon is irrelevant..."
	redo(name)
	exit(0)
entrance(name)



	
