    # -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 11:42:00 2022

@author: christian
"""

from modifyStack import modifyStack

stack1 = modifyStack()

# emptying the stack completely
stack1.push(4)
stack1.push(5)
stack1.push(6)

print(stack1.size())

stack1.empty_stack()

print(stack1.size())


# returning top two items in stack as a tuple
stack1.push(7)
stack1.push(8)

print(stack1.top_two_items())


# checking if two stacks are the same from top to bottom
stack2 = modifyStack()
stack3 = modifyStack()

stack2.push(4)
stack2.push(5)
#stack2.push(6)
stack3.push(4)
stack3.push(5)
stack3.push(6)

print(stack2.compare_two_stacks(stack3))


# rewriting size method without len()
stack4 = modifyStack()

stack4.push(4)
stack4.push(5)
stack4.push(6)

print(stack4.size()) # testing if both original size, and my new size are the same
print(stack4.size_naive())















