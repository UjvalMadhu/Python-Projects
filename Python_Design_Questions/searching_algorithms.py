#////////////////////////////////////////////////////////////////////////////////////
#///                                                                              ///
#///                           Searching Algorithms                               ///
#///                                                                              ///
#////////////////////////////////////////////////////////////////////////////////////
#///                                                                              ///
#///   This Program demonstrates various sorting algorithm implementation         ///
#///   The Algorithms Include:                                                    ///
#///   1. Linear Search                                                           ///
#///   2. Binary Search                                                           ///
#///   3. Depth First Search                                                      ///
#///   4. Breath First Search                                                     ///
#///   5. Dijkstra's Algorithm                                                    ///
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
#//  Id: spiral_matrix.py, v 1.0
#//
#//  $Date: 2025-04-11
#//  $Revision: 1.0 
#//  $Author:  Ujval Madhu
import collections
# Linear Search
def linear_search(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return None

# Binary Search
def binary_search(arr, item):
    arr = merge_sort(arr)
    left = 0
    right = len(arr) -1

    while left <= right:
        mid = (left + right) // 2

        if item < mid:
            right = mid - 1
        elif item > mid:
            left = mid + 1
        else:
            return mid
    
    return None

# Merge sort for sorting in Binary Search

def merge_sort(arr):
    if(len(arr)<= 1):
        return arr
    
    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left,right)

def merge(left, right):
    i,j = 0,0
    result = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    
    result.extend(left[i:])
    result.extend(right[j:])

    return result

        
# Depth First Search
# Explore as far as possible along each branch and then backtrack

def dfs(graph, start_node, visited = None):
    if visited is None:
        visited = set()
    visited.add(start_node)
    print(f"Visiting node: {start_node}")
    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return list(visited)

# Breadth First Search
# Explores Nodes level by level, all immediate first then next level and so on.
def bfs(graph, start_node):
    visited = set()
    queue = collections.deque([start_node])
    visited.add(start_node)

    while queue:
        node = queue.popleft()
        print(node, end = " ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# Testing DFS and BFS
graph = {
    'A' : ['B', 'C'],
    'B' : ['A', 'D', 'E'],
    'C' : ['E', 'G', 'F'],
    'D' : ['F', 'A'],
    'E' : ['G', 'D', 'A'],
    'F' : ['A', 'C'],
    'G' : ['B', 'D'],
}
print("Depth First Search")
dfs(graph, 'A')
print("Breadth First Search")
bfs(graph,'A')


# Dijkstra's Algorithm
import heapq
def dijkstra(graph, start):
    distances = {node : float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    visited_nodes = set()

    while pq:
        dist, node = heapq.heappop(pq)

        if node in visited_nodes:
            continue

        visited_nodes.add(node)

        for neighbor, weight in graph.get(node, {}).items():
            if neighbor not in visited_nodes:
                n_dist = weight + dist

                if n_dist < distances[neighbor]:
                    distances[neighbor] = n_dist
                    heapq.heappush(pq, (n_dist, neighbor))
    
    return distances

# Testing

# Defining the Required Graph
graph_dj = {
    'A': {'B': 6, 'D': 1},
    'B': {'A': 6, 'D': 2, 'E': 2, 'C':5},
    'C': {'B': 5, 'E': 5},
    'D': {'A': 1, 'B': 2, 'E': 1},
    'E': {'B': 2, 'D': 1, 'C': 5}
}

print("\nDijkstra's Algorithm")

print(dijkstra(graph_dj, 'A'))
