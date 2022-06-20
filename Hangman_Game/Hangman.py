import random

# HANGMAN SET UP

gallows = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# RANDOM WORD GENERATION

def random_word():
    file = 'E:\Documents\GitHub\Python_Learning_Activities\Hangman_Game\word_bank.txt'
    with open(file, "rt") as f:
        bank = f.readlines()
        return bank[random.randint(0, len(bank))].strip()

# GAME PROCESSES

class Hangman():
    def __init__(self, word):
        self.word = word
        self.status = 0
        self.board = ['_'] * len(self.word)
        self.wrong_guesses = []

    def guess(self, letter):
        self.letter = letter

        if self.letter in self.word:
            i = 0
            for char in self.word:
                if char == self.letter:
                    self.board[i] = self.letter
                i += 1
        else:
            self.wrong_guesses.append(self.letter)
            print('Wrong guess!')
            self.status += 1

    def print_game_status(self):
        print(gallows[self.status])
        print(*self.board)
        print('Wrong guesses:', *self.wrong_guesses, sep=", ")

    def game_over(self):
        if (self.status == 6):
            self.print_game_status()
            print('GAME OVER! YOU LOSE.')
            print('The word is', self.word)
            return True
        if ('_' not in self.board):
            self.print_game_status()
            print('YOU WIN!')
            return True
        else:
            return False

# GAME EXECUTION

def main():
    game = Hangman(random_word())
    while not game.game_over():
        game.print_game_status()
        letter = input('Guess a letter: ')
        game.guess(letter)
        
main()
