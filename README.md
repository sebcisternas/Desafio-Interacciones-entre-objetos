# Desafío - Interacciones entre objetos

En este desafío, hemos desarrollado una aplicación de consola en Python 3.8 que simula la gestión de tiendas, productos y ventas. El objetivo principal del proyecto es aplicar los conceptos de **abstracción**, **encapsulamiento**, **colaboración** y **composición** en el diseño y la implementación de la arquitectura de clases.

## Archivos Principales

- **producto.py:** En este archivo se define la clase `Producto`, que representa un producto en el sistema. Esta clase utiliza **encapsulamiento** para garantizar el acceso controlado a los atributos de los productos, como nombre, precio y stock. Además, el método setter de `stock` se encarga de validar y actualizar el stock de un producto.

- **tienda.py:** Aquí se definen las clases que representan los diferentes tipos de tienda: `Tienda`, `Restaurante`, `Supermercado` y `Farmacia`. Estas clases utilizan **abstracción** y **encapsulamiento** para modelar las características y comportamientos específicos de cada tipo de tienda. También se implementan métodos para agregar productos, listar productos y realizar ventas, utilizando **composición** y **colaboración** entre objetos.

- **programa.py:** Este archivo contiene la lógica principal del programa. Aquí se interactúa con el usuario para crear tiendas, agregar productos, listar productos existentes, realizar ventas y salir del programa. Se solicita al usuario ingresar productos hasta que decida finalizar, y luego se presentan las opciones de acción disponibles.

Este proyecto proporciona una base para la gestión de tiendas en Python, utilizando las mejores prácticas de programación orientada a objetos. Los conceptos de abstracción, encapsulamiento, colaboración y composición son fundamentales para garantizar un diseño robusto y modular del sistema.