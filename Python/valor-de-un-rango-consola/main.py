from random import randint

valor_descubrir = randint(0,20)
intentos = 5
descubierto = False
while intentos > 0 and descubierto == False:
    valor_asignado = int(input("Ingrese un valor entre 1 y 20: "))
    if valor_asignado == valor_descubrir:
        descubierto = True
        print(f'''
                ----------------------------
                Felicidades, has adivinado el numero, quedantote {intentos} intentos
              ''')
    elif valor_asignado != valor_descubrir:
        intentos -= 1
        if valor_asignado > valor_descubrir and intentos > 0:
            print(f'''
                    ----------------
                    lo sentimos el numero que ingresaste es mayor al que fue asignado
                    te quedan {intentos} intentos
                  ''')
        elif valor_asignado < valor_descubrir and intentos > 0:
            print(f'''
                    ----------------
                    lo sentimos el numero que ingresaste es menor al que fue asignado
                    te quedan {intentos} intentos
                  ''')
        elif intentos == 0:
            print(f'''
                    ----------------
                    lo sentimos te quedaste sin intentos, el numero es {valor_descubrir}
                    buena suerte para la proxima
                  ''')
        
