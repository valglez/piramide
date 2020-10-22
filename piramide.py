import os

#Pirámide
def pintar_piramide(filas):
    for i in range(0,filas):
        for j in range(0,filas-i):
            print(' ', end='')
        for k in range(1,(i+1)*2):
            print('*', end='')
        print('\n')

#Pirámide inversa
def pintar_piramide_inversa(filas):
    for i in range(0,filas):
        for j in range(0,i):
            print(' ', end='')  
        for k in range(1, (filas-i)*2):
            print('*', end='')  
        print('\n')

salir = 'n'
while salir == 'n':
        print('Dime tipo de pirámide')
        tipo_piramide = input('1.Normal 2.Inversa: ')
        while tipo_piramide != '1' and tipo_piramide != '2':
            print('Tipo no válido, selecciona el correcto')
            tipo_piramide = input('1.Normal 2.Inversa: ')
        filas = input('Dime número de filas: ')
        filas = int(filas)
        if tipo_piramide == '1':
            pintar_piramide(filas)
        else:
            pintar_piramide_inversa(filas)
        salir = input('¿Salir?(s/n): ')
        os.system('cls')