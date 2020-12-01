"""
Collatz Sequence Program

If number is even, then collatz() prints number // 2 and returns that value.
If number is odd, then collatz() prints return 3 * number + 1.
Keeps calling collatz() on that number until the function returns the value 1.
"""


#pseudocode
# FUNCTION
# def Collatz(NUM):
#   IF NUM is EVEN:
#       print number // 2
#       returns number // 2
#   ELIF NUM is ODD:
#       print 3 * NUM + 1
#       return 3 * NUM + 1
#
# INPUT
# try:
#   N = INT(INPUT(Enter Number:))
# except:
#   print(Type a number!)
#
# PROCESSING
# WHILE N != 1:
#   N = Collatz(N)
#END

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1

while True:
    try:
        n = int(input("Enter Number: "))
        while n != 1:
            n = collatz(n)
    except:
        print("Not an integer!")


