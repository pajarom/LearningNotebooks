def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    
    # Complete the while loop condition.
    while multiplier <= 5:
        result = number * multiplier
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "×" + str(multiplier) + "=" + str(result))
        
        # Increment the appropriate variable
        multiplier += 1

# Calls to the function
multiplication_table(3)
# Should print
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

multiplication_table(5)
# Should print
# 5x1=5
# 5x2=10
