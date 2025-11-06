"""
Module 5: Topological Sort - Interactive Practice
==================================================

Master topological sorting for dependency resolution and task scheduling!

In this module, we'll cover:
1. Topological sort concept (only for DAG)
2. Kahn's algorithm (BFS-based, in-degree)
3. DFS-based topological sort (post-order)
4. Applications: course scheduling, build systems
5. Cycle detection via topological sort

Topological sort is essential for: dependency resolution, scheduling!
"""

from typing import List, Dict
from collections import defaultdict, deque

# =============================================================================
# PART 1: TOPOLOGICAL SORT FUNDAMENTALS
# =============================================================================

"""
CONCEPT: Topological Sort
==========================

Topological sort is a linear ordering of vertices in DAG such that:
For every edge u→v, u comes before v in the ordering.

Key constraint: Only valid for DAG (Directed Acyclic Graph)
If graph has cycle, topological sort doesn't exist!

Example:
Graph: 0→1, 0→2, 1→3, 2→3
Valid topological sorts:
- 0, 1, 2, 3
- 0, 2, 1, 3

Both valid because:
- 0 comes before 1, 2, 3 ✓
- 1 comes before 3 ✓
- 2 comes before 3 ✓

Real-world applications:
- Course scheduling (prerequisites)
- Task scheduling (dependencies)
- Build systems (compile order)
- Dependency resolution

Two algorithms:
1. Kahn's (BFS-based): Use in-degree
2. DFS-based: Use post-order finish times
"""

# =============================================================================
# PART 2: KAHN'S ALGORITHM (BFS-Based)
# =============================================================================

"""
CONCEPT: Kahn's Algorithm
==========================

Algorithm:
1. Compute in-degree for all vertices
2. Add all vertices with in-degree 0 to queue
3. While queue not empty:
   - Dequeue vertex u
   - Add u to result
   - For each neighbor v of u:
     - Decrease in-degree[v]
     - If in-degree[v] becomes 0, enqueue v
4. If result has all vertices → valid topological sort
   Else → cycle exists!

Time: O(V + E)
Space: O(V)

Advantage: Detects cycles! If result.size() < V → cycle exists
"""


def topologicalSort_kahn(n: int, edges: List[List[int]]) -> List[int]:
    """
    Topological sort using Kahn's algorithm (BFS)

    Example:
        n = 4, edges = [[0,1], [0,2], [1,3], [2,3]]
        Returns: [0, 1, 2, 3] or [0, 2, 1, 3]

    Args:
        n: Number of vertices
        edges: List of [u, v] directed edges

    Returns:
        List - Topological order, or empty if cycle exists

    Time: O(V + E)
    Space: O(V)
    """
    # TODO: Build graph and compute in-degrees
    # TODO: Add all vertices with in-degree 0 to queue
    # TODO: Process queue, decrease in-degrees, enqueue when becomes 0
    # TODO: Return result if size == n, else empty (cycle)
    pass


# TEACHER'S SOLUTION:
def topologicalSort_kahn_solution(n: int, edges: List[List[int]]) -> List[int]:
    """Kahn's algorithm for topological sort"""
    # Build graph and compute in-degrees
    graph = defaultdict(list)
    in_degree = [0] * n

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # Add all vertices with in-degree 0 to queue
    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)

    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        # Reduce in-degrees of neighbors
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If all vertices processed → valid topological sort
    # Else → cycle exists
    return result if len(result) == n else []


# =============================================================================
# PART 3: DFS-BASED TOPOLOGICAL SORT
# =============================================================================

"""
CONCEPT: DFS-Based Topological Sort
====================================

Algorithm:
1. Do DFS from all unvisited vertices
2. When a vertex finishes (all its descendants explored), add to stack
3. Stack in reverse order gives topological sort

Key insight: Vertices with higher finish times come first!

Finish time: When DFS backtracks from a vertex (after exploring all neighbors)

Example:
Graph: 0→1→2, 0→3
DFS from 0:
  - Visit 0 (start)
  - Visit 1 (neighbor of 0)
  - Visit 2 (neighbor of 1)
  - Finish 2 (no more neighbors) → add to stack
  - Finish 1 (no more neighbors) → add to stack
  - Visit 3 (neighbor of 0)
  - Finish 3 (no more neighbors) → add to stack
  - Finish 0 (no more neighbors) → add to stack

Stack: [0, 3, 1, 2]
Result: [2, 1, 3, 0] (reverse) ✓

Time: O(V + E)
Space: O(V)

Advantage: More intuitive DFS structure
Disadvantage: Doesn't obviously detect cycles
"""


