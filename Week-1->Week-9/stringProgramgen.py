import string
import random

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def id_generator2(size=6, chars=string.printable):
    return ''.join(random.choice(chars) for _ in range(size))


print(string.printable) #full set of ascii printable characters
print("  ")
print(string.ascii_uppercase) #set of ascii uppercase letters
print("  ")
print(string.digits) #set of ascii numbers
print("  ")
print(string.punctuation) #set of ascii printable punctuation symbols
print()
print(id_generator()) #see function above,
print("  ")
print(id_generator(3, "6793YUIO"))
print("  ")
print(id_generator2(5, string.printable))
print("  ")
#print(id_generator2(5, string.digits))


exit()
