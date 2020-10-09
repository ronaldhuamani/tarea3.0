def costoydescuento():
    #datos de entrada
    costo =float(input("ingrese el precio: "))
    #proceso
    if costo > 0:

        total=costo*200
    if 200<=costo:
            total = total*0.15
    elif 100<costo <200:
            total = total*0.12
    elif 100>costo:
            total = total*0.10
    #datos de salida
    print("el total a pagar es: " , format(total))
costoydescuento()    