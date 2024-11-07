import random
import string
try:
    print("Select a lengh")
    x = int(input())
    def generate_random_string(length):
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string

    random_string = generate_random_string(x)
    print(random_string)
except ValueError:
    print("The lengh can only be numeric!")
