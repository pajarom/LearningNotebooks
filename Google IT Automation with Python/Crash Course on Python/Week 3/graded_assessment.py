[1]
number = 15 # Initialize the variable
while number >= 5: # Complete the while loop condition
    print(number, end=" ")
    number -= 5 # Increment the variable

# Should print 15 10 5 

[2]
for number in range(5):
    if number % 2 == 1:
        print("even")
    else:
        print("odd")


# Should print:
# odd
# even
# odd
# even
# odd

[3]
def digits(n):
    count = 0
    if n == 0:
      count += 1
    while n > 0: # Complete the while loop condition
        # Complete the body of the while loop. This should include 
        # performing a calculation and incrementing a variable in the
        # appropriate order.  
        count += 1 
        n //= 10
    return count
    
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1

[4]
def sequence(low, high):
    # Complete the outer loop range to make the loop run twice
    # to create two rows
    for x in range(2): 
        # Complete the inner loop range to print the given variable
        # numbers starting from "high" to "low" 
        # Hint: To decrement a range parameter, use negative numbers
        for y in range(high, low - 1, -1): 
            if y == low:
                # Don’t print a comma after the last item
                print(str(y)) 
            else:
                # Print a comma and a space between numbers
                print(str(y), end=", ") 

sequence(1, 3)
# Should print the sequence 3, 2, 1 two times, as shown above.

[5]
def countdown(start):
    x = start
    if x > 0:
        return_string = "Counting down to 0: "
        while x >= 0: # Complete the while loop
            return_string += str(x) # Add the numbers to the "return_string"
            if x > 0:
                return_string += ","
            x -= 1 # Decrement the appropriate variable
    else:
        return_string = "Cannot count down to 0"
    return return_string


print(countdown(10)) # Should be "Counting down to 0: 10,9,8,7,6,5,4,3,2,1,0"
print(countdown(2)) # Should be "Counting down to 0: 2,1,0"
print(countdown(0)) # Should be "Cannot count down to 0"

[6]
def odd_numbers(maximum):
    
    return_string = "" # Initializes variable as a string

    # Complete the for loop with a range that includes all 
    # odd numbers up to and including the "maximum" value.
    for x in range(1, maximum+1, 2): 

        # Complete the body of the loop by appending the odd number
        # followed by a space to the "return_string" variable.
        return_string += str(x) + " " 

    # This .strip command will remove the final " " space 
    # at the end of the "return_string".
    return return_string.strip()


print(odd_numbers(6))  # Should be 1 3 5
print(odd_numbers(10)) # Should be 1 3 5 7 9
print(odd_numbers(1))  # Should be 1
print(odd_numbers(3))  # Should be 1 3
print(odd_numbers(0))  # No numbers displayed

[7]
x = 1
sum = 5
while x <= 10:
    sum += x
    x += 1
print(sum)
# Should print 55

[8]
for x in range(1, 10, 3):
    print(x)

[9]
num1 = 0
num2 = 0

for x in range(5):
    num1 = x
    print(x)
    for y in range(14):
        num2 = y + 3
        print(y)

print(num1 + num2)

[10]
def test_code(num):
  x = num
  while x % 2 == 0:
    x = x / 2

test_code(0)