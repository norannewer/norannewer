def hash_function(key):
    return key % 5


hash_table = [[] for _ in range(5)]
value_list = [3, 2, 9, 11, 7]

for value in value_list:
    key = hash_function(value)
    hash_table[key].append(value)

while True:
    print("Choose one of the following options:")
    print("1. Construct the whole hash table")
    print("2. Add a new element to the hash table")
    print("3. Update a value of a certain key")
    print("4. Delete an element from the hash table")
    print("5. Search for an element in the hash table")
    print("6. Print all elements with their keys of the hash table")

    choice = int(input())

    if choice == 1:
        print(hash_table)

    elif choice == 2:
        value = int(input("Enter a new value: "))
        key = hash_function(value)
        hash_table[key].append(value)

    elif choice == 3:
        key = int(input("Enter a key to update: "))
        if len(hash_table[key]) > 0:
            value = int(input("Enter a new value: "))
            index = hash_table[key].index(key)
            hash_table[key][index] = value
            print(f"Value {key} updated to {value}")
        else:
            print(f"No values found for key {key}")

    elif choice == 4:
        value = int(input("Enter a value to delete: "))
        key = hash_function(value)
        if len(hash_table[key]) > 0 and value in hash_table[key]:
            index = hash_table[key].index(value)
            del hash_table[key][index]
            print(f"Value {value} deleted from key {key}")
        else:
            print(f"No values found for key {key}")

    elif choice == 5:
        value = int(input("Enter a value to search: "))
        key = hash_function(value)
        if len(hash_table[key]) > 0 and value in hash_table[key]:
            print(f"Value {value} found at key {key}")
        else:
            print(f"No values found for key {key}")

    elif choice == 6:
        for i in range(len(hash_table)):
            print(f"Key {i}: {hash_table[i]}")

    else:
        print("Invalid choice. Please try again.")
