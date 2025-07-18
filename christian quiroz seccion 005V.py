#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video], ...]

productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

#stock = {modelo: [precio, stock], ...]

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}


# opcion 1
def stock_marca(marca):
    marca = marca.lower()
    total_stock=0
    for modelo , datos in productos.items():
        if datos [0].lower() == marca:
            total_stock += stock[modelo][1]
    print(f"Stok total de productos {marca.capitalize()}: {total_stock}")


#opcion 2
def busqueda_precio(p_min,p_max):
    productos_encontrados=[]
    for modelo, (precio,stock) in productos.items():
        if stock >0 and p_min <=precio <=p_max:
            modelo=productos(modelo)[0]
            productos_encontrados.append(f"{producto} -- {modelo}")
    if productos_encontrados:
        productos_encontrados.sort()
        print("produtos encontrados: ")
        for producto in productos_encontrados:
            print(producto)
    else:
        print("No hay prodcutos con el rango de precios") 



#opcion 3
def actualizar_precio( ):
    while True:
        modelo = input("Ingrese modelo a actualizar:").upper()
        if modelo in stock:
            try:
                nuevo_precio = int(input("Ingrese el nuevo precio"))
                stock[modelo][0] = nuevo_precio
                print("Precio actualizado")
            except ValueError:
                print("¡¡Debe ingresar valores enteros!!")
        else:
            print("No hay notebooks en ese rango de precios.")
        seguir = input("desea actualizar otro precio? (si/no): ").lower()
        if seguir != "si":
            break

def menu_pybooks():
    while True:
        print("\n *** Bienvenido a Pybooks")
        print("1. Stock Marca")
        print("2. Busqueda por precio")
        print("3. Actualizar precio")
        print("4. Salir")

        opc = input("Ingrese la opción que desea: ")

        if opc == "1":
            marca=input("Ingrese la marca que desea consultar: ")
            stock_marca(marca)
        elif opc == "2":
            busqueda_precio()
            p_min=int(input("Ingrese el precio minimo"))
            p_max=int(input("Ingrese el precio maximo"))
        elif opc == "3":
            actualizar_precio()

        elif opc == "4":
            print("Programa finalizado.")
            break
        else:
            print("opción inválida")
menu_pybooks()







