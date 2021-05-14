####################################################
# 7. Effortless Dictionary
####################################################

f1 = {}
f2 = {"samsung": 1, "volantis": 2, "cameron": 3}
f3 = {("fido", "fizz", "telus", "fonus"): [4, 3, 2, 1]}
print(f2)

print('\nlooking up the value for key samsung')
print(f2["samsung"])
print('\nPrint out the keys')
print(list(f2.keys()))
print('\nPrinting out the values')
print(list(f2.values()))
print('\nPrinting the items')
print(list(f2.items()))

print('\nInserting another item( key+ value) with setdefault')
f2.setdefault("exodia", 5)
print(f2)

print('\nUpdating the value of a key')
f2.update({"volantis": 22.2})
print(f2)

print('\nDeleting')
del f2["cameron"]
print(f2)
