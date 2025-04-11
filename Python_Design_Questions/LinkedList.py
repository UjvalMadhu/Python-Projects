class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        
        current_node.next = new_node

    def reverse(self):
        if self.head is None:
            return
        current = self.head
        prev_node = None
        while current:
            temp = current.next
            current.next = prev_node
            prev_node = current
            current = temp
            if current == None:
                break
        
        self.head = prev_node

        

    def print_ll(self):
        if self.head is None:
            return []
        
        current = self.head

        while current:
            print(str(current.data) + "->", end ="")
            current = current.next
        print("None")

def rev_rec(head):
    if head is None or head.next is None:
        return head
    
    new_head = rev_rec(head.next)
    head.next.next = head
    head.next = None

    return new_head

def reverse_linked_list_recursive(head):
    # Base case: empty list or last node
    if not head or not head.next:
        return head
    
    # Recursively reverse the rest of the list
    new_head = reverse_linked_list_recursive(head.next)
    
    # Reverse the pointer of the next node
    head.next.next = head
    
    # Set the current node's next to None (will be updated in the parent call)
    head.next = None
    
    return new_head

a = linked_list()
a.append(3)
a.append(5)
a.append(7)
a.append(0)
a.append(9)
print(str(a.head.next.data))
a.print_ll()
a.reverse()
a.print_ll()
y =linked_list()
a.head = reverse_linked_list_recursive(a.head)
a.print_ll()