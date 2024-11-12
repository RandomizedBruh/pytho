import random 

password = ""

# sym_1 = ord("F")

pass_len = int(input("Сколько символов в пароле?: "))



for i in range(pass_len):
    sym = chr(random.randint(65, 90))
    password = password + sym 
password += "_"
for i in range(pass_len):
    sym = chr(random.randint(48, 57))
    password = password + sym 
password += "_" 
for i in range(pass_len):
    sym = chr(random.randint(97, 122))
    password = password + sym 



print(password)

