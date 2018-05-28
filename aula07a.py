#!/usr/bin/env python3

nome = input('Qual é seu nome? ')
# Imprime o nome com 20 caracteres e alinhado a esquerda.
print('Prazer em te conhecer {:20}!'.format(nome) )
# Imprime o nome com 20 caracteres e alinhado a direita.
print('Prazer em te conhecer {:>20}!'.format(nome) )
# Imprime o nome com 20 caracteres e centralizado.
print('Prazer em te conhecer {:^20}!'.format(nome) )
print('Prazer em te conhecer {:=^20}!'.format(nome) )

n1 = int( input('Digite um valor: ') )
n2 = int( input('Outro valor: ') )
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d) )
print('A divisão inteira {} e potência {}'.format(di, e) )

#print('{:^50}'.format('Thiago Alexandre'), end='')
#print('Martins MONTEIRO')