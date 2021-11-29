def menu ():
    print ("1. Inicializar Juego")
    print ("2. Impimir  barcos")
    print ("3. Jugar")
    print ("3. Salir del juego")
menu ()


while True:
    opc = input("Ingrese una opcion del menu: ")
    if opc == '1':
        def inicializarBarcosComputadora():
            import random
            l= [0]*15
            l=l+[1,2,3,4,5]
            random.shuffle(l)
            return (l)
        barco = inicializarBarcosComputadora()
    
        
        
        def inializarBarcosJugador():
            l=[0]*20
            for i in range(1,6):
                posic=int(input("Deme una posicion para el barco número "+str(i)+": "))
                l[posic]=i
            return l
        barco2 = inializarBarcosJugador()
        print ("POSICIONES CREADAS")
        

    elif opc == '2':
        print ("Posicion de barcos de la computadora: ")
        print (barco)
        print ("Posicion de barcos del Jugador: ")
        print(barco2)
    #elif opc == '3':
        #posicionjugador =int(input("JUGADOR: Ingresa la posicion (de 1 a 20) a donde quieres disparar: "))
        #for i in range(len (inicializarBarcosComputadora())):

            #if posicionjugador in inicializarBarcosComputadora():
                #inicializarBarcosComputadora[i] = 0
        #print (inicializarBarcosComputadora())
    

    #PRUEBA
    elif opc == '3':
        
        def hacerDisparo(barco):

            posicionjugador = int(input("JUGADOR: Ingresa la posicion (de 1 a 20) a donde quieres disparar: "))
            for i in range(len (barco)):
                if posicionjugador in barco:
                   barco[i] = 0
                   return print ("TOMELA" ,barco) 
                else:
                    return print("MAMASTE")

        hacerDisparo(barco)

    elif opc == '4':
        print("bais")
        



       


            
           
            
        











