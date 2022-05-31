class Parachute:
    """The controler of the parachute.
    The responsability of the Parachute is to print the parachute every round and control 
    if the player has lost or not their parachute.

    Attributes:
        _parachute (array of strings): The characters for each level of the parachute.
    """
    def __init__(self):
        """Constructs a new Parachute inside an array.

        Args:
            self (parachute): An instance of Parachute.
        """
        self._parachute = [' ---',"/    \\","\    /"," \  /\n  O"," /|\ \n / \\"]

    def point_lost(self, counter):
        """Gets an integer with the amount of times the player guessed wrong.
        It writes a blank space in each position of _parachute. When the Player loses all
        of their parachute after the third wrong try, it replaces the head of the player with an 'X'.

        Args:
            self (parachute): An instance of Parachute.
            counter: an integer counting how many times the player guessed wrong.
        
        Returns:
            array of string: _parachute.
        """
        if counter == 4:
            self._parachute[counter-1] = '  X'
        else:
            self._parachute[counter-1] = ' '
        return self._parachute

    def print_parachute(self):
        """Prints each line of the _parachute array.

        Args:
            self (parachute): An instance of Parachute.
        """
        for line in self._parachute:
            print(line)

