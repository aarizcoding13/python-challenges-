a = int(input("enter a number for numerator"))
b = int(input("enter a number for the denominator"))

if a % b == 0 :
    print(f"{a} is divisible by {b}")
else:
    print(f"{a} is not divisible by {b}")