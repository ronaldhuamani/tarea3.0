def lugardevacaciones():
    #datos de entrada
    viaje=str(input("lugar que visitara el cliente de vacaciones: "))
    mexico=int(input("750: "))
    acapulco=int(input("1200: "))
    cancun=int(input("1800: "))
    #proceso
    if viaje=="mexico":
        costo=750
    if viaje=="acapulco":
        costo=1200
    if viaje=="acapulco":
        costo=1800
    #datos de salida
    print("elcriente deseara por este viaje: " , costo)
lugardevacaciones()