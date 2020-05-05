#coding=utf-8

'''
We have a sequence of books: the i-th book has thickness books[i][0] and height books[i][1].

We want to place these books in order onto bookcase shelves that have total width shelf_width.

We choose some of the books to place on this shelf (such that the sum of their thickness is <= shelf_width),
then build another level of shelf of the bookcase so that the total height of the bookcase has increased
by the maximum height of the books we just put down.  We repeat this process until there are no more books to place.

Note again that at each step of the above process, the order of the books we place is the same order as the given sequence of books.
  For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf,
  the third book on the second shelf, and the fourth and fifth book on the last shelf.

Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.
'''

#lightspot: 阶段没有重新组织划分，还是以原始books数组的每个元素为阶段
# 但是在当前阶段dp[i]，推演books[i]加入后能获得最小总体高度时，能够推演到最远的那个j，是受限的，
# 受制于[j..i]累积宽度 不能超过规定的shelft-width。

# 这里给出的启示是：设定的限制条件，可能只是限制了当前dp[i]，向低位推演的条件范围，不影响一般性质的阶段划分和状态转移

import sys
def minHeightShelves(books, shelf_width):
    N = len(books)

    # dp[i] min height after place (i-1)th book
    dp = [0] + [float("inf")] * N

    for i in range(1, N + 1):
        levelHight, width_left = 0, shelf_width

        j = i
        while j > 0:
            width_left -= books[j - 1][0]
            if width_left < 0:
                break

            levelHight = max(levelHight, books[j - 1][1])
            dp[i] = min(dp[i], dp[j - 1] + levelHight)

            j -= 1
    return dp[-1]


shelf_width = 10
#books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
books = [[7,3],[8,7],[2,7],[2,5]]
print(minHeightShelves(books, shelf_width))


