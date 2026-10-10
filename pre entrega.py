"""Catálogo de Papota. Datos en memoria: [nombre, categoría, precio]."""

productos = []

while True:
    print("\n" + "=" * 60)
    print('Supermercado y Distribuidora de Alimentos "Papota"')
    print("Sistema de gestión de productos")
    print("=" * 60)
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Seleccionar producto")
    print("5. Eliminar producto")
    print("6. Salir")

    opcion = input("Elegí una opción (1-6): ").strip()

    # 1. AGREGAR PRODUCTO
    if opcion == "1":
        print("\n--- Agregar producto ---")

        nombre = input("Nombre: ").strip()
        while nombre == "":
            print("Error: el nombre no puede estar vacío.")
            nombre = input("Nombre: ").strip()

        categoria = input("Categoría: ").strip()
        while categoria == "":
            print("Error: la categoría no puede estar vacía.")
            categoria = input("Categoría: ").strip()

        while True:
            precio_str = input(
                "Precio en ARS (sin centavos): "
            ).strip()

            if not precio_str.isascii() or not precio_str.isdigit():
                print("Error: ingresá un número entero positivo.")
                continue

            try:
                precio = int(precio_str)
            except ValueError:
                print("Error: el número es demasiado largo.")
                continue

            if precio <= 0:
                print("Error: el precio debe ser mayor que cero.")
                continue

            break

        productos.append([nombre, categoria, precio])
        print(f"Producto '{nombre}' agregado correctamente.")

    # 2. MOSTRAR PRODUCTOS
    elif opcion == "2":
        print("\n--- Lista de productos ---")

        if len(productos) == 0:
            print("Todavía no hay productos cargados.")
        else:
            for i in range(len(productos)):
                print(
                    f"\nNúmero: {i + 1}\n"
                    f"Nombre: {productos[i][0]}\n"
                    f"Categoría: {productos[i][1]}\n"
                    f"Precio: ARS {productos[i][2]}"
                )

    # 3. BUSCAR POR NOMBRE O CATEGORÍA
    elif opcion == "3":
        print("\n--- Buscar producto ---")

        if len(productos) == 0:
            print("Todavía no hay productos cargados.")
        else:
            busqueda = input(
                "Ingresá el nombre o categoría: "
            ).strip().lower()

            while busqueda == "":
                print("Error: el campo no puede estar vacío.")
                busqueda = input(
                    "Ingresá el nombre o categoría: "
                ).strip().lower()

            encontrados = []

            for i in range(len(productos)):
                nombre = productos[i][0].lower()
                categoria = productos[i][1].lower()

                if busqueda in nombre or busqueda in categoria:
                    encontrados.append(i)

            if len(encontrados) == 0:
                print("No se encontraron productos.")
            else:
                print("\nResultados de la búsqueda:")

                for posicion in encontrados:
                    print(
                        f"\nNúmero: {posicion + 1}\n"
                        f"Nombre: {productos[posicion][0]}\n"
                        f"Categoría: {productos[posicion][1]}\n"
                        f"Precio: ARS {productos[posicion][2]}"
                    )

                print(f"\nTotal encontrados: {len(encontrados)}")

    # 4. SELECCIONAR PRODUCTO
    elif opcion == "4":
        print("\n--- Seleccionar producto ---")

        if len(productos) == 0:
            print("No hay productos para seleccionar.")
        else:
            for i in range(len(productos)):
                print(
                    f"{i + 1}. {productos[i][0]} - "
                    f"{productos[i][1]} - "
                    f"ARS {productos[i][2]}"
                )

            while True:
                seleccion = input(
                    "Ingresá el número del producto: "
                ).strip()

                if not seleccion.isascii() or not seleccion.isdigit():
                    print("Error: ingresá un número entero.")
                    continue

                try:
                    numero = int(seleccion)
                except ValueError:
                    print("Error: el número es demasiado largo.")
                    continue

                if numero < 1 or numero > len(productos):
                    print(
                        f"Error: elegí un número entre "
                        f"1 y {len(productos)}."
                    )
                    continue

                break

            producto = productos[numero - 1]

            print("\nProducto seleccionado:")
            print(f"Nombre: {producto[0]}")
            print(f"Categoría: {producto[1]}")
            print(f"Precio: ARS {producto[2]}")

    # 5. ELIMINAR PRODUCTO
    elif opcion == "5":
        print("\n--- Eliminar producto ---")

        if len(productos) == 0:
            print("No hay productos para eliminar.")
        else:
            for i in range(len(productos)):
                print(
                    f"{i + 1}. {productos[i][0]} - "
                    f"{productos[i][1]} - "
                    f"ARS {productos[i][2]}"
                )

            while True:
                entrada = input(
                    "Número del producto a eliminar: "
                ).strip()

                if not entrada.isascii() or not entrada.isdigit():
                    print("Error: ingresá un número entero.")
                    continue

                try:
                    numero = int(entrada)
                except ValueError:
                    print("Error: el número es demasiado largo.")
                    continue

                if numero < 1 or numero > len(productos):
                    print(
                        f"Error: elegí un número entre "
                        f"1 y {len(productos)}."
                    )
                    continue

                break

            eliminado = productos.pop(numero - 1)
            print(f"Se eliminó el producto '{eliminado[0]}'.")

    # 6. SALIR
    elif opcion == "6":
        print("¡Gracias por elegir Papota!")
        break

    else:
        print("Opción no válida. Elegí un número del 1 al 6.")