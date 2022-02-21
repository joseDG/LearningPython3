'''
\n => retorno de linea
\r => retorno carro
\t => tabulador
\v => tabulador vertical
\\ => diagonal invertida
\" => comilla doble
\' => commilla simple
\xNN
\uNN
\oNN
'''

cadena1 = input("Introduzca la primera cadena:")
cadena2 = input("Introduzca la segunda cadena:")
cadena3 = input("Introduzca la tercera cadena:")
cadenaconsaltos = "\n\t" + cadena1 + "\n\t" + cadena2 + "\n\t"+ cadena3
print("Cadena con saltos:", cadenaconsaltos)