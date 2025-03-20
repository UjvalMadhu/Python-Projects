#////////////////////////////////////////////////////////////////////////////////////
#///                                                                              ///
#///                          Sorted Linked Lists                                 ///
#///                                                                              ///
#////////////////////////////////////////////////////////////////////////////////////
#///                                                                              ///
#///   This program implements a linked list structure, with capabilities, to     ///
#///   insert elements in a sorted manner from a random list, search for elements ///
#///   and delete duplicate values if required.                                   ///
#///                                                                              ///
#///   Acknowledgement: Ryan Mitchel, Python Data Structures: Linked Lists Course ///
#///                                                                              ///
#///   Copyright (C) 2025 Ujval Madhu,                                            ///
#///   This program is free software: you can redistribute it and/or modify       ///
#///   it under the terms of the GNU General Public License as published by       ///
#///   the Free Software Foundation, either version 3 of the License, or          ///
#///   (at your option) any later version.                                        ///
#///                                                                              ///
#///                                                                              ///
#///   This program is distributed in the hope that it will be useful,            ///
#///   but WITHOUT ANY WARRANTY; without even the implied warranty of             ///
#///   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the              ///
#///   GNU General Public License for more details.                               ///
#///                                                                              ///
#///   You should have received a copy of the GNU General Public License          ///
#///   along with this program.  If not, see <https://www.gnu.org/licenses/>.     ///
#///                                                                              ///
#////////////////////////////////////////////////////////////////////////////////////
#//  CVS Log
#//
#//  Id: linked_lists.py, v 1.0
#//
#//  $Date: 2025-3-19
#//  $Revision: 1.0 
#//  $Author:  Ujval Madhu

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedLists:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def search(self, data):                       # Checks whether an element is present in the Linked List
        current = self.data
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def delete(self, data):
        if not self.head:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def insert_sorted(self, data): # will only work for an already sorted Linked List
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
       
        if self.head.data > data:
            self.head.next = self.head
            self.head.data = data
            return
        
        current = self.head
        while current.next and current.next.data < data:
            current = current.next

        new_node.next = current.next
        current.next = new_node 

    def remove_dupes(self):
        items = []

        if self.head is None:
            return

        current = self.head
        items.append(current.data)
        while current:
            if current.next:
                if current.next.data in items:
                    current.next = current.next.next
                else: 
                    items.append(current.next.data)
                    current = current.next
            else: return


    def print(self):
        output =[]
        current = self.head
        while current is not None:
            output.append(str(current.data))
            current = current.next
        print('->'.join(output))



# Testing

ll1 = LinkedLists()
dl = [1,2,3,5,5,7,8,7,8,8,3,3,3,12,3]

for item in dl:
    ll1.append(item)
        

print('hi')
ll1.print()

ll1.remove_dupes()
ll1.print()