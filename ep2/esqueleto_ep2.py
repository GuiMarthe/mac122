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
  Turma: MAE
  Prof.: José Coelho de Pina

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
  
  Exemplo:
  - O algoritmo Quicksort foi baseado em 
  http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html

"""

'''
   TAREFA:
   Escreva as funções:
       - conta_palavras(texto)   ## QUE DEVE USAR A FUNÇÃO indice()
       - indice(item, seq)
       - ordena_decrescente(p, q)
       
   Não modifique a função main().
   Implemente outras funções que você achar necessário.
   Utilize apenas comandos básicos como vimos em aula, em particular, não use
   split() (*** AINDA! ***).

'''

#####################################################################
# CONSTANTES

MAIUSCULAS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÁÀÃÂÉÈÊÍÌÎÓÒÕÔÚÙÛÇ'
MINUSCULAS = 'abcdefghijklmnopqrstuvwxyzáàãâéèêíìîóòõôúùûç'
LETRAS     = MAIUSCULAS + MINUSCULAS

#####################################################################

def main():
    '''
    Programa que lê o nome de um arquivo e o texto contido nesse arquivo 
    e cria um dicionários em que as chaves são as palavras no texto e os
    respectivos valores são o número de ocorrências da palavra no texto. 

    Uma palavra é uma sequência de caracteres pertencentes ao string LETRAS
    definido acima.

    Ao final o programa exibe o dicionário criado e o dicionário em
    que as chaves são apresentadas em ordem decrescente de seu valores.

    O programa deverá ordenar o dcionário utilizando, obrigatoriamente, 
    a função ordena_decrescente(), que você também deve escrever

    *** OU SEJA, NÃO USE SORT DO PYTHON, AINDA! ***  

    Não altere essa função.
    '''

    nome = input("Digite o nome do arquivo: ")
    
    with open(nome, 'r', encoding='utf-8') as entrada:
        texto = entrada.read()

    palavra, quantidade = conta_palavras( texto )
    print("Palavras encontradas no arquivo ", nome)
    print("-------------------------------------------")
    imprima_palavras(palavra, quantidade)
    
    print()
    print("Palavras ordenadas decrescentemente pela frequência")
    print("----------------------------------------------------")
    ordena_decrescente(palavra, quantidade)
    imprima_palavras(palavra, quantidade)
        
    print("\nFIM!\n")

######################################################################

def imprima_palavras(pal, freq):
    ''' (list, list) -> None

    Recebe uma lista `pal` de palavras e outra lista `freq` com as frequências
    correspondentes. A função imprime uma tabela em que cada linha contém 
    uma palavra e sua frequência.

    Não altere esta função.
    '''
    
    i, n = 0, len(pal)
    
    print("Quantidade de palavras: %d"%(n))
    print("%21s | %s"%('Palavra', 'Quantidade'))

    while i<n:
        print("%21s | %d"%(pal[i], freq[i]))
        i += 1
                
######################################################################

def conta_palavras(texto):
    ''' (str) -> list, list

    Recebe um string 'texto' e retorna duas listas que representam 
    um dicionário:

        * a primeira lista deve conter as palavras encontradas no texto;
        * a segunda  lista deve conter a frequência das palavras 
          no texto.
        
    De tal forma que em cada posição i da segunda deve estar o número 
    de ocorrências da palavra na posição i da primeira lista.
  
    IMPORTANTE: Embora o texto possa ter caracteres maiúsculos e minúsculos,
    a função considera esses caracteres iguais (ou seja 'CASA' e 'casa' e
    'CaSa' são a mesma palavra). As palavras da primeira lista devem 
    possuir apenas caracteres minúsculos. 
    
    Exemplo:
    >>> conta_palavras("Fácil deMais é Muito MUITO fácil")
    ['fácil', 'demais', 'é', 'muito'], [2, 1, 1, 2]
    
    A função conta_palavras deve usar, obrigatoriamente,
    a função indice definida a seguir.
    '''
    print("Vixe, ainda não implementei a função conta_palavras!")
    return [], [] 
    
######################################################################

def indice (item, seq):
    '''(objeto,list ou str) -> int ou None

    Recebe um objeto 'item' e uma estrutura sequencial 'seq' e
    retorna o índice da posição em que item ocorre em seq.
    Caso item não ocorra em seq a função retorna o valor None.

    Exemplos:
    >>> indice(1,[-2,13,1,14])
    2
    >>> indice(1,[1,-2,13,14])
    0
    >>> indice(1,[2,13,14,1])
    3
    >>> indice(1,[2,13,14,-1])
    None
    >>> indice(1.3,[2,13,14,1.3])
    3
    >>> indice('x',[2,13,14,1.3])
    None
    >>> indice('x', 'ô xenti!')
    2
    '''
    print("Vixe, ainda não implementei a função indice!")
    return None

######################################################################

def ordena_decrescente(pal, freq):
    ''' (list, list)

    Recebe uma lista 'pal' de palavras e outra lista 'freq' de mesmo tamanho 
    com  o número de ocorrências das palavras de índices correspondentes.

    A função modifica as duas listas, acabando quando as palavras
    estiverem em ordem decrescente de número de ocorrências.    

    Observação: Note que função não tem return.  
    '''
    print("Vixe, ainda não implementei a função ordena_decrescente!")

######################################################################
  
if __name__ == "__main__":         
    main()
