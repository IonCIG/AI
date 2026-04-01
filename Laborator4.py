# import functools
# lis=[1,10,4,5,9]
# print (functools.reduce(lambda a,b:a+b,lis))
# def fibonaci(n):
#     if n<=1:
#         return n
#     else:
#         return fibonaci(n-1)+fibonaci(n-2)

# print(fibonaci(1))
##EX1
# alegere1=input("alege piatra hartie sau foarfeca(jucator 1): ")
# alegere2=input("alege piatra hartie sau foarfeca(jucator 2): ")
# if alegere1 == alegere2:
#     print('Egalitate')
# elif (alegere1 == "hartie" and alegere2 == "piatra") or (alegere1 == "piatra" and alegere2 == "foarfeca") or (alegere1 == "foarfeca" and alegere2 == "hartie"):
#     print('primul jucator a castigat')
# else:
#     print('al doilea jucator a castigat')

##EX2
def genereaza_factura(**kwargs):
    for nume, [nrprod, pret] in kwargs.items():
        print("%s,%s,%s" % (nrprod, nume, pret))

genereaza_factura(ION=[2,10], PAUL=[3,15], Andrei=[1,20])
        





