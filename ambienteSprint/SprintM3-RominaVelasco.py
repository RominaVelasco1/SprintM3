import random

def generar_contrasena():
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    contrasena = ''.join(random.choice(caracteres) for _ in range(8))
    return contrasena

usuarios = [
    "Paciente1",
    "Paciente2",
    "Paciente3",
    "Paciente4",
    "Paciente5",
    "Paciente6",
    "Paciente7",
    "Paciente8",
    "Paciente9",
    "Paciente10"
]

cuentas = {}

for usuario in usuarios:
    contrasena = generar_contrasena()
    cuenta = {
        'contrasena': contrasena,
        'telefono': ''
    }
    cuentas[usuario] = cuenta

for usuario, cuenta in cuentas.items():
    while True:
        telefono = input(f"Ingrese el número telefónico para {usuario}: ")
        if telefono.isdigit() and len(telefono) == 8:
            cuenta['telefono'] = telefono
            break
        else:
            print("El número telefónico debe tener 8 dígitos numéricos.")

print("Cuentas creadas:")
for usuario, cuenta in cuentas.items():
    print(f"Usuario: {usuario}, Contraseña: {cuenta['contrasena']}, Teléfono: {cuenta['telefono']}")
