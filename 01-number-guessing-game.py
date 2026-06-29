import random
comp=random.randint(1,100)
tries=0
while True:
    human=int(input("What is your guess:"))
    tries+=1
    if human==comp:
        print(f"Congrats! you won in {tries} tries")
        break
    elif tries==5:
        print("Game over, Play again")
        break
    elif human>comp:
        print("High guess go lower")
    elif human<comp:
        print("Low guess go higher")