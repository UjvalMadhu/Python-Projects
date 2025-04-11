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
            temp_node = current.next
            current.next = prev_node
            prev_node = current
            current = temp_node

        self.head = prev_node

    def print_ll(self):
        if self.head is None:
            return []
        
        current = self.head

        while current:
            print(str(current.data) + "->", end ="")
            current = current.next
        print("")



a = linked_list()
a.append(3)
a.append(5)
a.append(7)
a.append(0)
a.append(9)
a.print_ll()
a.reverse()
a.print_ll()