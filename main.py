def encode(password):
    list_password = list(password)
    for i in range(0, len(password)):
        list_password[i] = str(int(password[i]) + 3)
        i += 1
    return "".join(list_password)


if __name__ == "__main__":
    while True:
        print("Menu\n-------------")
        print("1. Encode\n2. Decode\n3. Quit")
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            enc_password = encode(password)
            print("Your password has been encoded and stored!")

        elif option == 2:
            print(f"The encoded password is {enc_password}, and the original password is .")

        else:
            break


