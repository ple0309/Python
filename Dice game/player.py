import die
class Player:
  """Represents the 3 dies when they have pair, series or three of kinds.
  Attribute:
    dice: a list of 3 Die objects.
    points(int): the point of player.
  """
  def __init__(self):
    """Creating 3 random dies and setting default points of the player."""
    self._dice = sorted([die.Die(),die.Die(),die.Die()])
    self._points = 0

  def get_points(self):
    """Return the points after rolling."""
    return self._points

  def roll_dice(self):
    """Rolling and getting the value for each die."""
    for i in self._dice:
      i.roll()
    self._dice.sort()
    
    
  def has_pair(self):
    """Return True if it has pair. 
    Points will be added by 1.
    """
    if self._dice[0] == self._dice[1] or self._dice[0] == self._dice[2] or self._dice[1] == self._dice[2]:
      self._points += 1
      return True

  def has_three_of_a_kind(self):
    """Return True if it has three of a kind.
    Points will be added by 3.
    """
    if self._dice[0] == self._dice[1] and self._dice[0] == self._dice[2]:
      self._points += 3
      return True

  def has_series(self):
    """Return True if it has series.
    Points will be added by 2.
    """
    if self._dice[2] - self._dice[1] == 1 and self._dice[1] - self._dice[0] == 1:
      self._points += 2
      return True

  def __str__(self):
    """Return the string in the format showing to the player."""
    return "D1=" + str(self._dice[0]) + ", D2=" + str(self._dice[1]) + ", D3=" + str(self._dice[2])