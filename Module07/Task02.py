names = set()

while True:
    name = input("Enter a name (empty string to stop): ")

    if name == "":
        break  # stop when empty string entered

    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("\nAll entered names:")
for n in names:
    print(n)