from producto import Producto

class Tienda():
    #constructor para la clase tienda con las variables solicitadas y encapsulamiento
    def __init__(self,nombre: str, costo_delivery: int,tipo: str):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []
        self.__tipo = tipo
    
        
    @property     
    def nombre(self):
        return self.__nombre
    
    @property
    def costo_delivery(self):
        return self.__costo_delivery
    
    def agregar_producto(self):
        
        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock del producto: "))
        
        if self.__tipo == "Restaurante":
            # para los restaurantes, el stock siempre debe ser 0
            stock = 0

        producto = Producto(nombre, precio, stock)
        
        for p in self.__productos:
            if p.nombre == producto.nombre:
                # si el producto ya existe, sumamos el stock
                p.stock += producto.stock
                print("Producto ya existente, se ha actualizado el stock.")
                return
        
        # Si el producto no existe, lo añadimos a la lista de productos
        self.__productos.append(producto)
        print("Producto ingresado exitosamente.")  
        
        
    def listar_productos(self):
        lista_productos = "Productos existentes en la tienda:\n"
        # si la tienda es de tipo Restaurante itera sobre los productos de la tienda solo listando sin especificaciones como supermercad oy farmacia
        if self.__tipo == "Restaurante":
            for producto in self.__productos:
                lista_productos += f"Nombre: {producto.nombre}, Precio: {producto.precio}\n"
        else:
            for producto in self.__productos:
                lista_productos += f"Nombre: {producto.nombre}, Precio: {producto.precio}"
                 #si la tienda es de tipo "Supermercado" y el stock del producto es menor a 10 agrega un mensaje indicando que hay pocos productos disponibles
                if self.__tipo == "Supermercado":
                    if producto.stock < 10:
                        lista_productos += " - Pocos productos disponibles"
                #si la tienda es de tipo "Farmacia" y el precio del producto es mayor a 15000 agrega un mensaje indicando que hay envío gratis al solicitar el producto
                elif self.__tipo == "Farmacia":
                    if producto.precio > 15000:
                        lista_productos += " - Envío gratis al solicitar este producto"
                lista_productos += "\n" #solo salto de linea
        return lista_productos
    
    def realizar_venta(self, nombre_producto: str, cantidad: int):
        print("Realizando venta...")  
        if self.__tipo == "Restaurante":
            print("Venta realizada exitosamente.")
            return
        for producto in self.__productos:
            if producto.nombre == nombre_producto:
                if self.__tipo == "Farmacia" and cantidad > 3:
                    # no se puede vender más de 3 unidades en Farmacia
                    print("No se puede vender más de 3 unidades en Farmacia.")
                    return
                if cantidad <= producto.stock:
                    #se puede vender la cantidad solicitada si es que hay stock
                    producto.stock -= cantidad
                    print("Venta realizada exitosamente.")  
                    return
                else:
                    # no hay suficiente stock para la venta
                    print("No hay suficiente stock para la venta.")
                    return
        #si el producto no está en la lista de productos de la tienda
        print("El producto solicitado no está disponible en la tienda.")