import heapq

def heapify():
    nums = [1,4,2,7,5]
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
    print(heap)

    sortRet = [heapq.heappop(heap) for _ in range(len(heap))]
    print(sortRet)

    heapq.heapify(nums)
    print(nums)

    sortRet = [heapq.heappop(nums) for _ in range(len(nums))]
    print(sortRet)

def heapOperate():
    nums = [1,4,2,7,5]
    #heapq.heapify(nums)

    ret1 = heapq.nlargest(2, nums)
    print(ret1)
    ret2 = heapq.nsmallest(2, nums)
    print(ret2)

heapOperate()