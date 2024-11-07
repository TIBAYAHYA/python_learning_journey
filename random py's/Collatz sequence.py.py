def collatz(number):
    """Generates the Collatz sequence for the given number."""
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(result)
    return result

def main():
    try:
        user_input = int(input("Enter an integer: "))
        while user_input != 1:
            user_input = collatz(user_input)
    except ValueError:
        print("Please enter a valid integer.")


main()