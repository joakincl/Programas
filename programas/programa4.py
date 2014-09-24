c = raw_input("Cadena a revisar?")
def invertir(c):
    return c[::-1]
z=invertir(c)
d=c.replace(" ","");
e=z.replace(" ","");
if d == e :
    print "Esta palabra es palindrome pues alreves se escribe asi", z, "y se puede leer de ambas maneras."
else:
    print "Esta palabra no es palindrome pues alreves se escribe asi", z
