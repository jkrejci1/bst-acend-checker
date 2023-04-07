import queue

class LinkedBinaryTree:
    class _Node:
        __slots__ = '_element', '_left', '_right'

        def __init__(self, element, parent = None, left = None, right = None):
            self._element = element
            self._left = left
            self._right = right

    def __init__(self):
        self._root = None
        self._size = 0

    def root(self):
        return self._root
    
    def __len__(self):
        return self._size

    def height(self):
        return self._height(self._root)

    def _height(self, p):
        if not p:
            return 0
        return 1 + max(self._height(p._left), self._height(p._right))


    def in_order(self):
        for e in self._in_order(self._root):
            yield e

    def _in_order(self, p):
        if p is not None:
            for other in self._in_order(p._left):
                yield other

            yield p._element
            for other in self._in_order(p._right):
                yield other


    def pre_order(self):
        for e in self._pre_order(self._root):
            yield e

    def _pre_order(self, p):
        if p:
            yield p._element
            for other in self._pre_order(p._left):
                yield other

            for other in self._pre_order(p._right):
                yield other

    def post_order(self):
        for e in self._post_order(self._root):
            yield e

    def _post_order(self, p):
        if p:
            for other in self._post_order(p._left):
                yield other

            for other in self._post_order(p._right):
                yield other

            yield p._element

    def breadth_first(self):
        q = queue.Queue()
        q.put(self._root)
        while not q.empty():
            p = q.get()
            print(p._element)
            if p._left:
                q.put(p._left)
            if p._right:
                q.put(p._right)

    #The binary search tree insert function
    def bst_insert(self, key):
        '''implement binary search tree insert algoritm'''
        #Need to assign self._root in order to save into the BST
        self._root = self._bst_insert(key, self._root)
        
    def _bst_insert(self, key, p):
        #Base Case:
        if p is None:
            #If the position is none then we have to add the key to the root of the tree
            new_node = self._Node(key)
            return new_node

        #Recursion
        elif key < p._element:
            #Keep going into left subtrees until the base case is met
            p._left = self._bst_insert(key, p._left)
        else:
            #Keep going into the right subtrees until the base case is met
            p._right = self._bst_insert(key, p._right)
        return p

    #The binary search tree search function
    def bst_search(self, key):
        '''implement binary search algorithm'''
        return self._bst_search(key, self._root)
    def _bst_search(self, key, p):
        #Return true if the positional element equals the key the user is trying to look for
        #Return false if p is none as it ran through the proper subtrees and never found it
        while p is not None:
            if p._element == key:
                return True 
            elif key < p._element:
                p = p._left
            else:
                p = p._right

        #If it gets through everything then it doesn't exist
        return False
    
    #The binary search tree print in ascending order function
    def print_in_order(self):
        #From the order in_order takes, it should always print the elements in ascending order!
        for v in my_bst.in_order():
            print(v)
    
#Main Code

#Create the binary search tree and insert some elements in it
my_bst = LinkedBinaryTree()
my_bst.bst_insert(4)
my_bst.bst_insert(11)
my_bst.bst_insert(6)
my_bst.bst_insert(7)
my_bst.bst_insert(24)
my_bst.bst_insert(5)
my_bst.bst_insert(9)
my_bst.bst_insert(2)
my_bst.bst_insert(0)
my_bst.bst_insert(1)
my_bst.bst_insert(3)
my_bst.bst_insert(100)

#Check to see if a certain element is in the BST
find = int(input("Insert an integer to see if it's in the BST or not: "))
print(find,"is in the BST (T/F):",my_bst.bst_search(find))

#Print the BST in ascending order
print("\n-----Below is the BST in ascending order-----")
my_bst.print_in_order()


