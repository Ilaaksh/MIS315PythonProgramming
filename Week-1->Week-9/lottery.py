import random
import math

num1 = random.randint(1,30)

num2 = random.randint(1,30)
if num2 == num1:
    num2 = random.randint(1,30)
    #continue

num3 = random.randint(1,30)
if num3 == num2 or num3 == num1:
    num3 = random.randint(1,30)
    # create while loop to check num1 and 2

num4 = random.randint(1,30)
if num4 == num3 or num4 == num2 or num4 == num1:
    num4 = random.randint(1,30)


num5 = random.randint(1,30)
if num5 == num4 or num5 == num3 or num5 == num2 or num5 == num1:
    num5 = random.randint(1,30)

print("Random option #1")
print(num1, num2, num3, num4, num5)
# combination 142,506

print()
print("-------------------------")
print("Random option #2 - while loop")

while (num2 == num1):
    num2 = random.randint(1,30)

print()
print("-------------------------")
print("Combination code")
#n = number of items
#k = number selected
n = 30
k = 5
print(math.comb(n, k))


print("Random - Array option")
num1 = random.randint(1,30)
num2 = random.randint(1,30)
num3 = random.randint(1,30)
num4 = random.randint(1,30)
num5 = random.randint(1,30)
numArray = [num1, num2, num3, num4, num5]
print(numArray)

lotArray = []
i = 0

while i < 5:
    inlist = False
    randomNum = random.randint(1,30)
    if randomNum in lotArray:
        inlist = True
    if inlist == False:
        lotArray.append(randomNum)
        i+=1
