

print("Welcome!")
while True: #while loop was used to keep asking the user everytime for their choice until they choose to quit
    users_input = input("Choose Q for Quit, E for Encrypt, D for Decrypt: ").upper()
    #.upper was used to make the program run even if the user entered a lower case
    #.lower could be also used if the dictionary was written in lower cases
    if users_input == 'Q':
        break
    elif users_input == 'E':
        alphabet_to_morse_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
            '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
            '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
            ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
            '$': '...-..-', '@': '.--.-.', ' ': '/' }

        text = input("Enter text to encrypt: ")
        text = " ".join(alphabet_to_morse_dict.get(c,' ') for c in text.upper())
        print(text)
    elif users_input == 'D': 
        #instead of rewritting the morsecode dictionary again a flip function was used which flips the key to value and vice versa
        flip = {value: key for key, value in alphabet_to_morse_dict.items()}
 # morse_to_alphabet_dict = {
        #     '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
        #     '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
        #     '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        #     '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
        #     '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',',
        #     '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&',
        #     '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"',
        #     '...-..-': '$', '.--.-.': '@', '/': ' '
        # } 

        text = input("Enter text to decrypt: ")
        text = "".join(flip.get(c, '') for c in text.split())
        print(text)  
    else: 
        print ("Invalid input")


        