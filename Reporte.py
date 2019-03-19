import csv

#función para escribir en el archivo
def reporte():
    nombre = ''
    apellido = ''
    telefono = ''
    usuario = ''
    proveedor = ''
    cuenta = ''
    ubicacionArroba = ''
    ubicacionPunto = ''

    with open('us-500.csv') as file:
        texto = csv.DictReader(file)
        for fila in texto:
            nombre = fila['first_name']
            apellido = fila['last_name']
            telefono = fila['phone2']
            correo = fila['email']
            ubicacionArroba = correo.find('@')
            usuario = correo[0:ubicacionArroba]
            proveedor = correo[ubicacionArroba+1:]
            ubicacionPunto = proveedor.find('.')
            cuenta = proveedor[0:ubicacionPunto]

            #se crea el archivo y se escriben las líneas
            with open('reporte.txt', 'a') as f:
                f.writelines(['Hola me llamo ', nombre,' ', apellido,'. ', 'Mi teléfono es ', telefono,'. ', 'Mi usuario de correo es: ', usuario, ' usando una cuenta de ', cuenta, '\n'])

#se llama a la función que escribe en el archivo de texto
reporte()

pass
