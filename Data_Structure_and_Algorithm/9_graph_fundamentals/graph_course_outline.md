# Graph Fundamentals - Learning Course Outline

## Course Overview
Master graphs - one of the most important and versatile data structures. Learn representation, traversal algorithms, and solve complex real-world problems.

---

## Module 1: Graph Basics

### 1.1 What is a Graph?
- Vertices (nodes) and edges (connections)
- Directed vs undirected graphs
- Weighted vs unweighted graphs
- Cyclic vs acyclic graphs (DAG)
- Connected vs disconnected graphs

### 1.2 Graph Representation
- Adjacency Matrix (2D array)
- Adjacency List (hash map of lists)
- Edge List
- Tradeoffs: Space O(V²) vs O(V+E)
- When to use each representation

### 1.3 Graph Terminology
- Degree (in-degree, out-degree)
- Path, cycle, connected component
- Tree vs graph
- Bipartite graphs
- Complete graphs

### Practice Problems:
- Build adjacency list from edge list
- Convert between representations
- LC 997: Find the Town Judge
- Count vertices, edges, degrees

---

## Module 2: Graph Traversal - DFS

### 2.1 Depth-First Search (DFS)
- Concept: Go deep before going wide
- Recursive implementation
- Iterative implementation (stack)
- Time: O(V+E), Space: O(V)

### 2.2 DFS Applications
- Find all paths
- Cycle detection
- Connected components
- Topological sort preparation

### 2.3 Visited Tracking
- Boolean array
- Hash set
- Marking in-place
- Backtracking (unmark after visit)

### Practice Problems:
- LC 200: Number of Islands
- LC 695: Max Area of Island
- LC 133: Clone Graph
- LC 797: All Paths From Source to Target

---

## Module 3: Graph Traversal - BFS

### 3.1 Breadth-First Search (BFS)
- Concept: Level-by-level exploration
- Queue-based implementation
- Shortest path in unweighted graph
- Time: O(V+E), Space: O(V)

### 3.2 BFS Applications
- Shortest path
- Level-order traversal
- Minimum steps problems
- Distance from source

### 3.3 BFS Patterns
- Single source BFS
- Multi-source BFS
- Bidirectional BFS
- 0-1 BFS for weighted graphs

### Practice Problems:
- LC 102: Binary Tree Level Order (review)
- LC 994: Rotting Oranges (multi-source)
- LC 127: Word Ladder
- LC 1091: Shortest Path in Binary Matrix

---

## Module 4: Cycle Detection

### 4.1 Cycle Detection in Undirected Graphs
- DFS with parent tracking
- Union-Find approach
- Detecting back edges

### 4.2 Cycle Detection in Directed Graphs
- DFS with three colors (white, gray, black)
- Detecting back edges in directed graph
- Recursion stack tracking

### 4.3 Applications
- Deadlock detection
- Dependency resolution
- Course prerequisites

### Practice Problems:
- LC 207: Course Schedule (cycle in directed)
- LC 210: Course Schedule II (topological sort)
- LC 684: Redundant Connection (undirected)
- LC 685: Redundant Connection II (directed)

---

## Module 5: Topological Sort

### 5.1 Topological Sort Concept
- Linear ordering of vertices
- Only for DAG (Directed Acyclic Graph)
- Multiple valid orderings possible
- Applications: task scheduling, build systems

### 5.2 Kahn's Algorithm (BFS-based)
- In-degree counting
- Queue of zero in-degree vertices
- Process and reduce in-degrees
- Detect cycle if not all processed

### 5.3 DFS-based Topological Sort
- Post-order DFS
- Reverse of finish times
- Stack-based approach

### Practice Problems:
- LC 207: Course Schedule
- LC 210: Course Schedule II
- LC 269: Alien Dictionary
- LC 1203: Sort Items by Groups

---

## Module 6: Union-Find (Disjoint Set)

### 6.1 Union-Find Basics
- Find operation (find root/parent)
- Union operation (merge sets)
- Applications: connected components, MST

### 6.2 Optimizations
- Path compression (find optimization)
- Union by rank/size
- Nearly O(1) amortized time

### 6.3 Union-Find Patterns
- Detecting cycles
- Connected components
- Dynamic connectivity
- Kruskal's MST algorithm

### Practice Problems:
- LC 200: Number of Islands (alternative approach)
- LC 547: Number of Provinces
- LC 684: Redundant Connection
- LC 721: Accounts Merge
- LC 990: Satisfiability of Equality Equations

---

## Module 7: Shortest Path Algorithms

### 7.1 BFS for Unweighted Graphs
- Shortest path in unweighted graph
- Single source shortest path
- All pairs in small graphs

### 7.2 Dijkstra's Algorithm
- Shortest path in weighted graph (non-negative)
- Priority queue (min-heap) implementation
- Time: O((V+E) log V)
- Greedy algorithm

### 7.3 Bellman-Ford Algorithm
- Handles negative weights
- Detects negative cycles
- Time: O(V*E)
- Dynamic programming approach

### Practice Problems:
- LC 743: Network Delay Time (Dijkstra)
- LC 787: Cheapest Flights Within K Stops
- LC 1334: Find City With Smallest Number of Neighbors
- LC 1514: Path with Maximum Probability

---

## Module 8: Minimum Spanning Tree (MST)

### 8.1 MST Concept
- Spanning tree: connects all vertices
- Minimum: smallest total edge weight
- Applications: network design, clustering

