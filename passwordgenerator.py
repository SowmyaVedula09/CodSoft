import string
import random
str1=list(string.ascii_uppercase)
str2=list(string.ascii_lowercase)
str3=list(string.digits)
str4=list(string.punctuation)
inp=input('Max Password Length:')
while True:
    try:
        charno=int(inp)
        if charno < 8:
            print('The minimum password length should be 8')
            inp=input('Retype the Passwrd Length again:')
        else:
            break
    except: 
        print('Enter the Password Length in numbers only')
        inp=input('Enter max Password Length:')
    
random.shuffle(str1)
random.shuffle(str2)
random.shuffle(str3)
random.shuffle(str4)

p1=round(charno * (30/100))
p2=round(charno * (20/100))
res = []
for i in range(p1):
    res.append(str1[i])
    res.append(str2[i])

for i in range(p2):
    res.append(str3[i])
    res.append(str4[i])

random.shuffle(res)
password = "".join(res)
print('The Generated Password: ', password)