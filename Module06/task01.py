import random

def roll_dice():
    return random.randint(1, 6)

def main():
    roll = 0
    # Keep rolling until we get a 6
    while roll != 6:
        roll = roll_dice()
        print(f"Rolled: {roll}")

if __name__ == "__main__":
    main()