from random import randint

nombre = input("Ingrese el nombre: ").upper()[0:2]
apellido = input("Ingrese el apellido: ").upper()[0:2]
anio_nacimiento = input("Ingrese el año de nacimiento: ")[2:4]
valor_aletorio = randint(0000,9999)

print(F'El id generado es : {nombre}{apellido}{anio_nacimiento}{valor_aletorio}')