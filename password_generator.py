import random

num = [1,2,3,4,5,6,7,8,9,0]
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","å","ä","ö"]
cap_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","Å","Ä","Ö"]
symbols = ["!","#","¤","%","&","/","(",")","=","+","?","@","£","$","€","{","[","]","}","^","*","'","-","_",";",":","<",">"]
password = []
pword = ""
inn =  int(input("Length of password:\n"))

nummer = int(input("Minimum number of numbers:\n"))

sym = int(input("Minimum number of symbols:\n"))

for i in range(nummer):
  choice = random.choice(num)
  password.append(choice)


for n in range(sym):
  choice = random.choice(symbols)
  password.append(choice)

if inn < (nummer + sym):
  inn = (nummer + sym)

inn = inn - (nummer + sym) 

for k in range(inn):
   outt = random.choices([1,2,3,4])
   if outt == [1]:
     choice = random.choice(letters)
     password.append(choice)
   elif outt == [2]: 
     choice = random.choice(cap_letters)
     password.append(choice)
   elif outt == [3]:
     choice = random.choice(symbols)
     password.append(choice)
   elif outt == [4]:
     choice = random.choice(num)
     password.append(choice)


random.shuffle(password) 

for p in (password):
  pword += str(p)


print(pword)