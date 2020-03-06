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

import sys
def minHeightShelves(books, shelf_width):
    # dp[i] min height after place (i-1)th book
    # dp[i] = min(curHeight + dp[i-1...0])
    N = len(books)
    dp = [sys.maxint]*(N+1)
    dp[0] = 0

    for i in range(1,N+1):
        width_left, tmp_height = shelf_width, 0

        j = i
        while j>0:
            width_left -= books[j-1][0]
            tmp_height = max(tmp_height, books[j-1][1])

            if width_left >= 0:
                dp[i] = min(dp[i], dp[j-1]+tmp_height)
            j -= 1

    return dp[-1]


shelf_width = 10
#books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
books = [[7,3],[8,7],[2,7],[2,5]]
print(minHeightShelves(books, shelf_width))


