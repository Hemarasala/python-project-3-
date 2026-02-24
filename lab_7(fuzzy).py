def union(a, b):
    result = {}
    for key in a:
        if key in b:
            result[key] = max(a[key], b[key])
        else:
            result[key] = a[key]
    
    for key in b:
        if key not in a:
            result[key] = b[key]
    
    return result

def intersection(a, b):
    result = {}
    for key in a:
        if key in b:
            result[key] = min(a[key], b[key])
    
    return result

def complement(a, b):
    result = {}
    for key in b:
        if key not in a:
            result[key] = b[key]
    return result

def difference(a, b):
    result = {}
    for key in a:
        if key not in b:
            result[key] = a[key]
    return result

# Test data
a = {'2': 1, '3': 0.5, '4': 0.3,'5':0.2,'6':0.9}
b = {'2': 0.5, '3': 0.7, '4': 0.2,'5': 0.4,'7':0.3}

# Function calls
nion = union(a, b)
print("Union of sets a and b:", nion)

tersection = intersection(a, b)
print("Intersection of sets a and b:", tersection)

complement_ab = complement(a, b)
print("Complement of a in b:", complement_ab)

difference_ab = difference(a, b)
print("Difference of a relative to b:", difference_ab)