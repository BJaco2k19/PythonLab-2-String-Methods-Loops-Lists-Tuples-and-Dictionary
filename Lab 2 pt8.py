#Part 8: Slicing
str1="America, land of the free"
print(str1)            #Test print to show the original string
str11=str1[0:7]
print(str11)           #Output should just be "America"
str12=str1[-4:]       
print(str12)           #Output should just be "free"
str13=str1[2::2]
print(str13)           #Output should just be every even indexed character in the
                       #string, starting from index 2
