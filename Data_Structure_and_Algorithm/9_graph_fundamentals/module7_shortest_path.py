"""
Module 7: Shortest Path Algorithms - Interactive Practice
==========================================================

Master shortest path algorithms for weighted and unweighted graphs!

In this module, we'll cover:
1. BFS for unweighted graphs (already covered, but reinforced)
2. Dijkstra's Algorithm for non-negative weights
3. Bellman-Ford Algorithm for negative weights
4. Negative cycle detection
5. All-pairs shortest path (Floyd-Warshall preview)

Shortest path is crucial for: maps, routing, networks, games!
"""

from typing import List, Dict, Tuple
from collections import defaultdict, deque
import heapq

# =============================================================================
# PART 1: BFS FOR UNWEIGHTED GRAPHS (REVIEW)
# =============================================================================

"""
CONCEPT: BFS for Unweighted Graphs
===================================

For unweighted graphs (all edges weight = 1), BFS finds shortest path in O(V+E).

Key property: BFS explores level-by-level, guaranteeing shortest path.

Example:
graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
Shortest path 0→3: distance = 2

Algorithm:
1. Queue-based level-order traversal
2. Track distance to each node
3. Return distance when reach target

Time: O(V + E)
Space: O(V)

Use when: Unweighted graphs, minimum hops
"""


def bfs_shortest_path(graph: Dict[int, List[int]], start: int, end: int) -> int:
    """
    Find shortest path in unweighted graph using BFS

    Example:
        graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        bfs_shortest_path(graph, 0, 3) → 2

    Args:
        graph: Adjacency list (unweighted)
        start: Starting vertex
        end: Target vertex

    Returns:
        int - Shortest distance, or -1 if unreachable

    Time: O(V + E)
    Space: O(V)
    """
    # TODO: Use BFS with distance tracking
    pass


# TEACHER'S SOLUTION:
def bfs_shortest_path_solution(graph: Dict[int, List[int]], start: int, end: int) -> int:
    """BFS shortest path for unweighted graphs"""
    if start == end:
        return 0

    visited = {start}
    queue = deque([(start, 0)])

    while queue:
        node, dist = queue.popleft()

        for neighbor in graph[node]:
            if neighbor == end:
                return dist + 1

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return -1


# =============================================================================
# PART 2: DIJKSTRA'S ALGORITHM
# =============================================================================

"""
CONCEPT: Dijkstra's Algorithm
==============================

Finds shortest path in weighted graph with NON-NEGATIVE weights.

Key idea: Greedy algorithm - always explore vertex with smallest known distance.

Why non-negative weights only?
- If negative weights exist, Dijkstra fails
- Use Bellman-Ford instead for negative weights

Algorithm:
1. Initialize distances: dist[start] = 0, others = ∞
2. Use min-heap (priority queue) to always process smallest distance
3. For each vertex u with smallest distance:
   - For each neighbor v of u:
     - If dist[u] + weight(u,v) < dist[v]:
       - Update dist[v]
       - Add (dist[v], v) to heap
4. Return distances

Example:
graph with edges:
  0→1 (weight 4)
  0→2 (weight 2)
  1→3 (weight 1)
  2→1 (weight 1)
  2→3 (weight 5)

Shortest distances from 0:
  0: 0
  1: 3 (0→2→1)
  2: 2 (0→2)
  3: 4 (0→2→1→3)

Time: O((V + E) log V) with min-heap
Space: O(V) for distances and heap

Visualization (Dijkstra process):
Initial: distances = [0, ∞, ∞, ∞]
After processing 0: [0, 4, 2, ∞]
After processing 2: [0, 3, 2, 7]
After processing 1: [0, 3, 2, 4]
After processing 3: [0, 3, 2, 4] (done)
"""


def dijkstra(graph: Dict[int, List[Tuple[int, int]]], start: int) -> Dict[int, int]:
    """
    Find shortest path from start to all vertices using Dijkstra's algorithm

    Example:
        graph = {
            0: [(1, 4), (2, 2)],
            1: [(3, 1)],
            2: [(1, 1), (3, 5)],
            3: []
        }
        dijkstra(graph, 0) → {0: 0, 1: 3, 2: 2, 3: 4}

    Args:
        graph: Adjacency list with (neighbor, weight) tuples
        start: Starting vertex

    Returns:
        Dict - Shortest distances from start to all vertices

    Time: O((V + E) log V)
    Space: O(V)
    """
    # TODO: Initialize distances (start=0, others=∞)
    # TODO: Use min-heap with (distance, vertex)
    # TODO: While heap not empty:
    #       - Pop vertex with smallest distance
    #       - For each neighbor, check if can improve distance
    #       - Update and push to heap if improved
    # TODO: Return distances dict
    pass


