import pyinputplus as pyip

# Prices for each option
prices = {
    'bread': {'wheat': 1.00, 'white': 0.75, 'sourdough': 1.25},
    'protein': {'chicken': 2.00, 'turkey': 2.50, 'ham': 2.00, 'tofu': 1.75},
    'cheese': {'cheddar': 0.50, 'Swiss': 0.75, 'mozzarella': 0.75},
    'extras': {'mayo': 0.25, 'mustard': 0.25, 'lettuce': 0.50, 'tomato': 0.50}
}

# Function to calculate the total cost
def calculate_total_cost():
    total_cost = 0

    # Ask for bread type
    total_cost += prices['bread'][pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt="Choose your bread type:\n")]

    # Ask for protein type
    total_cost += prices['protein'][pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt="Choose your protein type:\n")]

    # Ask if they want cheese
    if pyip.inputYesNo(prompt="Do you want cheese? ") == 'yes':
        total_cost += prices['cheese'][pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], prompt="Choose your cheese type:\n")]

    # Ask for extras
    total_cost += sum(prices['extras'][extra] for extra in prices['extras'] if pyip.inputYesNo(prompt=f"Do you want {extra}? ") == 'yes')

    # Ask for the number of sandwiches
    num_sandwiches = pyip.inputInt(prompt="How many sandwiches do you want? ", min=1)
    total_cost *= num_sandwiches

    return total_cost

# Calculate and display the total cost
total_cost = calculate_total_cost()
print(f"Total cost: ${total_cost:.2f}")