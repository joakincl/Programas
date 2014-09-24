print ("Valor de a?")
a = input()
print ("Valor de b?")
b = input()
def mayor(a,b):
    if a > b:
        print  a, "es mayor que", b
    elif a == b:
        print "Los numeros son iguales"
    else:
        print b, "es mayor que", a

mayor(a,b)
