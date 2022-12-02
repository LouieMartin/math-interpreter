from interpreter import Interpreter
from _parser import Parser
from lexer import Lexer

while True:
  try:
    text = input('>>> ')
    lexer = Lexer(text)
    tokens = lexer.generate_tokens()
    parser = Parser(tokens)
    tree = parser.parse()
    if not tree:
      continue
    interpreter = Interpreter()
    value = interpreter.visit(tree)
    print(value)
  except KeyboardInterrupt:
    print('\nQuit')
    quit()
  # except Exception as error:
  #   print(error)