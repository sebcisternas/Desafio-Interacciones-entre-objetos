from tienda import Tienda

def crear_tienda():
    print("Seleccione el tipo de tienda:")
    print("1. Restaurante")
    print("2. Supermercado")
    print("3. Farmacia")
    tipo_tienda = input("Ingrese el número correspondiente al tipo de tienda: ")

    if tipo_tienda == "1":
        tipo = "Restaurante"
    elif tipo_tienda == "2":
        tipo = "Supermercado"
    elif tipo_tienda == "3":
        tipo = "Farmacia"
    else:
        print("Opción inválida. Intente nuevamente.")
        return crear_tienda()

    nombre = input("Ingrese el nombre de la tienda: ")
    costo_delivery = int(input("Ingrese el costo de delivery: "))

    tienda = Tienda(nombre, costo_delivery, tipo)
    
    print("\n\n----------INGRESO DE PRODUCTOS-----------")
    continuar = 's'
    while continuar == 's':   
        tienda.agregar_producto()   
        continuar = input("¿Desea ingresar otro producto? (s/n): ")     
    return tienda

def main():
    tienda = crear_tienda()

    while True:
        print("\nSeleccione una opción:")
        print("1. Listar productos existentes")
        print("2. Realizar venta")
        print("3. Salir")

        opcion = input("Ingrese el número correspondiente a la opción: ")

       
        if opcion == "1":
            print("Productos existentes en la tienda:")
            print(tienda.listar_productos())
        elif opcion == "2":
            nombre_producto = input("Ingrese el nombre del producto a vender: ")
            cantidad = int(input("Ingrese la cantidad a vender: "))
            tienda.realizar_venta(nombre_producto, cantidad)
            
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()