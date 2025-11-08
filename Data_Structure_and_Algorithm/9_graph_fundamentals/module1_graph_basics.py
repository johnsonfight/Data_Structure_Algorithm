"""
Module 1: Graph Basics - Interactive Practice
==============================================

Master graph representation and basic operations!

In this module, we'll master:
1. Graph representations (adjacency list, matrix, edge list)
2. Building graphs from edges
3. Basic graph operations
4. Converting between representations

Graphs are everywhere - let's build the foundation!
"""

from collections import defaultdict, deque
from typing import List, Dict, Set

# =============================================================================
# PART 1: GRAPH REPRESENTATIONS
# =============================================================================

"""
CONCEPT: What is a Graph?
==========================

A GRAPH is a collection of vertices (nodes) connected by edges.

Components:
- Vertices (V): nodes/points
- Edges (E): connections between vertices

Types:
1. Directed vs Undirected
   - Directed: edges have direction (A → B)
   - Undirected: edges are bidirectional (A ↔ B)

2. Weighted vs Unweighted
   - Weighted: edges have values/costs
   - Unweighted: all edges equal weight

3. Cyclic vs Acyclic
   - Cyclic: contains cycles
   - Acyclic: no cycles (DAG = Directed Acyclic Graph)

Example Graph (undirected):
    0 --- 1
    |     |
    2 --- 3

Edges: [(0,1), (0,2), (1,3), (2,3)]
"""

"""
CONCEPT: Graph Representation
==============================

Three main ways to represent graphs:

1. ADJACENCY LIST (most common!)
   - Hash map: vertex → list of neighbors
   - Space: O(V + E)
   - Fast neighbor lookup: O(degree)
   - Best for sparse graphs

   Example: {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}

2. ADJACENCY MATRIX
   - 2D array: matrix[i][j] = 1 if edge exists
   - Space: O(V²)
   - Fast edge check: O(1)
   - Best for dense graphs

   Example:
       0  1  2  3
   0 [ 0  1  1  0 ]
   1 [ 1  0  0  1 ]
   2 [ 1  0  0  1 ]
   3 [ 0  1  1  0 ]

3. EDGE LIST
   - List of edges: [(u, v), ...]
   - Space: O(E)
   - Simple but slow queries
   - Best for algorithms like Kruskal's MST

   Example: [(0,1), (0,2), (1,3), (2,3)]

When to use:
- ✅ Adjacency List: Most interview problems (sparse graphs)
- ✅ Adjacency Matrix: Dense graphs, need fast edge lookup
- ✅ Edge List: Sorting edges, union-find problems
"""

def build_adjacency_list(n, edges, directed=False):
    """
    Build adjacency list from edge list

    Args:
        n: int - number of vertices (0 to n-1)
        edges: List[List[int]] - list of [u, v] edges
        directed: bool - whether graph is directed

    Returns:
        Dict[int, List[int]] - adjacency list

    Example:
        n = 4, edges = [[0,1],[0,2],[1,3],[2,3]]
        Returns: {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2]}
    """
    # TODO: Implement
    # Hint: Use defaultdict(list)
    # Hint: For undirected, add both u→v and v→u
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        if not directed:
            graph[v].append(u)

    return graph

# TEACHER'S SOLUTION:
def build_adjacency_list_solution(n, edges, directed=False):
    """Build adjacency list - most common representation"""
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        if not directed:
            graph[v].append(u)

    return graph

