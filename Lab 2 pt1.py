#Part 1: String Sequencing and built-in methods, 1.
my_name = "Bradley"
#First, display the first and last letters of my name
print("The first letter of my name is:", my_name[0])
print("The last letter of my name is:", my_name[-1])
#Next, display the length of my name
print("The length of my name is:", len(my_name))
#Next, display the first to third letters of my name, using a new variable to store the result
sub_name = my_name[0:3]
print("The first to third letters of my name are:", sub_name)
sub_name = my_name[:3]
print("The same as:", sub_name)
#Finally, the second to last letter of my name, first using index, then len()
sub_name2 = my_name[-2:-1]
print("The second to last letter of my name are:", sub_name2)
sub_name3 = my_name[len(my_name)-2:-1]
print("The same as:", sub_name3)
