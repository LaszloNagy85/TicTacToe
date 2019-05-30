# TocTacToe by Somnor and Demo

import os


def field_creation():
    os.system('cls||clear')
    while True:
        x = int(input("Please choose a field size:  "))
        if x < 3:
            print("Please choose a number higher or equal to 3. Thanks")
            continue
        else:
            break
    lines_prepare = []
    for lines_counter in range(x):
        rows = []
        for rows_counter in range(x):
            rows.append(" ")
        lines_prepare.append(rows)
    return (lines_prepare, x)


def field_printing(values, x):
    os.system('cls||clear')
    print("Tic Tac Toe\n\n  ", end="")
    for i in range(1, x+1):
        print(f"{i}   ", end="")
    print("")
    for i in range(x):
        print(i+1, end= "")
        for j in range(x):
            if values[j][i] == "X":
                if j == x-1:
                    print(f"\033[31m {values[j][i]}\33[37m", end="")
                else:
                    print(f"\033[31m {values[j][i]} \33[37m|", end="")
            elif values[j][i] == "O":
                if j == x-1:
                    print(f"\033[32m {values[j][i]}\33[37m", end="")
                else:
                    print(f"\033[32m {values[j][i]} \33[37m|", end="")
            else:
                if j == x-1:
                    print(f" {values[j][i]}", end="")
                else:
                    print(f" {values[j][i]} |", end="")
        print("\n","----"*(x-1) + "---")
    return


def player_input(field_list, player):
    while True:
        try:
            a = int(input(f"Player {player} give the x coordinate: "))-1
            b = int(input(f"Player {player} give the y coordinate: "))-1
            if a < 0 or b < 0:
                print("Please use valid coordinates.")
                continue
            if field_list[a][b] != " ":
                print("Already occupied, try another one!")
                continue
            else:
                break
        except (ValueError, IndexError):
            print("Please use valid(numbers) coordinates.")
            continue
    if player == 1:
        field_list[a][b] = ("X")
    elif player == 2:
        field_list[a][b] = "O"
    return [field_list, a, b]


def win_conditions(field, a, b):
    base_a = a
    base_b = b
    if len(field) == 3:
        a = base_a - 2
        for i in range(3):
            try:
                if a >= 0 and field[a][b] == field[a + 1][b] == field[a + 2][b]:
                    return True
            except IndexError:
                pass
            a += 1
        a = base_a
        b = base_b - 2
        for i in range(3):
            try:
                if b >= 0 and field[a][b] == field[a][b + 1] == field[a][b + 2]:
                    return True
            except IndexError:
                pass
            b += 1
        a = base_a - 2
        b = base_b - 2
        for i in range(3):
            try:
                if (a >= 0 and b >= 0) and field[a][b] == field[a + 1][b + 1] == field[a + 2][b + 2]:
                    return True
            except IndexError:
                pass
            a += 1
            b += 1
        a = base_a - 2
        b = base_b + 2
        for i in range(3):
            try:
                if (a >= 0 and b >= 0) and field[a][b] == field[a + 1][b - 1] == field[a + 2][b - 2]:
                    return True
            except IndexError:
                pass
            a += 1
            b -= 1
    else:
        a = base_a - 3
        for i in range(4):
            try:
                if a >= 0 and field[a][b] == field[a + 1][b] == field[a + 2][b] == field[a + 3][b]:
                    return True
            except IndexError:
                pass
            a += 1
        a = base_a
        b = base_b - 3
        for i in range(4):
            try:
                if b >= 0 and field[a][b] == field[a][b + 1] == field[a][b + 2] == field[a][b + 3]:
                    return True
            except IndexError:
                pass
            b += 1
        a = base_a - 3
        b = base_b - 3
        for i in range(4):
            try:
                if ((a >= 0 and b >= 0) and
                   field[a][b] == field[a + 1][b + 1] == field[a + 2][b + 2] == field[a + 3][b + 3]):
                    return True
            except IndexError:
                pass
            a += 1
            b += 1
        a = base_a - 3
        b = base_b + 3
        for i in range(4):
            try:
                if ((a >= 0 and b >= 0) and
                   field[a][b] == field[a + 1][b - 1] == field[a + 2][b - 2] == field[a + 3][b - 3]):
                    return True
            except IndexError:
                pass
            a += 1
            b -= 1
    return False


def endgame_check(counter, limit):
    if counter == limit:
        if input("Draw game! Would you like a rematch y/n?  ") == "y":
            return True
        else:
            return False

    if counter < limit:
        if input("Would you like a rematch y/n?  ") == "y":
            return True
        else:
            return False


def main():
    while True:
        field, field_size = field_creation()
        limit = field_size * field_size
        player = 1
        counter = 0
        field_printing(field, field_size)
        while counter <= limit:
            field, a, b = player_input(field, player)
            field_printing(field, field_size)
            if win_conditions(field, a, b):
                print(f"\nPlayer {player} won the game!\n")
                break
            if player == 1:
                player = 2
            else:
                player = 1
            counter += 1
            if counter == limit:
                break
        if endgame_check(counter, limit):
            continue
        else:
            break
    return


main()
