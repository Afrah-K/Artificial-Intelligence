board = [' ' for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i + 1]} | {board[i + 2]}")
        if i < 6:
            print("-" * 9)
def check_win(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)
def is_board_full():
    return ' ' not in board
def minimax(board, depth, is_maximizing):
    scores = {'X': 1, 'O': -1, 'tie': 0}
    if check_win('X'):
        return scores['X']
    if check_win('O'):
        return scores['O']
    if is_board_full():
        return scores['tie']

    best_eval = -float('inf') if is_maximizing else float('inf')
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X' if is_maximizing else 'O'
            eval = minimax(board, depth + 1, not is_maximizing)
            board[i] = ' '
            best_eval = max(best_eval, eval) if is_maximizing else min(best_eval, eval)
    return best_eval
def ai_move():
    best_move, best_eval = -1, -float('inf')
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            eval = minimax(board, 0, False)
            board[i] = ' '
            if eval > best_eval:
                best_eval, best_move = eval, i
    return best_move
while True:
    print_board() 
    while True:
        try:
            human_move = int(input("Enter your move (1-9): ")) - 1
            if board[human_move] == ' ':
                board[human_move] = 'O'
                break
            else:
                print("Invalid move. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter a number from 1 to 9.")

    if check_win('O'):
        print_board()
        print("Congratulations! You win!")
        break
    elif is_board_full():
        print_board()
        print("It's a tie!")
        break

    ai_best_move = ai_move()
    board[ai_best_move] = 'X'

    if check_win('X'):
        print_board()
        print("AI wins! Better luck next time.")
        break
