from values import Number
from nodes import *

class Interpreter:
  def visit(self, node):
    method_name = f'visit_{type(node).__name__}'
    method = getattr(self, method_name)
    return method(node)
  
  def visit_NumberNode(self, node):
    return Number(node.value)
  
  def visit_AddNode(self, node):
    return Number(self.visit(node.left_node).value + self.visit(node.right_node).value)

  def visit_MinusNode(self, node):
    return Number(self.visit(node.left_node).value - self.visit(node.right_node).value)

  def visit_MultiplyNode(self, node):
    return Number(self.visit(node.left_node).value * self.visit(node.right_node).value)

  def visit_DivideNode(self, node):
    try:
      return Number(self.visit(node.left_node).value / self.visit(node.right_node).value)
    except:
      raise Exception('Runtime math error')

  def visit_PositiveNode(self, node):
    return Number(+self.visit(node.node).value)

  def visit_NegativeNode(self, node):
    return Number(-self.visit(node.node).value)