nombre_admin = "Nother"
password_admin = "root"

username = input("Ingrese el nombre de usuario: ").strip()
password = input("Ingrese su contraseña: ").strip()

if nombre_admin.lower() == username.lower() and password_admin == password:
    print('Bienvenido usuario al sistema')
else:
    print("Lo sentimos, datos ingresados erróneos")