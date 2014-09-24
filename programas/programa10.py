#!/usr/bin/python
dir = []
nombre = 'var'
telefono= 'var'
correo = 'var'
def directorio(nombre, telefono, correo):
    global dir
    nombre = raw_input("Nombre?")
    telefono = raw_input("Telefono?")
    correo = raw_input("Correo?")
    dir.append([nombre,telefono,correo])
    c = raw_input("Deseas agregar mas Contactos SI/NO?")
    if c == 'SI':
        directorio(nombre, telefono, correo)
    else:
        d = raw_input("En que formato deseas guardar el archivo como XML o CVS?")
        if d == 'CVS':
            grabar = open('/tmp/dir.cvs', 'a')
            grabar.write('Nombre,telefono,correo'+'\n')
            grabar.close()
            for i in range (len(dir)):
                t=","
                grabar = open('/tmp/dir.cvs', 'a')
                grabar.write(t.join(dir[i]))
                grabar.write('\n')
                grabar.close()
        else:
            grabar = open('/tmp/dir.xml', 'a')
            grabar.write('<?xml version="1.0" encoding="iso-8859-1"?>'+'\n')
            grabar.write('<agenda>')
            grabar.write('\n')
            grabar.close()
            for i in range (len(dir)):
                grabar = open('/tmp/dir.xml', 'a')
                grabar.write('\t\t'+'<contacto>'+'\n')
                grabar.write('\t\t\t'+'<nombre>'+dir[i][0]+'</nombre>'+'\n')
                grabar.write('\t\t\t'+'<correo>'+dir[i][2]+'</correo>'+'\n')
                grabar.write('\t\t\t'+'<telefono>'+dir[i][1]+'</telefono>'+'\n')
                grabar.write('\t\t'+'</contacto>'+'\n')
                grabar = open('/tmp/dir.xml', 'a')
                grabar.close()
            grabar = open('/tmp/dir.xml', 'a')
            grabar.write('</agenda>')
            grabar.close()



directorio(nombre, telefono, correo)
