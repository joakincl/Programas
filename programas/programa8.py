#!/usr/bin/env python
# -*- coding: utf-8 -*-
z = 'var'
def passw(z):
    z = raw_input("Contraseña a revisar?")
    d = len(z)
    print d
    if d < 8:
        print "La Cadena deve contar con un minimo de 8 caracteres"
        passw(z)
    elif d > 7:
        a = []
        b = []
        c = []
        d = []
        for letra in z:
            if (letra.islower() == 1):
                a.append(letra)
            elif(letra.isupper() == 1):
                b.append(letra)
            elif(letra.isdigit() == 1):
                c.append(letra)
            elif(letra.isspace() == 1):
                print("La contraseña no puede incluir espacios en blanco")
                passw(z)
            else:
                d.append(letra)
        if ((len(a)) > 0 and (len(b)) > 0 and (len(c)) > 0 and (len(d)) > 0):
            print "La contraseña es segura"
#            return 1
        else:
            print "La contraseña debe incluir Mayusculas,Minusculas,Numeros y al menos un caracter no alfanumerico"
            passw(z)

passw(z)
