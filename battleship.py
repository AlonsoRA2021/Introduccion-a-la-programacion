import random

while True:
    def menu ():
        print ("1. Inicializar Juego")
        print ("2. Impimir  barcos")
        print ("3. Jugar")
        print ("3. Salir del juego")
    menu ()
    opc = input("Ingrese una opcion del menu: ")

    if opc == '1':
        def inicializarBarcosComputadora():
            l= [0]*15
            l=l+[1,2,3,4,5]
            random.shuffle(l)
            return (l)
        barco = inicializarBarcosComputadora()        
        
        def inializarBarcosJugador():
            l=[0]*20
            for i in range(1,6):
                posic=int(input("Deme una posicion para el barco número "+str(i)+": "))
                l[posic-1]=i
            return l
        barco2 = inializarBarcosJugador()
        print ("POSICIONES CREADAS")
        
    elif opc == '2':
        print ("Posicion de barcos de la computadora: ")
        print (barco)
        print ("Posicion de barcos del Jugador: ")
        print(barco2)

    elif opc == '3':
        
        def hacerDisparo(barco):
            contadorJugador = 0
            contadorCPU = 0
            for i in range(10):
                posicionjugador = int(input("JUGADOR intento "+str(i+1)+ ": Ingresa la posicion (de 1 a 20) a donde quieres disparar: "))
                if (barco[posicionjugador] != 0):
                    contadorJugador += 1
                    print ("DERRIBADO! BARCO: ", barco[posicionjugador], "Puntaje: ", contadorJugador)
                    barco[posicionjugador] = 0
                    if (contadorJugador >= 5):
                        print ("GANASTE! Has derribados todos los 5 barcos :D\nFin del juego...\n------------")
                        return
                else:
                    print ("TE EQUIVOCASTE! ", "Puntaje: ", contadorJugador-1)

            print ("----------------------------\nTurno de COMPUTADOR=>")
            for i in range(10):
                print ("COMPUTADOR intento "+str(i+1))
                posicionCPU = random.randint(0,19)
                if (barco[posicionCPU] != 0):
                    contadorCPU += 1
                    print ("DERRIBADO! BARCO: ", barco[posicionCPU], "Puntaje", contadorCPU)
                    barco[posicionCPU] = 0
                    if (contadorCPU >= 5):
                        print ("GANASTE! Has derribados todos sus 5 barcos :D\nFin del juego...\n------------")
                        return
                else:
                    print ("TE EQUIVOCASTE! ", "Puntaje: ", contadorCPU-1)

            print ("**************************************\nRESULTADOS DEL JUEGO:")
            print ("Barcos derribados de JUGADOR: ", contadorCPU)
            print ("Puntaje total JUGADOR", contadorJugador)
            print ("-------------------------------------")
            print ("Barcos derribados de COMPUTADOR: ", contadorJugador)
            print ("Puntaje total COMPUTADOR", contadorCPU)
            print ("-------------------------------------")
            if (contadorJugador > contadorCPU):
                print ("Felicidades JUGADOR has ganado!")
                print ("**************************************")
            elif (contadorJugador < contadorCPU):
                print ("COMPUTADOR ha ganado el juego")
                print ("**************************************")
            else:
                print ("JUEGO EMPATADO!")
                print ("**************************************")

        hacerDisparo(barco)

    elif opc == '4':
        print("bais")
        break


            
           
            
        











