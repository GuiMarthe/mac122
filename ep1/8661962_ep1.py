"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP,
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA.
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome : Guilherme Marthe
  NUSP : 8661962
  Turma: MAE, MAP, MAT etc
  Prof.: José Coelho de Pina

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.

  Exemplo:
  - O algoritmo Quicksort foi baseado em http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html

"""

'''
   TAREFA:
   Escreva a função conta_caracteres() e indice(), como definidas
       abaixo nesse esqueleto.
   Não modifique a função main().
   Implemente outras funções que você achar necessário.

'''

######################################################################
#

def main():
    '''
    Essa função main ilustra uma forma de ler um arquivo de texto.
    Para saber mais como manipular arquivos em seu programa, veja:
    https://panda.ime.usp.br/pensepy/static/pensepy/10-Arquivos/files.html

    '''

    nome = input("Digite o nome do arquivo: ")

    with open(nome, 'r', encoding='utf-8') as entrada:
        texto = entrada.read()

    caracter, quantidade = conta_caracteres( texto )

    i, n = 0, len(caracter)

    print("Quantidade de caracteres distintos no arquivo %s: %d"%( nome, n))
    print(" Caractere | Quantidade")

    while i < n:
        if caracter[i] == '\n':
            print("%10s | %d"%('\\n', quantidade[i]))
        elif caracter[i] == ' ':
            print("%10s | %d"%('branco', quantidade[i]))
        ## incluir outros casos específicos se houver
        else:
            print("%10s | %d"%(caracter[i], quantidade[i]))
        i += 1

    print("\nFIM!\n")

######################################################################
#

def conta_caracteres( texto ):
    ''' (str) -> list, list
    recebe um string texto e retorna duas listas:
    lista 1: a lista com os caracteres encontrados no texto,
             mantendo o ordem dos caracteres no texto.
    lista 2: a lista com o número de ocorrências do caractere
             correspondente à lista 1

    Exemplo:
    >>> conta_caracteres ("bbaccc")
    ['b', 'a', 'c'], [2, 1, 3]

    A função conta_caracteres deve usar, obrigatoriamente,
    a função indice definida a seguir.
    '''

    ## escreva a sua função no lugar das duas linhas abaixo
    caracteres = []
    frequencia = []
    n = len(texto)
    i = 0
    while i < n:
        char = texto[i]
        lugar_na_lista = indice(char, caracteres)

        if lugar_na_lista == 'None':
            caracteres.append(char)
            frequencia.append(1)
        else:
            frequencia[lugar_na_lista] += 1
        i = i + 1
    return caracteres , frequencia


######################################################################
#

def indice(item, lista):
    '''(objeto,list) -> int ou None

    Recebe um objeto 'item' e uma lista 'lista' e retorna o
    indice da posicao em que item ocorre na lista.
    Caso item nao ocorra na lista a funcao retorna None.

    Exemplos:
    >>> indice(1,[-2,13,1,14])
    2
    >>> indice(1,[1,-2,13,14])
    0
    >>> indice(1,[2,13,14,1])
    3
    >>> indice(1,[2,13,14,-1])
    >>> indice(1.3,[2,13,14,1.3])
    3
    >>> indice('x',[2,13,14,1.3])
    None
    '''
    n = len(lista)
    i = 0
    indice = 'None'
    while i < n:
        if lista[i] == item:
            indice = i
        i += 1
    return indice

######################################################################
#
#  ESCREVA A SEGUIR OUTRAS FUNÇÕES QUE DESEJAR
#
######################################################################



######################################################################
#
#  AGORA VAMOS CHAMAR A MAIN PRA RODAR O PROGRAMA
#
######################################################################

if __name__ == "__main__":
    main()
