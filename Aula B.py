print('Pode mudar o valor da tupla, conversento ela em list')

t1 = (1, 2, 3, 4, 5)
t1 = list(t1)
t1[1] = 3000
t1 = tuple(t1)

print(t1)

print('\nPode ter operaçoes aritmética')
t2 = (1, 2, 3, 4, 5) * 20
print(t2)

t3 = (1 * 10, 2 + 10, 3 - 10, 4 / 10, 5 // 10, 6 ** 10)
print(t3)
