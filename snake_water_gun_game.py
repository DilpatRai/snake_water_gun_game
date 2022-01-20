
import random
def game_win(computer, you):
    if computer==you:
        return None
    elif computer == "s":
        if you=="w":
            return False
        elif you=="g":
            return True
    elif computer=="w":
        if you=="g":
            return False
        elif you=="s":
            return True
    elif computer=="g":
        if you=="w":
            return True
        elif you=="s":
            return False
        
print("computer's turn: gun(g), snake(s), water(w)!!!  ")
random_number = random.randint(1, 3)
if random_number == 1:
    computer = "s"
elif random_number == 2:
    computer = "g"
elif random_number == 3: 
    computer = "w"
you = input("your's turn: snake(s), water(w), gun(g) ?")
decision = game_win(computer, you)
print(f"computer choosed {computer}")
print(f"you choosed {you}")
if decision == None:
    print("Tie!!")
elif decision:
    print("you win")
else:
    print("you loose")