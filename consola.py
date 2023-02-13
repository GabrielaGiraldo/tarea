from funciones import *
def menu(biblio):
    """
    Esta funcion contiene el menu o consola de controles del programa-
      (Se importan las funciones de otro archivo)
    
    PARAMETROS:

    - while: el ciclo while se encarga de ejecutar la funcion repetidamente hasta que el usuario de un pare.
    - selec: es una variable input que le permite al usuario decidir que acción se va a ejecutar.
    - match case: cada caso dentro del matchcase corresponde a una de las opciones dentro del menu,
      dependiendo del numero selecionado se va a ejecutar un "case", que a su vez contiene una funcion con la acción determinada. 
    """
    condicion = True
    while condicion:
        print(
        """_
        1.Ingresar usuario
        2.Actualizar usuario
        3.Eliminar usuario
        4.Visualizar usuario
        (x). Salir
    
    """
    )
        selec = str(input("Que desea visualizar: "))
        match selec:
            
         case "1":
            print(añadir(biblio))
         case "2":
            print(cambiar(biblio))
         case "3":
            print(eliminar(biblio))
         case "4":
            print(ver(biblio))
         case "x":
            print("salio de la biblioteca")
            break