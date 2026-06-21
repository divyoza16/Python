# Take input from the user as a floating point number.
# Convert float values into int values and print both values with a message explain difference.  
a = float(input("Enter the number: "))
b = int(a)  
print(f"Floating value is {a}") 
print(f"Integer value is {b}")   
print("Explain:")
print("The float value can contain decimal digits,")
print("while the integer value removes the decimal part.")