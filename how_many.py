def how_many(animals):

""" animals : dictionary where all values are lists
    returns : total number of values in the dictionary
"""
    count=0
    for e in animals:
        count = count + len(animals[e])
    return count