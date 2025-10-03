char=input()
#c1
print("Cách 1")
if char.isupper():
    print(char.lower())
else:
    print(char.upper())

#c2
print('Cách 2')
if char<'a':
    x=ord(char)+32
    print(chr(x))
else:
    x=ord(char)-32
    print(chr(x))

