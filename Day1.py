#Stack
#Operations in stack[linear data structure based on LIFO] are:-
#-isempty
#-isfull
#-top
#-push
#-pop
'''
class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__element=[None]*self.__max_size
        self.__top=-1
    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if(self.__top==-1):
            return True
        return False

    def push(self,data):
        if(self.is_full()):
            print("The stack is full")
        else:
            self.__top+=1
            self.__element[self.__top]=data
    def pop(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            data=self.__element[self.__top]
            self.__top-=1
            return data
    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__element[index])
                index-=1
                

    def get_max_size(self):
        return self.__max_size
ball_stack=Stack(4)
print("Is it empty",ball_stack.is_empty())
ball_stack.push(10)
print("Is it empty",ball_stack.is_empty())
ball_stack.push(11)
ball_stack.push(12)
ball_stack.push(13)
ball_stack.display()
print("Size of the stack",ball_stack.get_max_size())
print("The element deleted",ball_stack.pop())
print("After deleting the element")
ball_stack.display()
print("Size of the stack",ball_stack.get_max_size())
'''
#Queue
#-isempty
#-isfull
#-front(returns the element at front of queue)
#-enqueue(inserts an element at the rear)
#-dequeue(removes the element in front)
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
q1=Queue(11)
print("Is it full",q1.is_full())
print("Is it empty",q1.is_empty())
q1.enqueue(100)
q1.enqueue(101)
q1.enqueue(102)
q1.enqueue(103)
q1.enqueue(104)
q1.enqueue(105)
q1.enqueue(106)
q1.enqueue(107)
q1.enqueue(108)
q1.enqueue(109)
q1.enqueue(110)
q1.display()
print("The deleted element:",q1.dequeue())
print("After deletion")
q1.display()
print("Is it full",q1.is_full())
print("Is it empty",q1.is_empty())
#################################Problem-1#########################################
'''
'''
class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if(self.__rear==self.__max_size-1):
                return True
        return False

    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False

    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])


    def get_max_size(self):
        return self.__max_size

    def _str_(self):
        msg=[]
        index=self.__front
        while(index<=self.__rear):
            msg.append((str)(self.__elements[index]))
            index+=1
        msg=" ".join(msg)
        msg="Queue data(Front to Rear): "+msg
        return msg

def check_numbers(number_queue):
    size=number_queue.get_max_size()
    solution_queue1=Queue(size)
    while size>0:
        element=number_queue.dequeue()
        if all(element%i==0 for i in range(1,11)):
            solution_queue1.enqueue(element)
        size-=1 
    return solution_queue1

number_queue=Queue(5)
number_queue.enqueue(13983)
number_queue.enqueue(10080)
number_queue.enqueue(7113)
number_queue.enqueue(2520)
number_queue.enqueue(2500)
check_numbers(number_queue)
number_queue.display()
'''
#####################Problem-2################################
'''
l1=['A','app','a','d','ke','th','doc','awa']
l2=['y','tor','e','eps','ay',None,'le','n']
l3=l2[::-1]
str1=""
for i in range(0,len(l1)):
    if(l1[i]!=None and l3[i]!=None):
        str1+=l1[i]
        str1+=l3[i]
        str1+=" "
    elif(l1[i]==None):
        str1+=l3[i]
        str1+=" "
    else:
        str1+=l1[i]
        str1+=" "
print(str1)
'''
#########################Problem-3###########################
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
class first_queue(Queue):
    pass
class second_queue(Queue):
    pass
class result_queue(first_queue,second_queue):
    pass
    
n1=int(input())
n2=int(input())
obj1=first_queue(n1)
obj2=second_queue(n2)
obj3=result_queue(n1+n2)
for i in range(0,n1):
    obj1.enqueue(int(input()))
for i in range(0,n2):
    obj2.enqueue(input())
for i in range(min(n1,n2)):
    obj3.enqueue(obj1.dequeue())
    obj3.enqueue(obj2.dequeue())
for j in range(min(n1,n2),max(n1,n2)):
    if max(n1,n2)==n1:
        obj3.enqueue(obj1.dequeue())
    else:
        obj3.enqueue(obj2.dequeue())
obj3.display()
''' 
############################################################################
#Linked List
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
list=SLinkedList()
list.headval=Node("Mon")
e2= Node("Tue")
e3= Node("Wed")
e4= Node("Thu")
list.headval.nextval = e2
e2.nextval = e3
e3.nextval =e4
list.listprint()
















































