import random
import os
import time

# Oyun alanı boyutları
WIDTH = 10
HEIGHT = 20

# Blok şekilleri
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]]  # J
]

# Oyun alanını oluştur
board = [[0] * WIDTH for _ in range(HEIGHT)]

# Blok oluşturma işlevi
def new_block():
    shape = random.choice(SHAPES)
    x = WIDTH // 2 - len(shape[0]) // 2
    y = 0
    return shape, x, y

# Blokları çizme işlevi
def draw_board():
    os.system("cls" if os.name == "nt" else "clear")
    for row in board:
        print("".join(["█" if cell else " " for cell in row]))
    print()

# Blok hareket ettirme işlevi
def move_block(shape, x, y, dx, dy):
    if not check_collision(shape, x + dx, y + dy):
        return x + dx, y + dy
    return x, y

# Çarpışma kontrolü işlevi
def check_collision(shape, x, y):
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell and (y + i >= HEIGHT or x + j < 0 or x + j >= WIDTH or board[y + i][x + j]):
                return True
    return False

# Blok yerleştirme işlevi
def place_block(shape, x, y):
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell:
                board[y + i][x + j] = cell

# Satır temizleme işlevi
def clear_lines():
    global board
    new_board = [row for row in board if any(cell == 0 for cell in row)]
    lines_cleared = HEIGHT - len(new_board)
    new_board = [[0] * WIDTH for _ in range(lines_cleared)] + new_board
    board = new_board

def main():
    current_shape, x, y = new_block()

    while True:
        draw_board()
        time.sleep(0.5)

        x, y = move_block(current_shape, x, y, 0, 1)
        if check_collision(current_shape, x, y):
            place_block(current_shape, x, y - 1)
            clear_lines()
            current_shape, x, y = new_block()
            if check_collision(current_shape, x, y):
                print("Oyun Bitti!")
                break

if __name__ == "__main__":
    main()
