#Deletion of node
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
def minValue(node):
    current=node
    while (current.left is not None):
        current=current.left
    return current
def deleteNode(root,key):
    if (root is None):
        return root
    if (key<root.key):
        root.left = deleteNode(root.left,key)
    elif(key>root.key):
        root.right = deleteNode(root.right,key)
    else:
        if (root.left is None):
            temp=root.right
            root=None
            return temp
        elif (root.right is None):
            temp=root.left
            root=None
            return temp
        temp=minValue(root.right)
        root.key=temp.key
        root.right=deleteNode(root.right,temp.key)
    return root
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
i=int(input("\nEnter the value to be deleted"))
root=deleteNode(root,i)
print("Inorder traversal",end="")
inorder(root)
'''
##################Program-1(Even Queue & Odd Queue)####################
#2 7 9 4 6 5 10
#Even queue:
#2 4 6 10
#Odd queue:
#7 9 5
'''
class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__element=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        return False
    def is_empty(self):
        if(self.__rear<self.__front):
            return True
        return False
    def enqueue(self,data):
        if(self.is_full()):
            print("Full")
        else:
            self.__rear+=1
            self.__element[self.__rear]=data
        
    def dequeue(self):
        if(self.is_empty()):
            print("Empty")
        else:
            data=self.__element[self.__front]
            self.__front+=1
            return data
    def display(self):
        for i in range(self.__front,self.__rear+1):
            print(self.__element[i])
    def get_max_size(self):
        return self.__max_size
    def odd_element(self):
        for index in range(q1.__front,q1.__rear+1):
            if(q1.__element[index]%2!=0):
                self.enqueue(q1.__element[index])
    def even_element(self):
        for index in range(q1.__front,q1.__rear+1):
            if(q1.__element[index]%2==0):
                self.enqueue(q1.__element[index])
q1=Queue(7)
q1.enqueue(2)
q1.enqueue(7)
q1.enqueue(9)
q1.enqueue(4)
q1.enqueue(6)
q1.enqueue(5)
q1.enqueue(10)
q1.display()
q2=Queue(7)
print("Odd Queue:")
q2.odd_element()
q2.display()
q3=Queue(12)
print("Even Queue:")
q3.even_element()
q3.display()
'''
##############################Problem-2####################################
#list1=1-2-4-3-5
#list2=9-8-11
#n=2=>1-2-9-8-11-4-3-5
'''
class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class SLinkedList:
    def __init__(self):
        self.headval= None
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    def merge(self,n):
        start=self.headval
        c=0
        while(start is not None):
            c+=1
            if(c==n):
                break
            start=start.nextval
        start1=list2.headval
        while(start1.nextval is not None):
            start1=start1.nextval
        start1.nextval=start.nextval
        start.nextval=list2.headval
    def display(self):
        start=self.headval
        while(start is not None):
            print(start.dataval,"->",end='')
            start=start.nextval
list1=SLinkedList()
list1.headval=Node(1)
e2= Node(2)
e3= Node(4)
e4= Node(3)
e5= Node(5)
list1.headval.nextval = e2
e2.nextval =e3 
e3.nextval =e4
e4.nextval =e5
e5.nextval =None


list2=SLinkedList()
list2.headval=Node(9)
f2= Node(8)
f3= Node(11)
list2.headval.nextval = f2
f2.nextval =f3 
f3.nextval =None
list2.listprint()
n=int(input("Enter the value"))
list1.merge(n)
list1.display()
'''
############################Problem-3########################################
#original list=12 95 140 110 40
#new list=12 95 100 110 40
class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class SLinkedList:
    def __init__(self):
        self.headval= None
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def max(self,n):
        large=0
        start=self.headval
        while(start is not None):
            if(start.dataval>large):
                large=start.dataval
                add=start
            start=start.nextval
        add.dataval=n
list1=SLinkedList()
list1.headval=Node(12)
f2= Node(95)
f3= Node(140)
f4= Node(110)
f5= Node(40)

list1.headval.nextval = f2
f2.nextval =f3 
f3.nextval =f4
f4.nextval =f5
print("Original list")
list1.listprint()
n=int(input("Enter the value"))
print("New list")
list1.max(n)
list1.listprint()









































