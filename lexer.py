from errors import IllegalCharacterError
from tokens import TokenType, Token

WHITESPACE = ' \t\r\n\f'
DIGITS = '.0123456789'

characters = {
  '+': TokenType.PLUS,
  '-': TokenType.MINUS,
  '/': TokenType.DIVIDE,
  '(': TokenType.LPAREN,
  ')': TokenType.RPAREN
}

class Lexer:
  def __init__(self, text):
    self._text = text
    self.text = iter(text)
    self.advance()
  
  def advance(self):
    try:
      self.current_character = next(self.text)
    except StopIteration:
      self.current_character = None
  
  def generate_tokens(self):
    while self.current_character != None:
      if self.current_character in WHITESPACE:
        self.advance()
      elif self.current_character in DIGITS:
        yield self.generate_number()
      elif self.current_character == '*':
        self.advance()

        token = Token(TokenType.POWER) if self.current_character == '*' else Token(TokenType.MULTIPLY)

        self.advance()

        yield token
      else:
        if self.current_character not in characters:
          raise IllegalCharacterError(self.current_character)
        
        yield Token(characters[self.current_character])
        self.advance()
  
  def generate_number(self):
    decimal_point_count = 1 if self.current_character == '.' else 0
    number_string = self.current_character

    self.advance()

    while self.current_character != None and self.current_character in DIGITS:
      if self.current_character == '.':
        decimal_point_count += 1
        if decimal_point_count > 1:
          break
      
      number_string += self.current_character
      self.advance()
    
    if number_string.startswith('.'):
      number_string = '0' + number_string
    if number_string.endswith('.'):
      number_string += '0'

    if decimal_point_count == 0:
      return Token(TokenType.INTEGER, int(number_string))
    else:
      return Token(TokenType.FLOAT, float(number_string))