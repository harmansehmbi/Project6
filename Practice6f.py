# Definition of function : addNumbers
# num1 and num2 are inputs
def addNumbers(num1, num2):
    num3 = num1 + num2
    print("Sum of {} and {} is {}".format(num1, num2, num3))
    return num3
# Execution of function addNumbers
print("Sum is: ", addNumbers(56, 78))