#TocTacToe by Somnor and Demo

import os


def field_creation(x):
    lines_prepare = []
    for lines_counter in range(field_size):
        rows = []
        for rows_counter in range(field_size):
            rows.append(" ")
        lines_prepare.append(rows)
    return lines_prepare


def player_input(field_list, player):
    while True:
        try:
            a = int(input(f"Player{player} Give the x coordinate:"))-1
            b = int(input(f"Player{player} Give the y coordinate:"))-1
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
    return field_list



#def win_conditions()


field_size = 3

while True:
    os.system('cls||clear')
    field = []
    field = field_creation(field_size)
    player = 1
    a = ""
    b = ""
    print("Tic Tac Toe\n\n  1   2   3\n1 {0} | {1} | {2}\n  ---------\n2 "
          "{3} | {4} | {5}\n  ---------\n3 {6} | {7} | {8}\n"
          .format(field[0][0], field[1][0], field[2][0],
                  field[0][1], field[1][1], field[2][1],
                  field[0][2], field[1][2], field[2][2]))
    while True:
        if player == 1:
            field = player_input(field, player)
            os.system('cls||clear')
            print("Tic Tac Toe\n\n  1   2   3\n1 {0} | {1} | {2}\n  ------"
                    "---\n2 {3} | {4} | {5}\n  ---------\n3 {6} | {7} | {8}\n"
                    .format(field[0][0], field[1][0], field[2][0],
                            field[0][1], field[1][1], field[2][1],
                            field[0][2], field[1][2], field[2][2]))
            if ((field[0][0] == field[0][1] == field[0][2] == "X") or
                (field[1][0] == field[1][1] == field[1][2] == "X") or
                (field[2][0] == field[2][1] == field[2][2] == "X") or
                (field[0][0] == field[1][0] == field[2][0] == "X") or
                (field[0][1] == field[1][1] == field[2][1] == "X") or
                (field[0][2] == field[1][2] == field[2][2] == "X") or
                (field[0][0] == field[1][1] == field[2][2] == "X") or
                (field[0][2] == field[1][1] == field[2][0] == "X")):
                print("\nPlayer1 won the game!\n")
                break
            player = 2
        else:
            field = player_input(field, player)
            os.system('cls||clear')
            print("Tic Tac Toe\n\n  1   2   3\n1 {0} | {1} | {2}\n  ------"
                    "---\n2 {3} | {4} | {5}\n  ---------\n3 {6} | {7} | {8}\n"
                    .format(field[0][0], field[1][0], field[2][0],
                            field[0][1], field[1][1], field[2][1],
                            field[0][2], field[1][2], field[2][2]))
            if ((field[0][0] == field[0][1] == field[0][2] == "O") or
                (field[1][0] == field[1][1] == field[1][2] == "O") or
                (field[2][0] == field[2][1] == field[2][2] == "O") or
                (field[0][0] == field[1][0] == field[2][0] == "O") or
                (field[0][1] == field[1][1] == field[2][1] == "O") or
                (field[0][2] == field[1][2] == field[2][2] == "O") or
                (field[0][2] == field[1][1] == field[2][0] == "O") or
                (field[0][0] == field[1][1] == field[2][2] == "O")):
                print("\nPlayer2 won the game!\n")
                break
            player = 1

    if input("Would you like a rematch y/n?  ") == "y":
        continue
    else:
        break
