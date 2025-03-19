#////////////////////////////////////////////////////////////////////////////////////
#///                                                                              ///
#///                           Printer Queue Manger                               ///
#///                                                                              ///
#////////////////////////////////////////////////////////////////////////////////////
#///                                                                              ///
#///   This program aims to simulate a printer that can handle multiple documents ///
#///   and report the time for each document in queue for printing                ///
#///   The printer has a speed of 2pages/min                                      ///
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
#//  Id: printer_queue.py, v 1.0
#//
#//  $Date: 2025-3-18
#//  $Revision: 1.0 
#//  $Author:  Ujval Madhu

class Queue:
    def __init__(self):
        self.list = []
    
    def enqueue(self,data):
        self.list.append(data)
    
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Empty Queue, cannot Dequeue")
        return self.list.pop(0)
    
    def front(self):
        if self.isEmpty():
            raise IndexError("Empty Queue")
        return self.list[0]
    
    def rear(self):
        if self.isEmpty():
            raise IndexError("Empty Queue")
        return self.list[-1]
    
    def get_size(self):
        return len(self.list)
    
    def isEmpty(self):
        return len(self.list) == 0
    

def printDocuments(documents):
    # Args: Documents: Tuples of format [("name1", count1), ("name2", count2), ("name3", count3)]
    # name1 = string name of the document, count = number of copies

    pq = Queue()
    result = []

    for item in documents:
        pq.enqueue(item)
    
    for i in range(0, pq.get_size()):
        task = pq.dequeue()
        name = task[0]
        copies = task[1]
        ptime = int(copies)*2
        result.append("Document "+name+" printed in "+str(ptime)+"minutes")
    
    print(result)


# Testing

documents = [("Notes", 10), ("Questions", 3), ("Report", 7)]
printDocuments(documents)


