import os, random, string, pyperclip 

f = open('pwd.txt', 'w')

length = 13
chars = string.ascii_letters + string.digits
random.seed = (os.urandom(1024))

pwd =  ''.join(random.choice(chars) for i in range(length))
pyperclip.copy(pwd)
f.write(pwd)
f.close()





