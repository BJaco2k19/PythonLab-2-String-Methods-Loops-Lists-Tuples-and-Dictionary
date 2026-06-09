#Lab 2 pt25, using lists to total amounts without using sum() function
year1 = [200, 320, 180, 210, 175, 305]
total1 = 0
for i in year1:
    total1 += i
print("Total for year 1: $", total1)
year2 = [550, 285, 195, 410]
total2 = 0
for i in year2:
    total2 += i
print("Total for year 2: $", total2)
if total2 > total1:
    print("Year 2 had a higher total.")
else:
    print("Year 1 had a higher total.")