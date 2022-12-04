from tokens import TokenType, KEYWORDS, Token
from errors import IllegalCharacterError
from string import ascii_letters

WHITESPACE = ' \t\r\n\f'
LETTERS = ascii_letters
DIGITS = '.0123456789'

characters = {
  '+': TokenType.PLUS,
  '-': TokenType.MINUS,
  '*': TokenType.MULTIPLY,
  '/': TokenType.DIVIDE,
  '^': TokenType.POWER,
  '=': TokenType.EQUALS,
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
      elif self.current_character in LETTERS:
        yield self.generate_identifier()
      elif self.current_character in DIGITS:
        yield self.generate_number()
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
  
  def generate_identifier(self):
    identifier_string = ''

    while self.current_character != None and self.current_character in LETTERS + DIGITS + '_':
      identifier_string += self.current_character
      self.advance()

    token_type = TokenType.KEYWORD if identifier_string in KEYWORDS else TokenType.IDENTIFIER
    token = Token(token_type, identifier_string)

    return token
