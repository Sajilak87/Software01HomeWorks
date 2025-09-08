import math


def pizza_unit_price(diameter_cm, price_euros):
    radius_m = (diameter_cm / 2) / 100
    area_m2 = math.pi * (radius_m ** 2)
    return price_euros / area_m2



def main():
    print("Enter details for the first pizza:")
    d1 = float(input("Diameter (cm): "))
    p1 = float(input("Price (€): "))

    print("\nEnter details for the second pizza:")
    d2 = float(input("Diameter (cm): "))
    p2 = float(input("Price (€): "))

    unit1 = pizza_unit_price(d1, p1)
    unit2 = pizza_unit_price(d2, p2)

    print(f"\nFirst pizza unit price: {unit1:.2f} €/m²")
    print(f"Second pizza unit price: {unit2:.2f} €/m²")

    if unit1 < unit2:
        print("The first pizza provides better value for money.")
    elif unit2 < unit1:
        print("The second pizza provides better value for money.")
    else:
        print("Both pizzas provide the same value for money.")



if __name__ == "__main__":
    main()