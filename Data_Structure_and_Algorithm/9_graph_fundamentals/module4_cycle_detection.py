"""
Module 4: Cycle Detection - Interactive Practice
=================================================

Master cycle detection in directed and undirected graphs!

In this module, we'll cover:
1. Cycle detection in undirected graphs (DFS with parent tracking)
2. Cycle detection in directed graphs (3-color DFS)
3. Union-Find approach for undirected graphs
4. Applications: dependency resolution, course scheduling
5. Back edges and forward edges

Cycle detection is crucial for: task scheduling, dependency resolution!
"""

from typing import List, Dict, Set
from collections import defaultdict, deque

# =============================================================================
# PART 1: CYCLE DETECTION IN UNDIRECTED GRAPHS
# =============================================================================

"""
CONCEPT: Cycle Detection (Undirected)
======================================

In undirected graph, cycle exists if we visit a node that:
1. Is already visited
2. Is not the parent of current node

Why exclude parent? In undirected graph, edge 0-1 is same as 1-0,
so going back to parent is not a cycle.

Example:
Graph: 0-1-2
       |___|
No cycle? Actually YES! 0-1-2-0 is a cycle.

Algorithm using DFS:
1. Start DFS from each unvisited node
2. Track parent of each node
3. If visit a node that's already visited AND it's not parent → cycle!

Time: O(V + E)
Space: O(V)
"""


def hasCycle_undirected(n: int, edges: List[List[int]]) -> bool:
    """
    Detect cycle in undirected graph

    Example:
        n = 3, edges = [[0,1], [1,2], [2,0]]
        Returns: True (cycle: 0-1-2-0)

        n = 3, edges = [[0,1], [1,2]]
        Returns: False (no cycle)

    Args:
        n: Number of vertices
        edges: List of [u, v] edges

    Returns:
        bool - True if cycle exists, False otherwise

    Time: O(V + E)
    Space: O(V)
    """
    # TODO: Build adjacency list from edges
    # TODO: DFS from each unvisited node
    # TODO: In DFS, check if visit node that's visited and not parent
    pass


# TEACHER'S SOLUTION:
def hasCycle_undirected_solution(n: int, edges: List[List[int]]) -> bool:
    """Detect cycle in undirected graph using DFS"""
    # Build adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node, parent):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                # Explore unvisited neighbor
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                # Found back edge (cycle)
                return True

        return False

    # Check each component
    for i in range(n):
        if i not in visited:
            if dfs(i, -1):
                return True

    return False


# =============================================================================
# PART 2: CYCLE DETECTION IN DIRECTED GRAPHS
# =============================================================================

"""
CONCEPT: Cycle Detection (Directed)
====================================

In directed graph, cycle exists if we encounter a node that is:
1. Currently being explored (in recursion stack)
2. Not just any visited node (must be in CURRENT path)

Algorithm using 3-color DFS:
- WHITE (0): Unvisited
- GRAY (1): Currently exploring (in recursion stack)
- BLACK (2): Fully explored

When visit a GRAY node from current node → Back edge → CYCLE!

Example:
Graph: 0→1→2→0
When exploring 0→1→2, find edge 2→0 where 0 is GRAY → CYCLE!

Time: O(V + E)
Space: O(V)
"""


def hasCycle_directed(n: int, edges: List[List[int]]) -> bool:
    """
    Detect cycle in directed graph

    Example:
        n = 2, edges = [[1,0]]
        Returns: False (no cycle)

        n = 2, edges = [[0,1], [1,0]]
        Returns: True (cycle: 0→1→0)

    Args:
        n: Number of vertices
        edges: List of [u, v] directed edges

    Returns:
        bool - True if cycle exists, False otherwise

    Time: O(V + E)
    Space: O(V)
    """
    # TODO: Build adjacency list
    # TODO: Use 3-color DFS (WHITE=0, GRAY=1, BLACK=2)
    # TODO: If visit GRAY node → back edge → cycle
    pass


