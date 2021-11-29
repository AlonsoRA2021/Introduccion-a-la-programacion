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
            puntajeJugador = 0
            puntajeCPU = 0
            for i in range(10):
                posicionjugador = int(input("JUGADOR intento "+str(i+1)+ ": Ingresa la posicion (de 1 a 20) a donde quieres disparar: "))
                if (barco[posicionjugador] != 0):
                    contadorJugador += 1
                    puntajeJugador+=contadorJugador
                    print ("DERRIBADO! BARCO: ", barco[posicionjugador], "Puntaje: ", contadorJugador)
                    barco[posicionjugador] = 0
                else:
                    print ("TE EQUIVOCASTE! ", "Puntaje: ", contadorJugador-1)
            if (contadorJugador >=5):
                print ("HAS DERRIBADO TODOS LOS BARCOS!")

            for i in range(10):
                posicionCPU = random.randint(0,19)
                if (barco[posicionCPU] != 0):
                    print ("DERRIBADO! BARCO: ", barco[posicionCPU], "Puntaje", contadorCPU)
                    contadorCPU += 1
                    puntajeCPU+=contadorCPU
                    barco[posicionCPU] = 0
                else:
                    print ("TE EQUIVOCASTE! ", "Puntaje: ", contadorCPU-1)
            return contadorJugador, contadorCPU, puntajeJugador, puntajeCPU
        hacerDisparo(barco)

        def imprimirGanador():
            print ("Barcos derribados de JUGADOR: ", hacerDisparo(barco))
            print ("Puntaje total JUGADOR", puntajeJugador)
            print ("-------------------------------------")
            print ("Barcos derribados de COMPUTADOR: ", contadorCPU)
            print ("Puntaje total COMPUTADOR", puntajeCPU)
            print ("-------------------------------------")
            if (contadorJugador > contadorCPU):
                print ("Felicidades JUGADOR has ganado!")
            elif (contadorJugador < contadorCPU):
                print ("COMPUTADOR ha ganado el juego")
            else:
                print ("JUEGO EMPATADO!")
        imprimirGanador()
    elif opc == '4':
        print("bais")


            
           
            
        











