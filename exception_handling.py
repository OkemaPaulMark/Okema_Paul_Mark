# This script demonstrates exception handling in Python by performing division
# and handling various exceptions that may occur.
# including ZeroDivisionError, ValueError, and KeyboardInterrupt.
while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = num1 / num2
        print(f"Result: {result}")
        break  # Exit loop if successful

    except ZeroDivisionError:
        print("Error: Cannot divide by zero. Please enter a different second number.\n")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values only.\n")

    except KeyboardInterrupt:
        print("\nError: Program interrupted by user. Exiting...")
        break

    except Exception as e:
        print(f"Unexpected error: {e}\n")
    finally:
        print("Attempt completed. Please try again if needed.\n")