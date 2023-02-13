def cambiar(
    g:dict
) -> dict:
    """
    -Esta función sirve para modificar la informacion de un usuario-
    
    PARAMETROS:
    x: Es una variable de tipo input que le pregunta al usuario si su elección es la que
       desea ejecutar.
    if x == "si": Es el condicional que dependiendo de la respuesta del usuario va a ejecutar 
        el resto del programa (Pedir información y modificarla en el diccionario)
        ant: es una variable que pregunta a que usuario desea modificar.
        nom:lib = En este caso "nom" y "lib" equivalen a la información añadida (lo nuevo)
        g.pop(): elimina la información vieja
        g.update(): se usa para añadir la información que se desea cambiar (nombre y libro)  
    else: si la respuesta del usuario en "x" es diferente a "si", el else se ejecuta para repetir el ciclo
    """
    x = str(input("Desea modificar un usuario? (si/no) "))
    x = x.lower()
    if x == "si":
         ant = str(input("Nombre de usuario por cambiar:"))
         ant = ant.lower()
         nom = str(input("Nombre de usuario nuevo: "))
         nom = nom.lower()
         lib = str(input("Añadir libro del nuevo usuario: "))
         lib = lib.lower()
         g.pop(ant)
         g.update({nom:lib})
    else:
         print("No se desea cambiar ningun usuario")
print("-"*40)