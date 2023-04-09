#Linear Search in Python
#Time complexity=O(n)
'''
def linearSearch(array,n,x):
    for i in range(0,n):
        if(array[i] == x):
            return i
    return -1
array=[2,4,0,1,9]
x=1
n=len(array)
result=linearSearch(array,n,x)
if (result==-1):
    print("Element not found")
else:
    print("Element found at index:",result)
'''
#Binary Search in Python
#Time complexity=O(logn)
'''
def binarySearch(array,x,low,high):
    while low<=high:
        mid = low +(high - low)//2
        if array[mid]==x:
            return mid
        elif array[mid] < x:
            low=mid+1
        else:
            high=mid-1
    return -1
array=[3,4,5,6,7,8,9]
x=4
result=binarySearch(array,x,0,len(array)-1)
if result != -1:
    print("Element is present at index "+str(result))
else:
    print("Not found")
'''
#A Python class that represents an individual node in a binary tree
#Inorder,Postorder & Preorder Traversal
'''
class Node:
    def __init__(self,item):
        self.left=None
        self.right=None
        self.val=item
def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val)+ "->", end='')
        inorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val)+ "->", end='')
def preorder(root):
    if root:
            #Traverse root
        print(str(root.val)+ "->", end='')
            #Traverse left
        preorder(root.left)
            #Traverse right
        preorder(root.right)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
print("Inorder traversal")
inorder(root)
print("\nPostorder traversal")
postorder(root)
print("\nPreorder traversal")
preorder(root)
'''
#Binary Search Tree
#The left subtree of a node contains only nodes with keys lesser than the node's keys
#The left subtree of a node contains only nodes with keys lesser than the node's keys
#The left and right subtree each must also be a binary search tree
#Inorder,Postorder & Preorder Traversal
'''
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key

def insert(node,key):
    #Return new node if the node is empty
    if (node is None):
        return Node(key)
    #Traverse to the right palce and insert the node
    if (key<node.key):
        node.left = insert(node.left,key)
    else:
        node.right = insert(node.right,key)
    return node
def inorder(root):
    if (root is not None):
        inorder(root.left)
        print(str(root.key)+ "->", end='')
        inorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.key)+ "->", end='')
def preorder(root):
    if root:
        print(str(root.key)+ "->", end='')
        preorder(root.left)
        preorder(root.right)
root=None
root=insert(root,8)
root=insert(root,3)
root=insert(root,1)
root=insert(root,6)
root=insert(root,7)
root=insert(root,10)
root=insert(root,14)
root=insert(root,4)
print("Inorder traversal",end="")
inorder(root)
print("\nPostorder traversal")
postorder(root)
print("\nPreorder traversal")
preorder(root)
'''
#######################Problem-1 Day-4###########################
class Node:
    def __init__(self,name,people,seat):
        self.name=name
        self.seat=seat
        self.people=people
        self.nextval=None
 
class Compartment:
    def __init__(self):
        self.headval=None
    def display(self):
        start=self.headval
        while(start is not None):
            print(start.name)
            start=start.nextval
class Train:
    def __init__(self,train_name,compartment_list): 
        self.__train_name=train_name 
        self.__compartment_list=compartment_list
    
    def get_train_name(self):
        return self.__train_name
    def get_compartment_list(self):
        start= self.__compartment_list.headval
        while(start is not None):
            print(start.train_name)
            start=start.nextval
    
    def count_compartments(self):
        start = self.__compartment_list.headval
        count=0
        while(start is not None):
            count+=1
            start=start.nextval
        return count
    def check_vacancy(self):
        start=self.__compartment_list.headval
        count=0
        while(start is not None):
            if(start.seat-start.people > start.seat*0.5):
                count+=1
            start=start.nextval
        return count
Comparts= Compartment()    
Comparts.headval=Node("SL",250,400)   
e2=Node("2AC",125,280)   
e3=Node("3AC",120,300)
e4=Node("FC",160,300)
e5=Node("1AC",100,210)
Comparts.headval.nextval=e2
e2.nextval=e3
e3.nextval=e4
e4.nextval=e5
train1=Train("RajyaRani",Comparts)
print("Number of compartments:",train1.count_compartments())
print("Compartments which have more than 50% vacancy:",train1.check_vacancy())






































































































