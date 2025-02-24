def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Satırları kontrol et
    for row in board:
        if all(s == player for s in row):
            return True
    # Sütunları kontrol et
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    # Çaprazları kontrol et
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(all(cell != " " for cell in row) for row in board)

def xox():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, row (0, 1, 2): "))
        col = int(input(f"Player {current_player}, col (0, 1, 2): "))

        if board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Cell is already taken, try again.")

def xoxmenu():
    while True:
        print("╔════════════════════════════════════════╗")
        print("║                                        ║")
        print("║                XOX                     ║")
        print("║                                        ║")
        print("║         1-Oyunu Başlat                 ║")
        print("║         2-Çıkış                        ║")
        print("║                                        ║")
        print("╚════════════════════════════════════════╝")

        secim = input("Seçiminiz nedir? ")
        if secim == "1":
            xox()
        elif secim == "2":
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    xoxmenu()