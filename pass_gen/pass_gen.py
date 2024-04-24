import random

def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

upper1= chr(random.randint(65,90))
upper2= chr(random.randint(65,90))
lower1= chr(random.randint(97,122))
lower2= chr(random.randint(97,122))

password = upper1 + lower1 + upper2 +lower2
password = shuffle(password)

print(password)