import random
def devPass(c):
    password = []
    length = 0
    if c == 1:
        length = 6
    if c == 2:
        length = 5
    if c == 3:
        length = 4
    for x in range(length):
        password.append(random.randint(0,9))
    return password
print ("Welcome to Password Generator")
print ("How secure would you like your password to be?")
print ("1:Highly Secure")
print ("2:Moderately Secure")
print ("3:Simple")
choice = int(input(""))
final = ""
passcode = devPass(choice)
for a in passcode:
    final += str(a)
print (final)
#print ("Your password is %d") % devPass(choice)
