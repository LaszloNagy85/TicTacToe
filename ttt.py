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

def win_conditions()


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
        try:
            if player == 1:
                try:
                    while True:
                        a = int(input("P1 Give the 1st coordinate:"))-1
                        b = int(input("P1 Give the 2nd coordinate:"))-1
                        if a == -1 or b == -1:
                            print("0 is not a valid coordinate.")
                            continue
                        else:
                            break
                except ValueError:
                    print("Please use only the coordinates of the play table!")
                    continue
                if field[a][b] == "X" or field[a][b] == "O":
                    print("already occupied, try other one")
                    continue
                os.system('cls||clear')
                field[a][b] = "X"
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
                try:
                    while True:
                        a = int(input("P1 Give the 1st coordinate:"))-1
                        b = int(input("P1 Give the 2nd coordinate:"))-1
                        if a == -1 or b == -1:
                            print("0 is not a valid coordinate.")
                            continue
                        else:
                            break
                except ValueError:
                    print("Please use only the coordinates of the play table!")
                    continue
                if field[a][b] == "X" or field[a][b] == "O":
                    print("already occupied, try other one")
                    continue
                os.system('cls||clear')
                field[a][b] = "O"
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
                    print("\nPlayer2 wonthe game!\n")
                    break
                player = 1
        except IndexError:
            print("\nPlease choose only the coordinates of the play table!\n")
    restart = input("Would you like a rematch y/n?  ")
    if restart == "y":
        continue
    else:
        break
