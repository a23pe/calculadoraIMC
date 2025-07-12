# Proyecto Calculadora de IMC

print('                   Bienvenido a Calculadora de IMC')

print('''
Por favor, Introduzca su apellido paterno
''')
apellido1 = input()

print('''
Introduzca su apellido materno
''')
apellido2 = input()

print('''
Ahora introduzca su Nombre
¡Ya casi acabamos!
''')

nombre = input()

print(f'''
Muy bien {nombre}, 
¡Sigue así!
''')

print(f'Nombre de Usuario: {nombre} {apellido1} {apellido2}')

print('Presione "Enter" para continuar')
input()
# Registro de nombre de usuario finalizado

# Validación de peso
while True:
    try:
        peso = float(input('Ingrese su peso en kilogramos (puede incluir decimales): '))
        if peso <= 0:
            print('⚠️ El peso debe ser mayor a 0. Inténtalo de nuevo.')
            continue
        break
    except ValueError:
        print('⚠️ Entrada inválida. Usa solo números. Ejemplo: 80.24')

# Validación de estatura
while True:
    try:
        estatura = float(input('Ingrese su estatura en metros (ejemplo: 1.70): '))
        if estatura <= 0:
            print('⚠️ La estatura debe ser mayor a 0. Inténtalo de nuevo.')
            continue
        break
    except ValueError:
        print('⚠️ Entrada inválida. Usa solo números. Ejemplo: 1.70')

# Cálculo de IMC
imc = peso / estatura ** 2

print(f'''
Perfecto {nombre} {apellido1} {apellido2}
Tu índice de masa corporal es: {imc:.2f}
''')
