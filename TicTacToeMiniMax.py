# Tic-Tac-Toe solving agent utilizing minimax search.
# The player (you) will go against the the AI agent who is bound to never lose

import random

# the indexes of the winning combinations
winning_slots = (
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6])

def _other(Player):
    if Player == 'X':
        return 'O'
    return 'X'

# The Board class. Top left corner will be position 0 and bottom right corner will be position 8.
# The grid will be a one dimensional array.

class Board(object):
    def __init__(self, grid = None):
        if not grid:
            grid = [None for i in xrange(9)]
        self.grid = grid

    states_explored = 0

    #prints the board
    def _print(self):
        for element in [self.grid[x:x + 3] for x in xrange(0, 9, 3)]:
            print element
        print

    # checks if the current tic tac toe board is complete
    def _complete(self):
        if None not in self.grid:
            return True
        if self._winner():
            return True
        else:
            return False

    # returns the a list of indexes of all available spots on the board
    # used for exploring available states in _miniMax()
    def _openSlots(self):
        return [i for i, j in enumerate(self.grid) if j is None]

    # gets all the positions of a certain player (needed for checking winner)
    def _getPositions(self, Player):
        return [i for i, j in enumerate(self.grid) if j == Player]

    # checks and returns the winner, if no winner, then returns None
    def _winner(self):
        for player in ('X', 'O'):
            positions = self._getPositions(player)
            for combo in winning_slots:
                win = True
                for pos in combo:
                    if pos not in positions:
                        win = False
                if win:
                    return player
        return None

    # take turn for a certain player. E.g. Places an 'X' or an 'O' in the appropriate position
    def _takeTurn(self, position, Player):
        self.grid[position] = Player

    # Player 'X' will try to minimize, Player 'O' will try to maximize
    def _miniMax(self, state, Player):
        self.states_explored += 1 #increment number of states explored
        if state._complete():
            if state._winner() == 'X':
                return -1
            elif state._winner() == 'O':
                return 1
            else:
                return 0
        if Player == 'O': #maximizing player
            bestValue = -1
            for slot in state._openSlots():
                state._takeTurn(slot, Player) #take the move
                _value = self._miniMax(state, _other(Player)) #analyze the move for the opponent
                state._takeTurn(slot, None) #reverse the move
                if _value > bestValue: #update bestValue if _value returned from recursive call is bigger
                    bestValue = _value
            return bestValue
        if Player == 'X': #minimizing player
            bestValue = 1
            for slot in state._openSlots():
                state._takeTurn(slot, Player)
                _value = self._miniMax(state, _other(Player))
                state._takeTurn(slot, None)
                if _value < bestValue: #update bestValue
                    bestValue = _value
            return bestValue

# function that will return the best move for the 'X' player (minimizer)
def TakeTurnX(state, Player):
    state.states_explored = 0 #update states explored to be 0 with every new turn.
    a = 1
    moves = [] #will hold an array of best moves
    for slot in state._openSlots(): #will analyze making each available move with minimax
        state._takeTurn(slot, Player) #make the move
        _value = state._miniMax(state, _other(Player)) #analyze
        state._takeTurn(slot, None) #reverse the move
        if _value < a: #make decision
            a = _value
            moves = [slot]
        elif _value == a:
            moves.append(slot)
    print "Explored", state.states_explored, "states."
    print moves
    return random.choice(moves)

# Function that will return the best move for the 'O' player
def TakeTurnO(state, Player):
    state.states_explored = 0
    a = -1
    moves = []
    for slot in state._openSlots():
        state._takeTurn(slot, Player)
        _value = state._miniMax(state, _other(Player))
        state._takeTurn(slot, None)
        if _value > a:
            a = _value
            moves = [slot]
        elif _value == a:
            moves.append(slot)
    print "Explored", state.states_explored, "states."
    return random.choice(moves)


# initialization and running of the game below
print "Welcome to Tic-Tac-Toe!"

while True:
    choice = raw_input("Would you like to go first 'X' or second 'O'?")
    if choice in ["first", "1st", "1", "f", "X", "x"]:
        player = 'X'
    else:
        player = 'O'

    board = Board()
    board._print()

    if player == 'X': # PLayer will go first
        while not board._complete():
            player_move = int(raw_input("Your next move in 1-index: ")) - 1
            if not player_move in board._openSlots():
                continue
            board._takeTurn(player_move, player)
            board._print()

            if board._complete():
                break
            player = _other(player)
            computer_move = TakeTurnO(board, player)
            board._takeTurn(computer_move, player)
            board._print()
            player = _other(player)
    elif player == 'O': #Computer will go first
        while not board._complete():
            computer_move = TakeTurnX(board, _other(player))
            board._takeTurn(computer_move, _other(player))
            board._print()

            if board._complete():
                break
            # player = _other(player)
            player_move = int(raw_input("Your next move in 1-index: ")) - 1
            if not player_move in board._openSlots():
                continue
            board._takeTurn(player_move, player)
            board._print()


    print "And the winner is", board._winner(), "!"

    choice = raw_input("Would you like to play again? Yes 'Y' or No 'N'")
    if choice in ["n", "N", "NO", "No", "no", "2"]:
        print "Thank you for playing!"
        break
