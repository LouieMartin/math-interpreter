from dataclasses import dataclass
from enum import Enum

class TokenType(Enum):
  INTEGER    = 0
  FLOAT      = 1
  PLUS       = 2
  MINUS      = 3
  MULTIPLY   = 4
  DIVIDE     = 5
  POWER      = 6
  LPAREN     = 7
  RPAREN     = 8

@dataclass
class Token:
  type: TokenType
  value: any = None

  def __repr__(self):
    return self.type.name + (f':{self.value}' if self.value != None else '')