# TEACHER'S SOLUTION:
def dijkstra_solution(graph: Dict[int, List[Tuple[int, int]]], start: int) -> Dict[int, int]:
    """Dijkstra's algorithm using min-heap"""
    # Initialize distances
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # Min-heap: (distance, vertex)
    heap = [(0, start)]

    while heap:
        current_dist, current_vertex = heapq.heappop(heap)

        # Skip if we've already found a better path
        if current_dist > distances[current_vertex]:
            continue

        # Relax edges
        for neighbor, weight in graph[current_vertex]:
            distance = current_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


# =============================================================================
# PART 3: NETWORK DELAY TIME (LC 743)
# =============================================================================

"""
CONCEPT: Network Delay Time
============================

Problem: Find time for signal to reach all nodes from source.

Graph: Directed weighted graph (network nodes and delays).
Find: Minimum time for signal from source to reach all nodes.

This is finding the maximum shortest distance from source!

Example:
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4, k = 2 (start from node 2)

Edges: 2→1 (1ms), 2→3 (1ms), 3→4 (1ms)
Times from 2: 1→1ms, 3→1ms, 4→2ms
Maximum = 2ms

Algorithm:
1. Use Dijkstra to find shortest distance from source to all nodes
2. Return maximum distance (time to reach all nodes)
3. If any node unreachable, return -1

Time: O((V + E) log V)
Space: O(V)
"""


def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    """
    Find time for signal to reach all nodes from source k

    Example:
        times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
        Returns: 2 (signal reaches all nodes in 2ms)

    Args:
        times: List of [source, target, delay] edges
        n: Number of nodes (1 to n)
        k: Starting node

    Returns:
        int - Time to reach all nodes, or -1 if impossible

    Time: O((V + E) log V)
    Space: O(V)
    """
    # TODO: Build adjacency list with weights
    # TODO: Use Dijkstra to find distances from k
    # TODO: Return max distance if all reachable, else -1
    pass


# TEACHER'S SOLUTION:
def networkDelayTime_solution(times: List[List[int]], n: int, k: int) -> int:
    """Network delay time using Dijkstra"""
    # Build graph
    graph = defaultdict(list)
    for source, target, delay in times:
        graph[source].append((target, delay))

    # Dijkstra from source k
    distances = {i: float('inf') for i in range(1, n + 1)}
    distances[k] = 0

    heap = [(0, k)]

    while heap:
        current_dist, node = heapq.heappop(heap)

        if current_dist > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            distance = current_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    # Maximum distance to reach any node
    max_time = max(distances.values())
    return max_time if max_time != float('inf') else -1


# =============================================================================
# PART 4: BELLMAN-FORD ALGORITHM
# =============================================================================

"""
CONCEPT: Bellman-Ford Algorithm
================================

Finds shortest path from source to all vertices, handling NEGATIVE weights!

Key advantage over Dijkstra:
- Works with negative weight edges
- Can detect negative cycles

Why Bellman-Ford is slower:
- Must relax edges V-1 times
- Time: O(V*E) vs Dijkstra O((V+E) log V)

Algorithm:
1. Initialize distances (source=0, others=∞)
2. Relax all edges V-1 times:
   - For each edge (u, v, weight):
     - If dist[u] + weight < dist[v]:
       - dist[v] = dist[u] + weight
3. Check for negative cycle:
   - Relax edges one more time
   - If any distance improves → negative cycle exists!

Example with negative weights:
Edges: 0→1(4), 0→2(2), 1→2(-3), 1→3(2), 2→3(4)

After relaxation:
Distances: [0, 4, 1, 5]

Why multiple relaxations?
- First relaxation: distances reach neighbors
- Second relaxation: paths via one-hop neighbors
- ...
- V-1 relaxation: all shortest paths found

Time: O(V*E)
Space: O(V)
"""


def bellmanFord(n: int, edges: List[List[int]], start: int) -> Dict[int, int]:
    """
    Find shortest path with negative weights using Bellman-Ford

    Example:
        edges = [[0,1,4],[0,2,2],[1,2,-3],[1,3,2],[2,3,4]]
        n = 4, start = 0
        Returns: {0: 0, 1: 4, 2: 1, 3: 5}

    Args:
        n: Number of vertices
        edges: List of [source, target, weight] edges
        start: Starting vertex

    Returns:
        Dict - Shortest distances, or None if negative cycle

    Time: O(V*E)
    Space: O(V)
    """
    # TODO: Initialize distances (start=0, others=∞)
    # TODO: Relax all edges V-1 times
    # TODO: Check for negative cycle (relax once more)
    # TODO: Return distances if valid, None if negative cycle
    pass


