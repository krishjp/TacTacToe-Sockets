#import tkinter from the standard library
import tkinter as tk
from gameboard4 import BoardClass
import socket
import threading

#Definine a TikUI Class for the User Interface
class TikUIpacker():
   hPlayer = BoardClass()

   master = 0

   host_ip= ''
   host_port = 0
   host_user = ''
   client_user = ''
   connect_status = 'Not Connected...'
   serverSocket = 0
   connect_completed = False
   position = 0
   
   #Define my class constructor
   def __init__(self):
      '''Initializes and created the canvas used to connect the two players
      '''
      self.canvasSetup()
      self.initTKVariables()
      self.createHostIpEntry()
      self.createHostPortEntry()
      self.createUserEntry()
      self.createSubmitButton()
      self.createQuitButton()
      self.connectedLabel()

   def initTKVariables(self):
      '''Initializes my tk variables
      '''
      self.host_ip = tk.StringVar()
      self.host_port = tk.IntVar()
      self.host_user = tk.StringVar()
      self.client_user = tk.StringVar()
      self.connection_status = tk.StringVar()
      self.closed = False
      self.connect_completed = False

   def canvasSetup(self):
      '''Creates the base canvas for my GUI
      '''
      self.master = tk.Tk()
      self.master.title("Host - Basic Tik Tac Toe")
      self.master.geometry('700x400')
      self.master.configure(background='#D7E5F0')
      self.master.resizable(0,0)

   def createQuitButton(self):
      '''Creates the quit button to destroy the GUI
      '''
      self.quitButton = tk.Button(self.master,text="Quit",command=self.closeAll, fg='red').place(x=0, y=375)
   
   def createHostIpEntry(self):
      '''Creates an entry box for the Host IP
      '''
      self.hostIpEntry = tk.Entry(self.master, textvariable=self.host_ip)
      self.hostIpEntry.insert(0, 'Host IP')
      self.hostIpEntry.place(x=0, y=0)
   
   def createHostPortEntry(self):
      '''Creates an entry box for Host Port
      '''
      self.hostPortEntry = tk.Entry(self.master)
      self.hostPortEntry.insert(0, 'Host Port')
      self.hostPortEntry.place(x=0, y=25)

   def createUserEntry(self):
      '''Creates an entry box for the player's Username
      '''
      self.userEntry = tk.Entry(self.master)
      self.userEntry.insert(0, 'Username')
      self.userEntry.place(x=0, y=50)

   def connectedLabel(self):
      '''Creates a label to show the connection status
      '''
      self.resultLabel = tk.Label(self.master, text=self.connect_status,width=15).place(x=0,y=100)
      
   def startUpServer(self):
      '''Tries to create a socket connection using the data inputted by the user
      '''
      try:    
         self.connect_status = 'Not Connected...'
         self.connectedLabel()
         self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         server_port = int(self.hostPortEntry.get())
         server_addy = self.hostIpEntry.get()
         self.hPlayer.username = self.userEntry.get()
         if not self.hPlayer.username.isalnum():
            raise NameError
         self.serverSocket.bind((server_addy,server_port))
         self.serverSocket.listen(0)
         self.clientSocket, clientAddy = self.serverSocket.accept()
         self.connect_status = 'Connected!'
         self.connectedLabel()
         self.submitButton['state'] = 'disabled'
         self.hPlayer.opponent = self.clientSocket.recv(1024)
         self.hPlayer.opponent = self.hPlayer.opponent.decode()
         self.clientSocket.send(self.hPlayer.username.encode())
         self.createButtons()
         self.createLabels()
         self.connect_completed = True
      except:
         self.connect_status = 'Invalid Username!'
         self.connectedLabel()
         self.userEntry.delete(0, 'end')
         self.userEntry.insert(0, 'Username')

   def closeAll(self):
      '''Closes the server socket if it is created and terminates the GUI
      '''
      if self.serverSocket:
         self.serverSocket.close()
      self.master.destroy()
      self.closed = True

   def createSubmitButton(self):
      '''Defines a submit button to run the startUpServer function
      '''
      self.submitButton = tk.Button(self.master,text="Submit", command=self.startUpServer)
      self.submitButton.place(x=0, y=75)
   
   def createButtons(self):
      '''Creates the buttons used to play the game and formats the buttons and their displayed location
      '''
      gameTitleLabel = tk.Label(text = "Game Board", font=('Times', 18))
      gameTitleLabel.place(x=0, y=125)
      self.btn1 = tk.Button(highlightbackground = '#f0f0f0',text=" ",width=5,height=2,font=('Times', 26), command=self.buttonClick1)
      self.btn1.place(x = 0, y = 150)
      self.btn2 = tk.Button(highlightbackground = '#f0f0f0',text=" ",width=5,height=2,font=('Times', 26), command=self.buttonClick2)
      self.btn2.place(x = 100, y = 150)
      self.btn3 = tk.Button(highlightbackground = '#f0f0f0',text=" ",width=5,height=2,font=('Times', 26), command=self.buttonClick3)
      self.btn3.place(x = 200, y = 150)
      self.btn4 = tk.Button(highlightbackground = '#f0f0f0',text=" ",width=5,height=2,font=('Times', 26), command=self.buttonClick4)
      self.btn4.place(x = 0, y = 220)
      self.btn5 = tk.Button(highlightbackground = '#f0f0f0',text=" ",width=5,height=2,font=('Times', 26), command=self.buttonClick5)
      self.btn5.place(x = 100, y = 220)
      self.btn6 = tk.Button(highlightbackground = '#f0f0f0',text=" ",width=5,height=2,font=('Times', 26), command=self.buttonClick6)
      self.btn6.place(x = 200, y = 220)
      self.btn7 = tk.Button(highlightbackground = '#f0f0f0',text=" ",width=5,height=2,font=('Times', 26), command=self.buttonClick7)
      self.btn7.place(x = 0, y = 290)
      self.btn8 = tk.Button(highlightbackground = '#f0f0f0',text=" ",width=5,height=2,font=('Times', 26), command=self.buttonClick8)
      self.btn8.place(x = 100, y = 290)
      self.btn9 = tk.Button(highlightbackground = '#f0f0f0',text=" ",width=5,height=2,font=('Times', 26), command=self.buttonClick9)
      self.btn9.place(x = 200, y = 290)

   def buttonClick1(self):
      '''Changes the button text to an O and sends the move to the other player
      '''
      if self.connect_completed == True and self.btn1['text'] == ' ' and self.hPlayer.lastPlayer == self.hPlayer.opponent:
         self.btn1['text'] = 'O'
         self.btn1['highlightbackground'] = 'orange'
         self.master.update_idletasks()
         self.hPlayer.lastPlayer = self.hPlayer.username
         position = '0'
         self.clientSocket.send(position.encode())
         self.hPlayer.playMove(0,"O")
         self.turnLabel['text'] = self.hPlayer.opponent
         self.handleWin()
   def buttonClick2(self):
      '''Changes the button text to an O and sends the move to the other player
      '''
      if self.connect_completed == True and self.btn2['text'] == ' ' and self.hPlayer.lastPlayer == self.hPlayer.opponent:
         self.btn2['text'] = 'O'
         self.btn2['highlightbackground'] = 'orange'
         self.master.update_idletasks()
         self.hPlayer.lastPlayer = self.hPlayer.username
         position = '1'
         self.clientSocket.send(position.encode())
         self.hPlayer.playMove(1,"O")
         self.turnLabel['text'] = self.hPlayer.opponent
         self.handleWin()
   def buttonClick3(self):
      '''Changes the button text to an O and sends the move to the other player
      '''
      if self.connect_completed == True and self.btn3['text'] == ' ' and self.hPlayer.lastPlayer == self.hPlayer.opponent:
         self.btn3['text'] = 'O'
         self.btn3['highlightbackground'] = 'orange'
         self.master.update_idletasks()
         self.hPlayer.lastPlayer = self.hPlayer.username
         position = '2'
         self.clientSocket.send(position.encode())
         self.hPlayer.playMove(2,"O")
         self.turnLabel['text'] = self.hPlayer.opponent
         self.handleWin()
   def buttonClick4(self):
      '''Changes the button text to an O and sends the move to the other player
      '''
      if self.connect_completed == True and self.btn4['text'] == ' ' and self.hPlayer.lastPlayer == self.hPlayer.opponent:
         self.btn4['text'] = 'O'
         self.btn4['highlightbackground'] = 'orange'
         self.master.update_idletasks()
         self.hPlayer.lastPlayer = self.hPlayer.username
         position = '3'
         self.clientSocket.send(position.encode())
         self.hPlayer.playMove(3,"O")
         self.turnLabel['text'] = self.hPlayer.opponent
         self.handleWin()
   def buttonClick5(self):
      '''Changes the button text to an O and sends the move to the other player
      '''
      if self.connect_completed == True and self.btn5['text'] == ' ' and self.hPlayer.lastPlayer == self.hPlayer.opponent:
         self.btn5['text'] = 'O'
         self.btn5['highlightbackground'] = 'orange'
         self.master.update_idletasks()
         self.hPlayer.lastPlayer = self.hPlayer.username
         position = '4'
         self.clientSocket.send(position.encode())
         self.hPlayer.playMove(4,"O")
         self.turnLabel['text'] = self.hPlayer.opponent
         self.handleWin()
   def buttonClick6(self):
      '''Changes the button text to an O and sends the move to the other player
      '''
      if self.connect_completed == True and self.btn6['text'] == ' ' and self.hPlayer.lastPlayer == self.hPlayer.opponent:
         self.btn6['text'] = 'O'
         self.btn6['highlightbackground'] = 'orange'
         self.master.update_idletasks()
         self.hPlayer.lastPlayer = self.hPlayer.username
         position = '5'
         self.clientSocket.send(position.encode())
         self.hPlayer.playMove(5,"O")
         self.turnLabel['text'] = self.hPlayer.opponent
         self.handleWin()
   def buttonClick7(self):
      '''Changes the button text to an O and sends the move to the other player
      '''
      if self.connect_completed == True and self.btn7['text'] == ' ' and self.hPlayer.lastPlayer == self.hPlayer.opponent:
         self.btn7['text'] = 'O'
         self.btn7['highlightbackground'] = 'orange'
         self.master.update_idletasks()
         self.hPlayer.lastPlayer = self.hPlayer.username
         position = '6'
         self.clientSocket.send(position.encode())
         self.hPlayer.playMove(6,"O")
         self.turnLabel['text'] = self.hPlayer.opponent
         self.handleWin()
   def buttonClick8(self):
      '''Changes the button text to an O and sends the move to the other player
      '''
      if self.connect_completed == True and self.btn8['text'] == ' ' and self.hPlayer.lastPlayer == self.hPlayer.opponent:
         self.btn8['text'] = 'O'
         self.btn8['highlightbackground'] = 'orange'
         self.master.update_idletasks()
         self.hPlayer.lastPlayer = self.hPlayer.username
         position = '7'
         self.clientSocket.send(position.encode())
         self.hPlayer.playMove(7,"O")
         self.turnLabel['text'] = self.hPlayer.opponent
         self.handleWin()
   def buttonClick9(self):
      '''Changes the button text to an O and sends the move to the other player
      '''
      if self.connect_completed == True and self.btn9['text'] == ' ' and self.hPlayer.lastPlayer == self.hPlayer.opponent:
         self.btn9['text'] = 'O'
         self.btn9['highlightbackground'] = 'orange'
         self.master.update_idletasks()
         self.hPlayer.lastPlayer = self.hPlayer.username
         position = '8'
         self.clientSocket.send(position.encode())
         self.hPlayer.playMove(8,"O")
         self.turnLabel['text'] = self.hPlayer.opponent
         self.handleWin()

   def createLabels(self):
      '''Creates the labels that display the username, opponent, and the whose's turn. Also sets up the area for the game stats to be displayed
      '''
      lbl1 = tk.Label(self.master, text='Player: ',width=15, height=2).place(x=400,y=0)
      playerLabel = tk.Label(self.master, text=self.hPlayer.username,width=15, height=2)
      playerLabel.place(x=550,y=0)
      lbl2 = tk.Label(self.master, text='Opponent : ',width=15, height=2).place(x=400,y=35)
      opponentLabel = tk.Label(self.master, text=self.hPlayer.opponent,width=15, height=2)
      opponentLabel.place(x=550,y=35)
      lbl3 = tk.Label(self.master, text="Who's turn: ",width=15, height=2).place(x=400,y=70)
      self.turnLabel = tk.Label(self.master, text= self.hPlayer.opponent,width=15, height=2)
      self.turnLabel.place(x=550,y=70)

      lbl4 = tk.Label(self.master, text='Games Played: ',width=15, height=2).place(x=400,y=110)
      self.totalGamesLabel = tk.Label(self.master, text='',width=15, height=2)
      self.totalGamesLabel.place(x=550,y=110)
      lbl5 = tk.Label(self.master, text='Wins: ',width=15, height=2).place(x=400,y=145)
      self.winsLabel = tk.Label(self.master, text='',width=15, height=2)
      self.winsLabel.place(x=550,y=145)
      lbl6 = tk.Label(self.master, text='Losses: ',width=15, height=2).place(x=400,y=180)
      self.lossesLabel = tk.Label(self.master, text='',width=15, height=2)
      self.lossesLabel.place(x=550,y=180)
      lbl7 = tk.Label(self.master, text='Ties: ',width=15, height=2).place(x=400,y=215)
      self.tiesLabel = tk.Label(self.master, text='',width=15, height=2)
      self.tiesLabel.place(x=550,y=215)

   def receiveMove(self):
      '''Receives a move from the other player and updates the 3x3 board to show the other player's move
      '''
      while True:
         if self.connect_completed == True:
            try:
               pos = self.clientSocket.recv(1024)
               pos = pos.decode()
               if pos == 'Again':
                  self.reset()
                  self.turnLabel['text'] = self.hPlayer.opponent
                  pass
               elif pos == 'Done':
                  self.connect_completed = False
                  stat_holder = self.hPlayer.computeStats()
                  self.totalGamesLabel['text'] = stat_holder[0]
                  self.winsLabel['text'] = stat_holder[1]['O']
                  self.lossesLabel['text'] = stat_holder[1]['X']
                  self.tiesLabel['text'] = stat_holder[2]
                  self.reset()
                  self.clientSocket.close()
                  pass
               else:
                  self.hPlayer.lastPlayer = self.hPlayer.opponent
                  self.hPlayer.playMove(int(pos), 'X')
                  self.updateBoard(int(pos))
                  self.turnLabel['text'] = self.hPlayer.username
                  self.handleWin()
            except:
               pass
   
   def updateBoard(self, newPos):
      '''Takes the move made by the other player and displays it in the GUI
      '''
      if newPos == 0:
         self.btn1['text'] = "X"
         self.btn1['highlightbackground'] = 'blue'
      elif newPos == 1:
         self.btn2['text'] = "X"
         self.btn2['highlightbackground'] = 'blue'
      elif newPos == 2:
         self.btn3['text'] = "X"
         self.btn3['highlightbackground'] = 'blue'
      elif newPos == 3:
         self.btn4['text'] = "X"
         self.btn4['highlightbackground'] = 'blue'
      elif newPos == 4:
         self.btn5['text'] = "X"
         self.btn5['highlightbackground'] = 'blue'
      elif newPos == 5:
         self.btn6['text'] = "X"
         self.btn6['highlightbackground'] = 'blue'
      elif newPos == 6:
         self.btn7['text'] = "X"
         self.btn7['highlightbackground'] = 'blue'
      elif newPos == 7:
         self.btn8['text'] = "X"
         self.btn8['highlightbackground'] = 'blue'
      elif newPos == 8:
         self.btn9['text'] = "X"
         self.btn9['highlightbackground'] = 'blue'

   def reset(self):
      '''Completely reset the 3x3 game board in preparation for a new game or the stats being printed.
      '''
      self.hPlayer.resetGameBoard()
      self.btn1['text'] = ' '
      self.btn2['text'] = ' '
      self.btn3['text'] = ' '
      self.btn4['text'] = ' '
      self.btn5['text'] = ' '
      self.btn6['text'] = ' '
      self.btn7['text'] = ' '
      self.btn8['text'] = ' '
      self.btn9['text'] = ' '
      self.btn1['highlightbackground'] = '#f0f0f0'
      self.btn2['highlightbackground'] = '#f0f0f0'
      self.btn3['highlightbackground'] = '#f0f0f0'
      self.btn4['highlightbackground'] = '#f0f0f0'
      self.btn5['highlightbackground'] = '#f0f0f0'
      self.btn6['highlightbackground'] = '#f0f0f0'
      self.btn7['highlightbackground'] = '#f0f0f0'
      self.btn8['highlightbackground'] = '#f0f0f0'
      self.btn9['highlightbackground'] = '#f0f0f0'

   def handleWin(self):
      '''Changes variable values to stop the host player from playing agian once a win situation has been detected
      '''
      finish = self.hPlayer.isWinner()
      if finish:
         self.hPlayer.totalGames += 1
         self.hPlayer.resetGameBoard()
         self.hPlayer.lastPlayer = self.hPlayer.username

   def runUI(self):
      '''Runs the GUI and keeps the GUI active
      '''
      self.master.mainloop()
      
def createThread(con):
   '''Creates the basic format for the use for the threading Class
   '''
   thread = threading.Thread(target=con)
   thread.daemon = True
   thread.start()

if __name__ == '__main__':
   basicTicTacToe = TikUIpacker()
   createThread(basicTicTacToe.receiveMove)
   basicTicTacToe.runUI()