import heapq

li = [1, 5, 6, 7, 9, 2, 4, 3]

new_heap = []
print(heapq.heappush(new_heap, li.pop()))
print(heapq.heappush(new_heap, li.pop()))
print(heapq.heappush(new_heap, li.pop()))
print(heapq.heappush(new_heap, li.pop()))
print(heapq.heappush(new_heap, li.pop()))
print(heapq.heappush(new_heap, li.pop()))
print(heapq.heappush(new_heap, li.pop()))
print(heapq.heappush(new_heap, li.pop()))

print(heapq.heappop(new_heap))
print(heapq.heappop(new_heap))
print(heapq.heappop(new_heap))
print(heapq.heappop(new_heap))
print(heapq.heappop(new_heap))
print(heapq.heappop(new_heap))
print(heapq.heappop(new_heap))
print(heapq.heappop(new_heap))
print(heapq.heappop(new_heap))
print(heapq.heappop(new_heap))





