# CLASSES

# Criando uma classe

class Circulo(): # nomes de classes começam com maíuscula
    pi = 3.14
    #Criando métodos. _init_ inicializa cada objeto criado a partir da classe.
    def __init__(self, raio=1): # Se 'raio' não inserido, ele usa 1 por padrão.
        #Criando atributos.
        self.raio = raio

    def area(self):
        return (self.raio * self.raio) * Circulo.pi

    def setRaio(self, novo_raio):
        self.raio = novo_raio

    def getRaio(self):
        return self.raio
        
# Criando uma classe sem atributos e métodos

class Carro(object):
    pass

# Instanciando a classe
circ1 = Circulo(5)

# Chamando atributo
circ1.raio

# Chamando método
circ1.area()

# Operações sobre atributos
hasattr(objct,'titulo')
setattr(objct, name, value)
getattr(objct, name)
delattr(objct, name)


# SUB CLASSES COM HERANÇA

class ClasseBase():
    def __init__(self, atributo1 = 'atributo1'):
        self.atributo1 = atributo1
        self.atributo2 = atributo1 * 2 # atributo não tem sempre que ser parâmetro 
        
    def metodo1(self):
        print("método1 da Classe Base executado")

    def metodo2(self):
        print('método2 da Classe Base executado')


class SubClasse(ClasseBase):
    def __init__(self, atributo1, atributo3 = 'atributo3'):
        ClasseBase.__init__(self, atributo1)
        self.atributo3 = atributo3

    def metodo1(self):
        print('método1 da Subclasse executado')

    def metodo3(self):
        print('método3 da Subclasse executado')








