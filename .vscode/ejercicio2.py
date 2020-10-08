def sueldosemanal():
    #datos de entrada
    tipopago=str(input("ingrese el sueldo que recibira el cliente: "))
    A=int(input("resibira sueldo normal:"))
    B=int(input("resibira sueldo doble:"))
    #proceso

    if tipopago=="sueldo":
        costopagado=40
    else:
        costopagado=40*2
    if A==A:
        costopagado=costopagado
    if B==B:
        costopagado=costopagado+(costopagado*2)

    #datos de salida
    print("el tipo de pago es:" , costopagado)
sueldosemanal()
