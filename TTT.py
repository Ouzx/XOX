x = 1
o = 0
n = 10
board =[[n,n,n],
        [n,n,n],
        [n,n,n]]

X = ["|==========|",
    "|   \  /   |",
    "|    \/    |",
    "|    /\    |",
    "|   /  \   |",
    "|==========|"]

O = ["|==========|",
    "|   ————   |",
    "|  |    |  |",
    "|  |    |  |",
    "|   ————   |",
    "|==========|"]

N = ["|==========|",
    "|          |",
    "|          |",
    "|          |",
    "|          |",
    "|==========|"]
    
class TTT:
    def __init__(self):
        print("Welcome to Tic-Tac-Toe game")
        print("First of all you have to know board coordinates,you can check your knowledge below")
        print(" ——————————— ")
        print("|0,0|0,1|1,1|")
        print("|1,0|1,1|1,1|")
        print("|2,0|2,1|2,1|")
        print(" ——————————— ")
        print("Game will start in 1 second")
        x_counter = 0 #player1
        o_counter = 0 #player0
        namee = "X"
        self.name = namee
        self.x_counter = x_counter
        self.o_counter = o_counter
        self.draw()
        end = False
        turn = 1 #X
        self.turn = turn
        self.end = end
        self.play()
        
    
    def draw(self):
        
        global board
        global o
        global x
        global n

        global X
        global O
        global N

        j = o
        for i in range(3):
            for k in range(6):
                print("|",end="")
                if(board[i][j] == x):
                    print(X[k],end="")
                if(board[i][j] == o):
                    print(O[k],end="")
                if(board[i][j] == n):
                    print(N[k],end="")
                
                if(board[i][j+x] == x):
                    print(X[k],end="")
                if(board[i][j+x] == o):
                    print(O[k],end="")
                if(board[i][j+x] == n):
                    print(N[k],end="")
                
                if(board[i][j+2] == x):
                    print(X[k],end="")
                if(board[i][j+2] == o):
                    print(O[k],end="")
                if(board[i][j+2] == n):
                    print(N[k],end="")
                print("|")

    def check_board(self):
        #row/column/diagonal check
        sum_diagonal_1 = 0
        sum_diagonal_2 = 0
        for i in range(3):
            sum_row = 0
            sum_column = 0
            sum_row = board[i][0] + board[i][1] + board[i][2] 
            sum_column = board[0][i] + board[1][i] + board[2][i]
            sum_diagonal_1 += board[i][i]
            sum_diagonal_2 += board[2-i][i]
            if(sum_row == 3 or sum_column == 3 or sum_column == 0 or sum_row == 0):
                self.end_game()
        if(sum_diagonal_1 == 3 or sum_diagonal_2 == 3 or sum_diagonal_1 == 0 or sum_diagonal_2 == 0):
            self.end_game()

    def end_game(self):
        print("Player"+ self.name +" WIN!!")  
        ans = input("Do you want to continue? Y/y: Yes - N/n: No:      ")
        if(ans == "Y" or ans == "y"):
            self.end = False
            global board
            global n
            board = [[n,n,n],
                    [n,n,n],
                    [n,n,n]]
            self.draw()
        else:
            self.end = True
        if(self.turn == 1):
            self.x_counter += 1
        else:
            self.o_counter += 1  
        
        
    def Act(self):
        self.draw()
        self.check_board()
        if(self.turn == 1): 
            self.turn = 0
        elif(self.turn == 0):
            self.turn = 1
        if(self.end != True):
            self.play()

                
    def play(self):
        print("X's: " + str(self.x_counter) + "       O's: " + str(self.o_counter))
        
        if(self.turn == 1):
            self.name = "X"
        else:
            self.name = "O"
        ans = input("player"+self.name+": " )
        _x = 0
        _y = 0
        try:
            _x = int(ans[0])
            _y = int(ans[1])
            _z = self.turn
            if(_z == 0 or _z == 1):
                if(board[_x][_y] != n):
                    print("That location is already used!")
                    print("Try Again!")
                    self.play()
                else:
                    board[_x][_y] = _z
                    self.Act()
            else:
                print("Please try wrting true format!")
                print("X = 1(one), O = 0(zero)")
        except Exception as ex:
            print(ex)
            print("Your input is not defined!")
            print("Sample playing input should be like this> 100")
            print("1 is location in X axis , 0 is location in Y axis, 0(zero) is O")
            self.play()
        
game = TTT()





       




