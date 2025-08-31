SIZE_LIMIT = 42

length = int(input("Enter the length of the zander (cm): "))

if length < SIZE_LIMIT:
    difference = SIZE_LIMIT - length
    print(f"The zander is too small. Release it back into the lake!")
    print(f"It is {difference} cm below the size limit.")
else:
    print("The zander meets the size limit. You can keep it.")