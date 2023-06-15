import random2
let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sym = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_sum =int(input("How many elements would you like in your password?\n"))
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
if nr_sum-(nr_letters+nr_symbols+nr_numbers)==0:


    pass_list = []

    for char in range(0, nr_letters + 1):
        pass_list.append(random2.choice(let))
    for char in range(0, nr_numbers + 1):
        pass_list.append(random2.choice(num))
    for char in range(0, nr_symbols + 1):
        pass_list.append(random2.choice(sym))

    # random2.shuffle(pass_list)
    # random2/random.shuffle listdeki elementlerin yerini random olaraq deyisir

    password = ""
    for i in pass_list:
        password += i
    print(password)

#password =" "

#for i in range(0, nr_letters+1):
#    password+=random2.choice(let)
#for i in range(0, nr_numbers+1):
 #   password+=random2.choice(num)
#for i in range(0, nr_symbols+1):
 #   password+=random2.choice(sym)

#print(password)
else:
    print("Please, choose correct numbers")
