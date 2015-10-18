# simple binary tree
# in this implementation, a node is inserted between an existing node and the root


class BinaryTree():

    def __init__(self,rootid):
      self.left = None
      self.right = None
      self.rootid = rootid

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.rootid = value
    def getNodeValue(self):
        return self.rootid
    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree        
    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.left = self.left
            self.left = tree
    def preOrder(self):
        print(self.rootid)
    	if self.left:
        	self.left.inOrder()
        if self.right:
        	self.right.inOrder()
    def inOrder(self):
    	if self.left:
        	self.left.inOrder()
        print(self.rootid)
        if self.right:
        	self.right.inOrder()
    def postOrder(self):
    	if self.left:
        	self.left.inOrder()
        if self.right:
        	self.right.inOrder()
        print(self.rootid)
            


# test tree

def testTree():
    myTree = BinaryTree("Maud")
    myTree.insertLeft("Bob")
    myTree.insertLeft("Lisa")
    myTree.insertRight("Tony")
    myTree.insertRight("Steven")
    print 'inorder----------------'
    myTree.inOrder()
    print 'preorder----------------'
    myTree.preOrder()
    print 'postorder----------------'
    myTree.postOrder()



if __name__ == '__main__':
    testTree()
        
