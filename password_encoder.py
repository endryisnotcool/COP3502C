def main():     # Endry Rodriguez
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        menu_option = int(input('Please enter an option: '))
        if menu_option == 1:
            password = input('Please enter a password to encode: ')
            encoded_password = encode(password)
            print('Your passsword has been encoded and stored!')
            continue
        elif menu_option == 2:
            print(f'The encoded password is {encode(password)}, and the original password is {decode(encoded_password)}.')
        elif menu_option == 3:
            break
        False

def encode(string):
    encode_output = ''
    for num in string:
            x = str((int(string[num]) + 3) % 10)
            encode_output += x
    return encode_output

def decode():
    pass


if __name__ == " __main__":
    main()
