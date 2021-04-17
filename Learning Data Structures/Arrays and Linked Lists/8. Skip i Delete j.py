# Problem Statement
# - You are given the head of a linked list and two integers, i and j. 
# - You have to retain the first i nodes and then delete the next j nodes. Continue doing so until the end of the linked list.


# LinkedList Node class for reference
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def skip_i_delete_j(head, i, j):
    """
    :param: head - head of linked list
    :param: i - first `i` nodes that are to be skipped
    :param: j - next `j` nodes that are to be deleted
    return - return the updated head of the linked list
    """
    
    if i == 0:
        return None
    
    elif j == 0:
        return head
    
    elif head is None or i < 0 or j < 0:
        return None
    
    else:
        current = head
        prev = None
        
        while current:
            for _ in range(i - 1):   #loop over the first i-1 elements
                if current is None:
                    return head
                    
                else:
                    current = current.next
            prev = current
            current = current.next
                                            
            for _ in range(j):
                if current is None:
                    break
                    
                else:
                    current = current.next
            prev.next = current
         
        
        return head 
