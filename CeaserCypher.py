newList = []
myString = input("String: ")
CIPHERKEY = int(input("Key: "))

for x in myString:
    newList.append(ord(x) + CIPHERKEY)

myString = ""
for x in newList:
    myString += chr(x)

print(f"New Message: {myString}")
