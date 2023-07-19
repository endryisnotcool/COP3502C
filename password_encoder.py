encode_output = None
original_password = None
encoded_password = None

def encode(string):
    global encode_output
    encode_output = ''
    for x in string[0:8]:
        if int(x) <= 9:
            x = chr(ord(x)+3)
            encode_output += x
        else:
            break
    return encode_output

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
            print(f'The encoded password is {encoded_password}, and the original password is {password}.')
        elif menu_option == 3:
            break
        False

if __name__ == " __main__":
    main()
