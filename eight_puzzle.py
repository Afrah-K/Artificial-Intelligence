import random

def initialize_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, ' ']
    random.shuffle(board)
    return board

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], '|', board[i + 1], '|', board[i + 2])
        if i < 6:
            print('---------')

def is_solved(board):
    return board == [1, 2, 3, 4, 5, 6, 7, 8, ' ']

def find_empty_space(board):
    return board.index(' ')

def perform_move(board, direction):
    empty_index = find_empty_space(board)

    if direction == 'left' and empty_index % 3 != 2:
        board[empty_index], board[empty_index + 1] = board[empty_index + 1], board[empty_index]
    elif direction == 'right' and empty_index % 3 != 0:
        board[empty_index], board[empty_index - 1] = board[empty_index - 1], board[empty_index]
    elif direction == 'up' and empty_index < 6:
        board[empty_index], board[empty_index + 3] = board[empty_index + 3], board[empty_index]
    elif direction == 'down' and empty_index > 2:
        board[empty_index], board[empty_index - 3] = board[empty_index - 3], board[empty_index]

def main():
    board = initialize_board()
    print("Welcome to the 8-Puzzle Game!")

    while True:
        print_board(board)

        if is_solved(board):
            print("Congratulations! You've solved the puzzle!")
            break

        direction = input("Enter a move (left, right, up, down): ").strip().lower()
        if direction in ['left', 'right', 'up', 'down']:
            perform_move(board, direction)
        else:
            print("Invalid move. Use 'left', 'right', 'up', or 'down'.")

if __name__ == "__main__":
    main()
