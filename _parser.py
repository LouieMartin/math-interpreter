from tokens import TokenType
from nodes import *

class Parser:
  def __init__(self, tokens):
    self.tokens = iter(tokens)
    self.advance()
  
  def raise_error(self):
    raise Exception('Invalid Syntax')

  def advance(self):
    try:
      self.current_token = next(self.tokens)
    except StopIteration:
      self.current_token = None
  
  def parse(self):
    if self.current_token == None:
      return None

    result = self.expression()

    if self.current_token != None:
      self.raise_error()

    return result

  def expression(self):
    result = self.term()

    if self.current_token.matches(TokenType.KEYWORD, 'var'):
      self.advance()

      if self.current_token.type != TokenType.IDENTIFIER:
        self.raise_error()

      variable_name = self.current_token

      self.advance()

      if self.current_token.type != TokenType.EQUALS:
        self.raise_error()

      self.advance()

      # Something...

    while self.current_token != None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
      if self.current_token.type == TokenType.PLUS:
        self.advance()
        result = AddNode(result, self.term())
      elif self.current_token.type == TokenType.MINUS:
        self.advance()
        result = MinusNode(result, self.term())
    
    return result
  
  def term(self):
    result = self.factor()

    while self.current_token != None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
      if self.current_token.type == TokenType.MULTIPLY:
        self.advance()
        result = MultiplyNode(result, self.factor())
      elif self.current_token.type == TokenType.DIVIDE:
        self.advance()
        result = DivideNode(result, self.factor())

    return result
  
  def factor(self):
    token = self.current_token

    if token.type == TokenType.PLUS:
      self.advance()
      return PositiveNode(self.factor())
    elif token.type == TokenType.MINUS:
      self.advance()
      return NegativeNode(self.factor())
    
    return self.power()
  
  def power(self):
    result = self.atom()

    while self.current_token != None and self.current_token.type == TokenType.POWER:
      self.advance()
      result = PowerNode(result, self.factor())

    return result

  def atom(self):
    token = self.current_token

    if token.type == TokenType.LPAREN:
      self.advance()

      result = self.expression()

      if self.current_token.type != TokenType.RPAREN:
        self.raise_error()

      self.advance()
      return result
    elif token.type in (TokenType.INTEGER, TokenType.FLOAT):
      self.advance()
      return NumberNode(token.value)
    elif token.type == TokenType.IDENTIFIER:
      self.advance()
      
      # Something...
    
    self.raise_error()