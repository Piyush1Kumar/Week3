def oddTuples(tup):

"""
tup : a tuple
returns : tuple, every other element of tup from first
"""

    new_tup=()
    for i in range(len(tup)):
        if i%2==0:
            new_tup = new_tup + (tup[i],)
    return new_tup