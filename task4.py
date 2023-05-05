def hash_key(v, m):
    return v % m


# To use this function, simply call it with the value and size of the input list as arguments:

m = 7
v = 3
print(hash_key(v, m))  # returns 3
