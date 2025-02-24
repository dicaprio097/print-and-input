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

# Tetris oyununu başlatma işlevi
def start_tetris():
    global board
    board = [[0] * WIDTH for _ in range(HEIGHT)]
    shape, x, y = new_block()
    while True:
        draw_board()
        time.sleep(0.5)
        # Blok hareketi ve kontrolü burada yapılacak
        # Bu örnekte sadece basit bir çizim gösteriliyor
        y += 1
        if y + len(shape) > HEIGHT:
            break
    print("Oyun bitti!")

# Tetris menüsü
def tetrismenu():
    while True:
        print("╔════════════════════════════════════════╗")
        print("║                                        ║")
        print("║                TETRIS                  ║")
        print("║                                        ║")
        print("║         1-Oyunu Başlat                 ║")
        print("║         2-Çıkış                        ║")
        print("║                                        ║")
        print("╚════════════════════════════════════════╝")

        secim = input("Seçiminiz nedir? ")
        if secim == "1":
            start_tetris()
        elif secim == "2":
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    tetrismenu()