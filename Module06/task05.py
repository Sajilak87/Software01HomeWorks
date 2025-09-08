def remove_odds(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


def main():

    my_list = [3, 7, 12, 5, 9, 4, 8]
    filtered_list = remove_odds(my_list)

    print(f"Original list: {my_list}")
    print(f"List without odd numbers: {filtered_list}")


if __name__ == "__main__":
    main()