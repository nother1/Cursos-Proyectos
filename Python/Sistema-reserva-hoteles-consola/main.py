nombre_cliente = input("Ingrese nombre del cliente: ")
dias_estancia = int(input("Ingrese cuantos dias de estancia estara: "))
tarifa_diaria = int(input("Cual es la tarifa diara de la habitacion: "))
vista_al_mar_input = input("Tiene vista al mar? (si/no): ").strip().lower()
print("------------------------------")
vista_al_mar = vista_al_mar_input in ['si','sí','s']
total_pagar = dias_estancia * tarifa_diaria + 500 if vista_al_mar else dias_estancia * tarifa_diaria

print('Cliente', nombre_cliente)
print('Dias de estancia', dias_estancia)
print('Tarifa Diaria', tarifa_diaria)
print('Tiene Vista al mar', vista_al_mar)
print('Valor total a pagar', total_pagar)