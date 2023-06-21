class MDate(object):

  def __init__(self, year=1900, month=1, day=1):
    for arg in [year, month, day]:
      if type(arg) != int:
        raise TypeException('Year, month, and day must be `int`')

    self.year = year
    self.month = month
    self.day = day
