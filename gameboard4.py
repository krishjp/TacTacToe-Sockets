
class BoardClass:
    """A simple class to store and handle information about the players.

    Attributes:
        username (str): The username of the player
        opponent(str): The username of the opponent
        lastPlayer (str): The user name of the last player to have a turn
        wins (int): Total number of wins
        ties (int): Total number of ties
        losses (int): Total number of losses
        totalGames (int): Total games played
        board (list[str]): A list representing the playing board

    """
    def __init__(self, username: str = "", opponent: str = "",lastPlayer: str = "", ties: int = 0, totalGames: int = 0, board: list = []) -> None:
        """Initialize the BoardClass
        Args:
            
        """
        self.setUsername(username)
        self.setLastPlayer(lastPlayer)
        self.opponent = opponent
        self.wins = {'X': 0, 'O': 0}
        self.loss = {'X': 0, 'O': 0}
        self.ties = ties
        self.totalGames = totalGames
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    
    def lastPlayUpdater(self, newLast: str) -> None:
        """Updates the last player to make a move.

        Args:
            newLast(str): last player to make a move.
        """
        self.lastPlayer = newLast

    def setUsername(self, username: str) -> None:
        """Set the username of the player.

        Args:
            username(str): username of the player.
        """
        self.username = username
    
    def setLastPlayer(self, lastPlayer: str) -> None:
        """Set the username of the last player to play.

        Args:
            lastPlayer(str): the user name of the last player to have a turn.
        """
        self.lastPlayer = lastPlayer
    
    def updateGamesPlayed(self) -> None:
        """Increment the times the user has played the game by 1.
        """
        self.totalGames += 1

    def updateBoard(self, input: int, symbol: str) -> None:
        """Updates the board with a player's move.

        Args:
            input(int): The user's input
            symbol(str): The string ('X' or 'O') that will be placed in the location the user selected
        """
        self.board[int(input)-1] = symbol
    
    def resetGameBoard(self) -> None:
        """Completely reset the game board list
        """
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def isWinner(self):       
        win = False
        if (self.board[0]==self.board[1] and self.board[0]==self.board[2] and self.board[0]=="O") or (self.board[3]==self.board[4] and self.board[3]==self.board[5] and self.board[3]=="O") or (self.board[6]==self.board[7] and self.board[6]==self.board[8] and self.board[6]=="O"):
            win = True
            self.wins["O"] = self.wins["O"] + 1
            self.loss["X"] = self.loss["X"] + 1
        elif (self.board[0]==self.board[3] and self.board[0]==self.board[6] and self.board[0]=="O") or (self.board[1]==self.board[4] and self.board[1]==self.board[7] and self.board[1]=="O") or (self.board[2]==self.board[5] and self.board[2]==self.board[8] and self.board[2]=="O"):
            win = True
            self.wins["O"] = self.wins["O"] + 1
            self.loss["X"] = self.loss["X"] + 1
        elif (self.board[0]==self.board[1] and self.board[0]==self.board[2] and self.board[0]=="X") or (self.board[3]==self.board[4] and self.board[3]==self.board[5] and self.board[3]=="X") or (self.board[6]==self.board[7] and self.board[6]==self.board[8] and self.board[6]=="X"):
            win = True
            self.wins["X"] = self.wins["X"] + 1
            self.loss["O"] = self.loss["O"] + 1
        elif (self.board[0]==self.board[3] and self.board[0]==self.board[6] and self.board[0]=="X") or (self.board[1]==self.board[4] and self.board[1]==self.board[7] and self.board[1]=="X") or (self.board[2]==self.board[5] and self.board[2]==self.board[8] and self.board[2]=="X"):
            win = True
            self.wins["X"] = self.wins["X"] + 1
            self.loss["O"] = self.loss["O"] + 1
        elif (self.board[0]==self.board[4] and self.board[0]==self.board[8] and self.board[0]=="X") or (self.board[6]==self.board[4] and self.board[6]==self.board[2] and self.board[6]=="X"):
            win = True
            self.wins["X"] = self.wins["X"] + 1
            self.loss["O"] = self.loss["O"] + 1
        elif (self.board[0]==self.board[4] and self.board[0]==self.board[8] and self.board[0]=="O") or (self.board[6]==self.board[4] and self.board[6]==self.board[2] and self.board[6]=="O"):
            win = True
            self.wins["O"] = self.wins["O"] + 1
            self.loss["X"] = self.loss["X"] + 1
        elif self.boardIsFull():
            win = True
        
        return win
    
    def boardIsFull(self) -> bool:
        """Checks each position of the board and tallys up the total number of filled spots.
        If all positions are filled, returns True and increment ties and total games played.
        Otherwise, return False.
        """
        filled = 0
        for i in range(9):
            if self.board[i] == 'X' or self.board[i] == 'O':
                filled += 1
        if filled != 9:
            return False
        elif filled == 9:
            self.ties += 1
            return True
        
    def playMove(self,position, key):
        self.board[position] = key
        self.lastMove = self.username

    def computeStats(self) -> list:
        """Returns the stats for a user in a list.
        """
        holder = []
        holder.append(self.totalGames)
        holder.append(self.wins)
        holder.append(self.ties)
        return holder
        