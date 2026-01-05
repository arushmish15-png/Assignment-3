x = float(input("enter a number:"))


if x < 0:
    print("factorial not possible")
elif x != int(x):
    print("factorial not possible for decimal numbers")

else:
    result = 1

    for i in range(int(x), 1, -1):
        result = result * i
    print(f"Factorial of {x} is", result)
