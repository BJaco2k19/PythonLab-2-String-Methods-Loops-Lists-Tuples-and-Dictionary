#Part 13, using if-elif-else statements to determine grade
Marissa = sum([82, 91, 79, 63, 97]) / len([82, 91, 79, 63, 97])
if Marissa >= 90:
    print("Marissa's grade is A at %.2f." % Marissa)
elif Marissa >= 80:
    print("Marissa's grade is B at %.2f." % Marissa)
elif Marissa >= 70:
    print("Marissa's grade is C at %.2f." % Marissa)
elif Marissa >= 60:
    print("Marissa's grade is D at %.2f." % Marissa)
else:
    print("Marissa's grade is F at %.2f." % Marissa)