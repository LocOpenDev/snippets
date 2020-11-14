import random, sys

class Error(Exception):
    """Tictactoe module base Error class"""
    pass

class DuplicationInputError(Error):
    """Duplication input error"""
    pass

class OutOfRangeInputError(Error):
    """Out of range input error"""
    pass

class Node:
    """Tictactoe node
    
    Attributes:
        name: name of node (x or o)
    """

    def __init__(self, name):
        self.name = name
    
    def __eq__(self, other):
        return type(self) == type(other) and self.name == other.name

class Board:
    """Tictactoe game board"""

    def __init__(self):
        """Create 3x3 tictactoe game board"""
        self.board = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
        ]
        self.chose = set()
    
    def flat_board(self):
        """Flat self.board into list for later check win"""
        flated_board = []
        flated_board.extend(self.board)
        flated_board.extend([[row[i] for row in self.board] for i in range(3)])
        flated_board.append([self.board[0][0], self.board[1][1], self.board[2][2]])
        flated_board.append([self.board[0][2], self.board[1][1], self.board[2][0]])
        return flated_board

    def check_win(self):
        """Return win node name"""
        floated_board = self.flat_board()
        for row in floated_board:
            is_win = False
            for i in range(1, len(row)):
                if row[i - 1] == row[i]:
                    is_win = True
                else:
                    is_win = False
            if is_win:
                return row[0]

    def add_node(self, position, node):
        """Add node to self.board at position
        
        Exceptions:
            DuplicationInputError: when player input chose number, raise this exception
        """
        if position in self.chose:
            raise DuplicationInputError
        for row in self.board:
            for i in range(len(row)):
                if not isinstance(row[i], Node) and row[i] == str(position):
                    row[i] = node.name
                    self.chose.add(position)
                    return

    def display(self):
        """Display tictactoe game board"""
        print('|'.join(self.board[0]))
        print('-' * 5)
        print('|'.join(self.board[1]))
        print('-' * 5)
        print('|'.join(self.board[2]))

    def reset(self):
        """Reset game board for new game"""
        self.board = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
        ]
        self.chose = set()

def play():
    """Wow! Play tictactoe"""
    # Input two player name
    player1 = str(input('Input first player name: '))
    player2 = str(input('Input second player name: '))

    # Welcome
    print('{} - {}, welcome to Tictactoe game!\n'.format(player1, player2))

    # Random first play
    turn = random.randint(1, 2)

    player1_node = Node('x')
    player2_node = Node('o')

    # Create game board
    board = Board()
    print('Game start!!!')
    board.display()

    # Play game
    while True:
        if turn == 1:
            try:
                position = int(input('\n{} input your choice: '.format(player1)))
                if position <= 0 or position > 9:
                    raise OutOfRangeInputError
                board.add_node(position, player1_node)
                turn = 2
            except (ValueError, OutOfRangeInputError):
                print('Please input from 1 to 9!')
                continue
            except DuplicationInputError:
                print('{} is chose, please in put other choice!'.format(position))
                continue
        else:
            try:
                position = int(input('\n{} input your choice: '.format(player2)))
                if position <= 0 or position > 9:
                    raise OutOfRangeInputError
                board.add_node(position, player2_node)
                turn = 1
            except (ValueError, OutOfRangeInputError):
                print('Please input from 1 to 9!')
                continue
            except DuplicationInputError:
                print('{} is chose, please in put other choice!'.format(position))
                continue
        
        board.display()
        win = board.check_win()

        if win:
            if player1_node.name == win:
                print('\n*****', player1, 'win this game!!!*****\n')
            else:
                print('\n*****', player2, 'win this game!!!*****\n')
            
            while True:
                new_game = str(input('Play new game? (y/n): '))
                if new_game not in ['n', 'y']:
                    print('Please input y or n!')
                    continue
                if new_game == 'n':
                    sys.exit()
                else:
                    # Reset game board before new game start!!!
                    board.reset()
                    print('\nGame start!!!')
                    board.display()
                    # Random first play
                    turn = random.randint(1, 2)
                    break

if __name__ == '__main__':
    play()