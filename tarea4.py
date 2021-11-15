
print ("BIENVENIDO AL MENU DE COMPAÑIA NACIONAL DE FUERZA Y LUZ")
def menu():
     print("1. Calcular el mes con mas consumo ")
     print("2. Calcular la eco factura del mes ")
     print("3. Salir")
menu()
opc = input("Elija una opcion: ")


while opc !=3:

    if opc == '1':
      
      def mesmayorconsumo(consumo1,consumo2,consumo3,consumo4,consumo5,consumo6):
          if consumo1 > consumo2 and consumo1 > consumo3 and consumo1 > consumo4 and consumo1 > consumo5 and consumo1 > consumo6:
             print("El mes de mayor consumo es: ",mes1)
             return
          elif consumo2 > consumo1 and consumo2 > consumo3 and consumo2 > consumo4 and consumo2 > consumo5 and consumo2 > consumo6:
               print("El mes de mayor consumo es: ",mes2)
               return 
          elif consumo3 > consumo1 and consumo3 > consumo2 and consumo3 > consumo4 and consumo3 > consumo5 and consumo3 > consumo6:
               print("El mes de mayor consumo es: ",mes3)
               return 
          elif consumo4 > consumo1 and consumo4 > consumo2 and consumo4 > consumo3 and consumo4 > consumo5 and consumo4 > consumo6:
               print("El mes de mayor consumo es: ",mes4)
               return
          elif consumo5 > consumo1 and consumo5 > consumo2 and consumo5 > consumo3 and consumo5 > consumo4 and consumo5 > consumo6:
               print("El mes de mayor consumo es: ",mes5)
               return 
          elif consumo6 > consumo1 and consumo6 > consumo2 and consumo6 > consumo3 and consumo6 > consumo4 and consumo5 > consumo6:
               print("El mes de mayor consumo es: ",mes6)
               return 
          else:
               print("Los meses ingresados tienen la misma cantidad de consumo")
               return 

      print("Ingrese el nombre de los ultimos seis meses y su consumo: ")   
      mes1 = input("Ingrese mes 1: ")
      consumo1 =input("Ingrese consumo: ")
      mes2 = input("Ingrese mes 2: ")
      consumo2 =input("Ingrese consumo: ")
      mes3 = input("Ingrese mes 3: ")
      consumo3 =input("Ingrese consumo: ")
      mes4 = input("Ingrese mes 4: ")
      consumo4 =input("Ingrese consumo: ")
      mes5= input("Ingrese mes 5: ")
      consumo5 =input("Ingrese consumo: ")
      mes6 = input("Ingrese mes 6: ")
      consumo6 =input("Ingrese consumo: ")
      

      resultado = mesmayorconsumo(consumo1,consumo2,consumo3,consumo4,consumo5,consumo6)
                  
      resultado
    if opc =='2':
        def montoenergia(totalkwhpunto,totalkwhvalle,totalkwhnoct):
            
            if totalkwhpunto <=500:
                totalpunto = totalkwhpunto * 167.72
            else:
                totalpunto = totalkwhpunto * 207.39
                return
            if totalkwhvalle <= 500:
                totalvalle = totalkwhvalle *68.75
            else:
                totalvalle = totalkwhvalle * 83.71
                return
            if totalkwhnoct <= 500:
                totalnoct = totalkwhnoct *28.77
            else:
                totalnoct = totalkwhnoct * 38.74
                return
        nombremes = input("Ingrese el mes de la factura: ")
        totalkwhpunto = input("Ingrese el total consumido en horario punta: ")
        totalkwhvalle = input("Ingrese el total consumido en horario valle: ")
        totalkwhnoct = input("Ingrese el total consumido en horario nocturno: ")
        totalfacturadoenergia = totalkwhpunto + totalkwhvalle + totalkwhnoct
        totalconsumido = totalkwhpunto + totalkwhvalle + totalkwhnoct
        def montoalumbradopublico(totalconsumido):
            totalconsumido *= 3.37
        def montotributobomberos (totalconsumido):
            totalconsumido *= 1.75
        def montoIva (totalconsumido,totalfacturadoenergia):
            if totalfacturadoenergia >=280:
                totalconsumido * 0.13
        def imprimirEcofactura(nombremes,totalconsumido):
            print("Mes facturado: ",nombremes)
            print("total de KWH: " ,totalconsumido)
            print("monto correspondiente a energia: " ,totalfacturadoenergia)
            print("monto correspondiente a alumbrado publico: " ,montoalumbradopublico)
            print("monto correspondiente a tributo a bomberos: " ,montotributobomberos)
            print("monto correspondiente al IVA: " ,montoIva)
            print("monto total a pagar en la factura: " ,totalconsumido)

        mostrar = imprimirEcofactura(nombremes,totalconsumido)
        mostrar

