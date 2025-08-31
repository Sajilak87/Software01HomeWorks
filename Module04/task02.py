INCH_TO_CM = 2.54

while True:
    inches = float(input("Enter length in inches (negative to quit): "))

    if inches < 0:
        print("Program ended.")
        break

    centimeters = inches * INCH_TO_CM
    print(f"{inches} inches = {centimeters:.2f} cm")