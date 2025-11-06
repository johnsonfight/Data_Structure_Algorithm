"""
Module 2: Graph Traversal - Depth-First Search (DFS)
=====================================================

Master DFS - the fundamental graph traversal algorithm for exploring graphs deeply!

In this module, we'll cover:
1. DFS concept and implementation (recursive and iterative)
2. Time and space complexity analysis
3. DFS applications: paths, cycles, connectivity
4. Visited tracking strategies
5. Backtracking with DFS

DFS is essential for: cycles, components, topological sort, and backtracking!
"""

from typing import List, Dict, Set
from collections import defaultdict, deque

# =============================================================================
# PART 1: DFS FUNDAMENTALS
# =============================================================================

"""
CONCEPT: Depth-First Search (DFS)
==================================

DFS explores a graph by going as deep as possible before backtracking.

Key idea: Use recursion (or stack) to explore deep into graph.

Algorithm:
1. Start at a node
2. Mark it as visited
3. Recursively visit all unvisited neighbors
4. Backtrack when no more neighbors

Example: DFS on graph [0-1-3, 0-2-3]
    0 (start)
    ├─ 1
    │  └─ 3
    └─ 2
       └─ 3 (already visited)

Visitation order: 0, 1, 3, 2

Time: O(V + E) - visit each vertex once, traverse each edge once
Space: O(V) - recursion stack or explicit stack for visited nodes

Compare to BFS:
- DFS: Goes DEEP (recursive/stack)
- BFS: Goes WIDE (queue, level-by-level)

When to use DFS:
- Finding all paths
- Cycle detection
- Connected components
- Topological sort
- Backtracking problems
"""

# =============================================================================
# PART 2: RECURSIVE DFS
# =============================================================================


def dfs_recursive(graph: Dict[int, List[int]], start: int) -> Set[int]:
    """
    Perform DFS starting from vertex using recursion

    Example:
        graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        dfs_recursive(graph, 0) → {0, 1, 2, 3}

    Args:
        graph: Adjacency list
        start: Starting vertex

    Returns:
        Set of visited vertices

    Time: O(V + E)
    Space: O(V) recursion stack
    """
    # TODO: Create visited set
    # TODO: Define helper function with (node, visited)
    # TODO: Mark node as visited
    # TODO: Recursively visit all unvisited neighbors
    pass


def dfs_recursive_helper(graph: Dict[int, List[int]], node: int, visited: Set[int]):
    """Helper function for recursive DFS"""
    # TODO: Mark node as visited
    # TODO: For each neighbor, recursively call if not visited
    pass


# TEACHER'S SOLUTION:
def dfs_recursive_solution(graph: Dict[int, List[int]], start: int) -> Set[int]:
    """Recursive DFS implementation"""
    visited = set()

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)

    dfs(start)
    return visited


# =============================================================================
# PART 3: ITERATIVE DFS (STACK-BASED)
# =============================================================================


def dfs_iterative(graph: Dict[int, List[int]], start: int) -> Set[int]:
    """
    Perform DFS using explicit stack (iterative)

    Example:
        graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        dfs_iterative(graph, 0) → {0, 1, 2, 3}

    Args:
        graph: Adjacency list
        start: Starting vertex

    Returns:
        Set of visited vertices

    Time: O(V + E)
    Space: O(V) for stack
    """
    # TODO: Initialize stack with start node
    # TODO: Initialize visited set
    # TODO: While stack not empty:
    #       - Pop node
    #       - If not visited: mark as visited
    #       - Push all unvisited neighbors to stack
    pass


# TEACHER'S SOLUTION:
def dfs_iterative_solution(graph: Dict[int, List[int]], start: int) -> Set[int]:
    """Iterative DFS using stack"""
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            # Add neighbors to stack (in reverse for consistent order)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited


# =============================================================================
# PART 4: NUMBER OF ISLANDS (LC 200)
# =============================================================================

"""
CONCEPT: Number of Islands
===========================

Problem: Count the number of islands in a 2D grid.
Island = 1s connected horizontally or vertically (not diagonally).

Example:
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Returns: 3 islands

Algorithm using DFS:
1. Iterate through each cell
2. When find '1', do DFS to mark entire island
3. Increment island count
4. Mark all connected 1s as visited ('0')

Time: O(m*n) - visit each cell once
Space: O(m*n) - recursion stack in worst case
"""


