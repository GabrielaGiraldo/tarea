from funciones import *
def menu(biblio):
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