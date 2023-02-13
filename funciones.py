def añadir(
    dicc:dict
) -> dict:
    """
    -Esta función sirve para añadir un usuario-
    
    PARAMETROS:
    x: Es una variable de tipo input que le pregunta al usuario si su elección es la que
       desea ejecutar.
    if x == "si": Es el condicional que dependiendo de la respuesta del usuario va a ejecutar 
        el resto del programa (Pedir información y añadirla al diccionario)
        nom:lib= son dos variables de tipo input, la variable "nom" agrega el nombre del nuevo usuario
        la variable "lib" añade el libro del mismo (Estas variables luego son añadidas al diccionario) 
    else: si la respuesta del usuario en "x" es diferente a "si", el else se ejecuta para repetir el ciclo
    """
    x = str(input("Desea añadir un usuario? (si/no) "))
    x = x.lower()
    if x == "si":
         nom = str(input("Añadir usuario: "))
         nom = nom.lower()
         lib = str(input("Añadir libro del nuevo usuario: "))
         lib = lib.lower()
         dicc.update({nom:lib})
    else:
         print("No se desea añadir ningun usuario")
print("-"*40)
def eliminar(
    dicc:dict
) -> dict:
    """
    -Esta función sirve para eliminar un usuario-
    
    PARAMETROS:
    x: Es una variable de tipo input que le pregunta al usuario si su elección es la que
       desea ejecutar.
    if x == "si": Es el condicional que dependiendo de la respuesta del usuario va a ejecutar 
        el resto del programa (Pedir información y eliminarnla del diccionario)
        nom: es una variable tipo input que pregunta el usuario que desea ser eliminado
        del dicc[nom]: se usa el metodo "del" para eliminar el usuario seleccionado.    
    else: si la respuesta del usuario en "x" es diferente a "si", el else se ejecuta para repetir el ciclo
    """
    x = str(input("Desea eliminar un usuario? (si/no) "))
    x = x.lower()
    if x == "si":
         nom = str(input("Que usuario desea eliminar: "))
         nom = nom.lower()
         del dicc[nom]
         
    else:
         print("No se desea eliminar ningun usuario")
print("-"*40)
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
def ver(
    g:dict
) -> dict:
    """
    -Esta función sirve para ver la informacion de todos los usuarios registrados-
    
    PARAMETROS:
    x: Es una variable de tipo input que le pregunta al usuario si su elección es la que
       desea ejecutar.
    if x == "si": Es el condicional que dependiendo de la respuesta del usuario va a ejecutar 
        el resto del programa (Ver la información contenida en el diccionario)
        ant: es una variable que pregunta a que usuario desea modificar.
        nom:lib = En este caso "nom" y "lib" equivalen a la información añadida (lo nuevo)
        g.pop(): elimina la información vieja
        g.update(): se usa para añadir la información que se desea cambiar (nombre y libro)  
    else: si la respuesta del usuario en "x" es diferente a "si", el else se ejecuta para repetir el ciclo
    """
    x = str(input("Desea ver un usuario? (si/no) "))
    x = x.lower()
    if x == "si":
        for i in g.items():
            print(i)

    else:
         print("No se desea ver ningun usuario")
print("-"*40)
