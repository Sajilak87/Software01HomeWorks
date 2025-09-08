def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def main():
    # Example list
    my_list = [3, 7, 12, 5, 9]
    result = sum_list(my_list)
    print(f"The sum of {my_list} is {result}")


if __name__ == "__main__":
    main()