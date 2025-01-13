def main():
    user_input = int(input("please enter a number: "))
    while user_input != 1:
        try:
            user_input = collatz(user_input)
        except ValueError:
            print("Invalid Input")
def collatz(number):
    if number%2 == 0:
        result = number // 2
    else:
        result = 3* number + 1  
    print(result)
    return result
main()
    