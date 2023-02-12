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
        
        if selec == "1":
            print(añadir(biblio))
        if selec == "2":
            print(cambiar(biblio))
        if selec == "3":
            print(eliminar(biblio))
        if selec == "4":
            print(ver(biblio))
        if selec == "x":
            print("salio de la biblioteca")
            break