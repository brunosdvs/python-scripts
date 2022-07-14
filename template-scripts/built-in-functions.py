# LIST COMPREHENSION

# Itera a string retornando caracteres 
list1 = [x for x in 'python']

# Itera lista, calculando sobre cada elemento
list2 = [ x*2 for x in [1,2,3,4]]

#Itera lista, calculando sobre cada elemento, se condicional satisfeita
list3 = [ x*2 for x in [1,2,3,4] if x % 2 == 0]

#Operações aninhadas
list4 = [ x**2 for x in [x**2 for x in range(11)]]


# ZIP

list_zip = list(zip([1,2,3],['a','b','c','d']))

# Trocando valor entre dois dicionários
def trocaValores (dic1, dic2):
    dicTemp = {}
    for dic1_key, dic2_val in zip(dic1,dic2.values()):
        dicTemp[dic1_key] = dic2_val
    return dicTemp

d1 = {'a':1, 'b':2}
d2 = {'c':3, 'd':4}
d3 = trocaValores(d1, d2)

# ENUMERATE

list_enumerate = list(enumerate(['a','b','c','d']))

