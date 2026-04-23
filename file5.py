# Taking input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Before swapping:")
print(a, b, c)

# Swapping using a temporary variable
temp = a
a = b
b = c
c = temp

