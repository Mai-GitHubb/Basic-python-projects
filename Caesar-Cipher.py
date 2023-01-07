logo = """           
     ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
    a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
    8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
    "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
     `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
                88             88                                 
               ""             88                                 
                              88                                 
     ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
    a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
    8b         88 88       d8 88       88 8PP""""""" 88          
    "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
     `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                  88                                             
                  88           
    """
print(logo)


def caeser_cipher():
    import string
    eod = input("Type 'encode' to encrypt or 'decode' to decrypt:\n")
    user_input = input('Type your message:\n')
    num = int(input('Type the shift number:\n'))
    output = ''
    alpha = list(string.ascii_lowercase)
    if eod.lower() == 'encode':
        for i in user_input:
            output += alpha[(alpha.index(i)+num) % 25]
        print(f'Your ENCODED message is {output}')

    elif eod.lower() == 'decode':
        for i in user_input:
            output += alpha[(alpha.index(i) - num) % 25]
        print(f'Your DECODED message is {output}')
    go_again = input('Do you want to go again? (yes/no):\n')
    if go_again.lower() == 'yes':
        return caeser_cipher()
    elif go_again.lower() == 'no':
        print('Goodbye! See you again.')


caeser_cipher()
