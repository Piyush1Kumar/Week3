def biggest(animals):
"""
animals : dictionary where all the values are lists
returns : The key with the largest number of values associated with it.
"""
    big = 0
    if len(animals) == 0:
        return None
    for e in animals:
        l = len(animals[e])
        if l>big:
            big = l
            key = e
    return e