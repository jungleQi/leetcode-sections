'''

'''

def wiggleMaxLength(nums):
    N = len(nums)

    #up[i] is the length of a longest wiggle subsequence of {nums[0],...,nums[i]}, with a
    #  positive difference between its last two numbers. This subsequence may or may not
    #  include nums[i] and there may be several such subsequences (of the same length).
    #  We call this a subsequence of type U.
    up = [1]*N

    #down[i] is the length of a longest wiggle subsequence of {nums[0],...,nums[i]}, with a
    #  negative difference between its last two numbers. This subsequence may or may not
    #  include nums[i] and there may be several such subsequences (of the same length).
    #  We call this a subsequence of type D.
    down = [1]*N

    for i in range(1,N):
        up[i] = up[i-1]
        down[i] = down[i-1]
        if nums[i]-nums[i-1]>0:
            '''
                    If nums[i] > nums[i-1], then we can use nums[i] to make a longer subsequence of type U
                    Proof: We consider a subsequence of type D in {0,...,i-1} (its length is down[i-1]).
                    Let N be the last number of this subsequence.
                    - If nums[i] > N, then we can add nums[i] to the subsequence and it gives us a longer
                    valid subsequence of type U.
                    - If nums[i] <= N, then:
                    (1) N cannot be nums[i-1], because nums[i-1] < nums[i] <= N i.e. nums[i-1] < N
                    (2) We can replace N with nums[i-1] (we still have a valid
                    subsequence of type D since N >= nums[i] > nums[i-1] i.e. N > nums[i-1]),
                    and then add nums[i] to the subsequence, and we have a longer subsequence of type U.
                    Therefore up[i] = down[i-1] + 1
                    
                    There is no gain in using nums[i] to make a longer subsequence of type D.
                    Proof: Let N be the last number of a subsequence of type U
                    in {0,...,i-1}.
                    Assume we can use nums[i] to make a longer subsequence of type D. Then:
                    (1) N cannot be nums[i-1], otherwise we would not be able to use nums[i]
                    to make a longer subsequence of type D as nums[i] > nums[i-1]
                    (2) Necessarily nums[i] < N, and therefore nums[i-1] < N since nums[i-1] < nums[i].
                    But this means that we could have used nums[i-1] already to make a longer
                    subsequence of type D.
                    So even if we can use nums[i], there is no gain in using it, so we keep the old value of
                    down (down[i] = down[i-1])                   
            '''
            down[i] = down[i-1]+1
        elif nums[i]-nums[i-1]<0:
            # The reasoning is similar
            up[i] = up[i-1]+1

    return max(down[-1], up[-1])

nums = [1]
print(wiggleMaxLength(nums))