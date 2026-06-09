#Part 16: While Loops
foods = [9.99, 5.25, 2.75, 2.99, 2.99, 5.25, 3.75]
sub_total = 0
index = 0
while index < len(foods):
    sub_total += foods[index]
    index += 1
print("The subtotal is: $" + str(round(sub_total, 2)))    