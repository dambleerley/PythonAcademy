""" As variáveis em python não são
fortemente tipadas como em 
java, c ou c++ elas assumem o tipo
do valor armazenado, a variável nome receba
um nome ex. nome = 'carlos' ela será do tipo
str ou string, caso esta mesma variável receba outro
tipo de valor, exemple: nome = 1, ela sará do tipo int.
É possível determinar o tipo de valor que a variável
irá armazenar através de funsão, ex: a = int(1), desta maneira
apenas números do tipo inteiro serão permitidos"""

variavel_simples = 3+2j
variavel_composta1,variavel_composta2 = "Hello Word",334
a = int(8.5)
nome = "Carlos";

print(type(variavel_simples))
print(type(variavel_composta1))
print(type(variavel_composta2))
print(type(a))

for n in nome:
   print(n)
   
print(len(nome))