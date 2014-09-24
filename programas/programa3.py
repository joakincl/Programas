print ("Valor de x?")
x = input()
y = 1
def factorial(x, y):
    while x >= 1:
        y = y * x
        x = x - 1
    return y
print "El factorial de", x,"es", factorial(x,y)


