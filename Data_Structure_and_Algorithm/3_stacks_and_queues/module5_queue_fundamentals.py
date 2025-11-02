"""
Module 5: Queue Fundamentals - Interactive Practice
===================================================

Master queues, circular queues, and deques - essential for BFS, scheduling,
and streaming problems!

In this module, we'll cover:
1. Queue basics and FIFO principle
2. Array-based queue implementation
3. Circular queue (fixed-size, efficient)
4. Double-ended queue (deque)
5. Queue vs Stack comparison

Queues are fundamental to BFS, level-order traversal, and system design!
"""

from typing import Optional
from collections import deque as collections_deque

# =============================================================================
# PART 1: QUEUE BASICS
# =============================================================================

"""
CONCEPT: Queue (FIFO - First In First Out)
===========================================

A queue is a linear data structure where elements are added at the REAR
and removed from the FRONT.

Key Properties:
- FIFO principle: First element added is first to be removed
- O(1) time for enqueue, dequeue, peek operations
- Restricted access: Only access front and rear

Real-world analogy:
- Printer queue: First document printed first
- Customer service: First customer served first
- Traffic: First car in line goes first

Visual representation:
    Front → [1] [2] [3] [4] [5] ← Rear

Operations:
1. enqueue(x): Add element x to rear - O(1)
2. dequeue(): Remove and return front element - O(1)
3. peek(): View front element without removing - O(1)
4. isEmpty(): Check if queue is empty - O(1)
5. size(): Return number of elements - O(1)

Example trace:
q = Queue()
q.enqueue(1)  → [1]
q.enqueue(2)  → [1, 2]
q.enqueue(3)  → [1, 2, 3]
q.dequeue()   → Returns 1, queue: [2, 3]
q.peek()      → Returns 2, queue unchanged: [2, 3]
q.dequeue()   → Returns 2, queue: [3]

Why not use Python list for queue?
- list.pop(0) is O(n) - we'd need to shift all elements!
- Use deque or circular array instead
"""

# =============================================================================
# PART 2: ARRAY-BASED QUEUE USING PYTHON DEQUE
# =============================================================================

class SimpleQueue:
    """
    Queue implementation using Python's collections.deque

    This is the simplest and most efficient for general use.

    Advantages:
    - O(1) operations from both ends
    - Python standard library
    - Handles everything we need

    Disadvantages:
    - Not building implementation from scratch
    - Less educational for understanding internals

    Example:
        q = SimpleQueue()
        q.enqueue(1)
        q.enqueue(2)
        assert q.dequeue() == 1
        assert q.size() == 1
    """

    def __init__(self):
        """Initialize empty queue"""
        # TODO: Initialize using deque
        pass

    def enqueue(self, val):
        """Add element to rear"""
        # TODO: Append to rear
        pass

    def dequeue(self):
        """Remove and return front element"""
        # TODO: Remove from front
        # TODO: Raise error if empty
        pass

    def peek(self):
        """View front element without removing"""
        # TODO: Return front element
        # TODO: Raise error if empty
        pass

    def is_empty(self):
        """Check if queue is empty"""
        # TODO: Return whether queue is empty
        pass

    def size(self):
        """Return number of elements"""
        # TODO: Return length
        pass


# TEACHER'S SOLUTION:
class SimpleQueueSolution:
    """Simple queue using deque"""

    def __init__(self):
        """Initialize with deque"""
        self.items = collections_deque()

    def enqueue(self, val):
        """Add element to rear"""
        self.items.append(val)

    def dequeue(self):
        """Remove and return front element"""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.popleft()

    def peek(self):
        """View front element"""
        if self.is_empty():
            raise IndexError("Peek at empty queue")
        return self.items[0]

    def is_empty(self):
        """Check if queue is empty"""
        return len(self.items) == 0

    def size(self):
        """Return number of elements"""
        return len(self.items)


# =============================================================================
# PART 3: CIRCULAR QUEUE (LC 622)
# =============================================================================

