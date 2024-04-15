#importing random and string modules
import random

import string


#create function for generate password
def generate_password(length):


    #combining aplhabets (lower and upper),number and special characters
    characters=string.ascii_letters+string.digits+string.punctuation


    #randomly selecting k number of characters 
    password=''.join(random.choices(characters,k=length))
    return password


#prompt the user for length    
length=int(input("enter length of your choice:")) 
password=generate_password(length)


#Display the password
print(f"generated password is:{password}")