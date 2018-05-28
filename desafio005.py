#!/usr/bin/env python3

# Desafio 005
#
# Faça um programa que leia um número Inteiro e
# mostre na tela o seu sucessor e seu antecessor.

numero = int( input('Informe um número: ') )
antecessor = numero - 1
sucessor = numero + 1
print('Número informado:', numero)
print('Antecessor:', antecessor)
print('Sucessor:', sucessor)