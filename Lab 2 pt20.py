#Lab 2 pt20, 2D Lists
students = [['Jack', 'Lisa', 'Tomas', 'Daniel'], [22, 27, 30, 19]]
for i in range(len(students)):
    for j in range(len(students[i])):
        print(students[i][j])
print([i[1] for i in students])
print(students[0][1])
print(students[1][1])