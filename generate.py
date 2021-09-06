digits = '0123456789'
chars = 'abcdefghijklmn' + \
        'opqrstuvwxyz'
up = chars.upper()
special = '_!$%&?ù'
all = digits+chars+up+special
from random import choice

password = ''.join (
    choice(all) for i in range(10)
)

f = open('ascii.txt', 'r')
file_contents = f.read()


print("\x1b[1;32m                    ")
print (file_contents)
f.close()
print("\033[0;31m")
print(password)
print("\033[0;37;40m")
