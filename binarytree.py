class BinaryTree:
  def __init__(self,value):
    self.left = None
    self.right = None
    self.data = value

  def insert(self, value):
    ask = input('which node want to insert L/R:\t')
    if ask == 'L' :
      self.left = BinaryTree(value)
    elif ask == 'R' :
      self.right = BinaryTree(value)
    else :
      print('No insertion')

  def printTree(self):
    print(self.data)
    if self.left != None :
      print('Left',end=' ')
      self.left.printTree()
    if self.right != None :
      print('right',end=' ')
      self.right.printTree()

root = int(input('Enter root value:'))
obj = BinaryTree(root)
while True :
  i = input('do want to insert:y/n\t')
  if i == 'y' :
    obj.insert(int(input('Enter node value:\t')))
  else :
    break
obj.printTree()