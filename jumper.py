# The puzzle is a secret word randomly chosen from a list.
# The player guesses a letter in the puzzle.
# If the guess is correct, the letter is revealed.
# If the guess is incorrect, a line is cut on the player's parachute.
# If the puzzle is solved the game is over.
# If the player has no more parachute the game is over.
import random

class Puzzle:
    def __init__(self):
        self._playing = True
        self._guessedletters = ''
        
    def printGuessedLetters(self):
        print('\nLetters already guessed: ', end=' ')
        for i in range(0,len(self._guessedletters)):
            print(self._guessedletters[i], end=' - ')
        print()
        
    def playing(self):
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
                            


        

class Player:
    def __init__(self):
        self._guessing = ''

    def guess_new(self):
        self._guessing = input('Guess a letter (a-z): ')
        return self._guessing

    def keep_playing(self, counter):
        play_again = False
        if counter > 3:
            return play_again
        else:
            play_again = True
            return play_again

    
class Secret_word:
    def __init__(self):
        self._possibleWords = ['carpet','mahogany','spaceship','eukaryote','digital','calculus','pillar','comforter','restauration','rampant']
        self._secretWord = ''
        self._secretWordOculted = []

    def getSecretWord(self):
        return self._secretWord
    
    def printSecretWordOculted(self):
        for i in range(0, len(self._secretWordOculted)):
            print(self._secretWordOculted[i],end=' ')

    def setSecretWord(self):
        self._secretWord = self._possibleWords[random.randint(0,9)]
    
    def setSecretWordOculted(self):   
        for i in range(0,len(self._secretWord)):
            self._secretWordOculted.append('-')
            
    def change_letter(self,i):
        letter = self._secretWord[i]
        self._secretWordOculted.insert(i,letter)
        del self._secretWordOculted[i+1]

    def is_letter(self, guessed):
        it_is = False
        if guessed in self._secretWord:
            for i in range(0,len(self._secretWord)):
                if self._secretWord[i] == guessed:  
                    self.change_letter(i)
                    it_is = True
        return it_is

    def winner(self):
        winner = False
        for i in range(0,len(self._secretWord)):
            if self._secretWord[i] == self._secretWordOculted[i]:
                winner = True
            else:
                winner = False
                return winner
        return winner
            
        

class Parachute:
    def __init__(self):
        self._parachute = [' ---',"/    \\","\    /"," \  /\n  O"," /|\ \n / \\"]

    def point_lost(self, counter):
        if counter == 4:
            self._parachute[counter-1] = '  X'
        else:
            self._parachute[counter-1] = ' '
        return self._parachute

    def print_parachute(self):
        for line in self._parachute:
            print(line)


puzzle = Puzzle()
puzzle.playing()