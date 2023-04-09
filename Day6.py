#Selectionsort sorting tech
'''
def selectionsort(array,size):
    for step in range(size):#step0=20,12,10,15,2
                            #step2=2,12,10,15,20
        min_idx=step        #step3=2,10,12,15,20
        for i in range(step+1,size):
            if  array[i]< array[min_idx]:
                min_idx=i
        (array[step],array[min_idx])=(array[min_idx],array[step])

data=[20,12,10,15,2]
size=len(data)
selectionsort(data,size)
print("Sorted array in assending order")
print(data)
'''
#Problem-3 Day-6
#Question
'''
The owner of a BakeHouse wants to keep track of the tables 
that are occupied in his cafe. Assume that there are 10 tables
in his cafe numbered from 1 to 10. As and when a table is occupied,
it must be added to the occupied_table_list and when a customer
leaves, the corresponding table must be removed from the list.

BakeHouse
- occupied_table_list
_init_()
+ get_occupied_table_list()
+ allocate_table()
+ deallocate_table(table_number)
Write a python program to implement BakeHouse class. 
Represent occupied_table_list using an appropriate data 
structure.

Note: Table numbers should be maintained in ascending order
in the occupied_table_list.
Tables should be allocated and de-allocated as mentioned
in the example below:

Example:Suppose tables 1, 2, 3 and 4 are initially allocated.
Now if a new customer arrives, he should be allocated table 5
and the table list should be accordingly updated. If now
customer at table 2 leaves, table list should be accordingly
updated and the next new customer should be allocated table 2
as it is the first free table.

Implement the allocation logic in allocate_table() method
and de-allocation logic in deallocate_table() method.
'''
#Answers
'''
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new
class BakeHouse:
    def __init__(self):
        self.occupied_table = []

    def get_occupied_table(self):
        return self.occupied_table

    def allocate_table(self):
        if len(self.occupied_table) >= 10:
            return -1  
        table_number = 1
        while table_number in self.occupied_table:
            table_number += 1
        self.occupied_table.append(table_number)
        self.occupied_table.sort()#ascending order
#       self.occupied_table.sort(reverse=True)#descending order
        return table_number
    def deallocate_table(self, table_number):
        if table_number not in self.occupied_table:
            return -1
        self.occupied_table.remove(table_number)
        self.occupied_table.sort()
        return table_number
bakehouse = BakeHouse()
print("Numbers of table currently occupied",bakehouse.get_occupied_table())  
print("Table allocated:",bakehouse.allocate_table())  
print("Table allocated:",bakehouse.allocate_table())
print("Table allocated:",bakehouse.allocate_table())
print("Table allocated:",bakehouse.allocate_table())
print("Table allocated:",bakehouse.allocate_table())
print("Table currently occupied are:",bakehouse.get_occupied_table())  
print("Table empty:",bakehouse.deallocate_table(2))
print("Table currently occupied are:",bakehouse.get_occupied_table())
print("Table allocated:",bakehouse.allocate_table())
print("Table currently occupied are:",bakehouse.get_occupied_table())
'''
#Problem-4 Day-6
#Question
'''A teacher is conducting a camp for a group of five children.
 Based on their performance and behavior during the camp, the
 teacher rewards them with chocolates.
Write a Python function to Find the total number of chocolates
received by all the children put together.
Assume that each child is identified by an id and it is stored
in a tuple and the number of chocolates given to each child
is stored in a list.
The teacher also rewards a child with few extra chocolates 
for his/her best conduct during the camp.
If the number of extra chocolates is less than 1, an error 
message "Extra chocolates is less than 1", should be 
displayed.
If the given child Id is invalid, an error message 
"Child id is invalid" should be displayed. Otherwise,
the extra chocolates 
provided for the child must be added to his/her existing 
number of chocolates and display the list containing the
total number of chocolates received by each child.
child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]
functions
calculate_total_chocolates()
reward_child(child_id_rewarded,extra_chocolates)
'''
#Answer
'''
def calculate_total_chocolates():
    return sum(chocolates_received)

def reward_child(child_id,child_id_rewarded,extra_chocolates):
        index = child_id.index(child_id_rewarded)
        if extra_chocolates < 1:
            print("Extra chocolates is less than 1") 
        elif child_id_rewarded not in child_id:
            print("Child id is invalid")
        else:
            chocolates_received[index] += extra_chocolates
            print(chocolates_received)
                   
child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]
c=int(input("Enter id of the chhild:"))
e=int(input("Enter extra number of choclates:"))
reward_child(child_id,c,e)
print("Total candies:",calculate_total_chocolates())
'''
#QuickSort
'''
def partition(array,low,high):
    pivot=array[high]#pivot=2
    i=low-1         #i=-1
    for j in range(low,high):#0to5
        if array[j]<=pivot:
            i=i+1
            (array[i],array[j])=(array[j],array[i])
    (array[i+1],array[high])=(array[high],array[i+1])
    return i+1
def quickSort(array,low,high):
    if low < high:
        pi=partition(array,low,high)
        quickSort(array,low,pi-1)
        quickSort(array,pi+1,high)
print("Unsorted array")
#data=[10,80,30,90,40,50,70]
data=list(map(int,input().split()))
#data=[8, 7, 6, 1, 0, 9, 2]
print("Unsorted array")
size=len(data)
quickSort(data,0,size-1)
print("Sorted array in ascending order")
print(data)
'''
#Problem-5
#Question
'''
Write a python program that accepts a text and displays a 
string which contains the word with the largest frequency
in the text and the frequency itself separated by a space.
Rules:
The word should have the largest frequency.
In case multiple words have the same frequency, then choose 
the word that has the maximum length.
Assumptions:
The text has no special characters other than space.
The text would begin with a word and there will be only a 
single space between the words.
Perform case insensitive string comparisons wherever 
necessary.
'''
#Answer
'''
def find_most_frequent_word(text):
    text = text.lower()
    words = text.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    max_freq = 0
    max_word = ''
    for word in freq:
        if freq[word] > max_freq:
            max_freq = freq[word]
            max_word = word
        elif freq[word] == max_freq:
            if len(word) > len(max_word):
                max_word = word
    return max_word + ' ' + str(max_freq)

text =input()
print(find_most_frequent_word(text))
'''
#Problem-6
#Question
'''
Write a python function, check_anagram() which accepts two 
strings and returns True, if one string is an anagram of 
another string. 
Otherwise returns False.
The two strings are considered to be an anagram if they
 contain repeating characters but none of the characters
repeat at the same position.
The length of the strings should be the same.
'''
#Answers

def check_anagram(s1, s2):
    if len(s1) == len(s2):
        for i in s1:
            if s1.index(i)==s2.index(i):
                return False
            else:
                continue
        return True
    else:
        return False
    s1 = s1.lower().replace(' ', '')
    s2 = s2.lower().replace(' ', '')  
    count = {}
    for char in s1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for char in s2:
        if char in count:
            count[char] -= 1
            if count[char] == 0:
                del count[char]
        else:
            return False
    if not count:
        return True
    else:
        return False
s1=input()
s2=input()
print(check_anagram(s1, s2))

#Problem-7
#Question








































        
