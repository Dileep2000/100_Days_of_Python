def encrypt(text, shift):
    encrypted_text = ""
    for i in text:
        if i.isupper():
            if ord(i)+shift > ord("Z"):
                encrypted_text += chr(ord("A") + (ord(i) + shift - ord("Z")) - 1)
            else:
                encrypted_text += chr(ord(i)+shift)
        else:
            if ord(i)+shift > ord("z"):
                encrypted_text += chr(ord("a") + (ord(i)+shift-ord("z")) - 1)
            else:
                encrypted_text += chr(ord(i)+shift)
    return encrypted_text

def decrypt(text,shift):
    decrypted_text = ""
    for i in text:
        if i.isupper():
            if ord(i) - shift < ord("A"):
                decrypted_text += chr(ord("Z") - (ord(i) - shift - ord("A")) -1)
            else:
                decrypted_text += chr(ord(i) - shift)
        else:
            if ord(i) - shift > ord("z"):
                decrypted_text += chr(ord("z") - (ord(i) - shift - ord("a")) - 1)
            else:
                decrypted_text += chr(ord(i) - shift)
    return decrypted_text

def caesar(test, shift, encrypt_or_decrypt):
    return_text = ""
    for i in text:
        if i.isalpha():
            if encrypt_or_decrypt.lower() == "decrypt":
                return_text += decrypt(i,shift=shift)
            else:
                return_text += encrypt(i,shift=shift)
        else:
            return_text += i
    return return_text

if __name__ == "__main__":
    print("""
                                            _       _               
                                   (_)     | |              
  ___ __ _  ___  ___  __ _ _ __ ___ _ _ __ | |__   ___ _ __ 
 / __/ _` |/ _ \/ __|/ _` | '__/ __| | '_ \| '_ \ / _ \ '__|
| (_| (_| |  __/\__ \ (_| | | | (__| | |_) | | | |  __/ |   
 \___\__,_|\___||___/\__,_|_|  \___|_| .__/|_| |_|\___|_|   
                                     | |                    
                                     |_|     
        """)
    print("Welcome tp CAESAR CIPHER!")
    while True:
        encrypt_or_decrypt = input("What to you like to do Encrypt or Decrypt? ")
        text = input(f"Please enter your text to be {encrypt_or_decrypt}\n")
        shift = int(input("Please type the shift number: "))
        print(f"The {encrypt_or_decrypt.capitalize()} text is {caesar(text,shift,encrypt_or_decrypt)}")
        continue_or_not = input("Would to like to continue to encrypt or decrypt or would you like to exit? Type 'yes' to continue and 'no' to exit: ")
        if continue_or_not.lower() == "no":
            print("Goodbye. Thank you for using CAESAR CIPHER. Please visit again!!")
            break