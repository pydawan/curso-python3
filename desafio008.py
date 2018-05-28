#!/usr/bin/env python3

# Desafio 008
# Escreva um programa que leia um valor em metros e
# o exiba convertido em centímetros e milímetros.
metros = int( input('Informe a quantidade de metros: ') )
centimetros = metros * 100
milimetros = metros * 1000
print('{0} metros equivale a {1} centímetros'.format(metros, centimetros) )
print('{0} metros equivale a {1} milímetros'.format(metros, milimetros) )
