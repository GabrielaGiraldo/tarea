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