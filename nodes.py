from dataclasses import dataclass

@dataclass
class NumberNode:
  value: float

  def __repr__(self):
    return f'{self.value}'

@dataclass
class AddNode:
  left_node: any
  right_node: any

  def __repr__(self):
    return f'({self.left_node} + {self.right_node})'

@dataclass
class MinusNode:
  left_node: any
  right_node: any

  def __repr__(self):
    return f'({self.left_node} - {self.right_node})'
  
@dataclass
class MultiplyNode:
  left_node: any
  right_node: any

  def __repr__(self):
    return f'({self.left_node} * {self.right_node})'

@dataclass
class DivideNode:
  left_node: any
  right_node: any

  def __repr__(self):
    return f'({self.left_node} / {self.right_node})'

@dataclass
class PositiveNode:
  node: any

  def __repr__(self):
    return f'(+{self.node})'

@dataclass
class NegativeNode:
  node: any

  def __repr__(self):
    return f'(-{self.node})'