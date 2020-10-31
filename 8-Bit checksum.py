"""
8-Bit checksum calculator(dodgy code)
"""
# Just bashed my way through this one, but hey it works!

# chrBin = format((ord(totalSum)),"b") # Format(,'b') turns ascii num into binary
# cool function ^^

# INPUT
message = input("Message: ")
totalSum = 0

# PROCCESSING
for x in message:  
    totalSum = totalSum + ord(x)

# flip bits as a string
sumBinary = bin(totalSum).replace("b","")

# restrict totalSum length or add more "0"
if len(sumBinary) > 8:
    rev = sumBinary[::-1]
    clipped = "%.8s" % rev
    normal = clipped[::-1]
    
elif len(sumBinary) < 8:
    amount = 8 - len(sumBinary)
    normal = sumBinary + ("0" * amount)
    
flipBinary = normal.replace("1","U").replace("0","1").replace("U","0")

# OUTPUT
print("Sum:", normal, hex(int(normal,2)).replace("0x",'').upper())
print("Flipped:", flipBinary, hex(int(flipBinary,2)).replace("0x","").upper())
print("Checksum:",hex(int(flipBinary,2)+1).replace("0x","").upper())
