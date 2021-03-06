# Suppose you have a linked list where the value of each node is a sorted linked list (i.e., it is a nested list). 
# Your task is to flatten this nested list—that is, to combine all nested lists into a single (sorted) linked list.


#----------------------------------- Generating Nodes and A Linked List --------------------------------#
# Helper code

# A class behaves like a data-type, just like an int, float or any other built-in ones. 
# User defined class
class Node:
    def __init__(self, value): # <-- For simple LinkedList, "value" argument will be an int, whereas, for NestedLinkedList, "value" will be a LinkedList
        self.value = value
        self.next = None
    
    def __repr__(self):
        return str(self.value)
    
# User defined class
class LinkedList: 
    def __init__(self, head): # <-- Expects "head" to be a Node made up of an int or LinkedList
        self.head = head
    
    '''
    For creating a simple LinkedList, we will pass an integer as the "value" argument
    For creating a nested LinkedList, we will pass a LinkedList as the "value" argument
    '''
    def append(self, value):
        
        # If LinkedList is empty
        if self.head is None:
            self.head = Node(value)
            return
        
        # Create a temporary Node object
        node = self.head
        
        # Iterate till the end of the currrent LinkedList
        while node.next is not None:
            node = node.next
        
        # Append the newly creataed Node at the end of the currrent LinkedList
        node.next = Node(value)

        
    '''We will need this function to convert a LinkedList object into a Python list of integers'''
    def to_list(self):
        out = []          # <-- Declare a Python list
        node = self.head  # <-- Create a temporary Node object
        
        while node:       # <-- Iterate untill we have nodes available
            out.append(int(str(node.value))) # <-- node.value is actually of type Node, therefore convert it into int before appending to the Python list
            node = node.next
        
        return out
      
      
#---------------------------------------- Write the Two Function Fefinitions ----------------------------------------------#
################# Define Merge Method ##############

def merge(list1, list2):
    # TODO: Implement this function so that it merges the two linked lists in a single, sorted linked list.
    # assume both input linked lists have be sorted
    '''
    The arguments list1, list2 must be of type LinkedList.
    The merge() function must return an instance of LinkedList.
    '''
    new_list = LinkedList(None)
    if list1 is None:
        return list2
    
    elif list2 is None:
        return list1
    
    elif list1 is None and list2 is None:
        return None
    
    else:
        node_1 = list1.head
        node_2 = list2.head
        
        while node_1 != None or node_2 != None:
            if node_1 is None:
                new_list.append(node_2.value)
                node_2 = node_2.next
            
            elif node_2 is None:
                new_list.append(node_1.value)
                node_1 = node_1.next
            
            else:
                if node_1.value <= node_2.value:
                    new_list.append(node_1.value)
                    node_1 = node_1.next
                
                else:
                    new_list.append(node_2.value)
                    node_2 = node_2.next
        
        return new_list
      
################## Define NestedLinkedList Method ####################      
      
 ''' In a NESTED LinkedList object, each node will be a simple LinkedList in itself'''
class NestedLinkedList(LinkedList):
    def flatten(self):
        return self._flatten(self.head) # <-- self.head is a node for NestedLinkedList

    '''  A recursive function ''' 
    def _flatten(self, node):
        
        # A termination condition
        if node.next is None:
            return merge(node.value, None) # <-- First argument is a simple LinkedList
        
        # _flatten() is calling itself untill a termination condition is achieved
        return merge(node.value, self._flatten(node.next)) # <-- Both arguments are a simple LinkedList each
