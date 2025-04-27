nombre_producto = input("Ingresa el nombre del producto: ")
precio_producto = float(input("Ingresa el precio del producto: "))
cantidad_inventario = int(input("Ingresa la cantidad en el inventario: "))
disponibilidad = False

total_pagar = precio_producto * cantidad_inventario if disponibilidad else 0

print('---------------------')
print("Usted ha comprado", nombre_producto)
print("Por el precio individual de", precio_producto)
print("Y la cantidad de ", cantidad_inventario)
print("Total a pagar", total_pagar) if total_pagar > 0 else print("Productos no disponibles")