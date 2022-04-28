# 1 - imports / bibliotecas
# 2 - Classe
# 3 - Metodos e Funções
# def = definition = definição
def print_Oi(name):
    print(f'Oi,{name}')
    print('Oi,'+name)
#Calculando a área do Retangulo
def calcular_area_do_retagulo(largura,comprimento):
    arear = largura * comprimento
    return arear
#Calculando a área do Quadrado
def calcular_area_do_quadrado(lado):
    areaq = lado * lado
    return areaq

#Calculando a área do Triangulo
def calcular_area_do_triangulo(largura, comprimento):
    areat = largura * comprimento/2
    return areat
#Contagem progressiva
def contagem_progressiva(fim):
    for numero in range(fim):#repetir o bloco de zero até o fim
        print(numero)        #exibir o numero

def apoiar_candidato(nome, vezes):
    for numero in range(vezes):
      #  contador = numero + 1
      #  print(f'{contador} - {nome}')
      if numero < 9:
          print(f'00{numero + 1} - {nome}')
      elif numero < 99:
          print(f'0{numero + 1} - {nome}')
      else:
          print(numero + 1, '-', nome)

def brincar_de_plim(fim):
    for numero in range(fim):
        if numero % 4 == 0:
            print('PLIM!!!')
        else:
            print('{:0>3}'.format(numero))
           #print('{:0>3}'.format(numero))

if __name__ == '__main__':
    print_Oi('Ademar Rodrigues')

    #Chamar a funcão da area de retangulo
    arear = calcular_area_do_retagulo(3, 4)
    print(f'A área do retangulo é de {arear}m²')

    #chamar a função de area do quadrado
    areaq = calcular_area_do_quadrado(5)
    print(f'A área do quadrado é de {areaq}m²')

    #chmar a função de area do triangulo
    areat = calcular_area_do_triangulo(5, 5)
    print(f'A área do Triangulo é {areat}m²')

    #chamar a função contagem progressiva
    contagem_progressiva(11)

    #chamar a função apoiar cadidato
    apoiar_candidato('Faker', 100)

    #Chamar a função de plim
    brincar_de_plim(100)