def build_adjacency_matrix(n, edges, directed=False):
    """
    Build adjacency matrix from edge list

    Args:
        n: int - number of vertices
        edges: List[List[int]] - edges
        directed: bool - directed graph

    Returns:
        List[List[int]] - n x n matrix

    EXAMPLE (Undirected Graph):
    ============================
    Input:
        n = 4
        edges = [[0,1], [0,2], [1,3], [2,3]]
        directed = False

    Output (4x4 matrix):
            0  1  2  3
        0 [ 0  1  1  0 ]  ← Row 0: edges to vertices 1, 2
        1 [ 1  0  0  1 ]  ← Row 1: edges to vertices 0, 3
        2 [ 1  0  0  1 ]  ← Row 2: edges to vertices 0, 3
        3 [ 0  1  1  0 ]  ← Row 3: edges to vertices 1, 2

    How to read the matrix:
        - matrix[u][v] = 1 means there IS an edge between u and v
        - matrix[u][v] = 0 means there is NO edge between u and v
        - For undirected: matrix[u][v] = matrix[v][u] (symmetric!)
        - For directed: only one direction is marked

    Visualization of graph:
        0 --- 1
        |     |
        2 --- 3

    EXAMPLE (Directed Graph):
    ==========================
    Input:
        n = 4
        edges = [[0,1], [0,2], [1,3], [2,3]]
        directed = True

    Output (4x4 matrix):
            0  1  2  3
        0 [ 0  1  1  0 ]  ← Row 0: outgoing edges to 1, 2
        1 [ 0  0  0  1 ]  ← Row 1: outgoing edge to 3
        2 [ 0  0  0  1 ]  ← Row 2: outgoing edge to 3
        3 [ 0  0  0  0 ]  ← Row 3: no outgoing edges

    How to read:
        - matrix[0][1] = 1 means edge 0→1 exists
        - matrix[1][0] = 0 means edge 1→0 does NOT exist (one-way!)
        - NOT symmetric for directed graphs

    Visualization of graph:
        0 → 1
        ↓   ↓
        2 → 3
    """
    # TODO: Implement
    # Hint: Create n x n matrix of zeros
    # Hint: Set matrix[u][v] = 1 for each edge
    # Hint: For undirected, also set matrix[v][u] = 1
    matrix = [[0] * n for _ in range(n)]

    for u, v in edges:
        matrix[u][v] = 1
        if not directed:
            matrix[v][u] = 1
    return matrix

# TEACHER'S SOLUTION:
def build_adjacency_matrix_solution(n, edges, directed=False):
    """Build adjacency matrix"""
    matrix = [[0] * n for _ in range(n)]

    for u, v in edges:
        matrix[u][v] = 1
        if not directed:
            matrix[v][u] = 1

    return matrix

def adjacency_list_to_matrix(graph, n):
    """
    Convert adjacency list to matrix

    Args:
        graph: Dict[int, List[int]] - adjacency list
        n: int - number of vertices

    Returns:
        List[List[int]] - adjacency matrix
    """
    matrix = [[0] * n for _ in range(n)]

    for u in graph:
        for v in graph[u]:
            matrix[u][v] = 1

    return matrix

# TEACHER'S SOLUTION:
def adjacency_list_to_matrix_solution(graph, n):
    """Convert list to matrix"""
    matrix = [[0] * n for _ in range(n)]

    for u in graph:
        for v in graph[u]:
            matrix[u][v] = 1

    return matrix

# =============================================================================
# PART 2: BASIC GRAPH OPERATIONS
# =============================================================================

def count_edges(graph, directed=False):
    """
    Count number of edges in graph

    Args:
        graph: Dict[int, List[int]] - adjacency list
        directed: bool - is directed

    Returns:
        int - number of edges
    """
    # TODO: Count edges
    # Hint: For undirected, divide by 2 (each edge counted twice)
    total = 0
    for vertices in graph.values():
        total += len(vertices)

    if not directed:
        total //= 2

    return total

# TEACHER'S SOLUTION:
def count_edges_solution(graph, directed=False):
    """Count edges in adjacency list"""
    total = sum(len(neighbors) for neighbors in graph.values())

    if not directed:
        total //= 2  # Each edge counted twice

    return total

def get_degree(graph, node, directed=False):
    """
    Get degree of a node

    For directed graphs:
    - out_degree = number of outgoing edges
    - in_degree = number of incoming edges

    Args:
        graph: Dict[int, List[int]]
        node: int - vertex
        directed: bool

    Returns:
        int - degree (or out-degree for directed)
    """

    return len(graph[node])

# TEACHER'S SOLUTION:
def get_degree_solution(graph, node, directed=False):
    """Get node degree (out-degree for directed)"""
    return len(graph[node])

def has_edge(graph, u, v):
    """
    Check if edge exists between u and v

    Args:
        graph: Dict[int, List[int]]
        u, v: int - vertices

    Returns:
        bool - True if edge exists
    """
    # TODO: Check if v in graph[u]
    return v in graph.get(u, [])

# TEACHER'S SOLUTION:
def has_edge_solution(graph, u, v):
    """Check edge existence"""
    return v in graph.get(u, [])

