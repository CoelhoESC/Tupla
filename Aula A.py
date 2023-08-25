"""
Tuplas - Imutavel
"""
print('Criando uma tupla')
t1 = (1, 2, 3, 4, 'a', 'everton')
t2 = tuple()
t3 = 1, 2, 3, 4, 5, 6, 7

print('\nAcessando a tupla e seus valores com indices')
print(t1)
print(t1[4])

print('\nPode iterar sobre a tupla')
for v in t1:
    print(v)

print(t1[2:])

print('\nPode concatenar')
t4 = t1 + t2 + t3

print('\nPode desempacotar')
n1, n2, n3, *_ = t4
print(*_)
