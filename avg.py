# Create a program avg.py that calculates and prints the average of
# 10 real (i.e., decimal) numbers entered by the user. Make sure you
# ask (i.e., prompt) the user to enter each number (the user will hit
# enter after each number). 

#make a loop that asks user to input 10 numbers
#store the inputted numbers in an array
#then calculate the avg of the 10 numbers
#print it out

newSum = 0 #aggregator variable must be initialized before the loop

for num in range(10):
    num = float(input("please enter a number: "))
    newSum += num
print("the average of your numbers is: ", newSum/10)