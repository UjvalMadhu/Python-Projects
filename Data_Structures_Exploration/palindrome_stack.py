#////////////////////////////////////////////////////////////////////////////////////
#///                                                                              ///
#///       Palindrome Checker using Stack implemented with a Linked List          ///
#///                                                                              ///
#////////////////////////////////////////////////////////////////////////////////////
#///                                                                              ///
#///   Checks whether a given string is a Palindrome or not, (same when reversed) ///
#///   overlooks case, spaces, and punctuation marks                              ///
#///   Examples 'madam', 'mom', 'race-car', 'Madam, I'm Adam'                     ///
#///                                                                              ///
#///   Acknowledgement: Dhhyey Desai, Python Data Structures Course               ///
#///                                                                              ///
#///   Copyright (C) 2025 Ujval Madhu,                                            ///
#///   This program is free software: you can redistribute it and/or modify       ///
#///   it under the terms of the GNU General Public License as published by       ///
#///   the Free Software Foundation, either version 3 of the License, or          ///
#///   (at your option) any later version.                                        ///
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
#//  Id: palindrome_stack.py, v 1.0
#//
#//  $Date: 2025-3-18
#//  $Revision: 1.0 
#//  $Author:  Ujval Madhu

import re

class Node:                                   # Node for representing the Stack Head
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:                                 # Linked List Implementation of Stack
    def __init__(self, in_list = None):
        self.head = None
        self.size = 0

        if in_list:
            for item in in_list:
                self.push(item)

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def is_empty(self):
        return self.head is None

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is Empty, cannot Pop")
        data = self.head
        self.head = self.head.next
        self.size -=1
        return data
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is Empty, cannot Peek")
        return self.head
        
    def get_size(self):
        return self.size
    

#======================================================================================
print("\n*** Palindrome Checker *** \n")

str = input("Enter String: ")
#str = "321 123"
letters = re.findall(r'[a-zA-Z0-9]',str.lower())

s1 = Stack(letters)
s2 = letters[::-1]


for i in range(0,s1.get_size()):
    if(s1.pop().data != s2.pop()):
        print("\""+str+"\" is not a palindrome")
        exit(0)
print("\""+str+"\" is a Palindrome")