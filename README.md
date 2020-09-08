"HOW TO OPEN THE PROGRAM"

"Download the zipped setGame folder (all python files were built with Python version 3.8), for ease I would reccommend having it download to your desktop since that is where I will explain how to access it (If you do decide to download the folder somewhere else, these instructions will not be exact, but you can mimic the commands to get to where you have it saved.) Next go into your Terminal if you are on a Mac or Command Prompt if you are on Windows.  You should be able to find the Terminal by going into your Utilities folder under Applications.  For windows I go into my search bar next to the Windows Icon in the bottom left corner of my screen, and type in Command Prompt.  We will have to do one more thing before we locate the folder we downloaded.

For me, when I open Command Prompt my location in C:/Users/ashe>, yours will be different.  First type in pip install Pillow , it will be needed to run the game later.  Your line should look something like: C:/Users/ashe>pip install Pillow  .After that goes through we are ready to work towards the location of our setGame folder. I have the folder downloaded to my desktop, so our next step is to: cd Desktop  If at any point you are lost or don't know where to go next, you can type in dir which will show you the files available at your given level.  If you accidently went into something and want to go back you can type in cd..\ for Command Prompt or cd- for Terminal to go back a level"

"Your location should now say, in my case, C:/Users/ashe/Desktop> , we want to do this again to go into the folder we just downloaded. So cd setGame , and now we are at: C:/Users/ashe/Desktop/setGame> At this point we are ready to play the game.  Now type in: python gui.py , the whole line of Command Prompt will look like this: C:Users/ashe/Desktop/setGame>python gui.py  This will open up a pop up window with the game.  Click the New Game button and the grid will come alive with all the cards.  As you play the game you can select and deselect the cards by clicking on them.  There is also a Quit Game button which will close the program at any point when you click it.  And there is also a Check # Sets button if you are ever curious or forget how many sets you have completed."


"RULES FOR SET"

"There are different characteristics each of the cards can have: three different colors (red, green, and blue), three different shades (clear, lined, solid), three different shapes (oval, rectangle, diamond), and three different numbers of shapes (one, two, three)"
"The goal of the game is to form as many sets as possible.  In order to form a set, you must select three cards from the available 12 cards on the board.  You will keep trying to form sets of 3 until the cards run out in the deck, there are no possible sets left of the available cards, or until you decided to quit the game.  If throughout the game, there are no possible sets, three of the cards on the board will be replaced with new cards and there will be a message at the top of the window that says Redrawing"


"WAYS TO FORM SETS"

"If three of the characteristics of the cards are the same, and one is different, that is considered a set.  For exammple, one card was two red clear ovals, the next was two red lined ovals, and the last two red solid ovals.  All three have the same shape, the same color, the same number of symbols, but different shadings."

"Another type of set is when three of the chracteristics are different, and one is the same.  For example, one card is one green lined rectangle, the next is two blue lined ovals, and the last is three red lined diamonds.  All three have different shapes, different colors, different number of symbols, but they all have the same shading."

"The last type of set you can form is if all the cards are completely different.  They must have all different colors, all different shading, all different shapes, and each card must have a different number of symbols.  For example, one card is one blue lined oval, the next is two green solid diamonds, and the last is three red clear rectangles."
