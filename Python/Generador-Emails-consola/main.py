nombre = input('Ingrese su nombre: ').lower().strip().replace(' ','.')
empresa = input ("Ingrese el nombre de la empresa: ").lower().strip().replace(' ','.')
dominio = "com.co"
print(f'''
      ------------------------------
      Nombre ingresado {nombre}
      empresa ingresada {empresa}
      Correo asiganado {nombre}@{empresa}.{dominio}
      ''')