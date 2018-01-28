player = " "

def playIntro(player):

        print ("Holly: Welcome to the Total Immersion Video Game Red Dwarf. Who would you like to play as? (Type the character name below)")

        print ("Lister - Human")
        print ("Rimmer - Hologram")
        print ("Kryten - Android")
        print ("Cat - Cat")
        player = input()
        return player

def confirmPlayer(player):

        #Choose's Lister	
        if player == str("Lister"):
                print ("Are you sure you want to play as the semi illiterate space bum? Y or N")
                answer = input()

                if (answer == "y") or (answer == "Y"):
                        listersStory()
                else:
                        playIntro()
				
        #Choose's Rimmer
        if player == str("Rimmer"):
                print ("Are you sure you want to play as a man so was acquitted of mass murder on the basis that he is an idiot? Y or N")
                answer = input()

                if (answer == "y") or (answer == "Y"):
                        print ("Well you can't, I haven't written it yet")
                        playIntro()
                else:
                        playIntro()
				
        #Choose's Kryten
        if player == str("Kryten"):
                print ("Are you sure you want to play as the android? This is an adventure game you know and he's very obsessed with cleaning. Y or N")
                answer = input()

                if (answer == "y") or (answer == "Y"):
                        print ("Well you can't, I haven't written it yet")
                        playIntro()
                else:
                        playIntro()
	
	#Choose's Cat
        if player == str("Cat"):
                print ("Are you sure you want to play as the self obsessed feline that is the Cat? Y or N")
                answer = input()

                if (answer == "y") or (answer == "Y"):
                        print ("Well you can't, I haven't written it yet")
                        playIntro()
                else:
                        playIntro()

print ("Type help to see a list of example commands")
		
#Lister's story
def listersStory():

        print ("Holly: You are Dave Lister. You are approximately 3 million years old and have the body of a 55 year old. Your mission to find Kochanski and get back to Earth has not been going well.")

        print ("Holly: Time to wake up Dave.")

        print ("You awake with the hangover from hell, somewhere in the bowels of the ship. It is very dark.")

        print ("To progress in the story try typing commands or you can ask Holly to help")


player = playIntro(player)
confirmPlayer(player)