"""
CONCEPT: Circular Queue
=======================

A circular queue is a fixed-size queue that wraps around.

Why circular queue?
- Prevents "shift all elements" problem
- Uses fixed space efficiently
- Useful for bounded buffering

Array-based approach:
- Fixed array of size k
- front and rear pointers that wrap around
- When rear reaches end, it wraps to beginning

Visual representation (size=5):
        [0] [1] [2] [3] [4]
         ↑               ↑
       front           rear

Adding elements: 1, 2, 3
        [1] [2] [3] [ ] [ ]
         ↑           ↑
       front       rear

After dequeue and enqueue 4, 5, 6:
        [6] [2] [3] [4] [5]
             ↑           ↑
           front       rear

Key conditions:
- Empty: front == -1 or front == rear + 1
- Full: (rear + 1) % size == front
- Add: rear = (rear + 1) % size
- Remove: front = (front + 1) % size

Time: O(1) for all operations
Space: O(k) where k is queue size
"""


class CircularQueue:
    """
    Circular queue with fixed size k

    Example:
        cq = CircularQueue(3)
        cq.enQueue(1)
        cq.enQueue(2)
        cq.enQueue(3)
        assert cq.deQueue() == 1
        cq.enQueue(4)
        assert cq.Rear() == 4
    """

    def __init__(self, k: int):
        """Initialize circular queue with size k"""
        # TODO: Initialize array of size k
        # TODO: Initialize front and rear pointers
        pass

    def enQueue(self, value: int) -> bool:
        """
        Add element to rear

        Returns:
            bool - True if successful, False if queue is full

        Time: O(1)
        """
        # TODO: Check if queue is full
        # TODO: Add to rear and update pointer with wrap-around
        # TODO: Handle empty queue case (front == -1)
        pass

    def deQueue(self) -> bool:
        """
        Remove element from front

        Returns:
            bool - True if successful, False if queue is empty

        Time: O(1)
        """
        # TODO: Check if queue is empty
        # TODO: Remove from front and update pointer
        pass

    def Front(self) -> int:
        """Get front element, or -1 if empty"""
        # TODO: Return front element or -1
        pass

    def Rear(self) -> int:
        """Get rear element, or -1 if empty"""
        # TODO: Return rear element or -1
        pass

    def isEmpty(self) -> bool:
        """Check if queue is empty"""
        # TODO: Check if front == -1
        pass

    def isFull(self) -> bool:
        """Check if queue is full"""
        # TODO: Check if (rear + 1) % size == front
        pass


# TEACHER'S SOLUTION:
class CircularQueueSolution:
    """Circular queue implementation"""

    def __init__(self, k: int):
        """Initialize with fixed size k"""
        self.queue = [0] * k
        self.size = k
        self.front = -1
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        """Add element to rear"""
        if self.isFull():
            return False

        if self.isEmpty():
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        return True

    def deQueue(self) -> bool:
        """Remove element from front"""
        if self.isEmpty():
            return False

        if self.front == self.rear:
            # Last element, reset queue
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        return True

    def Front(self) -> int:
        """Get front element"""
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        """Get rear element"""
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        """Check if empty"""
        return self.front == -1

    def isFull(self) -> bool:
        """Check if full"""
        return (self.rear + 1) % self.size == self.front


# =============================================================================
# PART 4: DOUBLE-ENDED QUEUE (DEQUE) (LC 641)
# =============================================================================

"""
CONCEPT: Double-Ended Queue (Deque)
====================================

A deque allows adding and removing from BOTH ends!

Operations:
- insertFront(x): Add x to front
- insertLast(x): Add x to rear
- deleteFront(): Remove from front
- deleteLast(): Remove from rear
- getFront(): Get front element
- getRear(): Get rear element

Real-world analogy:
- Train: Can add/remove cars from both ends
- Playlist: Add to front (priority), add to back (queue)

Implementation using circular deque with front and rear pointers.

Time: O(1) for all operations
Space: O(k) where k is deque size
"""


