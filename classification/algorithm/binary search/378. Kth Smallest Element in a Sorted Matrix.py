import heapq

def kthSmallest(matrix, k):
    queue = []
    N = len(matrix[0])
    def push(i,j):
        if i<N and j<N:
            heapq.heappush(queue, (matrix[i][j], i,j))

    push(0, 0)
    while queue and k > 0:
        ret, i,j = heapq.heappop(queue)
        push(i,j+1)
        if j == 0:
            push(i+1, 0)

        k -= 1

    return ret

matrix = [[ 1,  5,  9],[10, 11, 13],[12, 13, 15]]
ret = kthSmallest(matrix, 9)
print(ret)