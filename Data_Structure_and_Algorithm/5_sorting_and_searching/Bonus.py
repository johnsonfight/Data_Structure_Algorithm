# ==== QUICKSORT ====
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left  = [x for x in arr if x < pivot]
    mid   = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + mid + quicksort(right)

# ==== MERGESORT ====
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    L = mergesort(arr[:mid])
    R = mergesort(arr[mid:])
    i = j = 0
    out = []
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            out.append(L[i]); i += 1
        else:
            out.append(R[j]); j += 1
    out.extend(L[i:])
    out.extend(R[j:])
    return out

# ==== HEAPSORT ====
import heapq
def heapsort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

# Try them
data = [64, 34, 25, 12, 22, 11, 90]
print("Quick :", quicksort(data[:]))
print("Merge :", mergesort(data[:]))
print("Heap  :", heapsort(data[:]))