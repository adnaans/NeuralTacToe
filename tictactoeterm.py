# import modules
import random
import sys
import copy
import numpy as np
import matplotlib.pyplot as plt


class Game:
    "Tic-Tac-Toe class. This class holds the user interaction, and game logic"
    def __init__(self):
        self.board = [' '] * 9
        self.player_marker = ''
        self.bot_name = 'TBot'
        self.bot_marker = ''
        self.turn = 0
        self.bot_turns_overall2=[]
        self.bot_turns_overall4=[]
        self.bot_turns_overall6=[]
        self.bot_turns_overall8=[]
        self.bot_turns_current=[]
        self.outputs2=[]
        self.outputs4=[]
        self.outputs6=[]
        self.outputs8=[]
        self.numerical_board=[0,0,0,0,0,0,0,0,0]
        self.winning_combos = (
        [6, 7, 8], [3, 4, 5], [0, 1, 2], [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6],
    )
        self.options=[0,1,2,3,4,5,6,7,8]
        self.middle = 4
        self.neural2 = Neural_Network(Lambda=0.0001)
        self.trainer2 = trainer(self.neural2)
        self.neural4 = Neural_Network(Lambda=0.0001)
        self.trainer4 = trainer(self.neural4)
        self.neural6 = Neural_Network(Lambda=0.0001)
        self.trainer6 = trainer(self.neural6)
        self.neural8 = Neural_Network(Lambda=0.0001)
        self.trainer8 = trainer(self.neural8)
        self.winner = 0
        self.testdatax2=np.array(([0, 0, 1, -1, 0, 0, 0, 0, 0],[0,0,0,0,0,0,1,-1,0], [1,0,0,0,0,0,0,0,-1], [0,1,0,0,0,-1,0,0,0]), dtype=float)
        self.testdatay2=np.array(([0],[1],[0.5],[1]), dtype=float)
        self.testdatax4=np.array(([1, 0, 0, -1, -1, 1, 0, 0, 0],[-1,1,0,-1,0,0,1,0,0], [-1,0,0,-1,1,0,1,0,0], [1,-1,-1,1,0,0,0,0,0]), dtype=float)
        self.testdatay4=np.array(([0.5],[1],[1],[0]), dtype=float)
        self.testdatax6=np.array(([0, -1, 0, 0, 1, 1, -1, 1, -1],[0,0,1,1,-1,-1,-1,0,1], [1,-1,0,0,1,0,-1,-1,0], [1,1,0,-1,-1,0,1,0,-1]), dtype=float)
        self.testdatay6=np.array(([0.5],[0.5],[1],[0]), dtype=float)
        self.testdatax8=np.array(([0, -1, -1, 1, -1, -1, 1, 1, 1],[1,-1,-1,1,1,-1,-1,1,0], [-1,1,1,1,-1,0,-1,-1,1], [1,-1,0,-1,1,1,-1,1,-1]), dtype=float)
        self.testdatay8=np.array(([1],[0],[0.5],[0.5]), dtype=float)

        self.form = '''
           \t| %s | %s | %s |
           \t-------------
           \t| %s | %s | %s |
           \t-------------
           \t| %s | %s | %s |
           '''      

    def reinitialize(self):
        self.board = [' '] * 9
        self.player_marker = ''
        self.bot_name = 'TBot'
        self.bot_marker = ''
        self.turn = 0
        self.numerical_board=[0,0,0,0,0,0,0,0,0]
        self.bot_turns_current=[]
        self.winning_combos = (
        [6, 7, 8], [3, 4, 5], [0, 1, 2], [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6],
    )
        self.options=[0,1,2,3,4,5,6,7,8]
        self.middle = 4
        self.winner = 0

        self.form = '''
           \t| %s | %s | %s |
           \t-------------
           \t| %s | %s | %s |
           \t-------------
           \t| %s | %s | %s |
           '''      
        trainX2 = np.array(self.bot_turns_overall2)
        trainY2 = np.array(self.outputs2)
        self.trainer2.train(trainX2, trainY2, self.testdatax2, self.testdatay2)
        if(len(self.bot_turns_overall4)>0):
          trainX4 = np.array(self.bot_turns_overall4)
          trainY4 = np.array(self.outputs4)
          self.trainer4.train(trainX4, trainY4, self.testdatax4, self.testdatay4)
        if(len(self.bot_turns_overall6)>0):
          trainX6 = np.array(self.bot_turns_overall6)
          trainY6 = np.array(self.outputs6)
          self.trainer6.train(trainX6, trainY6, self.testdatax6, self.testdatay6)

        if(len(self.bot_turns_overall8)>0):
          trainX8 = np.array(self.bot_turns_overall8)
          trainY8 = np.array(self.outputs8)
          self.trainer8.train(trainX8, trainY8, self.testdatax8, self.testdatay8)

                 

    def print_board(self,board = None):
        "Display board on screen"
        if board is None:
            print self.form % tuple(self.board[6:9] + self.board[3:6] + self.board[0:3])
        else:
            # when the game starts, display numbers on all the grids
            print self.form % tuple(board[6:9] + board[3:6] + board[0:3])

    def get_marker(self):
        return('X','O')
    

    def help(self):
        print '''
\n\t The game board has 9 sqaures(3X3).
\n\t Two players take turns in marking the spots/grids on the board.
\n\t The first player to have 3 pieces in a horizontal, vertical or diagonal row wins the game.
\n\t To place your mark in the desired square, simply type the number corresponding with the square on the grid 
 
\n\t Press Ctrl + C to quit
'''

    def quit_game(self):
        "exits game"
        self.print_board
        print "\n\t Thanks for playing :-) \n\t Come play again soon!\n"
        sys.exit()

    def is_winner(self, board, marker):
        "check if this marker will win the game"
        # order of checks:
        #   1. across the horizontal top
        #   2. across the horizontal middle
        #   3. across the horizontal bottom
        #   4. across the vertical left
        #   5. across the vertical middle
        #   6. across the vertical right
        #   7. across first diagonal
        #   8. across second diagonal
        for combo in self.winning_combos:
            if (board[combo[0]] == board[combo[1]] == board[combo[2]] == marker):
                return True
        return False

    def get_bot_move(self):
        #print(self.board)
        #print(self.turn)
        #print "here?"
        #print self.bot_turns_current
        #print "or na"
        max=0
        bestindex=0
        print"board"
        print self.numerical_board
        for i in range(0,9):
          if(self.is_space_free(self.board, i)):
            tempnumboard = self.numerical_board[:]
            tempnumboard[i] = 1
            tempnparray=np.array(tempnumboard)
            if(self.turn==2):
              tempval = self.neural2.forward(tempnparray)
            elif(self.turn==4):
              tempval = self.neural4.forward(tempnparray)
            elif(self.turn==6):
              tempval = self.neural6.forward(tempnparray)
            elif(self.turn==8):
              tempval = self.neural8.forward(tempnparray)
            print tempval
            if(max<tempval):
              max = tempval
              bestindex=i
        return bestindex
        # else, take one free space on the sides
        #return self.choose_random_move(self.options)

    def is_space_free(self, board, index):
        "checks for free space of the board"
        #  "SPACE %s is taken" % index
        return board[index] == ' '

    def is_board_full(self):
        "checks if the board is full"
        for i in range(1,9):
            if self.is_space_free(self.board, i):
                return False
        return True

    def make_move(self,board,index,move):
        board[index] =  move

    def choose_random_move(self, move_list):
        possible_winning_moves = []
        for index in move_list:
            if self.is_space_free(self.board, index):
                #print(self.board)
                possible_winning_moves.append(index)
        if len(possible_winning_moves) != 0:
            return random.choice(possible_winning_moves)
        else:
            return None
       
    def start_game(self):
       self.print_board(range(1,10))
       self.help()

       # get user's preferred marker 
       self.player_marker, self.bot_marker = self.get_marker()
       print "Your marker is " + self.player_marker
       
       self.enter_game_loop('h')


    def get_player_move(self):
        move = int(input("Pick a spot to move: (1-9) "))
        if(move == 0):
          self.quit_game()
        while move not in [1,2,3,4,5,6,7,8,9] or not self.is_space_free(self.board,move-1) :
            if(move==0):
              self.quit_game()
            move = int(input("Invalid move. Please try again: (1-9) "))
        return move - 1


    def enter_game_loop(self,turn):
       "starts the main game loop"
       is_running = True
       player = turn #h for human, b for bot
       self.bot_turns_current = []
       self.turn = 2
       while is_running:
           if player == 'h':
               user_input = self.get_player_move()
               self.numerical_board[user_input]=-1
               print "wtf"
               print self.numerical_board
               self.make_move(self.board,user_input, self.player_marker)

               if(self.is_winner(self.board, self.player_marker)):
                   self.print_board()
                   print "\n\tCONGRATULATIONS %s, YOU HAVE WON THE GAME!!! \\tn"
                   self.winner = 0
                   is_running = False
                   #break
               else:
                   if self.is_board_full():
                       self.print_board()
                       print "\n\t-- Match Draw --\t\n"
                       self.winner = 0.5
                       is_running = False
                       #break
                   else:
                       self.print_board()
                       player = 'b'
           # bot's turn to play
           else:
              bot_move =  self.get_bot_move()
              print "board2"
              print self.numerical_board
              print(bot_move)
              self.numerical_board[bot_move]=1
              nextelement = self.numerical_board[:]
              print self.numerical_board
              #print(nextelement)
              self.bot_turns_current.append(nextelement)
              self.make_move(self.board, bot_move, self.bot_marker)
              if (self.is_winner(self.board, self.bot_marker)):
                  self.print_board()
                  print "\n\t%s HAS WON!!!!\t\n" % self.bot_name
                  #self.incr_score(self.bot_name)
                  self.winner = 1
                  is_running = False
                  break
              else:
                  if self.is_board_full():
                      self.print_board()
                      print "\n\t -- Match Draw -- \n\t"
                      self.winner = 0.5
                      is_running = False
                      #break
                  else:
                      self.print_board()
                      player = 'h'
              self.turn = self.turn + 2

       self.add_data()

       # when you break out of the loop, end the game
       self.end_game()

    def end_game(self):
      print "--------------------------------------------------------------------"
      self.reinitialize()
      self.start_game()

    def add_data(self):
      for i in range(0,len(self.bot_turns_current)):
        if(i==0):
          self.outputs2.append([self.winner])
          self.bot_turns_overall2.append(self.bot_turns_current[i])
          print self.outputs2
          print self.bot_turns_overall2
        elif(i==1):
          self.outputs4.append([self.winner])
          self.bot_turns_overall4.append(self.bot_turns_current[i])
          print self.outputs4
          print self.bot_turns_overall4
        elif(i==2):
          self.outputs6.append([self.winner])
          self.bot_turns_overall6.append(self.bot_turns_current[i])
          print self.outputs6
          print self.bot_turns_overall6
        elif(i==3):
          self.outputs8.append([self.winner])
          self.bot_turns_overall8.append(self.bot_turns_current[i])
          print self.outputs8
          print self.bot_turns_overall8
      #print(self.bot_turns_overall)

