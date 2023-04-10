"""
Let's imagine a chessboard, the squares on which are marked with coordinates.
The coordinates are numbers between 1 and 8 inclusively.
The first number indicates a column, the second one indicates a row.

Chessboard coordinates

The chess king can stand on any square and can move one step horizontally,
vertically, or diagonally in any direction within the board.

The input will contain the coordinates on which the king is located.
ou should figure out and print how many moves the figure can make:
for example, from the position (1, 8), the king can make only 3 moves (right, down, diagonally).
"""

columna = int(input())
fila = int(input())

if 2 <= columna <= 7 and 2 <= fila <= 7:
    print(8)
elif 2 <= columna <= 7 and (fila == 1 or fila == 8):
    print(5)
elif (columna == 1 or columna == 8) and (fila == 1 or fila == 8):
    print(3)
else:
    print(5)