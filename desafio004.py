#!/usr/bin/env python3

# Desafio 004
#
# Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo e todas
# as informações possíveis sobre ele.

n = input('Digite algo: ')
print('Tipo de dado:', type(n) )
print('É numérico?', n.isnumeric() )
print('É alfabético?', n.isalpha() )
print('É alfanumérico?', n.isalnum() )
print('Está em minúsculas?', n.islower() )
print('Está em maiúsculas?', n.isupper() )
print('Está capitalizada?', n.istitle() )
print('Só contém espaços?', n.isspace() )
