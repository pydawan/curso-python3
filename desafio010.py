#!/usr/bin/env python3

# Desafio 010
# Crie um programa que leia quanto dinheiro
# uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere
# US$ 1,00 = R$ 3,27
print('{:=^50}'.format('CONVERSOR DE MOEDAS') )
print('{:^50}\n'.format('REAL BRASILEIRO - DÓLAR AMERICANO'))
print('Cotação do dia: US$ 1,00 = R$ 3,27')
reais = float( input('Informe quantos reais você têm em sua carteira: ') )
dolares = reais / 3.27
print('R$ {:0.2f}'.format(reais) )
print('US$ {:0.2f}'.format(dolares) )
