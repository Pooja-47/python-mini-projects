import random 
print("Choices are:\n1 for Rock\n2 for Paper\n3 for scissor\n")
compP=0
humanP=0
draw=0
game_count=1
while True:
    comp=(random.randint(1,3))
    human=int(input("Enter your choice from above choices:"))

    print(f"Computer chose {comp} and you chose {human} so")

    if human<1 or human>3:
        print("Invalid choice, choose again.")

    elif comp==human:
        print("Draw! choose again\n")
        draw+=1
        if draw==3:
            print("Next Round, scores reset to 0 \n")
            game_count+=1
            compP=0
            humanP=0
            draw=0

    elif (comp==1 and human==2) or (comp==2 and human==3) or (comp==3 and human==1):
        print("Computer lose and you get this point.\n")
        humanP=humanP+1
        draw=0
        print(f"Your points = {humanP}\nComputer points = {compP}")

        if humanP==5:
            break

    elif (comp==2 and human==1) or (comp==3 and human==2) or (comp==1 and human==3):
        print("You lose and computer get this point.\n")
        compP=compP+1
        draw=0
        print(f"Your points = {humanP}\nComputer points = {compP}")

        if compP==5:
            break

print(f"Total rounds= {round}")   
if compP==5:
    print(f"Computer won with {compP} points")
elif humanP==5:
    print(f"You won with {humanP} points")