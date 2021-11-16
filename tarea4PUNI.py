print ("BIENVENIDO AL MENU DE COMPAÑIA NACIONAL DE FUERZA Y LUZ")
def menu():
     print("1. Calcular el mes con mas consumo ")
     print("2. Calcular la eco factura del mes ")
     print("3. Salir")
menu()
opc = input("Elija una opcion: ")

while opc !=3:

    if opc == '1':
        def mesmayorconsumo():
            print("Ingrese el nombre de los ultimos seis meses y su consumo: ")   
            mes1 = input("Ingrese mes 1: ")
            consumo1 =input("Ingrese consumo: ")
            mes2 = input("Ingrese mes 2 : ")
            consumo2 =input("Ingrese consumo: ")
            mes3 = input("Ingrese mes 3 : ")
            consumo3 =input("Ingrese consumo: ")
            mes4 = input("Ingrese mes 4 : ")
            consumo4 =input("Ingrese consumo: ")
            mes5= input("Ingrese mes 5 : ")
            consumo5 =input("Ingrese consumo: ")
            mes6 = input("Ingrese mes 6 : ")
            consumo6 =input("Ingrese consumo: ")
            if consumo1 > consumo2 and consumo1 > consumo3 and consumo1 > consumo4 and consumo1 > consumo5 and consumo1 > consumo6:
                print("El mes de mayor consumo es:",mes1)
                return
            elif consumo2 > consumo1 and consumo2 > consumo3 and consumo2 > consumo4 and consumo2 > consumo5 and consumo2 > consumo6:
                print("El mes de mayor consumo es:",mes2)
                return 
            elif consumo3 > consumo1 and consumo3 > consumo2 and consumo3 > consumo4 and consumo3 > consumo5 and consumo3 > consumo6:
                print("El mes de mayor consumo es:",mes3)
                return 
            elif consumo4 > consumo1 and consumo4 > consumo2 and consumo4 > consumo3 and consumo4 > consumo5 and consumo4 > consumo6:
                print("El mes de mayor consumo es:",mes4)
                return
            elif consumo5 > consumo1 and consumo5 > consumo2 and consumo5 > consumo3 and consumo5 > consumo4 and consumo5 > consumo6:
                print("El mes de mayor consumo es:",mes5)
                return 
            elif consumo6 > consumo1 and consumo6 > consumo2 and consumo6 > consumo3 and consumo6 > consumo4 and consumo5 > consumo6:
                print("El mes de mayor consumo es:",mes6)
                return 
            else:
                print("Los meses ingresados tienen la misma cantidad de consumo")
                return 
        mesmayorconsumo()

    if opc =='2':
        def montoenergia(totalkwhpunta,totalkwhvalle,totalkwhnoct):
            
            if valorkwhpunta <= 500:
                totalpunta = totalkwhpunta * 167.72
            else:
                totalpunta = totalkwhpunta * 207.39
                return
            if valorkwhvalle <= 500:
                totalvalle = totalkwhvalle *68.75
            else:
                totalvalle = totalkwhvalle * 83.71
                return
            if valorkwhnoct <= 500:
                totalnoct = totalkwhnoct *28.77
            else:
                totalnoct = totalkwhnoct * 38.74
                return
            tot = totalpunta + totalvalle + totalnoct
            return tot
        nombremes = input("Nombre del mes a calcular factura: ")
        valorkwhpunta = int(input("Ingrese el total consumido en horario punta: "))
        valorkwhvalle = int(input("Ingrese el total consumido en horario valle: "))
        valorkwhnoct = int(input("Ingrese el total consumido en horario nocturno: "))
        totalconsumido = valorkwhpunta + valorkwhvalle + valorkwhnoct
        
        def montoalumbradopublico(totalconsumidokwh):
            totalalumbrado = totalconsumidokwh * 3.37
            return totalalumbrado

        def montotributobomberos (totalconsumidokwh):
            imp = totalconsumidokwh * 1.75 / 100
            return imp

        def montoIva (totalconsumidokwh,montofacturaenergia):
            if totalconsumidokwh >= 280:
                iva = montofacturaenergia * 13 / 100
                return iva

        def imprimirEcofactura(nombremes,valorkwhpunta,valorkwhvalle,valorkwhnoct):
            print("***************************************************")
            print("* La eco-factura del mes de" ,nombremes ,"es:")
            print("*")
            print("* Total de KWH consumidos: " ,totalconsumido)
            print("* Monto correspondiente a Energía: " ,montoenergia(valorkwhpunta,valorkwhvalle,valorkwhnoct))
            print("* Monto correspondiente a alumbrado público: " ,montoalumbradopublico(totalconsumido))
            print("* Monto correspondiente al tributo a bomberos: " ,montotributobomberos(totalconsumido))
            print("* Monto correspondiente al IVA: " ,montoIva(totalconsumido,montoenergia(valorkwhpunta,valorkwhvalle,valorkwhnoct)))
            print("* Monto total a pagar por su factura: " ,montoenergia(valorkwhpunta,valorkwhvalle,valorkwhnoct)+montoalumbradopublico(totalconsumido)+montotributobomberos(totalconsumido)+montoIva(totalconsumido,montoenergia(valorkwhpunta,valorkwhvalle,valorkwhnoct)))
            print("*")
            print("*\tMUCHAS GRACIAS CNFL")
            print("***************************************************")
        imprimirEcofactura(nombremes,valorkwhpunta,valorkwhvalle,valorkwhnoct)
