print("Samuel Grijalva 1205")
import datetime
#Zona de clase
class Inventario1205:
    ID_Orden1205=0
    ID_Cliente1205=0
    Fecha_Orden1205=datetime.date
    Total1205=0.0
    Estado1205=""
    Metodo_Pago1205=""
    Comentarios1205=""
    #zona de funciones
    def mostrar_datos1205(self):
        print("")

    def Listar_Productos1205(self):
        lista1205=["Cappuccino","Espresso","Americano","Mocca","Latte","Doppio","Flat White"]
        for x in lista1205:
            print(x)
        print()
    
    def Tupla_Ordenes1205(self):
        tupla1205=("No.123","No.434","No.2464","No.234","No.644","No.22","No.7117")
        for y in tupla1205:
            print(y)
        print()

    def Diccionario_Productos_Precio1205(self):
        diccionario1205={
            "Americano:": 90,
            "Black:": 70,
            "Mocca:": 60,
            "Espresso:": 80,
            "Normal:": 68,
            "Doppio:":79,
            "White:":10
        }
        for dick, di in diccionario1205.items():
            print(dick,di)
        print()

    def altas1205(self):
        print("La operación se realizo correctamente para los datos de la Orden")
        print()

    def bajas1205(self):
        print("La operación se realizo correctamente para los datos de la Orden")
        print()

#zona de objetos
Sammy1205=Inventario1205()

#zona de uso de objetos
Sammy1205.mostrar_datos1205()
print("Lista de Productos")
Sammy1205.Listar_Productos1205()
print("Tupla de Ordenes")
Sammy1205.Tupla_Ordenes1205()
print("Diccionario de Productos y Precios")
Sammy1205.Diccionario_Productos_Precio1205()
Sammy1205.altas1205()
Sammy1205.bajas1205()