import random,csv,time,os
from ExamenF import*

trabajadores=["Juan perez Sueldo:",sueldos,"Maria Garcia Sueldo:",sueldos,"Carloz Lopez Sueldo:",sueldos,"Ana Martinez",sueldos,"Pedro Rodriguez Sueldo:",sueldos,"Laura Hernandez Sueldo:",sueldos,"Miguel Sanchez Sueldo:",sueldos,"Isabel Gomez Sueldo: ",sueldos,"Francisco Diaz Sueldo:",sueldos,"Elena Fernandez",sueldos]









while True:
    print("Menu")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadistica")
    print("4. Reporte de sueldos")
    print("5. Salir")
    opc = int(input("Ingrese opcion: "))
    if opc ==1:
        opc1()
    elif opc ==2:
        opc2()
    elif opc ==3:
         opc3()
    elif opc ==4:
        opc4()
    else:
        opc5()

