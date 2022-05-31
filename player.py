class Player:
    """The Player of the game.
        The responsability of the Player is guess letters until guessed all of the word or loses their parachute.

        Attributes:
            _guessing(string): a guessed letter."""


    def __init__(self):  
        """Constructs a new player.

        Args:
            self (player): An instance of Player.
        """
        self._guessing = ''

    def guess_new(self):
        """Input a new letter and returns it.

        Args:
            self (player): An instance of Player.
        Returns:
            string: _guessing, the guessed letter.
        """
        self._guessing = input('Guess a letter (a-z): ')
        return self._guessing

    def keep_playing(self, counter):
        """Check how many times it guessed wrong to check if they can keep playing.

        Args:
            self (player): An instance of Player.
            counter(integer): A counter of how many times guessed wrong letters.
        Returns:
            boolean: play_again.
        """
        play_again = False
        if counter > 3:
            return play_again
        else:
            play_again = True
            return play_again