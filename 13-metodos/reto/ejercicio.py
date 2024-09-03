chess_board = [
['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]
print("chess_board")
for valor in chess_board:
    print("\t", valor, end=" ")
    print()

# movimiento del caballo
chess_board[7][1] = 0 # Casilla original del caballo ahora está vacía
chess_board[5][2] = 'N' # Nueva posición del caballo
print("chess_board despues de movimiento caballo")
for valor in chess_board:
    print("\t", valor, end=" ")
    print()

#Ejemplo: Tablero de Damas
checkers_board = [
[0, 'b', 0, 'b', 0, 'b', 0, 'b'],
['b', 0, 'b', 0, 'b', 0, 'b', 0],
[0, 'b', 0, 'b', 0, 'b', 0, 'b'],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
['w', 0, 'w', 0, 'w', 0, 'w', 0],
[0, 'w', 0, 'w', 0, 'w', 0, 'w'],
['w', 0, 'w', 0, 'w', 0, 'w', 0]
]
print("checkers_board")
for valor in checkers_board:
    print("\t", valor, end=" ")
    print()

# Aplicación de Matrices a Imágenes
image = [
[255, 0, 0, 0, 255],
[0, 255, 0, 255, 0],
[0, 0, 255, 0, 0],
[0, 255, 0, 255, 0],
[255, 0, 0, 0, 255]
]
print("image")
for valor in image:
    print("\t", valor, end=" ")
    print()
    

#link documento https://drive.google.com/file/d/1obWN5KyZFuoZwjlzwHuujjAJ198Xh6UB/view
