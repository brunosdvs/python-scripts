import numpy as np

#  Para criar matriz, faz-se uma lista e listas. Com o Numpy, usa-se função 
# ARRAY para transformar a lista em matriz
matriz = np.array([
       [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ])


transposta = matriz.T
inversa = np.linalg.inv(matriz)
autovalores, autovetores = np.linalg.eig(matriz)

print(autovalores)
print(autovetores)

#  Para descobrir o tamanho da matriz, função SHAPE. Retorna tupla com valores 
# de linha e colunas
tamanho = matriz.shape

I = np.eye(3)
A = np.random.random([3,3]) #números gerados conforme distribuição normal média 0, variância 1]
B = np.zeros([3,2])
C = np.ones([3,1])
D = np.ones([1,3])

#Para criar vetores de pontos igualmente espaçados. Ideal para criar discretização de domínios
xlin = np.linspace(0,10,5) #Limite inf, limite sup e quantdd de pontos
#Para criar espaçado em escala logarítmica
xlog = np.logspace(0, 10, 5) #Vai de 10^0 à 10^5, espaçado em 5 pontos

#  Numpy possui broadcasting. Ele possibilita operações com matrizes de 
# diferentes dimensões e facilita muito a passagem de arranjos para funçoes. Exe:
broadColunas = matriz + C #Numpy completa a matriz C para ter mais duas colunas copiando a primeira
broadNumeros = matriz + 2

quad =  lambda x: 3*x**2-2*x+1
broadFunc = quad(xlin) #permite aplicar a função a cada elemento do vetor xlin

# Por isso, caso quiser fazer operações matriciais de forma padrão, sem ser elemento a elemento. Deve-se usar ou np.matrix ou função .dot. Ex:
print (matriz*I)
print (matriz.dot(I))
    




# resolução de sistemas lineares fica fácil
import numpy as np
import numpy.linalg as la

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ])

b = np.array([
    [10],
    [20]])

x = la.solve(A,b)
