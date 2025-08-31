CORRECT_USERNAME = "python"
CORRECT_PASSWORD = "rules"

attempts = 0
MAX_ATTEMPTS = 5

while attempts < MAX_ATTEMPTS:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        print("Welcome!")
        break
    else:
        attempts += 1
        print(f"Incorrect username or password. Attempts left: {MAX_ATTEMPTS - attempts}")

if attempts == MAX_ATTEMPTS:
    print("Access denied.")