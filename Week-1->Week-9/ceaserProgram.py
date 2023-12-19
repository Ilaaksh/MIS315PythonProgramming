import string
import random

encPass = ""

def id_generator(size=6, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

def encrypt(password):
    global encPass
    for char in password:
        if char in alpha:
            idx = alpha.index(char)
            encPass = encPass + delta[idx]

alpha = string.ascii_lowercase
gamma = []
delta = []
shift = int(input("Select a shift number: [between 1 - 26]")) - 1
#password = id_generator()
password = "pizza"


print ("Username: KingofCats@dog.com")
# now generate password
print(password)

print(type(alpha))
print(alpha)
#print(alpha[shift])

for idx, c in enumerate(alpha):
    if idx >= shift:
        gamma.append(c)
        #print(idx, c)
        #print(gamma)
#print("Gamma is: ", gamma)

if shift == 0:
    delta = gamma
else:
    for idx, c in enumerate(alpha):
        if idx < shift:
            delta = gamma
            delta.append(c)
print("Delta is: ", delta)


encrypt(password)


print(encPass)

#beta =

