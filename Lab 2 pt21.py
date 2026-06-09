#Lab 2 pt21, Tuples
tuple1 = (8, 11, 16, [32, 46])
print(tuple1)
#Since Tuples are immutable, you need to convert them to a list to make changes, then convert 
#and then convert back to a tuple
list1 = list(tuple1)
list1[3] = [59, 66]
tuple2 = tuple(list1)
print(tuple2)
