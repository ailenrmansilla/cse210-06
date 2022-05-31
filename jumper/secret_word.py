import random
class Secret_word:
    """The secret word's controller.
    The responsability of the Secret_word object is to choose a random word to guess, 
    print it, and print the same word replaced by '-' to guess.

    Attributes:
        _possible words: An array with different words.
        _secretWord: A word from the array of possible words.
        _secretWordOculted: The secret word replaced with '-' at the beginning, and then with its guessed letters."""

    def __init__(self):
        """Constructs a new Secret_word object.

        Args:
            self (Secret_word): An instance of Secret_word.
        """

        self._possibleWords = ['carpet','mahogany','spaceship','eukaryote','digital','calculus','pillar','comforter','restauration','rampant']
        self._secretWord = ''
        self._secretWordOculted = []

    def getSecretWord(self):
        """Returns _secretWord.

        Args:
            self (secret_word): An instance of Secret_word.
        Returns:
            string: the value of _secretWord.
        """
        return self._secretWord
    
    def printSecretWordOculted(self):
        """Prints each letter in _secretWordOculted in a same line separated by a ' '.

        Args:
            self (secret_word): An instance of Secret_word.
        """

        for i in range(0, len(self._secretWordOculted)):
            print(self._secretWordOculted[i],end=' ')

    def setSecretWord(self):
        """Choose randomly a word from _possibleWords and assigns it to _secretWord.

        Args:
            self (secret_word): An instance of Secret_word.
        """
        self._secretWord = self._possibleWords[random.randint(0,9)]
    
    def setSecretWordOculted(self):   
        """Goes through every letter in the string _secretWord and append
        a '-' each time in the _secretWordOculted string.

        Args:
            self (secret_word): An instance of Secret_word.
        """
        for i in range(0,len(self._secretWord)):
            self._secretWordOculted.append('-')
            
    def change_letter(self,i):
        """Choose randomly a word from _possibleWords and assigns it to _secretWord.

        Args:
            self (secret_word): An instance of Secret_word.
            i (integer): the position in the _secretWordOculted to exchange by the letter in _secretWord stored in that same index.
        """
        letter = self._secretWord[i]
        self._secretWordOculted.insert(i,letter)
        del self._secretWordOculted[i+1]

    def is_letter(self, guessed):
        """Check if that letter is inside the string _secretWord.
        If it is, it calls the change_letter(i) method and returns True. 
        If it is not in the string, it returns False.

        Args:
            self (secret_word): An instance of Secret_word.
            guessed(string): A guessed letter.
        Returns:
            boolean: it_is
        """
        it_is = False
        if guessed in self._secretWord:
            for i in range(0,len(self._secretWord)):
                if self._secretWord[i] == guessed:  
                    self.change_letter(i)
                    it_is = True
        return it_is

    def winner(self):
        """Check if the Player has guessed all the secret word.
        It compares every letter in _secretWord with each one in _secretWordOculted,
        if they all are right, it returns True.

        Args:
            self (secret_word): An instance of Secret_word.
           
        Returns:
            boolean: winner
        """
        winner = False
        for i in range(0,len(self._secretWord)):
            if self._secretWord[i] == self._secretWordOculted[i]:
                winner = True
            else:
                winner = False
                return winner
        return winner
      