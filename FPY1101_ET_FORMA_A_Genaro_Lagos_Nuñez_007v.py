productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}
#menu principal
def menu():

    print("***MENU PRINCIPAL***")
    print("1. Stock Marca")
    print("2. Búsqueda por precio")
    print("3. Actualizar precio")
    print("4. Salir")

#funcion stock marca
def stock_marca(marca):
    stock_total=0
    encontrado=False

    for id, datos in productos.items():
        if id in stock and marca.lower() == datos[0].lower():
            stock_total+=stock[id][1]
            encontrado=True
            
    if not encontrado:
        print(f"No se han encontrado productos para la marca {marca}")
    else:
         print(f"El stock para {marca} es: {stock_total} ") #se imprime el stock para cada marca

def busqueda_precio(p_min, p_max):
    encontrado=False

    for id, datos in productos.items():
        if id in stock and stock[id][1] >0:
            precio=stock[id][0]
            if p_min <=precio <=p_max:
                print(f" Marca: {datos[0]} -- Modelo: {id}")
                encontrado=True
    if not encontrado:
        print("No hay Notebooks en este rango de precios.")

#funcion actualizar precio segun modelo
def actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0]=p
        return True
    else:
        return False
    
#función principal
def main():
    while True:
        menu()
        op=input("Ingrese una opcion 1/2/3/4: ")

        if op == "1":
            marca=input("Ingrese una marca para buscar productos asociados: ").strip().lower()
            stock_marca(marca)
    
        elif op == "2":
            while True:
                try:
                    p_min=int(input("Ingrese el precio minimo para su búsqueda: "))
                    p_max=int(input("ingrese el precio máximo para su búsqueda: "))
                    if p_min >=p_max:
                        print("el precio máximo debe ser mayor que el mínimo")
                        continue
                    else:
                        busqueda_precio(p_min, p_max)
                        break
                except ValueError:
                    print("Debe ingresar valores enteros!!")
        elif op == "3":
            while True:
                modelo=input("Ingrese el modelo del producto que desea actualizar: ").upper().strip()
                try:
                    p=int(input("Ingrese el nuevo precio a actualizar: "))

                    if actualizar_precio(modelo, p):
                        print("Precio actualizado!!")
                    else:
                        print("El modelo no existe!!")
                except ValueError:
                    print("Ingrese un numero entero")
                
                continuar=input("¿Desea actualizar otro producto? si / no: ")
                if continuar == "si":
                    continue
                else:
                    break

        elif op == "4":
            print("Programa finalizado.")
            break
        else:
            print("Debe ingresar una opción válida 1/2/3/4")

main()

#LINK EXAMEN PYTHON GITHUB: https://github.com/GenaLagos10/examen_duoc