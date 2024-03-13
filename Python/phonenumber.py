


def print_sorted_dict(phone_book):
    sorted_phone_book = dict(sorted(phone_book.items()))
    for name, number in sorted_phone_book.items():
        print(f"{name}: {number}")

def main():
    friends_phone_book = {
        "Alice": "1234567890",
        "Bob": "9876543210",
        "Charlie": "4561237890"
    }

    print("Phone Book:")
    print_sorted_dict(friends_phone_book)

    name = input("Enter a name: ")

    if name in friends_phone_book:
        print(f"{name}'s phone number is {friends_phone_book[name]}")
    else:
        number = input("Enter the phone number: ")
        friends_phone_book[name] = number
        print(f"{name}'s phone number ({number}) added to the phone book.")

    print("Updated Phone Book:")
    print_sorted_dict(friends_phone_book)

if __name__ == "__main__":
    main()