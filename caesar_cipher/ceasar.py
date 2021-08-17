import random
import re
from caesar_cipher.is_englesh import count_words

# chars = ['0'...'9']


def encrypt(plain, key):
    plain = re.sub(r'[^A-Za-z]+','', plain)
    

    encrypted_text = ""


    for char in plain:
        
        num=ord(char)
        # print(ord("z"))
        if char.islower():
            shifted_num = (num + key -97) % 26 +97
        else:
            shifted_num = (num + key -65) % 26 +65
        
        encrypted_text += f"{str(chr(shifted_num))}"
        # print(encrypted_text)
    encrypted_text = re.sub(r'[T]+',' ', encrypted_text)

    # print(encrypted_text)
        

    return encrypted_text


def decrypt(encoded, key):
    return encrypt(encoded, -key)



def crack(text):

    count=count_words(text)
    result=""
    
    for i in range(1,27):
        to_check=decrypt(text,i)
        count=count_words(to_check)
        percentage = int(count / len(text.split()) * 100)
        # print(percentage)
        if percentage > 50:
            result= (to_check, i)
    
    if result:
        return f"after decode the message will be {result[0]} and the key was {result[1]}"
    else:
        return "orginal message doesn't has meaningfull words"
        

    



if __name__ == "__main__":
    pins = [
        "anas check"
    ]

    # for pin in pins:
    #     key = 15
    #     print("plain pin", pin)
    #     encrypted_pin = encrypt(pin, key)
    #     print("encrypted_pin", encrypted_pin)
        # decrypted_pin = decrypt(encrypted_pin, key)
        # print("decrypted_pin", decrypted_pin)
    x=encrypt("True",16)
    y=crack(x)
    
    print(f"the encription message was {x}") 
    print(y)
