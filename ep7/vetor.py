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
  Prof.: José Coelho

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
#  MÓDULO vetor.py                                          #
#                                                           #
#  Modulo responsável pela classe Vetor que representa      #
#  vetores bidimensionais.                                  #
#                                                           #
#  Não importe outros módulos além do math.                 #
#                                                           #     
#############################################################

# módulo necessário para a função raiz quadrada: math.sqrt()
import math

# constantes 

#----------------------------------------------------------------
class Vetor:
    '''Classe utilizada para representar um vetor bidimensional.

    Cada objeto desta classe tem dois atributos de estado. 
    Os atributos são x e y. Esses valores são da classe int ou float 
    e representam o vetor (x,y).
    '''
    
    #------------------------------------------------------------
    def __init__(self, x = 0, y = 0):
        '''(Vetor, int|float, int|float) -> None
        
        Construtor: recebe 
        
            - `self`: referência/apelido para o objeto Vetor que 
              está sendo construído;
            - `x` e `y`: valores int ou float que representam 
              o vetor (x,y).

        e cria um objeto Vetor que representa (x,y).

        Exemplos:

        >>> v = Vetor()
        >>> v.x
        0
        >>> v.y
        0
        >>> v = Vetor(2,3)
        >>> v.x
        2
        >>> v.y
        3
        >>> w = Vetor(3.14,2)
        >>> w.x
        3.14
        >>> w.y
        2
        '''
        self.x = x
        self.y = y

    #------------------------------------------------------------
    def __str__(self):
        '''(Vetor) -> str

        Recebe uma referência/apelido `self` a um objeto da classe
        Vetor  e constrói e retorna o string utilizado por print()
        para exibir um objeto da classe.

        Esse também é o string retornado pela função nativa str().

        Para representar o valor de cada coordenada utilize "%.3g".

        O string retornado por este método deve ser igual aos
        exemplos a seguir.

        Exemplos:

        >>> v = Vetor()
        >>> print(v)
        (0,0)
        >>> str(v)
        '(0,0)'
        >>> v = Vetor(2,3)
        >>> print(v)
        (2,3)
        >>> str(v)
        '(2,3)'
        >>> w = Vetor(3.1415926,2.71828)
        >>> print(w)
        (3.14,2.72)
        >>> str(w)
        '(3.14,2.72)'
        >>> 
        '''
        xx = float(self.x)
        yy = float(self.y)

        return "(%.3g, %.3g)" % (xx, yy)
        

    #------------------------------------------------------------
    def __neg__(self):
        '''(Vetor) -> Vetor

        Recebe uma referência `self` para um objeto da classe
        Vetor e cria e retorna o Vetor que representa -self.

        Usado pelo Python quando escrevemos: -Vetor.

        Exemplos:

        >>> v = Vetor(2,3)
        >>> w = -v
        >>> print(w)
        (-2,-3)
        >>> print(v)
        (2,3)
        >>> u = Vetor(3.14,2.1)
        >>> x = -u
        >>> print(x)
        (-3.14,-2.1)
        >>> print(u)
        (3.14,2.1)
        >>> v = Vetor(-2.1,3.2)
        >>> w = -v
        >>> print(w)
        (2.1,-3.2)
        >>> print(v)
        (-2.1,3.2)
        >>> 
        '''
        return(Vetor(x = -self.x, y= -self.y))
    
    #------------------------------------------------------------
    def __add__(self, other):
        '''(Vetor, Vetor) -> Vetor

        Recebe referências `self` e `other` para objetos da classe
        Vetor e cria e retorna o Vetor que representa self+other.

        Usado pelo Python quando escrevemos: Vetor + Vetor.

        Exemplos:

        >>> v = Vetor(1,2)
        >>> w = Vetor(-0.5,3)
        >>> u = v + w
        >>> print(u)
        (0.5,5)
        >>> print(v)
        (1,2)
        >>> print(w)
        (-0.5,3)
        >>> 
                
        '''
        x_sum = self.x + other.x
        y_sum = self.y + other.y
        return Vetor(x = x_sum, y = y_sum)
        
    #------------------------------------------------------------
    def __sub__(self, other):
        '''(Vetor, Vetor) -> Vetor

        Recebe referências `self` e `other` para objetos da classe
        Vetor e cria e retorna o Vetor que representa self-other`.

        Usado pelo Python quando escrevemos: Vetor - Vetor.

        Exemplos:

        >>> v = Vetor(-1,2.1)
        >>> w = Vetor(0,-1)
        >>> u = v - w
        >>> print(u)
        (-1,3.1)
        >>> print(v)
        (-1,2.1)
        >>> print(w)
        (0,-1)
        >>> 
        '''
        x_sub = self.x - other.x
        y_sub = self.y - other.y
        return Vetor(x = x_sub, y = y_sub)        

   #------------------------------------------------------------
    def __mul__(self, other):
        '''(Vetor, int|float) -> Vetor.

        Recebe uma referências `self` para um objeto da classe
        Vetor e `other` para um int ou float e cria e retorna
        o Vetor que representa self*other.

        Usado pelo Python quando escrevemos: 
            Vetor * int   ou 
            Vetor * float.
        
        Exemplos:

        >>> w = Vetor(-0.5,3)
        >>> print(w)
        (-0.5,3)
        >>> v = Vetor(2,3)
        >>> w = v * 3
        >>> print(w)
        (6,9)
        >>> w = w * 3
        >>> print(w)
        (18,27)
        >>> print(v)
        (2,3)
        >>> w = w * 0.5
        >>> print(w)
        (9,13.5)
        >>> w = w * 2
        >>> print(w)
        (18,27)
        >>> w = w * 2
        >>> print(w)
        (36,54)
        >>> print(v)
        (2,3)
        >>> 
        '''
        return Vetor(x = self.x*other, y = self.y*other)
 
    #------------------------------------------------------------
    def __rmul__(self, other):
        '''(Vetor, int|float) -> Vetor

        Recebe referências `self` para um objeto da classe
        Vetor e `other` para uma um int ou float e cria e retorna
        o Vetor que representa  self*other.

        Usado pelo Python quando escrevemos: int   * Vetor  ou
                                             float * Vetor.

        Exemplos:

        >>> v = Vetor(1,2.1)
        >>> w = 2*v
        >>> print(v)
        (1,2.1)
        >>> print(w)
        (2,4.2)
        >>> w = 0.5 * w
        >>> print(w)
        (1,2.1)
        >>> 
        '''
        return self.__mul__(other)

   #------------------------------------------------------------
    def __truediv__(self, other):
        '''(Vetor, int|float) -> Vetor.

        Recebe uma referências `self` para um objeto da classe
        Vetor e `other` para um int ou float e cria e retorna
        o Vetor que representa self/other.

        Usado pelo Python quando escrevemos: 
            Vetor / int   ou 
            Vetor / float.
        
        Exemplos:

        >>> v = Vetor(2,3.4)
        >>> w = v/2
        >>> print(w)
        (1,1.7)
        >>> print(v)
        (2,3.4)
        >>> u = v / 3.4
        >>> print(u)
        (0.588,1)
        >>> print(v)
        (2,3.4)
        >>> v = Vetor(-12,-3.4)
        >>> w = v / 3
        >>> print(w)
        (-4,-1.13)
        >>> print(v)
        (-12,-3.4)
        >>> 
        '''
        return Vetor( x = self.x/other, y = self.y/other)
        
    
    #------------------------------------------------------------
    def distancia(self, other):
        '''(Vetor, Vetor) -> float

        Recebe referências `self` e `other` a dois objetos da classe
        Vetor representando a posição de dois pontos e retorna a 
        distância entre eles.

        Exemplos:
        
        >>> v = Vetor(0,0)
        >>> w = Vetor(1,1)
        >>> v.distancia(w)
        1.4142135623730951
        >>> w.distancia(v)
        1.4142135623730951
        >>> u = Vetor(2,0)
        >>> v.distancia(u)
        2.0
        >>> u.distancia(w)  
        1.4142135623730951
        >>> 

        '''

        R = math.sqrt((self.x - other.x)**2 + (self.x - other.y)**2)
        return R
 
