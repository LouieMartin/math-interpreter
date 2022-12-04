from dataclasses import dataclass
from enum import Enum

KEYWORDS = ['var']

class TokenType(Enum):
  INTEGER      = 0
  FLOAT        = 1
  IDENTIFIER   = 2
  KEYWORD      = 3
  PLUS         = 4
  MINUS        = 5
  MULTIPLY     = 6
  DIVIDE       = 7
  POWER        = 8
  EQUALS       = 9
  LPAREN       = 10
  RPAREN       = 11

@dataclass
class Token:
  type: TokenType
  value: any = None

  def __repr__(self):
    return self.type.name + (f':{self.value}' if self.value != None else '')
  
  def matches(self, type, value):
    return self.type == type and self.value == value