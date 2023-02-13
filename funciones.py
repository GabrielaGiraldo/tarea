def añadir(
    dicc:dict
) -> dict:
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
     x = str(input("Desea ver un usuario? (si/no) "))
     x = x.lower()
     if x == "si":
        for i in g.items():
            print(i)

     else:
         print("No se desea ver ningun usuario")
print("-"*40)
