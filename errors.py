class IllegalCharacterError(Exception):
  def __init__(self, character):
    super().__init__(f'Illegal Character: \'{character}\'')

class MathError(Exception):
  def __init__(self, message):
    super().__init__(f'Math Error: {message}')