#-----------------------------------------------------------------------------------

x = np.array(([3,5], [5,1], [10,2]), dtype=float)
y = np.array(([75], [82], [93]), dtype=float)
'''
print x
print y
'''
x = x/np.amax(x, axis=0)
y = y/100

class Neural_Network(object):
    def __init__(self, Lambda=0):        
        #Define Hyperparameters
        self.inputLayerSize = 9
        self.outputLayerSize = 1
        self.hiddenLayerSize = 20
        
        #Weights (parameters)
        self.W1 = np.random.randn(self.inputLayerSize,self.hiddenLayerSize)
        self.W2 = np.random.randn(self.hiddenLayerSize,self.outputLayerSize)
        
        self.Lambda = Lambda

    def forward(self, X):
        #Propogate inputs though network
        self.z2 = np.dot(X, self.W1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.W2)
        yHat = self.sigmoid(self.z3) 
        return yHat
        
    def sigmoid(self, z):
        #Apply sigmoid activation function to scalar, vector, or matrix
        return 1/(1+np.exp(-z))
    
    def sigmoidPrime(self,z):
        #Gradient of sigmoid
        return np.exp(-z)/((1+np.exp(-z))**2)
    
    def costFunction(self, X, y):
        #Compute cost for given X,y, use weights already stored in class.
        self.yHat = self.forward(X)
        J = 0.5*sum((y-self.yHat)**2)/X.shape[0] + (self.Lambda/2)*(np.sum(self.W1**2)+np.sum(self.W2**2))
        return J
        
    def costFunctionPrime(self, X, y):
        #Compute derivative with respect to W and W2 for a given X and y:
        self.yHat = self.forward(X)
        
        delta3 = np.multiply(-(y-self.yHat), self.sigmoidPrime(self.z3))
        dJdW2 = np.dot(self.a2.T, delta3)/X.shape[0] + self.Lambda*self.W2
        
        delta2 = np.dot(delta3, self.W2.T)*self.sigmoidPrime(self.z2)
        dJdW1 = np.dot(X.T, delta2)/X.shape[0] + self.Lambda*self.W1
        
        return dJdW1, dJdW2
    
    #Helper Functions for interacting with other classes:
    def getParams(self):
        #Get W1 and W2 unrolled into vector:
        params = np.concatenate((self.W1.ravel(), self.W2.ravel()))
        return params
    
    def setParams(self, params):
        #Set W1 and W2 using single paramater vector.
        W1_start = 0
        W1_end = self.hiddenLayerSize * self.inputLayerSize
        self.W1 = np.reshape(params[W1_start:W1_end], (self.inputLayerSize , self.hiddenLayerSize))
        W2_end = W1_end + self.hiddenLayerSize*self.outputLayerSize
        self.W2 = np.reshape(params[W1_end:W2_end], (self.hiddenLayerSize, self.outputLayerSize))
        
    def computeGradients(self, X, y):
        dJdW1, dJdW2 = self.costFunctionPrime(X, y)
        return np.concatenate((dJdW1.ravel(), dJdW2.ravel()))

