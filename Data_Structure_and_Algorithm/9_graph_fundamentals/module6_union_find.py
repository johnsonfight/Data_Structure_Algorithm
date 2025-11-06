"""
Module 6: Union-Find (Disjoint Set Union) - Interactive Practice
================================================================

Master Union-Find - a powerful data structure for connectivity and cycles!

In this module, we'll cover:
1. Union-Find basics (find and union operations)
2. Path compression and union by rank optimizations
3. Nearly O(1) amortized time complexity
4. Applications: connected components, cycle detection, Kruskal's MST
5. Dynamic connectivity

Union-Find is essential for: MST, dynamic connectivity, cycle detection!
"""

from typing import List, Tuple

# =============================================================================
# PART 1: UNION-FIND FUNDAMENTALS
# =============================================================================

"""
CONCEPT: Union-Find (Disjoint Set Union)
=========================================

Union-Find is a data structure for managing disjoint (non-overlapping) sets
and answering "are two elements in the same set?" queries efficiently.

Two main operations:

1. FIND(x): Find the representative (root) of set containing x
   - Simple: O(height of tree)
   - With path compression: O(α(n)) ≈ O(1) amortized

2. UNION(x, y): Merge sets containing x and y
   - Simple: O(height of tree)
   - With union by rank: O(α(n)) ≈ O(1) amortized

Optimizations:

1. PATH COMPRESSION: When finding root, make every node point directly to root
   Before: 4→3→2→1 (path compression needed)
   After:  4→1, 3→1, 2→1

2. UNION BY RANK: Always attach smaller tree under larger tree
   Keeps trees flat, reducing height

With both optimizations: α(n) ≈ O(1) for very large n!

Applications:
- Connected components (number of islands)
- Cycle detection (especially for undirected graphs)
- Kruskal's MST algorithm
- Dynamic connectivity
"""

# =============================================================================
# PART 2: BASIC UNION-FIND (Without Optimization)
# =============================================================================


class UnionFind:
    """
    Basic Union-Find implementation (with path compression only)

    Time: O(α(n)) ≈ O(1) amortized with path compression
    Space: O(n)

    Example:
        uf = UnionFind(5)
        uf.union(0, 1)
        uf.union(1, 2)
        assert uf.find(0) == uf.find(2)  # Same component
        assert uf.find(3) != uf.find(0)  # Different component
    """

    def __init__(self, n: int):
        """Initialize Union-Find with n elements"""
        # TODO: Initialize parent array
        # TODO: Each element is its own parent initially
        # TODO: Initialize rank array (all 0 initially)
        pass

    def find(self, x: int) -> int:
        """
        Find the root (representative) of set containing x

        With path compression: Make every node point to root

        Args:
            x: Element to find root for

        Returns:
            int - Root of set containing x

        Time: O(α(n)) ≈ O(1) amortized
        """
        # TODO: If x is not its own parent:
        #       - Recursively find root of parent
        #       - Apply path compression (set parent to root)
        # TODO: Return x if it's its own parent (root)
        pass

    def union(self, x: int, y: int):
        """
        Merge sets containing x and y using union by rank

        Args:
            x: Element in first set
            y: Element in second set

        Time: O(α(n)) ≈ O(1) amortized
        """
        # TODO: Find roots of x and y
        # TODO: If same root, already in same set → return
        # TODO: Otherwise, merge by rank (attach smaller under larger)
        pass

    def connected(self, x: int, y: int) -> bool:
        """Check if x and y are in same set"""
        # TODO: Return find(x) == find(y)
        pass


# TEACHER'S SOLUTION:
class UnionFindSolution:
    """Union-Find with path compression and union by rank"""

    def __init__(self, n: int):
        """Initialize with n elements"""
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        """Find root with path compression"""
        if self.parent[x] != x:
            # Path compression: point directly to root
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        """Union by rank"""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        # Attach smaller tree under larger tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

    def connected(self, x: int, y: int) -> bool:
        """Check if in same set"""
        return self.find(x) == self.find(y)


# =============================================================================
# PART 3: NUMBER OF PROVINCES (LC 547)
# =============================================================================

"""
CONCEPT: Number of Provinces (Connected Components)
====================================================

Problem: Count number of connected components (provinces).

Example:
isConnected = [
  [1,1,0],
  [1,1,0],
  [0,0,1]
]
Returns: 2 provinces (cities {0,1} and {2})

Algorithm using Union-Find:
1. For each pair (i, j) where isConnected[i][j] == 1:
   - Union cities i and j
2. Count unique roots (distinct components)

Time: O(n² * α(n)) ≈ O(n²)
Space: O(n)

Alternative: Can use DFS too, but Union-Find is cleaner!
"""


