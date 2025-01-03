import random
def sum(a, b, c):
    return a + b + c


def board(aChoice, bChoice):
    zero = 'X' if aChoice[0] else 'O' if bChoice[0] else 0
    one = 'X' if aChoice[1] else 'O' if bChoice[1] else 1
    two = 'X' if aChoice[2] else 'O' if bChoice[2] else 2
    three = 'X' if aChoice[3] else 'O' if bChoice[3] else 3
    four = 'X' if aChoice[4] else 'O' if bChoice[4] else 4
    five = 'X' if aChoice[5] else 'O' if bChoice[5] else 5
    six = 'X' if aChoice[6] else 'O' if bChoice[6] else 6
    seven = 'X' if aChoice[7] else 'O' if bChoice[7] else 7
    eight = 'X' if aChoice[8] else 'O' if bChoice[8] else 8
    print(f"| {zero} | {one} | {two} |")
    print(f"|---|---|---|")
    print(f"| {three} | {four} | {five} |")
    print(f"|---|---|---|")
    print(f"| {six} | {seven} | {eight} |")


def checkWin(aChoice, bChoice):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
        ]
    for win in wins:
        if sum(aChoice[win[0]], aChoice[win[1]], aChoice[win[2]]) == 3:
            print("PLAYER A WINS")
            return 1
        if sum(bChoice[win[0]], bChoice[win[1]], bChoice[win[2]]) == 3:
            print("PLAYER B WINS")
            return 0
    return -1


if __name__ == "__main__":
    i = 0
    aChoice = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    bChoice = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1
    print("WELCOME TO THE TIC TAC TOE:")
    while True:
        board(aChoice, bChoice)
        if turn == 1:
            # a = int(input('PLAYER A:'))
            rand = random.randint(0,8)
            print(f"PLAYER A: {rand}")
            aChoice[rand] = 1
        else:
            a = int(input('PLAYER B:'))
            bChoice[a] = 1
        win = checkWin(aChoice, bChoice)
        if win != -1:
            print("GAME OVER")
            break
        if i == 8:
            print("GAME DRAW")
            break
        turn = 1 - turn
        i += 1