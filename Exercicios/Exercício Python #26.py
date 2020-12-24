'''
Crie um programa que leia o nome completo e mostre:
- O nome com todas as letras maiusculas
- O nome com todas as letras minusculas
- Quantas letras ao todo, sem considerar os espaços.
- quantas letras tem o primeiro nome
'''

nome = str(input('Qual seu nome completo: '))

print(f'Todo maiúsculo: {nome.upper()}')
print(f'Todo minúsculo: {nome.lower()}')

nome_sem_espacos = nome.replace(' ','')
print(f'Possui, {len(nome_sem_espacos)} letras, desconsiderando os espaços')

primeiro_nome = nome.split()[0]
print(f'O primeiro nome possui {len(primeiro_nome)} letras')

