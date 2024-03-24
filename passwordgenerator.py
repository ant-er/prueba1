import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
passlength = int(input("Cuantos caracteres quieres que tenga la contraseña?:"))
password = ""
for i in range(passlength):
    password += random.choice(passlength)
print(password)
