class Task:
  """Represents a task in list.
  Attribute:
    desc(string): description of task.
    date(string): due day of task. (MM/DD/YYYY)
    time(string): time of task. (HH:MM)
  """

  def __init__(self, desc="", date="", time=""):
    """Initializes a Task object with a description, date, and time."""
    self.description = desc
    self.date = date
    self.time = time

  def get_description(self):
    """Returns the task's description."""
    return self.description

  def __str__(self):
    """Returns the task's information for display."""
    return f"{self.description} - Due: {self.date} at {self.time}"

  def __repr__(self):
    """Returns a string to write the task's information to the file."""
    return f"{self.description},{self.date},{self.time}"

  def __lt__(self, other):
    """Compares tasks by year, month, day, hour, minute, then description alphabetically."""
    #self month,day,year
    #self hour,minute

    month_self, day_self, year_self = self.date.split("/")

    hour_self, minute_self = self.time.split(":")

    #other month,day,year
    #other hour, minute
    month_other, day_other, year_other = other.date.split("/")

    hour_other, minute_other = other.time.split(":")

    return (year_self,month_self,day_self,hour_self,minute_self,self.description) <\
    (year_other,month_other,day_other,hour_other,minute_other,other.description)
