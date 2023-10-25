# method to encode the password
def encode(password):
    list_password = list(password)
    for i in range(0, len(password)):
        list_password[i] = str(int(password[i]) + 3)
        i += 1
    return "".join(list_password)

# method to decode the encoded password
def decode(password):
    pass_list = list(password)
    en_pass = list()
    for i in pass_list:
        i = int(i)
        i -= 3
        en_pass.append(str(i))
    en_pass = ''.join(en_pass)
    return en_pass

# main method that prints menu and encodes or decodes based on user selection
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
            print(f"The encoded password is {enc_password}, and the original password is {decode(enc_password)}.")

        else:
            break


