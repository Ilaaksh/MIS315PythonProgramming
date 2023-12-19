import time

password = "" #set the password first
password = "pizza"

print ("Username: KingofCats@dog.com")
passEntry = input("Password: ")

time.sleep(0.5)
print ("... checking ...")
time.sleep(0.5) 
print (" ")
time.sleep(1)

wordlist = ["secret", "cinnabun", "pizza", "password"]
# for loop to check user entered password against the "list"
for word in wordlist:
    passEntry = input("Password: ")
    if passEntry == word:
        print("You're Logged In")
    else:
        continue

        #print("Incorrect Password!!")


