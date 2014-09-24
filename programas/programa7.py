c= 'var'
def nombres(c):
    c = raw_input("Cadena a revisar?")
    d = len(c)
    if c.isalnum() == False:
        print "El nombre de usuario puede contener solo letras y numeros"
    else:
        if d < 6:
            print ("El nombre de usuario debe contener al menos 6 caracteres")
        elif d > 12:
            print("El nombre de usuario no puede contener mas de 12 caracteres")
        else:
            print ("El nombre de usuario es valido")

(nombres(c))

