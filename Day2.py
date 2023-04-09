#Linked List
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
            """
            for i in range(0,2):
                print(printval.dataval)
                continue
            """
            printval = printval.nextval
list=SLinkedList()
list.headval=Node("Mon")#headval contains the address of the first node object
e2= Node("Tue")
e3= Node("Wed")
e4= Node("Thu")
e5= Node("Fri")
e6= Node("Sat")
#Link 1st node to 2nd node
list.headval.nextval = e2
#Link 2nd node to 3rd node
e2.nextval =e3 #e2 storing the address of e3
e3.nextval =e4 # OR(list.headval.nextval.nextval.nextval = e4)
e4.nextval =e5
e5.nextval =e6
e6.nextval =None
list.listprint()
'''
#####################Add a value at begining########################
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
            """for i in range(0,2):
                print(printval.dataval)
                continue"""
            printval = printval.nextval
    def AtBegining(self,new):
        NewNode= Node(new)
        NewNode.nextval= self.headval
        self.headval = NewNode
list=SLinkedList()
list.headval=Node("Mon")
e2= Node("Tue")
e3= Node("Wed")
e4= Node("Thu")
e5= Node("Fri")
e6= Node("Sat")
list.headval.nextval = e2
e2.nextval =e3 
e3.nextval =e4 
e4.nextval =e5
e5.nextval =e6
e6.nextval =None
list.listprint()
print("After adding at begining:")
list.AtBegining("Sun")
list.listprint()
'''
#########################Add a value at end####################################
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
            """for i in range(0,2):
                print(printval.dataval)
                continue"""
            printval = printval.nextval
    def AtEnd(self,new):
        NewNode= Node(new)
        if self.headval is None:
            self.headval= NewNode
            return
        last= self.headval
        while(last.nextval is not None):
            last=last.nextval
        last.nextval=NewNode
list=SLinkedList()
list.headval=Node("Mon")#headval contains the address of the first node object
e2= Node("Tue")
e3= Node("Wed")
e4= Node("Thu")
e5= Node("Fri")
e6= Node("Sat")
list.headval.nextval = e2
e2.nextval =e3 
e3.nextval =e4
e4.nextval =e5
e5.nextval =e6
e6.nextval =None
list.listprint()
print("After adding at end:")
list.AtEnd("Sun")
list.listprint()
'''
######################Add a value at any point##################################
'''class Node:
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
    """
    def At(self,new):
        NewNode= Node(new)
        if self.headval is None:
            self.headval= NewNode
            return
        last= self.headval
        while(last.dataval !="Tue"):
            last=last.nextval
            NewNode.nextval=last.nextval
        last.nextval=NewNode
    """OR
    def InBet(self,middle,new):
        if middle is None:
            print("The mentioned node is absent")
            return
        newnode=Node(new)
        newnode.nextval = middle.nextval
        middle.nextval=newnode
list=SLinkedList()
list.headval=Node("Mon")
e2= Node("Tue")
e3= Node("Thu")
list.headval.nextval = e2
e2.nextval =e3
list.listprint()
#orlist.At("Wed")
list.InBet(list.headval.nextval,"Wed")#as i am printing wed at 3rd position so there will be one headval and one nextval
print("After adding :")
list.listprint()
'''
#############Deleting the end value and the begining value########################################
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
    def delete_at_start(self):
        if self.headval is None:
            print("Nothing to delete")
        self.headval=self.headval.nextval
    def delete_at_end(self):
        if (self.headval is None):
            print("Nothing to delete")
            return
        n=self.headval
        while (n.nextval.nextval is not None):
            n=n.nextval
        n.nextval=None
list1=SLinkedList()
list1.headval=Node(100)
e2= Node(200)
e3= Node(300)
e4= Node(400)
e5= Node(500)
e6= Node(600)
list1.headval.nextval = e2
e2.nextval =e3 
e3.nextval =e4
e4.nextval =e5
e5.nextval =e6
e6.nextval =None
list1.listprint()
list1.delete_at_end()
print("After deleting at end")
list1.listprint()
list1.delete_at_start()
print("After deleting at begining")
list1.listprint()
'''
################Reversing the single linked list#########################
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
    def rev(self):
        start=self.headval
        while(start is not None):
            while(start.nextval is not None):
                start=start.nextval
            print(start.dataval)
            start=self.headval
            self.delete_at_end()
    def delete_at_end(self):
        n=self.headval
        if (self.headval.nextval is None):
            exit()
        while (n.nextval.nextval is not None):
            n=n.nextval
        n.nextval=None
