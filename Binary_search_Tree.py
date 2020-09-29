class BinarySearchTree:
    # This is a Node class that is internal to the BinarySearchTree class. 
    class Node:
        def __init__(self,val,left=None,right=None):
            self.val = val
            self.left = left
            self.right = right
            
        def getVal(self):
            return self.val
        
        def setVal(self,newval):
            self.val = newval
            
        def getLeft(self):
            return self.left
        
        def getRight(self):
            return self.right
        
        def setLeft(self,newleft):
            self.left = newleft
            
        def setRight(self,newright):
            self.right = newright
            
        # This method deserves a little explanation. It does an inorder traversal
        # of the nodes of the tree yielding all the values. In this way, we get
        # the values in ascending order.
        def __iter__(self):
            if self.left != None:
                for elem in self.left:
                    yield elem
                    
            yield self.val
            
            if self.right != None:
                for elem in self.right:
                    yield elem

        def __repr__(self):
            return "BinarySearchTree.Node(" + repr(self.val) + "," + repr(self.left) + "," + repr(self.right) + ")"            
            
    # Below are the methods of the BinarySearchTree class. 
    def __init__(self, root=None,parent=None):
        self.root = root
        
    def insert(self,val):
        self.root = BinarySearchTree.__insert(self.root,val)
        
    def __insert(root,val):
        if root == None:
            return BinarySearchTree.Node(val)
        
        if val < root.getVal():
            root.setLeft(BinarySearchTree.__insert(root.getLeft(),val))
        else:
            root.setRight(BinarySearchTree.__insert(root.getRight(),val))
            
        return root
        
    def __iter__(self):
        if self.root != None:
            return iter(self.root)
        else:
            return iter([])

    def __str__(self):
        return "BinarySearchTree(" + repr(self.root) + ")"
        
    def delete(self,val):
    	BinarySearchTree.__delete(self.root,val)
    	
    
    def __delete(root,val):
    	node=root
    	
    	while val != node.getVal():
    		if val<node.getVal():
    			prenode=node
    			node=node.getLeft()
    		else:
    			prenode=node
    			node=node.getRight()
    	if node.getLeft()== None and node.getRight()== None:
    		node.setVal(None)
    	
    	if node.getLeft()==None and node.getRight()!=None:
    		prenode.setRight(node.getRight())
    		node.setRight(None)
    		
    	if node.getRight()==None and node.getLeft()!=None:
    		prenode.setLeft(node.getLeft())
    		node.setLeft(None)
    		
    		
    	if node.getLeft()!=None and node.getRight()!=None:
    		delNodeVal= node.getVal()
    		NodeRight=node.getLeft()
    		curNodeVal=NodeRight.getVal()
    		while NodeRight.getRight()!=None:
    			NodeRight=NodeRight.getRight()
    			curNodeVal=NodeRight.getVal()
    		NodeRight.setVal(None)
    		node.setVal(None)
    		NodeRight.setVal(delNodeVal)
    		node.setVal(curNodeVal)
    		NodeRight.setVal(None)
    	return root
    		
    		
    		
    		
    		
    	

    				