# =============================================================================
# PART 3: LEETCODE PROBLEMS
# =============================================================================

def findJudge(n, trust):
    """
    LC 997: Find the Town Judge

    The town judge:
    - Trusts nobody (out-degree = 0)
    - Everyone trusts them (in-degree = n-1)

    Example:
    Input: n = 3, trust = [[1,3],[2,3]]
    Output: 3 (person 3 is the judge)

    Args:
        n: int - number of people (1 to n)
        trust: List[List[int]] - [a, b] means a trusts b

    Returns:
        int - the judge, or -1 if none exists
    """
    # TODO: Implement
    # Hint: Track in-degree and out-degree for each person
    # Hint: Judge has in-degree = n-1 and out-degree = 0
    outgoing = defaultdict(int)
    incoming = defaultdict(int)
    
    for src, dst in trust:
        outgoing[src] += 1
        incoming[dst] += 1

    for i in range(1, n + 1):
        if outgoing[i] == 0 and incoming[i] == n - 1:
            return i
        
    return -1

# TEACHER'S SOLUTION:
def findJudge_solution(n, trust):
    """
    Degree counting approach
    O(E) time, O(n) space
    """
    if n == 1:
        return 1

    in_degree = [0] * (n + 1)
    out_degree = [0] * (n + 1)

    for a, b in trust:
        out_degree[a] += 1
        in_degree[b] += 1

    for person in range(1, n + 1):
        if in_degree[person] == n - 1 and out_degree[person] == 0:
            return person

    return -1

def validPath(n, edges, source, destination):
    """
    LC 1971: Find if Path Exists in Graph

    Check if path exists from source to destination.

    Example:
    Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
    Output: True

    Args:
        n: int - number of vertices (0 to n-1)
        edges: List[List[int]] - undirected edges
        source: int - start vertex
        destination: int - end vertex

    Returns:
        bool - True if path exists
    """
    # TODO: Build graph, then DFS/BFS to check connectivity
    # Hint: Will learn DFS/BFS in next module, but can try now!
    pass

# TEACHER'S SOLUTION:
def validPath_solution(n, edges, source, destination):
    """
    BFS to check connectivity
    O(V + E) time, O(V + E) space
    """
    if source == destination:
        return True

    # Build adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # BFS
    visited = set([source])
    queue = deque([source])

    while queue:
        node = queue.popleft()

        if node == destination:
            return True

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False

# =============================================================================
# PART 4: TESTING
# =============================================================================

def test_graph_basics():
    """Test all graph operations"""
    print("=" * 50)
    print("GRAPH BASICS TEST SUITE")
    print("=" * 50)

    # Test build adjacency list
    print("\nTEST 1: Build Adjacency List")
    edges = [[0,1], [0,2], [1,3], [2,3]]
    graph = build_adjacency_list_solution(4, edges)
    print(f"Edges: {edges}")
    print(f"Adjacency List: {dict(graph)}")

    # Test build adjacency matrix
    print("\nTEST 2: Build Adjacency Matrix")
    matrix = build_adjacency_matrix_solution(4, edges)
    print("Adjacency Matrix:")
    for row in matrix:
        print(row)

    # Test count edges
    print("\nTEST 3: Count Edges")
    edge_count = count_edges_solution(graph, directed=False)
    print(f"Number of edges: {edge_count}")

    # Test degree
    print("\nTEST 4: Node Degree")
    for node in range(4):
        degree = get_degree_solution(graph, node)
        print(f"Degree of node {node}: {degree}")

    # Test find judge
    print("\nTEST 5: Find the Town Judge")
    trust = [[1,3], [2,3]]
    judge = findJudge_solution(3, trust)
    print(f"Trust: {trust}")
    print(f"Judge: {judge}")

    # Test valid path
    print("\nTEST 6: Find if Path Exists")
    edges = [[0,1], [1,2], [2,0]]
    exists = validPath_solution(3, edges, 0, 2)
    print(f"Path from 0 to 2 exists: {exists}")

    print("\n" + "=" * 50)

if __name__ == "__main__":
    print("Welcome to Module 1: Graph Basics!")
    print("Master graph representations and operations!")
    print("\nComplete the TODOs, then run test_graph_basics()")
