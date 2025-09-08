numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == "":  # empty string -> quit
        break
    try:
        num = float(user_input)  # allow decimals too
        numbers.append(num)
    except ValueError:
        print("That wasn't a valid number, please try again.")

numbers.sort(reverse=True)

top_five = numbers[:5]

print("\nThe five greatest numbers are:")
for n in top_five:
    print(n)