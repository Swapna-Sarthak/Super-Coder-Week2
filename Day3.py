#Doubley linked list
############################Insert at begining#############################
'''
class Node:
    def __init__(self,value):
        self.previous=None
        self.data=value
        self.next=None
        
class Doubley_linked_list:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    def length(self):
        temp=self.head
        count=0
        while temp is not None:
            temp=temp.next
            count+=1
        return count
    def insertAtBegining(self,value):
        new_node=Node(value)
        if self.isEmpty():
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.previous = new_node
            self.head=new_node
    def printLinkedList(self):
        temp=self.head
        while temp is not None:
            print(temp.data,sep=",")
            temp=temp.next
            
x=Doubley_linked_list()
print(x.isEmpty())
x.insertAtBegining(5)
#x.printLinkedList()
x.insertAtBegining(15)
x.insertAtBegining(25)
x.insertAtBegining(35)
x.printLinkedList()
print("No of nodes",x.length())
'''
###############################Insert at end#############################
'''
class Node:
    def __init__(self,value):
        self.previous=None
        self.data=value
        self.next=None
        
class Doubley_linked_list:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    def length(self):
        temp=self.head
        count=0
        while temp is not None:
            temp=temp.next
            count+=1
        return count
    def insertAtBegining(self,value):
        new_node=Node(value)
        if self.isEmpty():
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.previous = new_node
            self.head=new_node
    def insertAtEnd(self,value):
        new_node=Node(value)
        if self.isEmpty():
            self.insertAtBegining(value)
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
            new_node.previous=temp
    def printLinkedList(self):
        temp=self.head
        while temp is not None:
            print(temp.data,sep=",")
            temp=temp.next
            
x=Doubley_linked_list()
print(x.isEmpty())
x.insertAtEnd(6)
x.insertAtBegining(5)
#x.printLinkedList()
x.insertAtBegining(15)
x.insertAtBegining(25)
x.insertAtBegining(35)
x.printLinkedList()
print("No of nodes",x.length())
'''
###########################Insert at any position###############################################
'''
class Node:
    def __init__(self,value):
        self.previous=None
        self.data=value
        self.next=None
        
class Doubley_linked_list:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    def length(self):
        temp=self.head
        count=0
        while temp is not None:
            temp=temp.next
            count+=1
        return count
    def insertAtBegining(self,value):
        new_node=Node(value)
        if self.isEmpty():
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.previous = new_node
            self.head=new_node
    def insertAtPos(self,value,pos):
        temp=self.head
        count=1
        while temp is not None:
            if count == pos-1:
                break
            count+=1
            temp=temp.next
        if pos ==1:
            self.insertAtBegining(value)
        elif temp is None:
            print("There are less than {}-1 element in the linked list. Can not insert at {} position.".format(position,position))
        elif temp.next is None:
            self.insertAtEnd(value)
        else:
            new_node = Node(value)
            new_node.next = temp.next
            new_node.previous = temp
            temp.next.previous = new_node
            temp.next = new_node
    def insertAtEnd(self,value):
        new_node=Node(value)
        if self.isEmpty():
            self.insertAtBegining(value)
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
            new_node.previous=temp
    def printLinkedList(self):
        temp=self.head
        while temp is not None:
            print(temp.data,sep=",")
            temp=temp.next
            
x=Doubley_linked_list()
print(x.isEmpty())
x.insertAtEnd(6)
x.insertAtBegining(5)
x.insertAtBegining(15)
x.insertAtBegining(25)
x.insertAtBegining(35)
x.printLinkedList()
print("No of nodes",x.length())
v=int(input("Enter value to be added"))
p=int(input("Enter position of value to be added"))
x.insertAtPos(v,p)
x.printLinkedList()
'''
#############################Delete from begining#################################################
'''
class Node:
    def __init__(self,value):
        self.previous=None
        self.data=value
        self.next=None
        
class Doubley_linked_list:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    def length(self):
        temp=self.head
        count=0
        while temp is not None:
            temp=temp.next
            count+=1
        return count
    def insertAtBegining(self,value):
        new_node=Node(value)
        if self.isEmpty():
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.previous = new_node
            self.head=new_node

    def deleteFromBegining(self):
        if self.isEmpty():
            print("Empty list can not delete element")
        elif self.head.next is None:
            self.head=None
        else:
            self.head=self.head.next
            self.head.previous = None
            
    def printLinkedList(self):
        temp=self.head
        while temp is not None:
            print(temp.data,sep=",")
            temp=temp.next
            
x=Doubley_linked_list()
print(x.isEmpty())
x.insertAtBegining(5)
x.insertAtBegining(15)
x.insertAtBegining(25)
x.insertAtBegining(35)
x.printLinkedList()
print("No of nodes",x.length())
x.deleteFromBegining()
x.printLinkedList()
print("No of nodes after deleting",x.length())
'''
#############################Delete from last#################################################
'''
class Node:
    def __init__(self,value):
        self.previous=None
        self.data=value
        self.next=None
        
class DoubleyLinkedList:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    def length(self):
        temp=self.head
        count=0
        while temp is not None:
            temp=temp.next
            count+=1
        return count
    def insertAtBegining(self,value):
        new_node=Node(value)
        if self.isEmpty():
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.previous = new_node
            self.head=new_node

    def deleteFromLast(self):
        if self.isEmpty():
            print("Empty list can not delete element")
        elif self.head.next is None:
            self.head=None
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.previous.next=None
            temp.previous=None
            
    def printLinkedList(self):
        temp=self.head
        while temp is not None:
            print(temp.data,sep=",")
            temp=temp.next
            
x=DoubleyLinkedList()
print(x.isEmpty())
x.insertAtBegining(5)
x.insertAtBegining(15)
x.insertAtBegining(25)
x.insertAtBegining(35)
x.printLinkedList()
print("No of nodes before deleting",x.length())
x.deleteFromLast()
x.printLinkedList()
print("No of nodes after deleting",x.length())
'''
#########################Delete from anywhere############################
'''
class Node:
    def __init__(self,value):
        self.previous=None
        self.data=value
        self.next=None
        
class DoubleyLinkedList:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    def length(self):
        temp=self.head
        count=0
        while temp is not None:
            temp=temp.next
            count+=1
        return count
    def insertAtBegining(self,value):
        new_node=Node(value)
        if self.isEmpty():
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.previous = new_node
            self.head=new_node
    def deleteFromBegining(self):
        if self.isEmpty():
            print("Empty list can not delete element")
        elif self.head.next is None:
            self.head=None
        else:
            self.head=self.head.next
            self.head.previous = None
    def deleteFromLast(self):
        if self.isEmpty():
            print("Empty list can not delete element")
        elif self.head.next is None:
            self.head=None
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.previous.next=None
            temp.previous=None            
    def deleteAtPos(self,pos):
        if self.isEmpty():
            print("Can not delete as Linked list is empty")
        elif pos==1:
            self.deleteFromBegining()
        else:
            temp=self.head
            count=1
            while temp is not None:
                if count==pos:
                    break
                temp=temp.next
                count+=1
            if temp is None:
                print("There are less than {} element in the linked list. Can not delete at postion {}".format(pos,pos))
                return
            elif temp.next is None:
                self.deleteFromLast()
                return
            temp.previous.next = temp.next
            temp.next.previous = temp.previous
            temp.next=None 
            temp.previous = None
    def printLinkedList(self):
        temp=self.head
        while temp is not None:
            print(temp.data,sep=",")
            temp=temp.next
            
x=DoubleyLinkedList()
x.insertAtBegining(5)
x.insertAtBegining(15)
x.insertAtBegining(25)
x.insertAtBegining(35)
x.printLinkedList()
print("No of nodes before deleting",x.length())
p=int(input("Enter position of value to be deleted"))
x.deleteAtPos(p)
x.printLinkedList()
'''
######################Postfix Evaluation User Input########################################
'''
class PostfixEvaluate:
    def __init__(self,capacity):
        self.top=-1
        self.capacity=capacity
        self.array=[]
    def isEmpty(self):
        return True if self.top == -1 else False
    def peek(self):
        return self.array[-1]
    def pop(self):
        if not self.isEmpty():
            self.top-=1
            return self.array.pop()
        else:
            return "$"
    def push(self,op):
        self.top+=1
        self.array.append(op)
        
    def evaluatePostfix(self,exp):
        for i in exp:
            if i.isdigit():
                self.push(i)
            else:
                val1=self.pop()
                val2=self.pop()
                self.push(str(eval(val2 + i + val1)))

        return int(self.pop())

exp=input("")
obj = PostfixEvaluate(len(exp))
print("Postfix evaluation: %d"%(obj.evaluatePostfix(exp)))
'''
###############Problem-1 Day-3#################
#Deleting duplicacy from the doubly linked list
class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class Dlinkedlist:
    def __init__(self):
        self.head=None
        
    def listprint(self):
        start=self.head
        while(start is not None):
            print(start.data)
            start=start.next
    def delete_end(self):
        end=self.head
        while(end.next.next is not None):
            end=end.next
        end.next=None
        return

    def remove_duplicate(self):
        start=self.head#23
        while(start is not None):
            dup=start.next#12
            while(dup is not None):
                if(dup.data == start.data):#true
                    print(dup.data,"deleted")
                    start.next=dup.next
                    dup.next.prev=start
                    dup=dup.next
                    continue
                else:
                    dup.prev.next=dup.next
                dup=dup.next#23
            start=start.next
            
list1=Dlinkedlist()
list1.head=Node(23)
n2=Node(12)
n3=Node(23)
n4=Node(73)
n5=Node(73)
n6=Node(10)
list1.head.next=n2
n2.prev=list1.head
n2.next=n3
n3.prev=n2
n3.next=n4
n4.prev=n3
n4.next=n5
n5.prev=n4
n5.next=n6
n6.prev=n5

print("The list is")
list1.listprint()
print("After removing duplicacy")
list1.remove_duplicate()
list1.listprint()










































































































