class Deque:
    """
    Double-ended queue with fixed size k

    Example:
        dq = Deque(3)
        dq.insertLast(1)
        dq.insertLast(2)
        dq.insertFront(0)  # Now: [0, 1, 2]
        assert dq.deleteFront() == True  # Remove 0
        assert dq.deleteLast() == True   # Remove 2
    """

    def __init__(self, k: int):
        """Initialize deque with size k"""
        # TODO: Initialize array, front, rear, size
        pass

    def insertFront(self, value: int) -> bool:
        """Add element to front"""
        # TODO: Check if full
        # TODO: Add to front with wrap-around
        pass

    def insertLast(self, value: int) -> bool:
        """Add element to rear"""
        # TODO: Check if full
        # TODO: Add to rear with wrap-around
        pass

    def deleteFront(self) -> bool:
        """Remove element from front"""
        # TODO: Check if empty
        # TODO: Remove from front with wrap-around
        pass

    def deleteLast(self) -> bool:
        """Remove element from rear"""
        # TODO: Check if empty
        # TODO: Remove from rear with wrap-around
        pass

    def getFront(self) -> int:
        """Get front element"""
        # TODO: Return front element or -1
        pass

    def getRear(self) -> int:
        """Get rear element"""
        # TODO: Return rear element or -1
        pass

    def isEmpty(self) -> bool:
        """Check if deque is empty"""
        # TODO: Check if count == 0
        pass

    def isFull(self) -> bool:
        """Check if deque is full"""
        # TODO: Check if count == size
        pass


# TEACHER'S SOLUTION:
class DequeSolution:
    """Double-ended queue implementation"""

    def __init__(self, k: int):
        """Initialize deque with size k"""
        self.deque = [0] * k
        self.size = k
        self.front = -1
        self.rear = -1
        self.count = 0

    def insertFront(self, value: int) -> bool:
        """Add element to front"""
        if self.isFull():
            return False

        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1) % self.size

        self.deque[self.front] = value
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        """Add element to rear"""
        if self.isFull():
            return False

        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.deque[self.rear] = value
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        """Remove element from front"""
        if self.isEmpty():
            return False

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        """Remove element from rear"""
        if self.isEmpty():
            return False

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.rear = (self.rear - 1) % self.size

        self.count -= 1
        return True

    def getFront(self) -> int:
        """Get front element"""
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self) -> int:
        """Get rear element"""
        if self.isEmpty():
            return -1
        return self.deque[self.rear]

    def isEmpty(self) -> bool:
        """Check if empty"""
        return self.count == 0

    def isFull(self) -> bool:
        """Check if full"""
        return self.count == self.size


# =============================================================================
# PART 5: TESTING
# =============================================================================

def test_queue_implementations():
    """Test all queue implementations"""
    print("=" * 60)
    print("QUEUE FUNDAMENTALS TEST SUITE")
    print("=" * 60)

    # Test Simple Queue
    print("\nTEST 1: Simple Queue (using deque)")
    q = SimpleQueueSolution()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(f"Enqueue 1, 2, 3: Size = {q.size()}")
    print(f"Peek: {q.peek()}")
    print(f"Dequeue: {q.dequeue()}")
    print(f"Size: {q.size()}")
    assert not q.is_empty()
    print("✓ Simple queue test passed")

    # Test Circular Queue
    print("\nTEST 2: Circular Queue")
    cq = CircularQueueSolution(3)
    print(f"Created circular queue of size 3")
    assert cq.enQueue(1) == True
    assert cq.enQueue(2) == True
    assert cq.enQueue(3) == True
    assert cq.enQueue(4) == False  # Full
    print(f"Enqueue 1, 2, 3 (4 fails - full)")
    assert cq.deQueue() == True
    print(f"Dequeue: Front = {cq.Front()}, Rear = {cq.Rear()}")
    assert cq.enQueue(4) == True
    print(f"Enqueue 4: Front = {cq.Front()}, Rear = {cq.Rear()}")
    print("✓ Circular queue test passed")

    # Test Deque
    print("\nTEST 3: Double-Ended Queue (Deque)")
    dq = DequeSolution(3)
    print(f"Created deque of size 3")
    assert dq.insertLast(1) == True
    assert dq.insertLast(2) == True
    assert dq.insertFront(0) == True
    print(f"InsertLast(1), InsertLast(2), InsertFront(0)")
    print(f"Front = {dq.getFront()}, Rear = {dq.getRear()}")
    assert dq.deleteFront() == True
    print(f"DeleteFront: Front = {dq.getFront()}")
    assert dq.deleteLast() == True
    print(f"DeleteLast: Rear = {dq.getRear()}")
    print("✓ Deque test passed")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    print("Welcome to Module 5: Queue Fundamentals!")
    print("Master FIFO structures: queues, circular queues, deques!")
    print("\nComplete the TODOs, then run test_queue_implementations()")
