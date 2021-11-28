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
    
        
        
        def inializarBarcosJugador():
            l=[0]*20
            for i in range(1,6):
                posic=int(input("Deme una posicion para el barco con num: "+str(i)))
                l[posic]=i
            return l
        print ("POSICIONES CREADAS")
        

    elif opc == '2':
        print ("Posicion de barcos de la computadora: ")
        print (inicializarBarcosComputadora())
        print ("Posicion de barcos del Jugador: ")
        print(inializarBarcosJugador())
    #elif opc == '3':
        #posicionjugador =int(input("JUGADOR: Ingresa la posicion (de 1 a 20) a donde quieres disparar: "))
        #for i in range(len (inicializarBarcosComputadora())):

            #if posicionjugador in inicializarBarcosComputadora():
                #inicializarBarcosComputadora[i] = 0
        #print (inicializarBarcosComputadora())
    

    #PRUEBA
    elif opc == '3':
        print ("CUSTODIAR" ,inicializarBarcosComputadora())
        def hacerDisparo(inicializarBarcosComputadora):

            print ("CUSTODIAR" ,inicializarBarcosComputadora())
            posicionjugador =int(input("JUGADOR: Ingresa la posicion (de 1 a 20) a donde quieres disparar: "))
            for i in range(len (inicializarBarcosComputadora())):
                if posicionjugador in inicializarBarcosComputadora():
                   inicializarBarcosComputadora()[i] = 0
                   print ("TOMELA" ,inicializarBarcosComputadora()) 
                else:
                    print("MAMASTE")
            print ("CUSTODIAR" ,inicializarBarcosComputadora())

        hacerDisparo(inicializarBarcosComputadora)
        break    
    elif opc == '4':
        print("bais")
        break



       


            
           
            
        











