import tkinter as tk
from tkinter import messagebox

from gameboard4 import BoardClass
import socket
import threading

#Definine a TikUI Class for the User Interface
class TikUIpacker():
   cPlayer = BoardClass()
   master = 0

   host_ip= ''
   host_port = 0
   operation = 0
   connect_status = 'Not Connected...'
   connect_completed = False
   connectionSocket = False
   
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
      self.operation = tk.StringVar()
      self.result = tk.IntVar()
      self.submitButton = tk.Button()
      self.closed = False
      self.connect_completed = False

   def canvasSetup(self):
      '''Creates the base canvas for my GUI
      '''
      self.master  = tk.Tk()
      self.master.title("Client - Basic Tik Tac Toe")
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
      self.resultLabel = tk.Label(self.master, text=self.connect_status,width=22).place(x=0,y=100)
      
   def tryConnect(self):
      '''Tries to connect to the server socket using the data inputted by the user
      '''
      try:
         self.connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         server_port = int(self.hostPortEntry.get())
         server_addy = self.hostIpEntry.get()
         self.cPlayer.username = self.userEntry.get()
         if not self.cPlayer.username.isalnum():
            raise NameError
         self.connectionSocket.connect((server_addy, server_port))
         self.connect_status = 'Connected!'
         self.connectedLabel()
         self.submitButton['state'] = 'disabled'
         self.connectionSocket.send(self.cPlayer.username.encode())
         self.cPlayer.opponent = self.connectionSocket.recv(1024)
         self.cPlayer.opponent = self.cPlayer.opponent.decode()
         self.createButtons()
         self.createLabels()
         self.connect_completed = True
         self.cPlayer.lastPlayer = self.cPlayer.opponent
      except NameError:
         self.connect_status = 'Invalid Username!'
         self.connectedLabel()
         self.userEntry.delete(0, 'end')
         self.userEntry.insert(0, 'Username')
      except:
         self.hostIpEntry.delete(0, 'end')
         self.hostIpEntry.insert(0, 'Host IP')
         self.hostPortEntry.delete(0, 'end')
         self.hostPortEntry.insert(0, 'Host Port')
         self.userEntry.delete(0, 'end')
         self.userEntry.insert(0, 'Username')
         againResp = messagebox.askyesno('Connection Failed', 'Want to try reconnecting?')
         if not againResp:
            self.closeAll()

   def createSubmitButton(self):
      '''Defines a submit button to run the tryConnect function
      '''
      self.submitButton = tk.Button(self.master,text="Submit", command=self.tryConnect)
      self.submitButton.place(x=0, y=75)
   
   def closeAll(self):
      '''Closes the connection socket if it's created and terminated the GUI
      '''
      if self.connectionSocket:
         self.connectionSocket.close()
      self.master.destroy()
      self.closed = True
      
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
      '''Changes the button text to an X and sends the move to the other player
      '''
      if self.connect_completed == True and self.btn1['text'] == ' ' and self.cPlayer.lastPlayer == self.cPlayer.opponent:
         self.btn1['text'] = 'X'
         self.btn1['highlightbackground'] = 'blue'
         self.master.update_idletasks()
         self.cPlayer.lastPlayer = self.cPlayer.username
         position = '0'
         self.connectionSocket.send(position.encode())
         self.cPlayer.playMove(0, "X")
         self.turnLabel['text'] = self.cPlayer.opponent
         self.handleWin()
   def buttonClick2(self):
      '''Changes the button text to an X and sends the move to the other player
      '''
      if self.connect_completed == True and self.btn2['text'] == ' ' and self.cPlayer.lastPlayer == self.cPlayer.opponent:
         self.btn2['text'] = 'X'
         self.btn2['highlightbackground'] = 'blue'
         self.master.update_idletasks()
         self.cPlayer.lastPlayer = self.cPlayer.username
         position = '1'
         self.connectionSocket.send(position.encode())
         self.cPlayer.playMove(1, "X")
         self.turnLabel['text'] = self.cPlayer.opponent
         self.handleWin()
   def buttonClick3(self):
      '''Changes the button text to an X and sends the move to the other player
      '''
      if self.connect_completed == True and self.btn3['text'] == ' ' and self.cPlayer.lastPlayer == self.cPlayer.opponent:
         self.btn3['text'] = 'X'
         self.btn3['highlightbackground'] = 'blue'
         self.master.update_idletasks()
         self.cPlayer.lastPlayer = self.cPlayer.username
         position = '2'
         self.connectionSocket.send(position.encode())
         self.cPlayer.playMove(2, "X")
         self.turnLabel['text'] = self.cPlayer.opponent
         self.handleWin()
   def buttonClick4(self):
      '''Changes the button text to an X and sends the move to the other player
      '''
      if self.connect_completed == True and self.btn4['text'] == ' ' and self.cPlayer.lastPlayer == self.cPlayer.opponent:
         self.btn4['text'] = 'X'
         self.btn4['highlightbackground'] = 'blue'
         self.master.update_idletasks()
         self.cPlayer.lastPlayer = self.cPlayer.username
         position = '3'
         self.connectionSocket.send(position.encode())
         self.cPlayer.playMove(3, "X")
         self.turnLabel['text'] = self.cPlayer.opponent
         self.handleWin()
   def buttonClick5(self):
      '''Changes the button text to an X and sends the move to the other player
      '''
      if self.connect_completed == True and self.btn5['text'] == ' ' and self.cPlayer.lastPlayer == self.cPlayer.opponent:
         self.btn5['text'] = 'X'
         self.btn5['highlightbackground'] = 'blue'
         self.master.update_idletasks()
         self.cPlayer.lastPlayer = self.cPlayer.username
         position = '4'
         self.connectionSocket.send(position.encode())
         self.cPlayer.playMove(4, "X")
         self.turnLabel['text'] = self.cPlayer.opponent
         self.handleWin()
   def buttonClick6(self):
      '''Changes the button text to an X and sends the move to the other player
      '''
      if self.connect_completed == True and self.btn6['text'] == ' ' and self.cPlayer.lastPlayer == self.cPlayer.opponent:
         self.btn6['text'] = 'X'
         self.btn6['highlightbackground'] = 'blue'
         self.master.update_idletasks()
         self.cPlayer.lastPlayer = self.cPlayer.username
         position = '5'
         self.connectionSocket.send(position.encode())
         self.cPlayer.playMove(5, "X")
         self.turnLabel['text'] = self.cPlayer.opponent
         self.handleWin()
   def buttonClick7(self):
      '''Changes the button text to an X and sends the move to the other player
      '''
      if self.connect_completed == True and self.btn7['text'] == ' ' and self.cPlayer.lastPlayer == self.cPlayer.opponent:
         self.btn7['text'] = 'X'
         self.btn7['highlightbackground'] = 'blue'
         self.master.update_idletasks()
         self.cPlayer.lastPlayer = self.cPlayer.username
         position = '6'
         self.connectionSocket.send(position.encode())
         self.cPlayer.playMove(6, "X")
         self.turnLabel['text'] = self.cPlayer.opponent
         self.handleWin()
   def buttonClick8(self):
      '''Changes the button text to an X and sends the move to the other player
      '''
      if self.connect_completed == True and self.btn8['text'] == ' ' and self.cPlayer.lastPlayer == self.cPlayer.opponent:
         self.btn8['text'] = 'X'
         self.btn8['highlightbackground'] = 'blue'
         self.master.update_idletasks()
         self.cPlayer.lastPlayer = self.cPlayer.username
         position = '7'
         self.connectionSocket.send(position.encode())
         self.cPlayer.playMove(7, "X")
         self.turnLabel['text'] = self.cPlayer.opponent
         self.handleWin()
   def buttonClick9(self):
      '''Changes the button text to an X and sends the move to the other player
      '''
      if self.connect_completed == True and self.btn9['text'] == ' ' and self.cPlayer.lastPlayer == self.cPlayer.opponent:
         self.btn9['text'] = 'X'
         self.btn9['highlightbackground'] = 'blue'
         self.master.update_idletasks()
         self.cPlayer.lastPlayer = self.cPlayer.username
         position = '8'
         self.connectionSocket.send(position.encode())
         self.cPlayer.playMove(8, "X")
         self.turnLabel['text'] = self.cPlayer.opponent
         self.handleWin()
   
   def createLabels(self):
      '''Creates the labels that display the username, opponent, and the whose's turn. Also sets up the area for the game stats to be displayed
      '''
      lbl1 = tk.Label(self.master, text='Player: ',width=15, height=2).place(x= 400,y=0)
      playerLabel = tk.Label(self.master, text=self.cPlayer.username,width=15, height=2)
      playerLabel.place(x= 550,y=0)
      lbl2 = tk.Label(self.master, text='Opponent : ',width=15, height=2).place(x= 400,y=35)
      opponentLabel = tk.Label(self.master, text=self.cPlayer.opponent,width=15, height=2)
      opponentLabel.place(x= 550,y=35)
      lbl3 = tk.Label(self.master, text="Who's turn: ",width=15, height=2).place(x= 400,y=70)
      self.turnLabel = tk.Label(self.master, text=self.cPlayer.username ,width=15, height=2)
      self.turnLabel.place(x= 550,y=70)

      lbl4 = tk.Label(self.master, text='Games Played: ',width=15, height=2).place(x= 400,y=110)
      self.totalGamesLabel = tk.Label(self.master, text='',width=15, height=2)
      self.totalGamesLabel.place(x= 550,y=110)
      lbl5 = tk.Label(self.master, text='Wins: ',width=15, height=2).place(x= 400,y=145)
      self.winsLabel = tk.Label(self.master, text='',width=15, height=2)
      self.winsLabel.place(x= 550,y=145)
      lbl6 = tk.Label(self.master, text='Losses: ',width=15, height=2).place(x= 400,y=180)
      self.lossesLabel = tk.Label(self.master, text='',width=15, height=2)
      self.lossesLabel.place(x= 550,y=180)
      lbl7 = tk.Label(self.master, text='Ties: ',width=15, height=2).place(x= 400,y=215)
      self.tiesLabel = tk.Label(self.master, text='',width=15, height=2)
      self.tiesLabel.place(x= 550,y=215)

   def receiveMove(self):
      '''Receives a move from the other player and updates the 3x3 board to show the other player's move
      '''
      while True:
         if self.connect_completed == True:
            try:
               pos = self.connectionSocket.recv(1024)
               pos = pos.decode()
               if pos != '':
                  self.cPlayer.lastPlayer = self.cPlayer.opponent
                  self.cPlayer.playMove(int(pos), 'O')
                  self.updateBoard(int(pos))
                  self.master.update_idletasks()
                  self.turnLabel['text'] = self.cPlayer.username
                  self.handleWin()   
            except:
               pass
   
   def updateBoard(self, newPos):
      '''Takes the move made by the other player and displays it in the GUI
      '''
      if newPos == 0:
         self.btn1['text'] = "O"
         self.btn1['highlightbackground'] = 'orange'
      elif newPos == 1:
         self.btn2['text'] = "O"
         self.btn2['highlightbackground'] = 'orange'
      elif newPos == 2:
         self.btn3['text'] = "O"
         self.btn3['highlightbackground'] = 'orange'
      elif newPos == 3:
         self.btn4['text'] = "O"
         self.btn4['highlightbackground'] = 'orange'
      elif newPos == 4:
         self.btn5['text'] = "O"
         self.btn5['highlightbackground'] = 'orange'
      elif newPos == 5:
         self.btn6['text'] = "O"
         self.btn6['highlightbackground'] = 'orange'
      elif newPos == 6:
         self.btn7['text'] = "O"
         self.btn7['highlightbackground'] = 'orange'
      elif newPos == 7:
         self.btn8['text'] = "O"
         self.btn8['highlightbackground'] = 'orange'
      elif newPos == 8:
         self.btn9['text'] = "O"
         self.btn9['highlightbackground'] = 'orange'

   def handleWin(self):
      '''Handles the program when a win condition is detected
      '''
      finish = self.cPlayer.isWinner()
      if finish:
         response = messagebox.askyesno('Play Again?', 'Want to play again?')
         if response:
            temp = 'Again'
            self.connectionSocket.send(temp.encode())
            self.cPlayer.updateGamesPlayed()
            self.turnLabel['text'] = self.cPlayer.username
            self.reset()
         else:
            self.cPlayer.updateGamesPlayed()
            self.connect_completed = False
            respo = 'Done'
            self.connectionSocket.send(respo.encode())
            self.connectionSocket.close()
            stat_holder = self.cPlayer.computeStats()
            self.totalGamesLabel['text'] = stat_holder[0]
            self.winsLabel['text'] = stat_holder[1]['X']
            self.lossesLabel['text'] = stat_holder[1]['O']
            self.tiesLabel['text'] = stat_holder[2]
            self.reset()

   def reset(self):
      '''Completely reset the 3x3 game board in preparation for a new game or the stats being printed.
      '''
      self.cPlayer.lastPlayer = self.cPlayer.opponent
      self.cPlayer.resetGameBoard()
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
   basicTicTakToe = TikUIpacker()
   createThread(basicTicTakToe.receiveMove)
   basicTicTakToe.runUI()