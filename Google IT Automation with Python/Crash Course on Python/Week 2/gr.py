def fractional_part(numerator, denominator):
    # Operate with numerator and denominator to
    # keep just the fractional part of the quotient 
    if denominator == 0 or numerator == 0:
        part = 0
    else:
        part = numerator/denominator
    return part


print(fractional_part(5, 5)) # Should print 0
print(fractional_part(5, 4)) # Should print 0.25
print(fractional_part(5, 0)) # Should print 0.66...
print(fractional_part(0, 5)) # Should print 0