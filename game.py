import random 
board = [' '] * 10
 

Griffindor = ' rupert john ginny harry ron george hermione fred sirius lucas  edward'.split()
slytherin = '  malfoy Voldemor, Severus Snape, Bellatrix Lestrange Draco Malfoy Horace Slughorn'.split()
playerhouse = []
used = []
usednames = []
options = [1,2,3,4,5,6,7,8,9]
n = 0
playerhouse1 = []

def drawBoard(board):
       # This function prints out the board that it was passed.
  
       # "board" is a list of 10 strings representing the board (ignore index 0)
      print('   |   |')
      print(' ' + board[7] + '   |   ' + board[8] + '   |   ' + board[9])
      print('   |   |')
      print('-----------')
      print('   |   |')
      print(' ' + board[4] + '   |   ' + board[5] + '   |   ' + board[6])
      print('   |   |')
      print('-----------')
      print('   |   |')
      print(' ' + board[1] + '   |   ' + board[2] + '   |   ' + board[3])
      print('   |   |')

def getplayer():
    playaa = raw_input("What is your house?: 1-Griffindor and anything to be a crappy  SLitherin: ")
    global playerhouse 
    if playaa == '1':
        playerhouse = Griffindor
        #print playerhouse
    else :
        
        playerhouse = slytherin
        #print playerhouse
    
    

def whogoesfirst():
    if   set(playerhouse)== set(Griffindor):
        return 'Griffindor you are on '
    
    elif set(playerhouse)== set(slytherin) :
        return 'SLitherin is on'

def makealist(n):
      global options 
      
      n = options[0]
      options.remove(n)
      return n
      

def MakeMove(board):
    global used
    global usednames 
    global playerhouse
    global n
    global options
    global i 
    while True:
          user = whogoesfirst()
          name = raw_input('Welcome ' + user + ' what is the name of someone in your house?: ')
          if name in playerhouse:
        
       
           i = makealist(n)
           if i == 9:
                 print 'game over ' +str(whogoesfirst())+ ' wins YAYAYYYAYYAYAY'
                 break
           #print i
           if i not in used:
              if name not in usednames:
                  board[i] = name
                  used.append(i)
                  usednames.append(name)
                  #print used
                  #print usednames
      
              else:
                  
                  i = options[0]   
                  print 'Try again bae: already used name '
                 
      
         
              drawBoard(board)

          else:
             print 'Whoops, check this out, the turns have tabled'
             playerhouse1 = Griffindor + slytherin  
             playerhouse1 =  [x for x in playerhouse1 if x not in playerhouse]
             playerhouse = playerhouse1
             #print playerhouse


             continue 


while True:
    getplayer()
    MakeMove(board)
    
        
    
#MakeMove(board)    
    



#drawBoard(board)
