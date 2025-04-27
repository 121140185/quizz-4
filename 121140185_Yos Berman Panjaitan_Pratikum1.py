import random

# Buat papan
board = [['?' for _ in range(3)] for _ in range(3)]

# Tentukan posisi bom secara acak
bomb_row = random.randint(0, 2)
bomb_col = random.randint(0, 2)

# Untuk menyimpan jumlah kotak aman yang sudah dibuka
safe_spots_opened = 0
total_safe_spots = 8  # 9 kotak - 1 bom

def print_board():
    for row in board:
        print(' '.join(row))
    print("="*40)

# Game loop
while True:
    print_board()
    try:
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue

        if board[row][col] != '?':
            print("This spot is already opened. Try another one.")
            continue

        if row == bomb_row and col == bomb_col:
            board[row][col] = 'X'
            print_board()
            print("Boom! Kamu kalah!")
            break
        else:
            board[row][col] = 'O'
            safe_spots_opened += 1
            if safe_spots_opened == total_safe_spots:
                print_board()
                print("Selamat! Kamu menang!")
                break
            else:
                print("Well, there's no bomb here. Congrats!")

    except ValueError:
        print("Invalid input. Please enter a number.")

