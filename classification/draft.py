def numTilePossibilities_counter(tiles):
    def helper(tiles, ret):
        if(not tiles):
            return

        for i, c in enumerate(tiles):
            if(i>0 and tiles[i-1] == c): continue
            ret[0] += 1
            helper(tiles[i+1:], ret)

    tiles.sort()
    ret = [0]
    helper(tiles, ret)
    return ret[0]
