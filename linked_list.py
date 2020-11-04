#!/usr/bin/env python
# coding: utf-8

# Using object-oriented programming, define a class Node that will hold the data as well as a reference to the next element. The class Node also needs a method insert that inserts a new element right after itself and before the previously next element. 

# This insert method is always doing the same amount of operations and hence should have a constant time complexity. Your second task is verifying this by creating differently sized lists and adding a new element somewhere (note that finding the element is not part of calculating the time complexity; hence you could always enter an element after the first position)

# # Linked list

# In[21]:


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
class LinkedList:
    
    def __init__(self):
        self.head = None # Always point to the first node of the linked list
        self.tail = None  
        # Always point to the last node of the linked list
        # We don't need to traverse the whole linked list when appending
        
    # Add a node at head
    # Creat a new node, which points to the original head(self.head)
    # Change the new linked_list head to the new node
    def insert_head(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
           
            
    # Append a node in the end without tail pointer
    # 1 Creat a new subject from Class Node
    # 2 If the linked_list is empty, the new node is the head
    # 3 Otherwise 
    # -- Linked list has no indexes, traverse to the last node
    # -- The last node of the original linked list points to the new node
    def insert_last(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node
        
    # Append a node in the end with tail pointer
    def append(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
  
    # Search for an element(key) in the linked list
    # Set the current node = linked_list's head.data
    # If the current.node.data = key, Then return True
    # Otherwise, current node = current node.next
    def search_element(self, key):
        current_node = self.head
        while (current_node.next):
            if current_node.data == key:
                return current_node
            else:
                current_node = current_node.next
        return None
    
    
    # Search for an element according to its position 
    # Count position_index from 1 and traverse to the position_index
    def search_postion(self,index):
        if index == 1:
            return self.head.data
        else:
            position_index = 1
            current_node = self.head
            while position_index < index:
                if current_node.next == None:
                    return "This is the last one in the linked list"
                else:
                    current_node = current_node.next
                    position_index +=1
        
                return current_node.data
    
    
    # Insert after a certain node
    # Search for the node(prev_node) after which to insert
    # Set new node pointer pointing to the node which after the prev_node
    # Reset the prev_node pointer pointing to the new node inserted
    def insertafter(self,prev_node_value,new_data):
        prev_node = self.search_element(prev_node_value)
        if prev_node is None:
            print("The given previous node is not in the linked list")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
        
        
    def printList(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next
            
            
my_list = LinkedList()
my_list.insert_head(1)
my_list.insert_head(9)
my_list.insert_head(5)
my_list.insert_head(11)
my_list.insert_head(6)
my_list.insertafter(11,7)
my_list.append(8)
my_list.printList()


# # Using tail pointer to append different size of elements

# In[4]:


# Creating a list of random numbers as node_data 
# The numer of the elements in the list: 2000,4000,8000,16000,32000,64000
# Append using tail pointer 
# Calculate the time of inserting different volumn of elements and draw pics


# In[22]:


import random
import time
import matplotlib.pyplot as plt
import seaborn as sns

def insertion_time():
    time_list = []
    volumn = [2000,4000,8000,16000,32000,64000]
    for v in volumn:
        
        random_list= random.sample(range(v),v)
        for num in random_list:
            start = time.time()
            my_list.append(num)
        end = time.time()
        duration = end-start
        time_list.append(duration)
        
    return time_list

insertion_time()


# In[23]:


volumn = [2000,4000,8000,16000,32000,64000]
time_list =[7.152557373046875e-07,
 9.5367431640625e-07,
 9.5367431640625e-07,
 1.1920928955078125e-06,
 9.5367431640625e-07,
 1.1920928955078125e-06]
time_per_insertion = [x/y for x, y in zip(time_list, volumn)]
sns.lineplot(x = volumn, y=time_per_insertion)
plt.ylim(top=1)


# In[ ]:




