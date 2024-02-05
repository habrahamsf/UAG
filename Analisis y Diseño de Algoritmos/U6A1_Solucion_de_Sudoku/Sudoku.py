
for test in range(2):

    def sudoku_R(sudoku):

        row, col = checkCelda(sudoku)
        
        # si no hay celdas vacias el Sudoku estara resuelto
        if row == -1:
            return True
        
        for num in range(1, 10):
            if checkNumber(sudoku, row, col, num):
                # si es valido entonces agregue el número a la celda
                sudoku[row][col] = num
                
                # continue resolviendo el Sudoku
                if sudoku_R(sudoku):
                    return True
                
                sudoku[row][col] = 0
        return False

    def checkCelda(sudoku):
        # Encontrar la próxima celda vacia en la tabla
        for row in range(9):
            for col in range(9):
                if sudoku[row][col] == 0:
                    return row, col
        return -1, -1

    def checkNumber(sudoku, row, col, num):
        # revisa si el numero ya esta en la fila y en la columna
        for i in range(9):
            if sudoku[row][i] == num or sudoku[i][col] == num:
                return False   
            
        # Verificar si el numero ya esta en el cuadrado
        square_row = (row // 3) * 3
        square_col = (col // 3) * 3
        for i in range(square_row, square_row + 3):
            for j in range(square_col, square_col + 3):
                if sudoku[i][j] == num:
                    return False
            
        return True
    if test == 0:
        sudoku = [    
            [5, 0, 0, 9, 1, 3, 7, 2, 0],
            [3, 0, 0, 0, 8, 0, 5, 0, 9],
            [0, 9, 0, 2, 5, 0, 0, 8, 0],
            [6, 8, 0, 4, 7, 0, 2, 3, 0],
            [0, 0, 9, 5, 0, 0, 4, 6, 0],
            [7, 0, 4, 0, 0, 0, 0, 0, 5],
            [0, 2, 0, 0, 0, 0, 0, 0, 0],
            [4, 0, 0, 8, 9, 1, 6, 0, 0],
            [8, 5, 0, 7, 2, 0, 0, 0, 3]
        ]

        sudoku_R(sudoku)
        print("Respuesta del Sudoku1:")
        for row in sudoku:
            print(row)
        print("\n")

    else:
        sudoku = [    
            [6, 9, 0, 0, 0, 0, 7, 0, 0],
            [0, 0, 0, 0, 9, 6, 0, 0, 0],
            [0, 8, 0, 7, 5, 3, 0, 9, 0],
            [0, 2, 0, 3, 7, 4, 5, 6, 1],
            [3, 6, 0, 0, 0, 5, 0, 2, 0],
            [0, 0, 0, 9, 6, 0, 3, 7, 8],
            [0, 0, 6, 0, 3, 1, 0, 8, 4],
            [0, 4, 5, 8, 0, 7, 6, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 5, 7]
        ]


        sudoku_R(sudoku)
        print("Respuesta del Sudoku2:")
        for row in sudoku:
            print(row)


