##Tipos de dados em python:

#String - "" ou '' - Texto
x = "Pedro"
y = "Thiago" 
z = x + y
print(z)

#Integer = 5 - Número inteiro
x=5 # Se o número fica entre os aspas ele vai concatenar 
y=10
z=x*y
print(z)
print(type(z))

#Float = 5.234 - Número fracionado
x=5.45
y=3.21
z=x*y
print(z)
print(type(z))

#Boolean = True or false - Boleana (Verdadeiro ou Falso)
x=True
y=False
p=""
print(bool(p))

##Tipos de variáveis 

# X = 1 - Variável padrão 
nome_usuario = 'Desafio Fabrica "2024.1"'

# CONSTANTE = 5 - Constante, seu valor não muda, é em letra maiúscula, também economiza memória

# () Tupla - Lista de elementos imutáveis
tupla = ('Camila', 'Joana', 'Giovanna')
tupla_1 = tupla [0] # para imprimir o indice 0 (Camila)

# [] - Lista de elementos mutáveis
lista = ['Kesia', 'Joana', 'Ana']
print(lista)

lista_1 = lista [0]
print (lista_1)

lista[0] = 'Judite'
print (lista)

# {} - Dicionário - Composto por chaves e valores
dicionario = {}
dicionario["modelo"] = "fiat"
dicionario["ano"] = 2020
print(dicionario)
ano = dicionario ['ano']
print(ano)
dicionario["cor"] = "azul"
cor = dicionario.get ("cor", "nao tem cor")
print(cor)