def encode(password):
    newstr = ""
    for c in password:
        if int(c) > 7:
            newstr += str( (int(c)+3)-10 )
        else:
            newstr += str(int(c) + 3)
    return newstr


def decode(password):
    int_password = []
    for num in password:
        if int(num) > 2:
            int_password.append(int(num) - 3)
        elif int(num) <= 2:
            int_password.append((int(num) + 10) - 3)
    decoded_password = ""
    for i in int_password:
        decoded_password += str(i)
    return decoded_password


def main():
    choice = ""
    first = True
    storage = ""
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode\n2. Decode\n3. Quit")
        print()
        choice = input("Please enter an option: ")
        if choice == "1":
            choice = input("Please enter the password to encode: ")
            storage = encode(choice)
            print("Your password has been encoded and stored!")
            print()
        elif choice == "2":
            print("The encoded password is " + storage + ", and the original password is " + decode(storage) + ".")
            print()
        elif choice == "3":
            exit()
    
if __name__ == "__main__":
    main()
