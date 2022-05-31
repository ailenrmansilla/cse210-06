from jumper.player import Player
from jumper.secret_word import Secret_word
from jumper.parachute import Parachute

class Puzzle:
    """The controler of the game.
    The responsability of the Puzzle is to run the game calling to other classes and their class methods.
    Attributes:
        _playing (boolean): The location of the hider (1-1000).
        _guessedletters (string): A string with the wrong guessed letters."""
    def __init__(self):
        """Constructs a new puzzle.

        Args:
            self (puzzle): An instance of Puzzle.
        """
        self._playing = True
        self._guessedletters = ''
        
    def printGuessedLetters(self):
        """Prints the wrong guessed letters in the same line, separated by a '-'.

        Args:
            self (puzzle): An instance of Puzzle.
        """
        print('\nLetters already guessed: ', end=' ')
        for i in range(0,len(self._guessedletters)):
            print(self._guessedletters[i], end=' - ')
        print()
        
    def playing(self):
        """Starts the Jumper game and runs it until the Player has not a parachute.
        It calls the class methods of each class (Player, Secret_word, and Parachute) to play it.
        When the player guessed all of the letters it will print a message telling them "You win!"
        If they lost, it will print a message telling them "You lost!" and revealing the secret word.
        It prints a message saying "Thanks for playing!".

        Args:
            self (puzzle): An instance of Puzzle.
        
        """
        counter = 0
        player = Player()
        parachute = Parachute()
        word = Secret_word()
        parachute.print_parachute()
        word.setSecretWord()
        word.setSecretWordOculted()
        word.getSecretWord()
        word.printSecretWordOculted()
        while self._playing:
            guessed_letter = player.guess_new()
            checking = word.is_letter(guessed_letter)
            if checking == True:
                print('Correct!')
            else:
                counter += 1
                print('That letter is not in the word!')
                parachute.point_lost(counter)
                self._guessedletters += guessed_letter
            if word.winner():
                print('---You win!---')
                break
            if player.keep_playing(counter):
                parachute.print_parachute()
                word.printSecretWordOculted()
                if self._guessedletters != '':
                    self.printGuessedLetters()
            else: 
                parachute.print_parachute()
                print('\n---You lost!---')
                print('The word was:')
                print(word.getSecretWord())
                break
        print('Thanks for playing!')
                            
