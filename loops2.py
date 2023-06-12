#Using the range function, print the multiples of 5 from 10 through -
# 25 (inclusive). The numbers should each be separated by a space.
# (Hint: use the end parameter to the print function like we did in
# for_range.py). Don’t forget to print a newline after this loop by
# calling print() with no parameters.

for i in range(10, 26, 5):
    print(i, end = " ")
print()

#Using the range function, print the multiples of 3 from -3 to 21
# (inclusive). Each number should be separated by a comma and a
# space. There should not be a comma after the final number (21).

for i in range(-3,21,3):
    print(i, end = ", ")
print(21)