### 8.2 Kruskal's Algorithm
- Sort edges by weight
- Union-Find to avoid cycles
- Greedy approach
- Time: O(E log E)

### 8.3 Prim's Algorithm
- Start from arbitrary vertex
- Grow tree by adding minimum edge
- Priority queue implementation
- Time: O((V+E) log V)

### Practice Problems:
- LC 1584: Min Cost to Connect All Points
- LC 1135: Connecting Cities With Minimum Cost
- LC 1168: Optimize Water Distribution

---

## Module 9: Advanced Graph Patterns

### 9.1 Bipartite Graphs
- Two-coloring problem
- BFS/DFS coloring
- Detecting bipartiteness
- Applications: matching problems

### 9.2 Strongly Connected Components (SCC)
- Kosaraju's algorithm
- Tarjan's algorithm
- Applications: web graph analysis

### 9.3 Articulation Points & Bridges
- Critical nodes/edges
- DFS-based detection
- Applications: network reliability

### Practice Problems:
- LC 785: Is Graph Bipartite?
- LC 886: Possible Bipartition
- LC 1192: Critical Connections in a Network
- LC 1568: Minimum Days to Disconnect Island

---

## Module 10: Matrix as Graph

### 10.1 Grid as Graph
- 4-directional vs 8-directional
- Treating cells as vertices
- DFS/BFS on grids
- Boundary handling

### 10.2 Common Grid Patterns
- Island problems
- Flood fill
- Shortest path in grid
- Multi-source BFS

### 10.3 Advanced Grid Problems
- Obstacles and walls
- Dynamic grids
- State-based grids

### Practice Problems:
- LC 200: Number of Islands
- LC 286: Walls and Gates (multi-source)
- LC 417: Pacific Atlantic Water Flow
- LC 1091: Shortest Path in Binary Matrix
- LC 1926: Nearest Exit from Entrance in Maze

---

## Learning Path Recommendations

### **Beginner Path**: Modules 1-3 (3-4 weeks)
Graph basics, DFS, BFS, basic traversal problems

### **Intermediate Path**: Modules 4-6 (4-6 weeks)
Cycle detection, topological sort, union-find

### **Advanced Path**: Modules 7-10 (4-6 weeks)
Shortest paths, MST, advanced patterns, grids

---

## Key Algorithms Summary

### Essential Algorithms:
1. **DFS** (recursive & iterative)
2. **BFS** (queue-based)
3. **Topological Sort** (Kahn's & DFS)
4. **Union-Find** (with path compression)
5. **Dijkstra's** (shortest path)
6. **Cycle Detection** (directed & undirected)
7. **Bipartite Check** (2-coloring)

### Time Complexities:
- DFS/BFS: O(V + E)
- Topological Sort: O(V + E)
- Union-Find: O(α(n)) ≈ O(1) amortized
- Dijkstra: O((V + E) log V)
- Bellman-Ford: O(V * E)
- Kruskal/Prim: O(E log E) or O((V+E) log V)

---

## Graph Representation Comparison

| Representation | Space | Check Edge | Get Neighbors | Add Vertex | Add Edge |
|----------------|-------|------------|---------------|------------|----------|
| Adj Matrix | O(V²) | O(1) | O(V) | O(V²) | O(1) |
| Adj List | O(V+E) | O(degree) | O(degree) | O(1) | O(1) |
| Edge List | O(E) | O(E) | O(E) | O(1) | O(1) |

**Most common**: Adjacency List (hash map of lists)

---

## Interview Tips

### When to Use Each Algorithm:
1. ✅ **DFS**: Paths, cycles, connectivity, backtracking
2. ✅ **BFS**: Shortest path (unweighted), level-order, minimum steps
3. ✅ **Topological Sort**: Dependencies, ordering, DAG
4. ✅ **Union-Find**: Dynamic connectivity, cycle detection, MST
5. ✅ **Dijkstra**: Shortest path (non-negative weights)
6. ✅ **BFS on grid**: Island problems, flood fill, matrix as graph

### Common Mistakes:
- ❌ Not handling disconnected graphs
- ❌ Forgetting visited tracking (infinite loops)
- ❌ Using DFS when BFS needed (shortest path)
- ❌ Wrong representation (matrix vs list)
- ❌ Not checking for cycles in topological sort
- ❌ Modifying graph during traversal

---

## Python Graph Templates

### Adjacency List (most common):
```python
# Build from edges
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)  # undirected

# DFS
def dfs(node, visited):
    if node in visited:
        return
    visited.add(node)
    for neighbor in graph[node]:
        dfs(neighbor, visited)

# BFS
def bfs(start):
    queue = deque([start])
    visited = {start}
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

---

## Success Metrics
- ✅ Implement DFS and BFS from scratch in < 10 minutes
- ✅ Detect cycles in directed/undirected graphs
- ✅ Perform topological sort (Kahn's algorithm)
- ✅ Solve island problems using DFS/BFS
- ✅ Implement Union-Find with optimizations
- ✅ Apply Dijkstra for shortest path problems
- ✅ Choose correct graph representation for problem

---

## Real-World Applications
- **Social Networks**: Friend recommendations (BFS)
- **Maps**: Shortest routes (Dijkstra)
- **Compilers**: Dependency resolution (Topological Sort)
- **Networks**: Minimum cost connections (MST)
- **Games**: Pathfinding (A*, Dijkstra)
- **Biology**: Protein interactions
- **Web**: PageRank (graph traversal)
