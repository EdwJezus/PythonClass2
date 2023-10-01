print('Teste 1: Números Inteiros')
print('')
for c in range(0,51, 2):
  print(c)
print('feito')

############

print('')
print('Teste 2')
n = int(input('Digite um número: '))
for c in range(0, n+1, 2):
  print(c)
print('Fim.')

############## Atividades

print('')
print('Atividade 1')
print('')
n = int(input('Digite um número: '))

for a in range(1, n+1):
  for b in range(1, a):
    c = b
    while b**2 + c**2 < a**2:
     c = c+1
    if b**2 + c**2 == a**2:
      print ('Hipotenusa é igual a', a, ', E os catetos são', b, 'e', c)
