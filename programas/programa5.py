c = 'cadena'
def invertir(c):
    c = raw_input("Cadena a revisar?")
    z = c[::-1]
    d=c.replace(" ","");
    e=z.replace(" ","");
    if d == e :
        return "Esta palabra es palindrome pues alreves se escribe asi", z, "y se puede leer de ambas maneras."
    else:
        return "Esta palabra no es palindrome pues alreves se escribe asi", z
print invertir(c)
f = raw_input("Quieres volver a analizar una palabra SI/FIN?")
#while f.strip() != 0:
while True:
    if f == 'FIN':
        print("Esto es el fin")
        break
    elif f == 'SI':
        print (invertir(c))
    f = raw_input("Quieres volver a analizar una palabra SI/FIN?")

