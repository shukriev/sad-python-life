# set provides: difference, intersection, union
print("SET EXAMPLES DIFFERENCE")
setExample = set("some set values")
print(setExample)

A = {10, 20, 30, 40, 80}
B = {100, 30, 80, 40, 60}


print("Set difference method")
print(A.difference(B))
print(B.difference(A))

print()

print("Minus operator")
print(A - B)
print(B - A)

print()

A2 = {10, 20, 30, 40, 80}
B2 = {10, 20, 30, 40, 80}

B2.add(100)
A2.add(120)

print(A2 - B2)
print(B2 - A2)

print()

print("Symmetric Difference")
print(A2.symmetric_difference(B2))
print(B2.symmetric_difference(A2))

print()

print("SET EXAMPLES INTERSECTION")

A2 = {10, 20, 30, 40, 80}
B2 = {10, 20, 30, 40, 80, 100}

print()

# INTERSECTION (Compares and returns whatever matches in both sets
intersection = B2.intersection(A2)

print(intersection)

print()
print("UNION EXAMPLES")
# UNION

print(A2.union(B2))
