class IllegalCharacterError(Exception):
  def __init__(self, character):
    self.message = f'Illegal Character: \'{character}\''

    super().__init__(self.message)

class MathError(Exception):
  def __init__(self, message):
    self.message = f'Math Error {message}'

    super().__init__(self.message)