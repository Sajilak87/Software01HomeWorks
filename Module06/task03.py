def gallons_to_liters(gallons):
    return gallons * 3.78541

# Main program
def main():
    while True:
        gallons = float(input("Enter volume in gallons (negative number to quit): "))
        if gallons < 0:
            print("Exiting program...")
            break
        liters = gallons_to_liters(gallons)
        print(f"{gallons} gallons is equal to {liters:.2f} liters.")


if __name__ == "__main__":
    main()