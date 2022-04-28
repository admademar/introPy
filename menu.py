# 1 - imports / bibliotecas
# 2 - Classe
# 3 - Metodos e Funções
# def = definition = definição
def print_Oi(name):
    print(f'Oi,{name}')
    #print('Oi,'+name)
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

def sair():
    print('Muito Obrigado, Volte Sempre')
def exibir_menu(escolha):
    opcao = {
        1: print_Oi('ademar rodrigues'),
        2: calcular_area_do_retagulo(3, 4),
        3: calcular_area_do_quadrado(5),
        4: calcular_area_do_triangulo(5, 5),
        5: contagem_progressiva(5),
        6: apoiar_candidato('Sabado', 10),
        7: brincar_de_plim(20),
        8: sair(),

    }
    return opcao.get(escolha, 'Opção Invalida')




if __name__ == '__main__':
    continua = True
    #while continua:
    print('************************************')
    print('*                                  *')
    print('* M E N U  D E  O P E R A Ç Õ E S  *')
    print('*                                  *')
    print('*       1 - Olá Mundo              *')
    print('*       2 - Àrea do Retangulo      *')
    print('*       3 - Àrea do Quadrado       *')
    print('*       4 - Àrea do Triangulo      *')
    print('*       5 - Contagem Progressiva   *')
    print('*       6 - Apoiar Candidato       *')
    print('*       7 - Brincar de Plim!!!     *')
    print('*                                  *')
    print('*       Z - Sair                   *')
    print('*                                  *')
    print('************************************')

    escolha = input("Escolha sua Opção")
    #print(f'A sua escolha foi:{escolha}')
    exibir_menu(escolha)





