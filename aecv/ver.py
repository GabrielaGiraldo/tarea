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
        for i in g.items():
            El ciclo for se encarga de recorrer el diccionario y junto al print (print(i)) muestra
            el contenido del diccionario en pantalla.
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