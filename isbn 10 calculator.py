"""
10 Digit ISBN checkbit Calculator
"""

# pseudocode
# INPUT
#   isbn : 10 digits
# PROCESSING
#   multiplier = 10
#   FOR x in isbn
#       sum += (x * multiplier)
#       multiplier -= 1
#   sum = sum mod 11
#   checkbit = 11 - mod
#   IF checkbit is 10, than use Roman numberal "X"
# OUTPUT
#   checkbit


# INPUT
print("10 Digit ISBN checkbit Calculator")
isbn = input("ISBN (With checkbit as 0): ")

# PROCESSING
multiplier = 10
sum = 0
for x in isbn:
    sum = sum + (int(x) * multiplier)
    """
    # Show working out
    print(f"{x} * {multiplier}: {int(x) * multiplier}")
    print("sum is: ", sum)
    """
    multiplier = multiplier - 1

mod = sum%11
checkbit = 11 - mod

if checkbit > 9:
    checkbit = "X" #Roman numeral for 10

# OUTPUT
print(f"ISBN of {isbn} has checkbit of {checkbit}")
