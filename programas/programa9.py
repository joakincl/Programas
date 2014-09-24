z = raw_input("Path del archivo a revisar?")
infile = open(z, 'r')
print('>>> Lectura del fichero linea a linea:')
for line in infile:
#    print(line)
#    print len(line)
#    print line.find("@")
#    print line.find(".")
#    print line.endswith(".")
    cuenta = 0
    for i in line:
        if (i == '@' or i == '.'):
            cuenta += 1
#    print cuenta
    if cuenta == 2:
        if (line.find("@") > 1 and line.find(".") > line.find("@")+1):
             r=line[line.find("@")+1:line.find(".")]
             m=line[line.find(".")+1:len(line)-1]
             if ((r.isalpha() == 1) and (m.isalpha() == 1)):
                 (line.replace("\n",'')+" Cadena correcta")
             else:
                 print (line.replace("\n",'')+" no es un correo valido")
        else:
            print (line.replace("\n",'')+" no es un correo valido")
    else:
        print (line.replace("\n",'')+" no es un correo valido")
infile.close()
























#    archi=open('/home/joakin/correos.txt','r')
#    lineas=archi.readlines()
#    print lineas
#    archi.close()


#leertxtenlista()

#!/usr/bin/python

# Abrimos el archivo codehero.txt
#fo = open("/home/joakin/correos.txt", "r")
#print "Nombre del archivo : ", fo.name
#print "Cerrado o no : ", fo.closed
#print "Modo de apertura : ", fo.mode
#fo.close()
#print "Cerrado o no : ", fo.closed