# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 13:02:40 2022

@author: christian
"""

class Node:
    """A node of a linked list"""

    def __init__(self, node_data):
        self.node_val = node_data   #the data item in the node
        self.next_node = None       #id of my next neighbor
        
    def print_node(self):
        
        print('node item = ', self.node_val)
        #id of next neighbor
        print('My next neighbor = ', self.next_node)

    def set_next_node(self, nn):
        self.next_node = nn
        
    def set_node_val(self, item):
        self.node_val = item
        
    def get_node_val(self):
        return self.node_val
    
    def get_node_next(self):
        return self.next_node
        
#make a node object
#node_val = 15
n1 = Node(15)
print(n1.get_node_val())
print(n1.get_node_next())
print('id of node n1 =', n1)
#make a node object
#node_val = 7
n2 = Node(7)
print(n2.get_node_val())
print(n2.get_node_next())
n2.set_next_node(n1)
#print(n2.get_node_next())

n2_tries_n1_id = n2.get_node_next() #id of node n1
print('n2 neighbor is ', n2_tries_n1_id.get_node_val())
print('n2 neighbor id is', n2.get_node_next())

n3 = Node(13)
#make n2 be the neighbor of node n3
n3.set_next_node(n2)

#n3 must verify that its neighbor is n2
print('id of node n2 = ', n2)
print('id of n3 neighbor is = ', n3.get_node_next())

#n3 also must verify that its neighbor's neighbor is n1


# print(n2.)