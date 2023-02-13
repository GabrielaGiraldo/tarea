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