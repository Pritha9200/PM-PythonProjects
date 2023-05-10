# Quiz Game Project
print("Welcome to my computer quiz!")

playing=input("Do you want to play ? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score=0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does WHO stand for? ")
if answer.lower() == "world health organization":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does PHD stand for? ")
if answer.lower() == "doctor of philosophy":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does MBA stand for? ")
if answer.lower() == "master of business administration":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does UPSC stand for? ")
if answer.lower() == "union public services commission":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does ORS stand for? ")
if answer.lower() == "oral rehydration solution":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

answer = input("What does NCERT stand for? ")
if answer.lower() == "national council of educational research and training":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

print("You got "+ str(score) + " questions correct!")
print("You got "+ str((score/10)*100) + "%")