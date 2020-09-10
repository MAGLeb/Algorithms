import heapq

f = open('G.txt', 'r')

n = int(f.readline())
array_first = list(map(int, f.readline().strip().split()))

m = int(f.readline())
array_second = list(map(int, f.readline().strip().split()))

k = int(f.readline())


def kSmallestPairs(nums1, nums2, k):
  if (not nums1) or (not nums2):
    return []
  ans = []
  heap = []
  heapq.heappush(heap, (nums1[0] + nums2[0], (0, 0)))
  visited = set()
  visited.add((0, 0))
  while len(ans) < k and heap:
    psum, (idx1, idx2) = heapq.heappop(heap)
    ans.append(sorted([nums1[idx1], nums2[idx2]]))
    if idx1 + 1 < len(nums1) and (idx1+1, idx2) not in visited:
      heapq.heappush(heap, (nums1[idx1 + 1] + nums2[idx2], (idx1 + 1, idx2)))
      visited.add((idx1+1, idx2))
    if idx2 + 1 < len(nums2) and (idx1, idx2+1) not in visited:
      heapq.heappush(heap, (nums1[idx1] + nums2[idx2 + 1], (idx1, idx2 + 1)))
      visited.add((idx1, idx2+1))
  return ans


def print_solution(solution):
    for item in sorted(solution, key=lambda x: x[0]):
        print(' '.join(list(map(str, item))))


print_solution(kSmallestPairs(array_first, array_second, k))
