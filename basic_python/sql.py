lst = []
a = [1,2,3,4,5]
lst.append(a)
del a 
a = [23232, 12312312]
lst.append(a)

print(lst)

a = set([1,2,3])
b = set([3,4,5])
a.difference_update(b)
print(a)
a = tuple([1,2,3])
b = tuple([3,4,5])
print(set(a+b))