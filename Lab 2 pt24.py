#Lab 2 pt 24, more Tuples
tupleNum = (10, 20, 30, 40)
print("Original Tuple: ", tupleNum)
#Tuples are immutable, so we convert to a list to make changes
listNum = list(tupleNum)
for i in range (len(listNum)):
    listNum[i] += 10
tupleNum = tuple(listNum)
print("Modified Tuple: ", tupleNum)