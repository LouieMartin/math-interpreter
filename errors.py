class IllegalCharacterError(Exception):
  def __init__(self, character):
    super().__init__(f'Illegal Character: \'{character}\'')

class MathError(Exception):
  def __init__(self, message):
    self.message = f'Math Error: {message}'

    super().__init__(self.message)
