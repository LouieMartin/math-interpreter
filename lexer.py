from tokens import TokenType, Token

WHITESPACE = ' \t\r\n\f'
DIGITS = '.0123456789'

class Lexer:
  def __init__(self, text):
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
      if self.current_character in DIGITS:
        yield self.generate_number()
      elif self.current_character == '+':
        self.advance()
        yield Token(TokenType.PLUS)
      elif self.current_character == '-':
        self.advance()
        yield Token(TokenType.MINUS)
      elif self.current_character == '*':
        self.advance()
        yield Token(TokenType.MULTIPLY)
      elif self.current_character == '/':
        self.advance()
        yield Token(TokenType.DIVIDE)
      elif self.current_character == '(':
        self.advance()
        yield Token(TokenType.LPAREN)
      elif self.current_character == ')':
        self.advance()
        yield Token(TokenType.RPAREN)
      else:
        raise Exception(f'Illegal Character "{self.current_character}"')
  
  def generate_number(self):
    decimal_point_count = 0
    number_string: str = self.current_character

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

    return Token(TokenType.NUMBER, float(number_string))