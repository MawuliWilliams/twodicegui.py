


from breezypythongui import EasyFrame
from tkinter.font import Font
import random

class TwoDice(EasyFrame):

	def __init__(self):
		"""sets up the window and the widgets."""
		EasyFrame.__init__(self, title = "Two Dice Game", background = "DarkSeaGreen", resizable = False,
			width = 320, height = 240)
		# Label for the GUI title
		self.addLabel(text = "Two Dice", row = 0, column = 0, columnspan = 2, sticky = "NSEW", font = Font(family =
			"Courier", size = 30, weight = "bold"), background = "DarkSeaGreen", foreground = "black")
		#Labels and fields from the players roll
		self.addLabel(text = "Players roll is:", row = 1, column = 0, background = "DarkSeaGreen")
		self.playerRoll = self.addIntegerField(value = 0, row = 1, column = 1, state = "readonly")
		#Labels and fields from the computers roll
		self.addLabel(text = "Computers roll is:", row = 2, column = 0, background = "DarkSeaGreen")
		self.compRoll = self.addIntegerField(value = 0, row = 2, column = 1, state = "readonly")
		# the command button
		self.addButton(text = "Roll", row = 3, column = 0, columnspan = 2, command = self.playGame)
		# Label for the game final result
		self.resultArea = self.addLabel(text = "", row = 4, column = 0, columnspan = 2,  background =
		 "DarkSeaGreen", foreground = "yellow", sticky = "NSEW")


    #Event handling Method 
	def playGame(self):
	    	# Variables and constants
	    	playerDie = random.randint(1, 6)
	    	compDie = random.randint(1, 6)

	    	# Calculation phase
	    	if playerDie > compDie:
	    		result = "Congrats!  You have won!"
	    	elif compDie > playerDie:
	    		result = "Sorry, the computer wins."
	    	else:
	    		result = "We have a tie!"

	    	# Output phase
	    	self.playerRoll.setNumber(playerDie)
	    	self.compRoll.setNumber(compDie)
	    	self.resultArea["text"] = result


# definition of the main() function for program entry
def main():
	"""Instantiates and pops up the wndow."""
	TwoDice().mainloop()

# global call to trigger the main() function
if __name__ == "__main__":
	main()