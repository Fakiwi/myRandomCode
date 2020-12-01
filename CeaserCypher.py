newList = []
myString = input("String: ")
CIPHERKEY = int(input("Key: "))

# Create list of character ascii values and shift by cipher key value
for x in myString:
    newList.append(ord(x) + CIPHERKEY)

# Create new string from list of ciphered values.
myString = ""
for x in newList:
    myString += chr(x)

print(f"New Message: {myString}")