def topologicalSort_dfs(n: int, edges: List[List[int]]) -> List[int]:
    """
    Topological sort using DFS (post-order)

    Example:
        n = 4, edges = [[0,1], [0,2], [1,3], [2,3]]
        Returns: [0, 1, 2, 3] or [0, 2, 1, 3] (different valid orders)

    Args:
        n: Number of vertices
        edges: List of [u, v] directed edges

    Returns:
        List - Topological order

    Time: O(V + E)
    Space: O(V)
    """
    # TODO: Build graph
    # TODO: DFS from each unvisited node
    # TODO: When backtrack (finish), add node to stack
    # TODO: Return stack reversed
    pass


# TEACHER'S SOLUTION:
def topologicalSort_dfs_solution(n: int, edges: List[List[int]]) -> List[int]:
    """DFS-based topological sort"""
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)  # Add after exploring all neighbors

    # DFS from each unvisited node
    for i in range(n):
        if i not in visited:
            dfs(i)

    return stack[::-1]  # Return reversed


# =============================================================================
# PART 4: COURSE SCHEDULE II (LC 210)
# =============================================================================

"""
CONCEPT: Course Schedule II
============================

Problem: Return valid course order given prerequisites.
If impossible, return empty array.

This is topological sort with cycle detection!

Example:
numCourses = 4
prerequisites = [[1,0], [2,0], [3,1], [3,2]]

Order: 0→1→3, 0→2→3
Valid courses: 0, 1, 2, 3 or 0, 2, 1, 3

Return any valid topological sort!
"""


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    Return valid course order (topological sort)

    Example:
        numCourses = 4, prerequisites = [[1,0], [2,0], [3,1], [3,2]]
        Returns: [0, 1, 2, 3] or [0, 2, 1, 3]

    Args:
        numCourses: Number of courses
        prerequisites: List of [a, b] meaning b must come before a

    Returns:
        List - Valid course order, or empty if impossible

    Time: O(V + E)
    Space: O(V)
    """
    # TODO: Use Kahn's algorithm for topological sort
    # TODO: Return result if valid order exists, else []
    pass


# TEACHER'S SOLUTION:
def findOrder_solution(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    """Course schedule II using topological sort"""
    # Build graph and compute in-degrees
    graph = defaultdict(list)
    in_degree = [0] * numCourses

    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    # Kahn's algorithm
    queue = deque()
    for i in range(numCourses):
        if in_degree[i] == 0:
            queue.append(i)

    result = []

    while queue:
        course = queue.popleft()
        result.append(course)

        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == numCourses else []


# =============================================================================
# PART 5: TESTING
# =============================================================================

def test_topological_sort():
    """Test topological sort implementations"""
    print("=" * 60)
    print("TOPOLOGICAL SORT TEST SUITE")
    print("=" * 60)

    # Test Kahn's Algorithm
    print("\nTEST 1: Kahn's Algorithm")
    n = 4
    edges = [[0, 1], [0, 2], [1, 3], [2, 3]]
    result = topologicalSort_kahn_solution(n, edges)
    print(f"Graph (4 vertices, edges: {edges})")
    print(f"Topological order: {result}")
    assert len(result) == n
    assert result[0] == 0
    print("✓ Kahn's algorithm test passed")

    # Test DFS-based
    print("\nTEST 2: DFS-Based Topological Sort")
    result = topologicalSort_dfs_solution(n, edges)
    print(f"Topological order: {result}")
    assert len(result) == n
    assert result[0] == 0
    print("✓ DFS-based test passed")

    # Test Cycle Detection (Kahn's)
    print("\nTEST 3: Cycle Detection via Kahn's")
    n = 2
    edges_cycle = [[0, 1], [1, 0]]
    result = topologicalSort_kahn_solution(n, edges_cycle)
    print(f"Graph with cycle: {edges_cycle}")
    print(f"Result (empty if cycle): {result}")
    assert len(result) == 0
    print("✓ Cycle detection test passed")

    # Test Course Schedule II
    print("\nTEST 4: Course Schedule II")
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    result = findOrder_solution(numCourses, prerequisites)
    print(f"Courses: {numCourses}, Prerequisites: {prerequisites}")
    print(f"Valid order: {result}")
    assert len(result) == numCourses
    print("✓ Course schedule test passed")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    print("Welcome to Module 5: Topological Sort!")
    print("Master ordering dependencies and task scheduling!")
    print("\nComplete the TODOs, then run test_topological_sort()")
