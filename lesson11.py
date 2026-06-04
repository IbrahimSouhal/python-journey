while True:
    try:
        number = int(input("Enter a number: "))
        result = 10 / number
        print(f"Result: {result}")
    except ValueError:
        print("That's not a number!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")