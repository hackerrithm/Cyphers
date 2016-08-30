ALPHABET_LETTER_COUNT = 26

#-----------------------------CAESER CYPHER--------------------

def _caserFetchChoice():
    while True:
        print('Encrypt or Decrypt?')
        choice = input().lower()
        if choice in 'encrytp e decrypt d'.split():
            return choice
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d". ')

def _caserGetMessage():
    print('Enter your string: ')
    return input()

def _caserGetKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (ALPHABET_LETTER_COUNT))
        key = int(input())
        if(key >= 1 and key <= ALPHABET_LETTER_COUNT):
            return key

def _caserGetTranslatedMessage(choice, message, key):
    if choice[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated

def caserCypher():
    mode = _caserFetchChoice()
    message = _caserGetMessage()
    key = _caserGetKey()

    print('Translated message is: ')
    print(_caserGetTranslatedMessage(mode, message, key))


#-------------------------------- VIGENERE ---------------------------------

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def _vigenereFetchChoice():
    while True:
        print('Encrypt or Decrypt')
        choice = input().lower()
        if choice in 'encrypt e decrypt d'.split():
            return choice
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d". ')

def _vigenereGetInput():
    print('Enter your message')
    return input()

def _vigenereEnterKey():
    print('Enter you key')
    return input()

def _viginereEncrypt(key, message):
    return _vigenereTranslateMessage(key, message, 'encrypt')


def _vigenereDecryt(key, message):
    return _vigenereTranslateMessage(key, message, 'dencrypt')

def _vigenereTranslateMessage(key, message, mode):
    translated = []

    keyIndex = 0
    key = key.upper()

    for symbol in message:
        num = alphabet.find(symbol.upper())
        if num != -1:
            if mode == 'e' or mode == 'encrypt':
                num += alphabet.find(key[keyIndex])
            elif mode == 'd' or mode == 'decrypt':
                num -= alphabet.find(key[keyIndex])

            num %= len(alphabet)

            if symbol.isupper():
                translated.append(alphabet[num])
            elif symbol.islower():
                translated.append(alphabet[num].lower())

            keyIndex += 1;
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated.append(symbol)

    return ''.join(translated)


def _vigenereCypher():
    mode = _vigenereFetchChoice()
    message = _vigenereGetInput()
    key = _vigenereEnterKey()
    print('Translated message is: ')
    print(_vigenereTranslateMessage(key, message, mode))

#-------------------------------- COLUMNAR -----------------------

def _columnarFetchChoice():
    while True:
        print('Encrypt or decrypt: ')
        choice = input().toupper()
        if choice in 'encrypt e decrypt d'.split():
            return choice
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d". ')

def _columnarGetMessage():
    print('Enter string: ')
    return input()

def _columnarGetKeyWord():
    print('Enter key word')


#-------------------------------- DRIVER -------------------------
print('CYPHERS\n 1. CAESER CYPHER\n 2. VIGENERE CYPHER\n Select one of the above options')
decide = input()
print('Enter test case for selected option')
testCase = int(input())
index = 0
if decide == '1':
    while (index < testCase):
        #caeserExample = caserCypher()
        print(caserCypher())
        index = index + 1
elif decide == '2':
    while (index < testCase):
        #vigenereExample = _vigenereCypher()
        print(_vigenereCypher())
        index = index + 1


