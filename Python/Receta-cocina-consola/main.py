nombre_plato = input("Ingrese nombre del plato: ").strip().capitalize()
ingredientes = input("Ingrese los ingredientes: ").strip().capitalize()
tiempo_preparacion = int(input("Ingrese tiempo de preparcion (en minutos). "))
dificultad = input("Ingrese la dificultad: ")

print(f'''
      ---------------------
      EL nombre de la receta es {nombre_plato}
      con los ingredientes de {ingredientes}
      con el tiempo de preparacion de {tiempo_preparacion}
      con la dificultad de {dificultad}
      ''')