def computeNumericalGradient(N, X, y):
    paramsInitial = N.getParams()
    numgrad = np.zeros(paramsInitial.shape)
    perturb = np.zeros(paramsInitial.shape)
    e = 1e-4

    for p in range(len(paramsInitial)):
        #Set perturbation vector
        perturb[p] = e
        N.setParams(paramsInitial + perturb)
        loss2 = N.costFunction(X, y)
        
        N.setParams(paramsInitial - perturb)
        loss1 = N.costFunction(X, y)

        #Compute Numerical Gradient
        numgrad[p] = (loss2 - loss1) / (2*e)

        #Return the value we changed to zero:
        perturb[p] = 0
        
    #Return Params to original value:
    N.setParams(paramsInitial)

    return numgrad 

from scipy import optimize


class trainer(object):
    def __init__(self, N):
        #Make Local reference to network:
        self.N = N
        
    def callbackF(self, params):
        self.N.setParams(params)
        self.J.append(self.N.costFunction(self.X, self.y))
        self.testJ.append(self.N.costFunction(self.testX, self.testY))  
        
    def costFunctionWrapper(self, params, X, y):
        self.N.setParams(params)
        cost = self.N.costFunction(X, y)
        grad = self.N.computeGradients(X,y)
        return cost, grad
        
    def train(self, trainX, trainY, testX, testY):
      #Make an internal variable for the callback function:
      self.X = trainX
      self.y = trainY
      self.testX = testX
      self.testY = testY
      #Make empty list to store training costs:
      self.J = []
      self.testJ = []
      params0 = self.N.getParams()
      options = {'maxiter': 200, 'disp' : True}
      _res = optimize.minimize(self.costFunctionWrapper, params0, jac=True, method='BFGS', \
                                 args=(trainX, trainY), options=options, callback=self.callbackF)
      self.N.setParams(_res.x)
      self.optimizationResults = _res




if __name__ == "__main__":   
     TicTacToe = Game()
     TicTacToe.start_game()