def findCircleNum(isConnected: List[List[int]]) -> int:
    """
    Count number of provinces (connected components)

    Example:
        isConnected = [[1,1,0],[1,1,0],[0,0,1]]
        Returns: 2

    Args:
        isConnected: Adjacency matrix (symmetric)

    Returns:
        int - Number of provinces

    Time: O(n² * α(n))
    Space: O(n)
    """
    # TODO: Create Union-Find
    # TODO: For each connected pair, union them
    # TODO: Count unique roots
    pass


# TEACHER'S SOLUTION:
def findCircleNum_solution(isConnected: List[List[int]]) -> int:
    """Count provinces using Union-Find"""
    n = len(isConnected)
    uf = UnionFindSolution(n)

    # Union connected cities
    for i in range(n):
        for j in range(i + 1, n):
            if isConnected[i][j] == 1:
                uf.union(i, j)

    # Count unique roots
    return len(set(uf.find(i) for i in range(n)))


# =============================================================================
# PART 4: REDUNDANT CONNECTION (LC 684)
# =============================================================================

"""
CONCEPT: Redundant Connection
==============================

Problem: Find an edge that when removed makes tree valid
(a tree with n nodes should have exactly n-1 edges).

Graph is connected, so exactly one extra edge creates one cycle.
Find that extra edge!

Example:
edges = [[1,2],[1,3],[2,3]]
Returns: [2,3] (removing this leaves valid tree)

Algorithm using Union-Find:
1. Iterate through edges in order
2. Try to union each edge
3. If union fails (same root), this edge creates cycle → return it!

Time: O(n * α(n)) ≈ O(n)
Space: O(n)

Why Union-Find is perfect:
- When find(u) == find(v) before union, adding edge u-v creates cycle!
"""


def findRedundantConnection(edges: List[List[int]]) -> List[int]:
    """
    Find redundant edge that creates cycle

    Example:
        edges = [[1,2],[1,3],[2,3]]
        Returns: [2,3]

    Args:
        edges: List of edges (1-indexed)

    Returns:
        List - Edge that creates cycle

    Time: O(n * α(n))
    Space: O(n)
    """
    # TODO: Create Union-Find
    # TODO: For each edge, try to union endpoints
    # TODO: If union fails (same component), return this edge
    pass


# TEACHER'S SOLUTION:
def findRedundantConnection_solution(edges: List[List[int]]) -> List[int]:
    """Find redundant edge using Union-Find"""
    n = len(edges)
    uf = UnionFindSolution(n + 1)  # 1-indexed

    for u, v in edges:
        if uf.find(u) == uf.find(v):
            # This edge creates cycle
            return [u, v]
        uf.union(u, v)

    return []


# =============================================================================
# PART 5: TESTING
# =============================================================================

def test_union_find():
    """Test Union-Find implementations"""
    print("=" * 60)
    print("UNION-FIND TEST SUITE")
    print("=" * 60)

    # Test Basic Union-Find
    print("\nTEST 1: Basic Union-Find Operations")
    uf = UnionFindSolution(5)
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)
    print(f"After unions: 0-1-2 and 3-4")
    assert uf.connected(0, 2)
    assert not uf.connected(0, 3)
    print(f"0 connected to 2: {uf.connected(0, 2)} ✓")
    print(f"0 connected to 3: {uf.connected(0, 3)} ✓")
    print("✓ Basic Union-Find test passed")

    # Test Path Compression
    print("\nTEST 2: Path Compression")
    uf = UnionFindSolution(5)
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(2, 3)
    uf.union(3, 4)
    print(f"Chain: 0-1-2-3-4")
    # Path compression happens during find
    root = uf.find(0)
    print(f"Root of 0: {root}")
    # After path compression, 0 should point directly to root
    assert uf.parent[0] == root
    print("✓ Path compression test passed")

    # Test Number of Provinces
    print("\nTEST 3: Number of Provinces")
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    result = findCircleNum_solution(isConnected)
    print(f"Provinces: {result}")
    assert result == 2
    print("✓ Provinces test passed")

    # Test Redundant Connection
    print("\nTEST 4: Redundant Connection")
    edges = [[1, 2], [1, 3], [2, 3]]
    result = findRedundantConnection_solution(edges)
    print(f"Edges: {edges}")
    print(f"Redundant edge: {result}")
    assert result == [2, 3]
    print("✓ Redundant connection test passed")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    print("Welcome to Module 6: Union-Find!")
    print("Master the elegant data structure for connectivity!")
    print("\nComplete the TODOs, then run test_union_find()")
