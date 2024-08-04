print("Welcome to the Quizgame")

player = input("Do you want to play:")

if player.lower() != "yes":
    quit()

print(" ok lets play")
score = 0

question = input("How many days in a week?\n")
if question.lower() == "seven":
    print("Correct")
    score += 1
else:
    print("Correct ans is:seven")

question = input("which is the national bird of india\n")
if question.lower() == "peacock":
    print("Correct")
    score += 1
else:
    print("Correct ans is:peacock")

question = input("Which is the fastest animal on land?\n")
if question.lower() == "cheetah":
    print("Correct")
    score += 1
else:
    print("Correct ans is:cheetak")        

question = input("Which is the largest ocean in the world?\n")
if question.lower() == "pacific ocean":
    print("Correct")
    score += 1
else:
    print("Correct ans is:pacific ocean")

question = input("In which direction does the sun rise?\n")
if question.lower() == "east":
    print("Correct")
    score += 1
else:
    print("Correct ans is:east")

print("Your score is : " + str(score))    