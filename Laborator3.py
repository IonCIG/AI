#Exercitiul5
import random
print('Bine ai venit la loteria Python''\n''Alege 6 numere intre 1 si 49')
x =random.sample(range(1,49), 6)
print(x)
n1 = int(input("Numarul 1: "))
n2 = int(input("Numarul 2: "))
n3 = int(input("Numarul 3: "))
n4 = int(input("Numarul 4: "))
n5 = int(input("Numarul 5: "))
n6 = int(input("Numarul 6: "))
y=[n1,n2,n3,n4,n5,n6]
z = []
ct=0
for i in x:
    for j in y:
        if(i==j):
            z.append(i)
            ct=ct+1

print(f'Numerele castigatoare sunt:{x}')
if(ct>0 and ct<=3):
    print(f'Ai nimerit {ct} numere. Acestea sunt:{z}''\n''Ai castigat un premiu mic')
elif(ct>3 and ct<=5):
    print(f'Ai nimerit {ct} numere. Acestea sunt:{z}''\n''Ai castigat un premiu destul de mare')
else:
    print(f'Ai nimerit {ct} numere. Acestea sunt:{z}''\n''AI CASTIGAT MARELE PREMIU!!!!!!')


