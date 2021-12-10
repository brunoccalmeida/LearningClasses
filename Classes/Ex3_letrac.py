from Ex3 import Retangulo

while True:
    base = input('Digite o tamanho da parede, em metros: ')
    try:
        float(base)
        break
    except:
        print('Valor inválido. Tente novamente.')

while True:
    altura = input('Digite o tamanho da parede, em metros: ')
    try:
        float(altura)
        break
    except:
        print('Valor inválido. Tente novamente.')

local = Retangulo(float(base), float(altura))
print(f'Serão necessários {local.calcular_area()} pisos de 1 metro quadrado cada e'
      f' {local.calcular_perimetro()} metros de rodapé para este local.')
