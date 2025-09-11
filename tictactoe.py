from random import randrange

board = [[1,2,3],
         [4,5,6],
         [7,8,9]
         ]
free_list = []

def display_board(board):
    for row in board:
        for number in row:
            print("+-------")
            print("|       |")
            print(f"|", {number},  sep=" | ")
            print("|       |")

def make_list_of_free_fields(board):
    for row in board:
        for number in row:
            if number != 'X' and number != 'O':
                free_list.append(number)
    return free_list

def enter_move(board):
    while True:
        user_choice = int(input("Enter you move: \n"))
        if user_choice not in free_list:
            print("please select a valid move")
        else:
            #currently assumes the list is 2d not 3x3
            position = board.index(user_choice)
            board[position] = 'O'
            return board
    




first_move = 'X'
board[1][1] = first_move
display_board(board)
make_list_of_free_fields(board)

while len(free_list) > 0:
    enter_move(board)




