import random # importing random module

def checkInputs(user, comp):
    if user == comp:
        return 0
    elif user == 0 and comp == 1:
        return 2
    elif user == 2 and comp == 0:
        return 2
    elif user == 1 and comp == 2:
        return 2
    return 1

if __name__ == "__main__":

    print("Welcome to WATER 0, GUN 1, SNAKE 2")
    i = 0
    while True:
        try:
            comp = random.randint(0, 2) # generating random num between (0,2) for comp chance
            user = int(input("Enter your choice (0, 1, 2): "))
            if user not in [0, 1, 2]:
                raise ValueError("Invalid input")
            print(f"USER: {user}--COMPUTER: {comp}")
            result = checkInputs(user, comp)
            if result == 0:
                print("DRAW")
            elif result == 1:
                print("COMP WIN")
            else:
                print("YOU WIN")
            i += 1
            if i == 9:
                break
        except ValueError:
            print("Please enter a valid input (0, 1, or 2)")