# TEACHER'S SOLUTION:
def bellmanFord_solution(n: int, edges: List[List[int]], start: int) -> Dict[int, int]:
    """Bellman-Ford algorithm for negative weights"""
    # Initialize distances
    distances = {i: float('inf') for i in range(n)}
    distances[start] = 0

    # Relax edges V-1 times
    for _ in range(n - 1):
        for source, target, weight in edges:
            if distances[source] != float('inf') and distances[source] + weight < distances[target]:
                distances[target] = distances[source] + weight

    # Check for negative cycle
    for source, target, weight in edges:
        if distances[source] != float('inf') and distances[source] + weight < distances[target]:
            return None  # Negative cycle detected

    return distances


# =============================================================================
# PART 5: CHEAPEST FLIGHTS WITHIN K STOPS (LC 787)
# =============================================================================

"""
CONCEPT: Cheapest Flights With K Stops
===============================================

Problem: Find cheapest price to travel from source to destination
with AT MOST K stops (K+1 flights).

This is shortest path with constraint on number of hops!

Example:
flights = [[0,1,100],[1,2,100],[0,2,500]]
src=0, dst=2, k=1
Returns: 200 (0→1→2 with 1 stop)

Why Bellman-Ford works:
- Each relaxation round relaxes paths with one more hop
- After k+1 relaxations: have shortest path with ≤k stops

Algorithm:
1. Use modified Bellman-Ford
2. Instead of V-1 relaxations, do k+1 relaxations
3. Return distance to destination after k+1 iterations

Time: O(K*E)
Space: O(V)
"""


def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    """
    Find cheapest flight price with at most k stops

    Example:
        flights = [[0,1,100],[1,2,100],[0,2,500]]
        n=3, src=0, dst=2, k=1
        Returns: 200

    Args:
        n: Number of cities
        flights: List of [from, to, price] edges
        src: Source city
        dst: Destination city
        k: Maximum stops allowed

    Returns:
        int - Minimum price, or -1 if unreachable

    Time: O(K*E)
    Space: O(V)
    """
    # TODO: Initialize prices (src=0, others=∞)
    # TODO: Relax edges k+1 times (for k stops)
    # TODO: Return price to dst if reachable, else -1
    pass


# TEACHER'S SOLUTION:
def findCheapestPrice_solution(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    """Cheapest flights with k stops using Bellman-Ford variant"""
    # Initialize prices
    prices = [float('inf')] * n
    prices[src] = 0

    # Relax edges k+1 times (k stops = k+1 flights)
    for _ in range(k + 1):
        # Create copy to avoid using updated values in same iteration
        new_prices = prices[:]

        for source, target, price in flights:
            if prices[source] != float('inf') and prices[source] + price < new_prices[target]:
                new_prices[target] = prices[source] + price

        prices = new_prices

    return prices[dst] if prices[dst] != float('inf') else -1


# =============================================================================
# PART 6: TESTING
# =============================================================================

def test_shortest_path():
    """Test shortest path implementations"""
    print("=" * 60)
    print("SHORTEST PATH TEST SUITE")
    print("=" * 60)

    # Test BFS (unweighted)
    print("\nTEST 1: BFS Shortest Path (Unweighted)")
    graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
    result = bfs_shortest_path_solution(graph, 0, 3)
    print(f"Graph: {graph}")
    print(f"Shortest path 0→3: {result}")
    assert result == 2
    print("✓ BFS test passed")

    # Test Dijkstra
    print("\nTEST 2: Dijkstra's Algorithm (Weighted)")
    graph = {
        0: [(1, 4), (2, 2)],
        1: [(3, 1)],
        2: [(1, 1), (3, 5)],
        3: []
    }
    result = dijkstra_solution(graph, 0)
    print(f"Shortest distances from 0: {result}")
    assert result[3] == 4
    print("✓ Dijkstra test passed")

    # Test Network Delay Time
    print("\nTEST 3: Network Delay Time (Dijkstra)")
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    result = networkDelayTime_solution(times, 4, 2)
    print(f"Times: {times}, n=4, start=2")
    print(f"Delay to all nodes: {result}")
    assert result == 2
    print("✓ Network delay test passed")

    # Test Bellman-Ford
    print("\nTEST 4: Bellman-Ford (Negative Weights)")
    edges = [[0, 1, 4], [0, 2, 2], [1, 2, -3], [1, 3, 2], [2, 3, 4]]
    result = bellmanFord_solution(4, edges, 0)
    print(f"Edges: {edges}")
    print(f"Shortest distances: {result}")
    assert result[3] == 5
    print("✓ Bellman-Ford test passed")

    # Test Cheapest Flights
    print("\nTEST 5: Cheapest Flights With K Stops")
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    result = findCheapestPrice_solution(3, flights, 0, 2, 1)
    print(f"Flights: {flights}")
    print(f"Cheapest with ≤1 stop: {result}")
    assert result == 200
    print("✓ Cheapest flights test passed")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    print("Welcome to Module 7: Shortest Path Algorithms!")
    print("Master Dijkstra, Bellman-Ford, and variants!")
    print("\nComplete the TODOs, then run test_shortest_path()")
