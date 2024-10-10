# Створення матриці 8х8 з пустими клітинками
chessboard = [['_' for _ in range(8)] for _ in range(8)]

# Розставлення тур по кутках таблиці
chessboard[0][0] = 'R'
chessboard[0][7] = 'R'
chessboard[7][0] = 'R'
chessboard[7][7] = 'R'

# Виведення шахівниці
for row in chessboard:
    print(' '.join(row))

