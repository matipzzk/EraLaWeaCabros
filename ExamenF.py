import random,csv,time,os

sueldos = random.randint(300000,2500000)
trabajadores=["Juan perez Sueldo:",sueldos,"Maria Garcia Sueldo:",sueldos,"Carloz Lopez Sueldo:",sueldos,"Ana Martinez",sueldos,"Pedro Rodriguez Sueldo:",sueldos,"Laura Hernandez Sueldo:",sueldos,"Miguel Sanchez Sueldo:",sueldos,"Isabel Gomez Sueldo: ",sueldos,"Francisco Diaz Sueldo:",sueldos,"Elena Fernandez",sueldos]

def opc1():
   print(trabajadores)



def opc2():
               print(f"""
            Sueldo Menores a 800.000 Total:
            Nombre empleado: Sueldo


            Sueldos entre $800.000 y 2.500.000$

             
            Nombre Empleado Sueldo:
             

            Sueldos Superiores a $2.000.000 
                  Total Sueldos
            """)

def opc3():
        print("Ver Estadistica")
        print("Sueldo Mas Alto")
        print("Sueldo Mas Bajo")
        print("Promedio de sueldos")
        print("Media geometrica")


def opc4():
        



        print("Reporte de sueldo")
        for x in trabajadores:
             print(f"Nombre Empleado: {[]} Sueldo Base Descuento afp Sueldo liquido")




def opc5():
        print("Finalizando Programa")
        print("Desarrolado por Matias Imil")
        print("Rut 21.836.200-1")
        exit()