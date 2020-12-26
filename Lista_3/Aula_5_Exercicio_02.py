# Analise o programa abaixo e detalhe passo a passo como o Python (segundo suas prioridades) resolveria a equação.
# x=2
# y=3
# z = 0.5
# print(x + x * x ** (y * x) / z)

print('\nPrioridade de Equação\n')
print('x=2, y=3, z = 0.5')
print('\n(x + x * x ** (y * x) / z)\n')
print('1º Passo: (y * x) -> (2 * 3) = 6\n')
print('2º Passo: (x * (1º Passo)) --> x * 6 --> 2 ** 6 = 64\n')
print('3º Passo: (x * (2º Passo)) --> x * 64 --> 2 * 64 = 128\n')
print('4º PAsso: ((3º Passo) / z) --> 128/z --> 128/0.5 = 256\n')
print('5º PAsso: (x + 4º Passo) --> x + 256 --> 2 + 256 = 258\n')