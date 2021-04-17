# Problem Statement
#- Given a linked list with integer data, arrange the elements in such a manner that all nodes with even numbers are placed after odd numbers. 
#- Do not create any new nodes and avoid using any other data structure. The relative order of even and odd elements must not change.


def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """
    if head is None:
        return None
    
    odd_head = None
    odd_tail = None
    
    even_head = None
    even_tail = None
    
    current_node = head
    
    while current_node:
        
        if current_node.data % 2 == 0:
            if even_head == None:
                even_head = current_node
                even_tail = current_node
            else:  
                even_tail.next = current_node
                even_tail = even_tail.next
        
        else:
             if odd_head == None:
                odd_head = current_node
                odd_tail = current_node
                
             else:
                odd_tail.next = current_node
                odd_tail = odd_tail.next
            

        current_node = current_node.next
        
    if odd_head is None:
        return even_head
    
    odd_tail.next = even_head 
    
    return odd_head
    
