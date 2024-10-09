import random
class Die:
  """Represents a single Die. Default to a 6-sided die.
  Attributes:
    sides(int): number of sides on the die.
    value(int): the value of the rolled die.
  """
  def __init__(self, sides = 6):
    """Sets the number of sides of the die(default 6)."""
    self._sides = sides
    self._value = 0

  def roll(self):
    """Rolls the die to set the value of the die.
    Return value of random between 1-6 between 1-sides.
    """
    self._value = random.randint(1, self._sides)
    return self._value

  def __str__(self):
    """Returns that string representation of the die."""
    return str(self._value)

  def __lt__(self,other):
    """Compare the two dice. Returns True if value of self less than value of other."""
    return self._value < other._value

  def __eq__(self,other):
    """Compares the two dice. Returns True if they are equal."""
    return self._value == other._value
    
  def __sub__(self,other):
    """Returns the difference of the values of self and other after subtracting"""
    return self._value - other._value