# TEACHER'S SOLUTION:
def hasCycle_directed_solution(n: int, edges: List[List[int]]) -> bool:
    """Detect cycle in directed graph using 3-color DFS"""
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    # 0: WHITE (unvisited), 1: GRAY (visiting), 2: BLACK (visited)
    color = [0] * n

    def dfs(node):
        if color[node] == 1:
            return True  # Back edge found (cycle)

        if color[node] == 2:
            return False  # Already explored

        color[node] = 1  # Mark as GRAY (visiting)

        for neighbor in graph[node]:
            if dfs(neighbor):
                return True

        color[node] = 2  # Mark as BLACK (visited)
        return False

    # Check each node
    for i in range(n):
        if color[i] == 0:
            if dfs(i):
                return True

    return False


# =============================================================================
# PART 3: COURSE SCHEDULE (LC 207)
# =============================================================================

"""
CONCEPT: Course Schedule
========================

Problem: Can you complete all courses?
Each course has prerequisites. If prerequisites form a cycle,
impossible to complete all courses.

This is cycle detection in directed graph!

Example:
numCourses = 2
prerequisites = [[1,0], [0,1]]
Returns: False (cycle: 1→0→1)

numCourses = 2
prerequisites = [[1,0]]
Returns: True (0 is prerequisite of 1, no cycle)

Algorithm:
1. Build graph where edge u→v means v is prerequisite of u
2. Detect if cycle exists
3. If cycle → False, else → True
"""


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    Determine if can complete all courses (cycle detection in directed graph)

    Example:
        numCourses = 2, prerequisites = [[1,0]]
        Returns: True

        numCourses = 2, prerequisites = [[1,0], [0,1]]
        Returns: False (cycle)

    Args:
        numCourses: Number of courses
        prerequisites: List of [a, b] meaning b is prerequisite of a

    Returns:
        bool - True if can complete all, False if cycle

    Time: O(V + E)
    Space: O(V)
    """
    # TODO: Use cycle detection in directed graph
    # TODO: If cycle exists → False, else → True
    pass


# TEACHER'S SOLUTION:
def canFinish_solution(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """Course schedule using cycle detection"""
    # Build graph
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    # 0: WHITE, 1: GRAY, 2: BLACK
    color = [0] * numCourses

    def has_cycle(node):
        if color[node] == 1:
            return True

        if color[node] == 2:
            return False

        color[node] = 1

        for neighbor in graph[node]:
            if has_cycle(neighbor):
                return True

        color[node] = 2
        return False

    # Check each course
    for i in range(numCourses):
        if color[i] == 0:
            if has_cycle(i):
                return False

    return True


# =============================================================================
# PART 4: TESTING
# =============================================================================

def test_cycle_detection():
    """Test cycle detection implementations"""
    print("=" * 60)
    print("CYCLE DETECTION TEST SUITE")
    print("=" * 60)

    # Test Undirected Cycle
    print("\nTEST 1: Cycle in Undirected Graph")
    test_cases = [
        (3, [[0, 1], [1, 2], [2, 0]], True),
        (3, [[0, 1], [1, 2]], False),
        (2, [[0, 1]], False),
    ]
    for n, edges, expected in test_cases:
        result = hasCycle_undirected_solution(n, edges)
        assert result == expected
        print(f"  n={n}, edges={edges} → {result} ✓")
    print("✓ Undirected cycle test passed")

    # Test Directed Cycle
    print("\nTEST 2: Cycle in Directed Graph")
    test_cases = [
        (2, [[1, 0]], False),
        (2, [[0, 1], [1, 0]], True),
        (3, [[0, 1], [1, 2]], False),
    ]
    for n, edges, expected in test_cases:
        result = hasCycle_directed_solution(n, edges)
        assert result == expected
        print(f"  n={n}, edges={edges} → {result} ✓")
    print("✓ Directed cycle test passed")

    # Test Course Schedule
    print("\nTEST 3: Course Schedule (Cycle Detection)")
    test_cases = [
        (2, [[1, 0]], True),
        (2, [[1, 0], [0, 1]], False),
        (3, [[0, 1], [1, 2]], True),
    ]
    for numCourses, prereqs, expected in test_cases:
        result = canFinish_solution(numCourses, prereqs)
        assert result == expected
        print(f"  courses={numCourses}, prereqs={prereqs} → {result} ✓")
    print("✓ Course schedule test passed")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    print("Welcome to Module 4: Cycle Detection!")
    print("Master detecting cycles in directed and undirected graphs!")
    print("\nComplete the TODOs, then run test_cycle_detection()")
