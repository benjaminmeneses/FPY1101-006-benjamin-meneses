'''administracion de Productos
 '''
#profe no me baje tanto =C
import os
#listas y diccionarios
dict = {'escoba':5,'huevo':25,'leche':9}
menu = ['Ver stock de productos','Añadir stock','Eliminar producto','Salir']
#menu principal
print('*'*50 , 'Administracion de stock', '*'*50)
while True:
    for num , element in enumerate(menu):
        print(f'{num + 1}. {element}')
    resp = input('¿Que quieres hacer? \n')
    if resp == '1':
        for numero , eleme in dict.items():
            print(f'{numero}. {eleme} \n')
    elif resp == '2':
            elem = str(input('¿Que elemento deseas agregar? \n'))
            unidad = int(input('¿Cuanto deseas agregar? \n'))
            for elem, unidad in dict.items:
                print()
    elif resp == '3':
        while True:
            try:
                elemento = str(input('¿Que deseas eliminar?\n'))
            except:
                print('Seleccion erronia, porfavor vuelva a intentarlo \n') 
            if str(elemento) in dict:
                cantidad = int(input('¿Cuanto deseas eliminar?\n'))
                if int(cantidad) in dict.items():
                    del dict[elemento(cantidad)]
                    print('Producto eliminado perfectamente')                          
    elif resp == '4':
        os.system('cls')
        exit('Adios!, Gracias por usar el programa')
    else:
        os.system('cls')
        print('Seleccion erronia, porfavor vuelva a intentarlo \n')
