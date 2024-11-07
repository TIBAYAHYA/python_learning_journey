def find_max(list_of_numbers):
    max = list_of_numbers[0]
    for number in list_of_numbers:
        if number >max:
            max = number
    print(max)

