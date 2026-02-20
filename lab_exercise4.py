# 1st

# def select_max_output(userInput):
#     n = len(userInput)
#     max_value = userInput[0]
#     for i in range(1, n):
#         if userInput[i] > max_value:
#            max_value = userInput[i]
#     return max_value

# userInput = list(map(int, input("Enter a list of numbers: ").split()))
# maxOutput = select_max_output(userInput)
# print(maxOutput)

# 2nd

# def numbers():
#     if num1 > num2 and num1 > num3:
#         print(f"{num1} is the greatest number.")
#     elif num2 > num1 and num2 > num3:
#         print(f"{num2} is the greatest number.")
#     elif num3 > num1 and num3 > num2:
#         print(f"{num3} is the greatest number.")
#     else:
#         print("All numbers are equal.")

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))

# numbers()

# 3rd

# def numbers(numInput1, numInput2, numInput3):
#     if numInput2 < numInput1 > numInput3:
#         print(f"{numInput2} is the greatest number.")
#     elif numInput1 < numInput2 > numInput3:
#         print(f"{numInput1} is the greatest number.")
#     elif numInput1 < numInput3 > numInput2:
#         print(f"{numInput3} is the greatest number.")
#     else:
#         print("All numbers are equal.")
    
# numInput1 = int(input("Enter first number: "))
# numInput2 = int(input("Enter second number: "))
# numInput3 = int(input("Enter third number: "))

# numbers(numInput1, numInput2, numInput3)