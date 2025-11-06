"""
Module 3: Graph Traversal - Breadth-First Search (BFS)
=======================================================

Master BFS - the fundamental algorithm for shortest paths and level-order exploration!

In this module, we'll cover:
1. BFS concept and implementation (queue-based)
2. Shortest path in unweighted graphs
3. BFS applications: level-order, multi-source, minimum steps
4. Bidirectional BFS (advanced)
5. 0-1 BFS for weighted graphs

BFS is essential for: shortest path, level-order, minimum steps!
"""

from typing import List, Dict, Set, Tuple
from collections import defaultdict, deque

# =============================================================================
# PART 1: BFS FUNDAMENTALS
# =============================================================================

"""
CONCEPT: Breadth-First Search (BFS)
====================================

BFS explores a graph level by level, ensuring shortest path in unweighted graphs.

Key idea: Use queue to explore level by level.

Algorithm:
1. Start at a node, add to queue
2. Mark as visited
3. While queue not empty:
   - Dequeue node
   - Process it
   - Enqueue all unvisited neighbors
4. All nodes at distance k are processed before any at distance k+1

Example: BFS on graph [0-1-3, 0-2-3]
Level 0: {0}
Level 1: {1, 2}
Level 2: {3}

Visitation order: 0, 1, 2, 3

Time: O(V + E) - visit each vertex once, traverse each edge once
Space: O(V) - queue can hold all vertices

Compare to DFS:
- DFS: DEEP first (recursive/stack)
- BFS: WIDE first (queue, level-by-level)

When to use BFS:
- Shortest path (unweighted)
- Minimum steps
- Level-order traversal
- Distance from source
- Multi-source problems
"""

# =============================================================================
# PART 2: BASIC BFS
# =============================================================================


def bfs(graph: Dict[int, List[int]], start: int) -> Set[int]:
    """
    Perform BFS starting from vertex

    Example:
        graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        bfs(graph, 0) → {0, 1, 2, 3}

    Args:
        graph: Adjacency list
        start: Starting vertex

    Returns:
        Set of visited vertices

    Time: O(V + E)
    Space: O(V) for queue
    """
    # TODO: Initialize queue with start node
    # TODO: Initialize visited set with start
    # TODO: While queue not empty:
    #       - Dequeue node
    #       - For each unvisited neighbor:
    #         - Mark as visited
    #         - Enqueue it
    pass


# TEACHER'S SOLUTION:
def bfs_solution(graph: Dict[int, List[int]], start: int) -> Set[int]:
    """Basic BFS implementation"""
    visited = {start}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited


# =============================================================================
# PART 3: SHORTEST PATH (Unweighted)
# =============================================================================

"""
CONCEPT: Shortest Path in Unweighted Graph
============================================

BFS guarantees shortest path in unweighted graph because it explores
all neighbors at distance k before distance k+1.

Algorithm:
1. Use BFS with distance tracking
2. Store (node, distance) or use separate distance dict
3. When reach target, return distance

Example:
graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
Shortest path from 0 to 3: distance = 2 (0→1→3 or 0→2→3)

Time: O(V + E)
Space: O(V)
"""


def shortestPath(graph: Dict[int, List[int]], start: int, end: int) -> int:
    """
    Find shortest path distance in unweighted graph

    Example:
        graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        shortestPath(graph, 0, 3) → 2

    Args:
        graph: Adjacency list
        start: Starting vertex
        end: Target vertex

    Returns:
        int - Shortest distance, or -1 if unreachable

    Time: O(V + E)
    Space: O(V)
    """
    # TODO: Use BFS to find shortest path
    # TODO: Track distance to each node
    # TODO: Return distance when reach end node
    pass


# TEACHER'S SOLUTION:
def shortestPath_solution(graph: Dict[int, List[int]], start: int, end: int) -> int:
    """Find shortest path using BFS"""
    if start == end:
        return 0

    visited = {start}
    queue = deque([(start, 0)])  # (node, distance)

    while queue:
        node, dist = queue.popleft()

        for neighbor in graph[node]:
            if neighbor == end:
                return dist + 1

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return -1  # Unreachable


# =============================================================================
# PART 4: ROTTING ORANGES (LC 994) - Multi-Source BFS
# =============================================================================

"""
CONCEPT: Multi-Source BFS
==========================

Problem: Track spread of rot in grid of oranges.
- 0: empty cell
- 1: fresh orange
- 2: rotten orange

Each minute, rotten oranges make adjacent fresh ones rotten.
Find minutes until all become rotten, or -1 if impossible.

Algorithm using multi-source BFS:
1. Start with ALL rotten oranges in queue
2. Process level by level (each level = 1 minute)
3. Count minutes until all fresh are rotten

Time: O(m*n) - visit each cell once
Space: O(m*n) - queue

Example:
grid = [[2,1,1],[1,1,0],[0,1,1]]
Returns: 4 (spread takes 4 minutes)
"""


