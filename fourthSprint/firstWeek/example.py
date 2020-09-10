import heapq

array = [(7, [1,2], [3,5]),(9, 'borisov'), (7, [1,2], [3,4])]

heap = []

for item in array:
  heapq.heappush(heap, item)

print([heapq.heappop(heap) for i in range(len(heap))])