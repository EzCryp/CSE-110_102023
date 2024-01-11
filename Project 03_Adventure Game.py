"""""
Author: Ezra Zacarias
Purpose: Create a text-base-adventure game
""""" 

# To start, we are going to create a prompt question variable that will hold the players answers throughout the game
answer = input("Welcome to EZ Adventure Game! \n\nWould you like to play? (YES / NO)\n").upper().strip()

# the first if - elif - else statement and the 1st prompt question
if answer == "YES":
    print()
    print("Let's Go Play!\n")
    
    answer = input('You and your friend Mike, finds yourself walking together in a dark and weary misty woods. As you walk, you come into a cross road,\nan intersection and you have to decide whether to chose LEFT or RIGHT. Which way do you want to go? \n').upper().strip()
        
# 1st level scenario
    if answer == "LEFT":
        print()
        print("You chose to go to the \"left\", and as you turn, you see that the path has closed behind you. \n\n...Strange, but you keep walking.\n")
        answer = input("Mike on the other hand sees up a sign up ahead saying: \"Adventure Bay --> this way\". \n\nYou feel like something is not right about it. Do you follow the sign? (YES / NO) \n").upper().strip()
    
# 2nd level scenario
# if the choice is yes, game over
        if answer == "YES":
            print()
            print("Bad idea, always trust your instinct! As you follow the sign, you seem to get impossibly sleepy. \nYou can't even keep your eyes open. You and Mike see a nice patch of grass up ahead and decide to lie down. \nExcept the patch of grass isn't grass and instead you are now falling. \nI guess you are on another adventure now... \n\nGame over!!!")
# if however the answer is no, go to the next level of the game    
        elif answer == "NO":
            print()
            print("You're a natural, good job sticking with your instincts. \n\nYou and Mike keep traveling the way you were and eventually come across a mysterious House. \n\nBut what is that, that you hear? ...A Bear?")
            answer = input("\nDo you want to go inside the house to find out what's in there? (YES / NO or OBSERVE)\n").upper().strip()
# 3rd level scenario
            if  answer == "YES":
                print()
                print("You enter the house, and as you enter a bear jump into you and eat you! \n\nYou died! =( \n\nGame Over!!!)")
            elif answer == "NO":
                print()
                print("Now what!? You and Mike have to run or else a Bear might get hold on you and eat you. \n\nIt's seems like You and Mike are on for a new adventure up ahead!")
            elif answer == "OBSERVE":
                print()
                print("Before you even move you decided to wait and observe the surroundings, \n\nGreat choice! \n\nA grizzly bear just past by and went inside the house.")
                answer = input("\nDespite seeing the bear that went inside the house, do you still want to GO IN or RUN AWAY\n").upper()
# 4th level scenario
                if answer == "GO IN":
                    print()
                    print("You enter the house, and as you are going in a bear jump into you and eat you! \n\nYou died! =( \n\nGame Over!!!)")
                elif answer == "RUN AWAY":
                    print()
            
                    print("Now what!? You and Mike have to run or else a Bear might get hold on you and eat you. \n\nIt's seems like You and Mike are on for a new adventure up ahead!")
                else:
                    print()
                    print("Kindly check your input, there might be a typographical error \n\nPlease try one more time!")
            else:
                print()
                print("Kindly check your input, there might be a typographical error \n\nPlease try one more time!")
        else:
            print()
            print("Kindly check your input, there might be a typographical error \n\nPlease try one more time!")
    if answer == "RIGHT":
        print()
        print("As you turn \'right\', there you got caught in a trap, where you won't be able to go out\nI am sorry!This time choosing right is not the best option =( \n\nGame Over!!!")

elif answer == "NO":
        print()
        print("I hate to see you go. \n\nIt's been nice playing with you, even for a short while. \n\nAnyways, till next time \n\nCIAO!")

else:
    print()
    print("Kindly check your input, there might be a typographical error \n\nPlease try one more time!")