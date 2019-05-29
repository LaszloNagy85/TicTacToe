# TocTacToe by Somnor and Demo

import os


def field_creation(x):
    lines_prepare = []
    for lines_counter in range(x):
        rows = []
        for rows_counter in range(x):
            rows.append(" ")
        lines_prepare.append(rows)
    return lines_prepare


def numbers_on_fields(values):
    os.system('cls||clear')
    print("Tic Tac Toe\n\n  1   2   3\n1 {0} | {1} | {2}\n  ------"
          "---\n2 {3} | {4} | {5}\n  ---------\n3 {6} | {7} | {8}\n"
          .format(field[0][0], field[1][0], field[2][0],
                  field[0][1], field[1][1], field[2][1],
                  field[0][2], field[1][2], field[2][2]))
    return


def player_input(field_list, player):
    while True:
        try:
            a = int(input(f"Player {player} give the x coordinate:"))-1
            b = int(input(f"Player {player} give the y coordinate:"))-1
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
        field_list[a][b] = "X"
    elif player == 2:
        field_list[a][b] = "O"
    return [field_list, a, b]


def win_conditions(field, a, b):
    base_a = a
    base_b = b
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
            if ((a >= 0 and b >= 0) and
               field[a][b] == field[a + 1][b + 1] == field[a + 2][b + 2]):
                return True
        except IndexError:
            pass
        a += 1
        b += 1
    a = base_a - 2
    b = base_b + 2
    for i in range(3):
        try:
            if ((a >= 0 and b >= 0) and
               field[a][b] == field[a + 1][b - 1] == field[a + 2][b - 2]):
                return True
        except IndexError:
            pass
        a += 1
        b -= 1
    return False


field_size = 4

while True:
    field = field_creation(field_size)
    player = 1
    counter = 0
    numbers_on_fields(field)
    while counter <= (field_size * field_size):
        input_return = player_input(field, player)
        field, a, b = input_return[0], input_return[1], input_return[2]
        numbers_on_fields(field)
        if win_conditions(field, a, b):
            print(f"\nPlayer {player} won the game!\n")
            break
        if player == 1:
            player = 2
        else:
            player = 1
        counter += 1
        if counter == (field_size * field_size):
            break
    if counter == (field_size * field_size):
        if input("Draw game! Would you like a rematch y/n?  ") == "y":
            continue
        else:
            break

    if counter < field_size * field_size:
        if input("Would you like a rematch y/n?  ") == "y":
            continue
        else:
            break
