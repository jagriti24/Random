#Problem : https://leetcode.com/problems/minesweeper/
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        i = click[0]
        j = click[1]
        squareStack = []
        length_m = len(board)
        length_n = len(board[0])
        if((i>=0 and i < length_m) and (j>=0 and j < length_n)):
            mines =  self.getMinesCount(board,i,j,length_m, length_n)
            if(board[i][j]=='M'):
                board[i][j]='X'
            
            elif(mines >0):
                board[i][j] = str(mines)
            
            elif(mines == 0):
                board[i][j] = 'B'
                squareStack = self.getAdjacentSquares(board,i,j,length_m, length_n,squareStack)
                while(len(squareStack) > 0):
                    square = squareStack.pop()
                    x = square[0]
                    y = square[1]
                    mines =  self.getMinesCount(board, x, y, length_m, length_n)
                    
                    if(mines >0):
                        board[x][y] = str(mines)
                        
                    elif(mines == 0):
                        board[x][y] = 'B'
                        squareStack = self.getAdjacentSquares(board,x,y,length_m, length_n,squareStack)
                    
        return board       
        
    def getMinesCount(self, board,i,j,length_m, length_n):
        mines = 0
        if(i-1 >= 0 and i-1 < length_m and board[i-1][j] == 'M'):
            mines = mines + 1
        if(i+1 >= 0 and i+1 < length_m and board[i+1][j] == 'M'):
            mines = mines + 1
        if(j-1 >= 0 and j-1 < length_n and board[i][j-1] == 'M'):
            mines = mines + 1 
        if(j+1 >= 0 and j+1 < length_n and board[i][j+1] == 'M'):
            mines = mines + 1     
        if((i-1 >= 0 and i-1< length_m) and (j-1 >= 0 and j-1 < length_n) and board[i-1][j-1] == 'M'):
            mines = mines + 1 
        if((i+1 >= 0 and i+1< length_m) and (j-1 >= 0 and j-1 < length_n) and board[i+1][j-1] == 'M'):
            mines = mines + 1
        if((i+1 >= 0 and i+1< length_m) and (j+1 >= 0 and j+1 < length_n) and board[i+1][j+1] == 'M'):
            mines = mines + 1 
        if((i-1 >= 0 and i-1< length_m) and (j+1 >= 0 and j+1 < length_n) and board[i-1][j+1] == 'M'):
            mines = mines + 1
        return mines
    
    def getAdjacentSquares(self,board,i,j,length_m , length_n, squareStack):
        if((i-1 >= 0 and i-1< length_m) and (j-1 >= 0 and j-1 < length_n) and board[i-1][j-1] == 'E'):
            squareStack.append([i-1,j-1])
            board[i-1][j-1]='V'
        if(j-1 >= 0 and j-1 < length_n and board[i][j-1] == 'E'):
            squareStack.append([i,j-1])
            board[i][j-1]='V'
        if((i+1 >= 0 and i+1< length_m) and (j-1 >= 0 and j-1 < length_n) and board[i+1][j-1] == 'E'):
            squareStack.append([i+1,j-1])
            board[i+1][j-1]='V'    
        if(i-1 >= 0 and i-1 < length_m and board[i-1][j] == 'E'):
            squareStack.append([i-1,j])
            board[i-1][j]='V'
        if(i+1 >= 0 and i+1 < length_m and board[i+1][j] == 'E'):
            squareStack.append([i+1,j])
            board[i+1][j]='V'
        if((i-1 >= 0 and i-1< length_m) and (j+1 >= 0 and j+1 < length_n) and board[i-1][j+1] == 'E'):
            squareStack.append([i-1,j+1])
            board[i-1][j+1]='V'    
        if(j+1 >= 0 and j+1 < length_n and board[i][j+1] == 'E'):
            squareStack.append([i,j+1])
            board[i][j+1]='V'  
        if((i+1 >= 0 and i+1< length_m) and (j+1 >= 0 and j+1 < length_n) and board[i+1][j+1] == 'E'):
            squareStack.append([i+1,j+1])
            board[i+1][j+1]='V'

        return squareStack;    
                    
                    
                
        
