def calcularedadmenor():
    #datos de entrada
    juan = float(input("ingrese el primer edad: "))
    nelson = float(input("ingrese el segundo edad: "))
    pedro = float(input("ingrese el tercer edad: "))
    #proceso
    juan < nelson , juan < pedro
    nelson < juan, nelson < pedro
    pedro < juan , pedro < nelson
    if nelson > juan < pedro:
        print("la edad menor es el primer nombre: " , juan)
    elif juan > nelson < pedro:
        print("la edad menor es el segundo nombre: " , nelson)
    elif juan > pedro < nelson:
        print("la edad menor es el tercer nombre: " , pedro)
         #datos de salida
    print("el nombre  de la persona menor es: " ,)
calcularedadmenor()