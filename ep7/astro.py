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

  Nome :
  NUSP :
  Turma: MAE, MAP, MAT, IF, Poli, ECA, etc
  Prof.:

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma referência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
  
  Exemplo:
  - O algoritmo Quicksort foi baseado em 
  http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html

  Não altere as assinaturas/protótipos/cabeçalhos das funções.
"""

#############################################################
#                                                           #
#  MÓDULO astro.py                                          #
#                                                           #
#  Modulo responsável pela implementação da classe Astro.   #
#                                                           #
#  Não altere o nome do arquivo.                            #
#                                                           #
#  Não importe outros módulos além de vetor.                #
#                                                           #     
#############################################################

# necessário para manipularmos os objetos da classe Vetor
from vetor import *

# constantes

# constante gravitacional universal 
G = 8.65e-13 # km**3 kg**-1 h**-2

#----------------------------------------------------------------------
class Astro:
    ''' Classe utilizada para representar um astro.

    Cada objeto desta classe tem 5 atributos de estado:

       * nome: um string com o nome do astro;

       * cor: um string com a cor do astro:
              "yellow", "white", "black", "red", "blue", "violet", 
               "green", ou "pink";  

       * vet_pos: uma referência a um objeto da classe Vetor que 
              representa a posição do astro;

       * massa: um valor que representa a massa do astro (kg); e

       * raio: um valor que representa o raio do astro (km).
    '''
    
    #------------------------------------------------------------------
    def __init__(self, nome, cor, x, y, massa, raio):
        '''(Astro, str, str, float, float, float, float) -> None

        Construtor: recebe um referência `self` ao objeto da classe
           Astro que está sendo contruído e os argumentos necessários
           para sua criação.

        Exemplos:

        >>> astro1 = Astro("Terra","blue",-192200,0,5.972e+24,6371)
        >>> astro1.nome
        'Terra'
        >>> astro1.cor
        'blue'
        >>> type(astro1.vet_pos)
        <class 'vetor.Vetor'>
        >>> print(astro1.vet_pos)
        (-1.92e+05,0)
        >>> str(astro1.vet_pos)
        '(-1.92e+05,0)'
        >>> astro1.massa
        5.972e+24
        >>> astro1.raio
        6371
        >>> astro2 = Astro("Lua","green",192200,0,7.35e+22,1737)
        >>> astro2.nome
        'Lua'
        >>> astro2.cor
        'green'
        >>> print(astro2.vet_pos)
        (1.92e+05,0)
        >>> astro2.massa
        7.35e+22
        >>> astro2.raio
        1737
        '''
        print("Vixe! Ainda não fiz o método Astro.__init__()")
        
    #--------------------------------------------------------------------
    def __str__(self):
        '''(Astro) -> str

        Recebe uma referência `self` a um objeto da classe Astro
        e constrói e retorna o string utilizado por print()
        para exibir um objeto da classe.
        
        Esse também é o string retornado pela função nativa str().
        
        Para representar o valor da massa utilize "%.3g".
        Para representar o valor do raio  utilize "%.3g".

        O string retornado por este método deve ser igual aos
        exemplos a seguir.

        Exemplos:

        >>> astro1 = Astro("Terra","blue",-192200,0,5.972e+24,6371)
        >>> print(astro1)
        Astro:
            Nome     = Terra
            Cor      = blue
            Posição  = (-1.92e+05,0)
            Massa    = 5.97e+24 kg
            Raio     = 6.37e+03 km
        >>> str(astro1)
        'Astro:\n    Nome     = Terra\n    Cor      = blue\n    Posição  = (-1.92e+05,0)\n    Massa    = 5.97e+24 kg\n    Raio     = 6.37e+03 km'
        >>> astro2 = Astro("Lua","green",192200,0,7.35e+22,1737)
        >>> str(astro2)
        'Astro:\n    Nome     = Lua\n    Cor      = green\n    Posição  = (1.92e+05,0)\n    Massa    = 7.35e+22 kg\n    Raio     = 1.74e+03 km'
        >>> print(astro2)
        Astro:
            Nome     = Lua
            Cor      = green
            Posição  = (1.92e+05,0)
            Massa    = 7.35e+22 kg
            Raio     = 1.74e+03 km
        >>>
        '''
        return "Vixe! Ainda não fiz o método Astro.__str__()."

    #--------------------------------------------------------------------
    def aceleracao_gravitacional(self, vet_pos):
        '''(Astro, Vetor) -> Vetor
        
        Recebe um referência `self` para um objeto da classe Astro,
        uma referência `vet_pos` para um objeto da classe Vetor que 
        representa a posição de um ponto no espaço (=plano).
        
        Calcula e retorna o vetor aceleração da força gravitacional 
        exercida pelo astro sobre um objeto na posição 
        dada pelo vetor posição `vet_pos`.
        
        Pré-condição: a distância entre [x_a,y_a] e [x,y] não é
        "próxima" de zero.
        
        Exemplos:

        >>> astro1 = Astro("Terra","blue",0,0,5.972e+24,6371)
        >>> vet_pos1 = Vetor(300000,300000)
        >>> vet_a = astro1.aceleracao_gravitacional(vet_pos1)
        >>> type(vet_a)
        <class 'vetor.Vetor'>
        >>> print(vet_a)
        (-20.3,-20.3)
        >>> 
        >>> vet_pos2 = Vetor(6371,0)
        >>> vet_a = astro1.aceleracao_gravitacional(vet_pos2)
        >>> print(vet_a)
        (-1.27e+05,-0)
        >>> 
        >>> astro2 = Astro("bla","bla-bla",0,0,1000,100)
        >>> vet_pos = Vetor(1000,-1000)
        >>> vet_acel = astro2.aceleracao_gravitacional(vet_pos)
        >>> type(vet_acel)
        <class 'vetor.Vetor'>
        >>> print(vet_acel)
        (-3.06e-16,3.06e-16)
        >>> astro3 = Astro("x","xx",0,0,1,1)
        >>> vet_pos = Vetor(1,0)
        >>> vet_acel = astro3.aceleracao_gravitacional(vet_pos)
        >>> print(vet_acel)
        (-8.65e-13,-0)
        >>> G
        8.65e-13
        >>> 
        '''
        print("Vixe! Ainda não fiz o método Astro.aceleracao_gravitacional().")
       
