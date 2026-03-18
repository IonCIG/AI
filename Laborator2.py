#print(type(1))
#print(10-3)
#print(10//3)
#print(round(10.567))
#print(pow(8,6))
#age=input("enter your age: ")
#age=int(age)
#print(type('hello'))
#print('hey you'[4])
#name='ionut'
#print(name[1])
#print(name[::-1])
#print('ionut'+'comanescu')
#print('ionut'*10)
#print(len('turtle'))
#print('i am alone'.strip())
#nume1 ='paul'
#nume2 ='ion'
#print(f'buna noi suntem {nume1} si {nume2}')
#print(bool(0))
#print(bool(3))
#lista=[2,2,4,'i',True]
#print(lista.count(2))
#print(lista[:1])
#dictionar = {'nume': 'ionut','age':21, 'inalt': False}
#print(dictionar['nume'])
#print(list(dictionar.keys()))
#tupla=('mar','para','banana')
#print(tupla[1])
#myset=set()
#myset.add(3)
#print(myset)
#mylist=[1,2,2,2,2,5,5,5,3,3,2,2,1,1,8,8,6,6]
#print(set(mylist))
# Ex1
picture = [
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]]
for i in picture:
    for j in i:
        if j == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
# Ex2
nota=input("intorduceti nota: ")
nota=int(nota)
if (nota>=9 and nota<11):
    print('Excelent')
elif (nota<9 and nota>=7):
    print('bine')
elif (nota<7 and nota>=5):
    print('suficient')
elif (nota<5 and nota>=0):
    print('reexaminare')
else:
    print('introdu o valoare valida')


# Ex3
import random

x = random.randint(1, 50)
ct = 1
print(x)
y = int(input("introduceti numarul: "))

if x == y:
    print('ai ghicit numarul din prima')
else:
    while y != x:
        if y < x:
            print('numarul este mai mare')
        else:
            print('numarul este mai mic')

        y = int(input("introduceti numarul: "))
        ct += 1

    print(f'ai ghicit numarul din {ct} incercari')

# Ex4
orase=['sibiu','bucuresti','bacau','timisoara','apoldu','cluj napoca']
lista=enumerate(orase, start=1)
for i, val in lista:
    print(i,".", val)




