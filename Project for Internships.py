print("Welcome to our computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Great! Let's play! :D")
score = 0

answer = input("What does cpu stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does AMD stand for? ")
if answer.lower() == "advanced micro devices":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does IBM stand for? ")
if answer.lower() == "international business machines":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does OS stand for? ")
if answer.lower() == "operating system":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score)+ " questions correct!")
print("You got " + str((score /4) *100) + "%.")
