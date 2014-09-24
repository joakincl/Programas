m=0
f=0
def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

def ejecucion(m):
    m = int(input("Cuantos elementos fibonancci quieres? "))
    if m <= 0:
        print("No es valido")
    else:
        print("Secuencia Fibonancci:")
        for i in range(1,m+1):
#            print i
            print(fibo(i))
ejecucion(m)
while True:
    f = raw_input("Quieres volver a calcular la serie de fibonacci? SI para continuar y FIN para terminar?")
    if f == 'FIN':
        print ("Esto es el fin")
        break
    elif f == 'SI':
        print (ejecucion(m))
    else :
        print("Opcion no valida, ")
