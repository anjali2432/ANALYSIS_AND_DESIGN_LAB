class BinaryTree:
  def __init__(self,value):
    self.left = None
    self.right = None
    self.data = value
  def insert(self, value):
    if value <= self.data:
      if self.left is None:
        self.left = BinaryTree(value)
      else:
        self.left.insert(value)
    else:
      if self.right is None:
        self.right = BinaryTree(value)
      else:
        self.right.insert(value)
  def printTree(self):
    if self.left is not None:
      self.left.printTree()
    print(self.data)
    if self.right is not None:
      self.right.printTree()

root = int(input('Enter root value:'))
obj = BinaryTree(root)
while True:
  i = input('do you want to insert:y/n\t')
  if i == 'y':
    obj.insert(int(input('Enter node value:\t')))
  else:
    break
obj.printTree()
