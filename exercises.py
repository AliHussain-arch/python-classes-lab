class Game ():
    number_of_turns = 0

    def __init__(self,turn = 'X', tie = False, winner = None, board = {
  'a1': None, 'b1': None, 'c1': None,
  'a2': None, 'b2': None, 'c2': None,
  'a3': None, 'b3': None, 'c3': None,
}):
        self.turn = turn
        self.tie = tie
        self.winner = winner
        self.board = board
    
    def play_game(self):
        return print('Welcome to Tic-tac-toe')
    
    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        if(self.tie == True):
            print("Tie game!")
        elif(self.winner):
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")
    
    def render(self):
        self.print_message()
        self.print_board()
        if(self.number_of_turns < 9):
            self.number_of_turns += 1
    
    def get_move(self):
        if(not self.number_of_turns > 9 and not self.winner and not self.tie):
            move = input(f"Enter a valid move (example: A1): ").lower()
            legalmoves = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
            while(move not in legalmoves or self.board[move] != None):
                print('Invalid Move')
                move = input(f"Enter a valid move (example: A1): ").lower()
            self.board[move] = self.turn

    def check_winner(self):
        if(self.board['a1'] and (self.board['a1'] == self.board['b1'] == self.board['c1'])):
            self.winner = self.turn
        elif(self.board['a2'] and (self.board['a2'] == self.board['b2'] == self.board['c2'])):
            self.winner = self.turn
        elif(self.board['a3'] and (self.board['a3'] == self.board['b3'] == self.board['c3'])):
            self.winner = self.turn
        elif(self.board['a1'] and (self.board['a1'] == self.board['a2'] == self.board['a3'])):
            self.winner = self.turn
        elif(self.board['b1'] and (self.board['b1'] == self.board['b2'] == self.board['b3'])):
            self.winner = self.turn
        elif(self.board['c1'] and (self.board['c1'] == self.board['c2'] == self.board['c3'])):
            self.winner = self.turn
        elif(self.board['a1'] and (self.board['a1'] == self.board['b2'] == self.board['c3'])):
            self.winner = self.turn
        elif(self.board['c1'] and (self.board['c1'] == self.board['b2'] == self.board['a3'])):
            self.winner = self.turn

    def check_tie(self):
        if(self.winner == None and self.number_of_turns == 9 ):
            self.tie = True

    def play_game(self):
        print("Shall we play a game?")
        while(self.number_of_turns < 10 and not self.winner and not self.tie):
            self.render()
            self.get_move()
            self.check_winner()
            self.check_tie()
            self.turn = 'O' if self.turn == 'X' else 'X' 
        self.render()

game_instance = Game()
game_instance.play_game()