list1=SLinkedList()
list1.headval=Node(100)
e2= Node(200)
e3= Node(300)
e4= Node(400)
e5= Node(500)
e6= Node(600)
list1.headval.nextval = e2
e2.nextval =e3 
e3.nextval =e4
e4.nextval =e5
e5.nextval =e6
e6.nextval =None
list1.listprint()
print("Reverse of list is")
list1.rev()
list1.listprint()
'''
##################Search an item is present or not############################################
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
    def search_item(self,x):
        if(self.headval is None):
            print("List has no element")
            return
        n=self.headval
        while(n is not None):
            if(n.dataval ==x):
                print("Item found")
                return True
            n=n.nextval
        print("Item not found")
        return False
list1=SLinkedList()
list1.headval=Node(100)
e2= Node(200)
e3= Node(300)
e4= Node(400)
e5= Node(500)
e6= Node(600)
list1.headval.nextval = e2
e2.nextval =e3 
e3.nextval =e4
e4.nextval =e5
e5.nextval =e6
e6.nextval =None
list1.listprint()
list1.search_item(500)
'''
########################Insert at index#################################
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
    def insert_at_index(self,index,data):
        if(index==1):
            new_node=Node(data)
            new_node.nextval=self.headval
            self.headval=new_node
        i=1
        n=self.headval
        while(i< index-1 and n is not None):
            n = n.nextval
            i=i+1
        if (n is None):
            print("Index out of bound")
        else:
            new_node=Node(data)
            new_node.nextval=n.nextval
            n.nextval=new_node

list1=SLinkedList()
list1.headval=Node(100)
e2= Node(200)
e3= Node(400)
e4= Node(500)
e5= Node(600)
e6= Node(700)
list1.headval.nextval = e2
e2.nextval =e3 
e3.nextval =e4
e4.nextval =e5
e5.nextval =e6
e6.nextval =None
list1.insert_at_index(3,300)
list1.listprint()
'''
##########################Problem-1 Day-2#####################################
#MARKS scored by student=89,78,99,76,77,67,99,78,98,90
#insert 78 mark at 8th position
#display mark of students at index number 5 and 7
'''
class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class Slinkedlist:
    def __init__(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while(printval is not None):
            print(printval.dataval)
            printval=printval.nextval
    def insert_node(self,pos_insert,val_insert):
        pos=self.headval
        c=1
        while(pos is not None):
            if(c == pos_insert-1):#doubt
                break
            else:
                c+=1
                pos=pos.nextval
        newnode=Node(val_insert)
        newnode.nextval=pos.nextval
        pos.nextval=newnode
    def view_node(self,pos):
        pos_node=self.headval
        c=1
        while(pos is not None):
            if(c == pos):
                break
            else:
                c+=1
                pos_node=pos_node.nextval
        return (pos_node.dataval)
list1=Slinkedlist()
list1.headval=Node(89)
e1=Node(78)
e2=Node(99)
e3=Node(76)
e4=Node(77)
e5=Node(67)
e6=Node(99)
e7=Node(98)
e8=Node(90)
#linking the list
list1.headval.nextval=e1
e1.nextval=e2
e2.nextval=e3
e3.nextval=e4
e4.nextval=e5
e5.nextval=e6
e6.nextval=e7
e7.nextval=e8
e8.nextval=None
list1.listprint()
n=int(input("Enter the value to be inserted"))
i=int(input("Enter the position"))
list1.insert_node(i,n)
print("After insertion")
list1.listprint()
print("Mark of person at 5th index is",list1.view_node(5))
print("Mark of person at 7th index is",list1.view_node(7))
'''
#########################Problem-2 Day-2###################################
#l1=[11,8,23,7,25,15]
#l2=[6,33,50,31,46,78,16,34]
#double=[8,23,25]
#without creating result node
'''
class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class Slinkedlist:
    def __init__(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while(printval is not None):
            print(printval.dataval)
            printval=printval.nextval
        
    def double_check(self):
        start=self.headval
        while(start is not None):
            inlist=list2.headval
            while(inlist is not None):
                if(start.dataval*2 == inlist.dataval):
                    print(start.dataval)
                    break
                else:
                    inlist=inlist.nextval
            start=start.nextval
list1=Slinkedlist()
list1.headval=Node(11)
e1=Node(8)
e2=Node(23)
e3=Node(7)
e4=Node(25)
e5=Node(15)

list1.headval.nextval=e1
e1.nextval=e2
e2.nextval=e3
e3.nextval=e4
e4.nextval=e5

list2=Slinkedlist()
list2.headval=Node(6)
f1=Node(33)
f2=Node(50)
f3=Node(31)
f4=Node(46)
f5=Node(78)
f6=Node(16)
f7=Node(34)

list2.headval.nextval=f1
f1.nextval=f2
f2.nextval=f3
f3.nextval=f4
f4.nextval=f5
f5.nextval=f6
f6.nextval=f7

print("first list is")
list1.listprint()
print("second list is")
list2.listprint()
print("The list of double is")
list1.double_check()
'''








































































































































