def numIslands(grid: List[List[str]]) -> int:
    """
    Count number of islands in grid

    Example:
        grid = [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ]
        Returns: 3

    Args:
        grid: 2D grid with "0" (water) and "1" (land)

    Returns:
        int - Number of islands

    Time: O(m*n)
    Space: O(m*n)
    """
    # TODO: Check empty grid
    # TODO: Iterate through each cell
    # TODO: When find "1", do DFS to mark entire island and increment count
    # TODO: Helper DFS function marks all connected "1"s as "0"
    pass


# TEACHER'S SOLUTION:
def numIslands_solution(grid: List[List[str]]) -> int:
    """Count islands using DFS"""
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])
    count = 0

    def dfs(i, j):
        # Boundary and water check
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
            return

        # Mark as visited (water)
        grid[i][j] = "0"

        # Explore 4 directions
        dfs(i + 1, j)  # down
        dfs(i - 1, j)  # up
        dfs(i, j + 1)  # right
        dfs(i, j - 1)  # left

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                count += 1
                dfs(i, j)

    return count


# =============================================================================
# PART 5: ALL PATHS FROM SOURCE TO TARGET (LC 797)
# =============================================================================

"""
CONCEPT: All Paths From Source to Target
==========================================

Problem: Find ALL paths from node 0 to node n-1 in a DAG.

Example:
graph = [[1,2], [3], [3], []]
Paths:
- 0 → 1 → 3
- 0 → 2 → 3

Returns: [[0,1,3], [0,2,3]]

Algorithm using DFS with backtracking:
1. Start at node 0
2. At each node, explore all neighbors
3. When reach target, add path to results
4. Backtrack and try other paths

Time: O(2^n * n) - exponential paths in DAG
Space: O(n) - recursion depth
"""


def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
    """
    Find all paths from 0 to n-1 in DAG

    Example:
        graph = [[1,2],[3],[3],[]]
        Returns: [[0,1,3],[0,2,3]]

    Args:
        graph: Adjacency list (DAG with nodes 0 to n-1)

    Returns:
        List of all paths from 0 to n-1

    Time: O(2^n * n)
    Space: O(n)
    """
    # TODO: Initialize results list
    # TODO: Define DFS helper with (node, path)
    # TODO: If node == n-1 (target), add path to results
    # TODO: Otherwise, explore all neighbors with backtracking
    pass


# TEACHER'S SOLUTION:
def allPathsSourceTarget_solution(graph: List[List[int]]) -> List[List[int]]:
    """Find all paths using DFS with backtracking"""
    n = len(graph)
    results = []

    def dfs(node, path):
        # Reached target
        if node == n - 1:
            results.append(path[:])  # Add copy of path
            return

        # Explore neighbors
        for neighbor in graph[node]:
            path.append(neighbor)
            dfs(neighbor, path)
            path.pop()  # Backtrack

    dfs(0, [0])
    return results


# =============================================================================
# PART 6: TESTING
# =============================================================================

def test_dfs():
    """Test DFS implementations"""
    print("=" * 60)
    print("DFS TEST SUITE")
    print("=" * 60)

    # Test Recursive DFS
    print("\nTEST 1: Recursive DFS")
    graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
    result = dfs_recursive_solution(graph, 0)
    print(f"Graph: {graph}")
    print(f"DFS from 0: {sorted(result)}")
    assert result == {0, 1, 2, 3}
    print("✓ Recursive DFS test passed")

    # Test Iterative DFS
    print("\nTEST 2: Iterative DFS")
    result = dfs_iterative_solution(graph, 0)
    print(f"DFS from 0: {sorted(result)}")
    assert result == {0, 1, 2, 3}
    print("✓ Iterative DFS test passed")

    # Test Number of Islands
    print("\nTEST 3: Number of Islands")
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    result = numIslands_solution(grid)
    print(f"Grid (4x5):")
    print(f"Islands: {result}")
    assert result == 3
    print("✓ Number of islands test passed")

    # Test All Paths
    print("\nTEST 4: All Paths From Source to Target")
    graph = [[1, 2], [3], [3], []]
    result = allPathsSourceTarget_solution(graph)
    print(f"Graph: {graph}")
    print(f"All paths: {result}")
    assert len(result) == 2
    assert [0, 1, 3] in result
    assert [0, 2, 3] in result
    print("✓ All paths test passed")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    print("Welcome to Module 2: Depth-First Search!")
    print("Master DFS and explore graphs deeply!")
    print("\nComplete the TODOs, then run test_dfs()")