def orangesRotting(grid: List[List[int]]) -> int:
    """
    Find minutes until all oranges rotten

    Example:
        grid = [[2,1,1],[1,1,0],[0,1,1]]
        Returns: 4

    Args:
        grid: 2D grid with 0 (empty), 1 (fresh), 2 (rotten)

    Returns:
        int - Minutes needed, or -1 if impossible

    Time: O(m*n)
    Space: O(m*n)
    """
    # TODO: Count fresh oranges and add all rotten to queue
    # TODO: BFS level by level (each level = 1 minute)
    # TODO: For each rotten, rot adjacent fresh oranges
    # TODO: Return minutes when all fresh are gone, or -1 if stuck
    pass


# TEACHER'S SOLUTION:
def orangesRotting_solution(grid: List[List[int]]) -> int:
    """Multi-source BFS for rotting oranges"""
    m, n = len(grid), len(grid[0])
    queue = deque()
    fresh = 0

    # Initialize: add all rotten oranges, count fresh
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j, 0))  # (row, col, time)
            elif grid[i][j] == 1:
                fresh += 1

    # If no fresh oranges, already done
    if fresh == 0:
        return 0

    # BFS level by level
    minutes = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        r, c, minutes = queue.popleft()

        # Rot adjacent oranges
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                queue.append((nr, nc, minutes + 1))

    # If fresh oranges remain, impossible
    if fresh > 0:
        return -1

    return minutes


# =============================================================================
# PART 5: SHORTEST PATH IN BINARY MATRIX (LC 1091)
# =============================================================================

"""
CONCEPT: Shortest Path in Grid
===============================

Problem: Find shortest path from (0,0) to (n-1,n-1) in binary grid.
- 0: walkable
- 1: obstacle

Can move in 8 directions (4 cardinal + 4 diagonal).

Algorithm:
1. BFS from (0,0)
2. For each cell, explore all 8 neighbors
3. Return distance when reach (n-1, n-1)

Time: O(m*n)
Space: O(m*n)
"""


def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    """
    Find shortest path in binary matrix

    Example:
        grid = [[0,1],[1,0]]
        Returns: 2 (path: (0,0) → (1,1))

    Args:
        grid: Binary grid with 0 (walkable) and 1 (obstacle)

    Returns:
        int - Shortest path length, or -1 if unreachable

    Time: O(m*n)
    Space: O(m*n)
    """
    # TODO: Check start and end are walkable
    # TODO: BFS from (0,0) with 8 directions
    # TODO: Return distance when reach (n-1, n-1)
    pass


# TEACHER'S SOLUTION:
def shortestPathBinaryMatrix_solution(grid: List[List[int]]) -> int:
    """Shortest path in binary matrix using BFS"""
    if not grid or grid[0][0] == 1:
        return -1

    n = len(grid)
    if n == 1:
        return 1

    # BFS with 8 directions
    queue = deque([(0, 0, 1)])  # (row, col, distance)
    visited = {(0, 0)}
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]

    while queue:
        r, c, dist = queue.popleft()

        # Explore all 8 neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] == 0:
                if nr == n - 1 and nc == n - 1:
                    return dist + 1

                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))

    return -1


# =============================================================================
# PART 6: TESTING
# =============================================================================

def test_bfs():
    """Test BFS implementations"""
    print("=" * 60)
    print("BFS TEST SUITE")
    print("=" * 60)

    # Test Basic BFS
    print("\nTEST 1: Basic BFS")
    graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
    result = bfs_solution(graph, 0)
    print(f"Graph: {graph}")
    print(f"BFS from 0: {sorted(result)}")
    assert result == {0, 1, 2, 3}
    print("✓ Basic BFS test passed")

    # Test Shortest Path
    print("\nTEST 2: Shortest Path")
    result = shortestPath_solution(graph, 0, 3)
    print(f"Shortest path from 0 to 3: {result}")
    assert result == 2
    print("✓ Shortest path test passed")

    # Test Rotting Oranges
    print("\nTEST 3: Rotting Oranges (Multi-Source)")
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    result = orangesRotting_solution(grid)
    print(f"Grid (3x3) with rotting spread")
    print(f"Minutes needed: {result}")
    assert result == 4
    print("✓ Rotting oranges test passed")

    # Test Shortest Path in Binary Matrix
    print("\nTEST 4: Shortest Path in Binary Matrix")
    grid = [[0, 1], [1, 0]]
    result = shortestPathBinaryMatrix_solution(grid)
    print(f"Grid: {grid}")
    print(f"Shortest path: {result}")
    assert result == 2
    print("✓ Binary matrix path test passed")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    print("Welcome to Module 3: Breadth-First Search!")
    print("Master BFS for shortest paths and level-order exploration!")
    print("\nComplete the TODOs, then run test_bfs()")
