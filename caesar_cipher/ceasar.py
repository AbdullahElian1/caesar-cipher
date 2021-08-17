import random
import re
from caesar_cipher.is_englesh import count_words

# chars = ['0'...'9']


def encrypt(plain, key):
    plain = re.sub(r'[^A-Za-z]+','_', plain)
    print(plain)
    

    encrypted_text = ""


    for char in plain:
        
        if char =="_":
            encrypted_text += " "
            continue
        num=ord(char)
        if char.islower():
            shifted_num = (num + key -97) % 26 +97
        else:
            shifted_num = (num + key -65) % 26 +65
        
        encrypted_text += f"{str(chr(shifted_num))}"
        

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
       
        if percentage > 50:
            result= (to_check, i)
    
    if result:
        return result
    
        

    



# if __name__ == "__main__":
#     pins = [
#         "anas check"
#     ]

#     # for pin in pins:
#     #     key = 15
#     #     print("plain pin", pin)
#     #     encrypted_pin = encrypt(pin, key)
#     #     print("encrypted_pin", encrypted_pin)
#         # decrypted_pin = decrypt(encrypted_pin, key)
#         # print("decrypted_pin", decrypted_pin)
#     x=encrypt("Good Dog be animial test ",23)
#     y=crack(x)
    
#     print(f"the encription message was {x}") 
#     print(y)
