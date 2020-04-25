'''
Write a program to find the n-th ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:
Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
'''

# Let's use three pointers i2,i3,i5 ,to mark the last ugly number which was multiplied by 2, 3 and 5, correspondingly.
def nthUglyNumber(n):
    nums = [1,]
    i2,i3,i5 = 0,0,0
    for i in range(1,n):
        ugly = min(nums[i2]*2, nums[i3]*3, nums[i5]*5)
        nums.append(ugly)

        #when ugly == 6, i2 and i3 must move forward both, so judge three case independent.
        if ugly == nums[i2]*2:
            i2 += 1
        if ugly == nums[i3]*3:
            i3 += 1
        if ugly == nums[i5]*5:
            i5 += 1
    return nums[-1]


n = 2
print(nthUglyNumber(n))

