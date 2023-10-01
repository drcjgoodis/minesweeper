class Board:


    def __init__(self, row, column):
        self.row_num = row
        self.column_num = column
        self.grid = []
        # [["_", "_", "_", _ _ _ _ _ _ _], []]
        for i in range(0,self.row_num,1):
            self.grid.append([])
            for j in range(0,self.column_num,1):
                self.grid[i].append("_")

    def print(self):
        for i in range(0,self.column_num,1):
            print("")
            for j in range(0,self.row_num,1):
                print(self.grid[i][j], sep=" ", end=" ")
        print("")
        print("")

board1 = Board(10,10)
board1.print()
board2 = Board(5,5)
board2.print()
board1.grid[6][4] = '*'
board1.print()