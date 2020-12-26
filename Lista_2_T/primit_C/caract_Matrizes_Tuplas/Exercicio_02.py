#Exercicio_02_Aula_4
# As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. Para isto contratou o seu grupo para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
# Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os represen- tantes do sindicato laboral, chegou-se a seguinte forma de cálculo:
# a. Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; b. O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo;
# Seu programa deverá permitir a digitação do salário de um número indefinido (de- sconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
# - O salário de cada funcionário, juntamente com o valor do abono;
# - O número total de funcionário processados;
# - O valor total a ser gasto com o pagamento do abono;
# - O número de funcionário que receberá o valor mínimo de 100 reais; - O maior valor pago como abono;
# A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa.

from io import RawIOBase


salario = []

salario_funci = -1
lista = 0
print('\nFUTURO GASTOS DO ABONO')
print('='*100)
print('\n')
while (salario_funci != lista):
    print('\nInforme os valores, e apos o termino precione 0 para sair\n ')
    salario_funci = float(input('salario: '))
    if(salario_funci < lista):
        continue
    if(salario_funci != lista):
        salario.append(salario_funci)
print ('salario\t\tabono')

''' totalAbono = 0.0
totalPiso = 0
maiorAbono = 0
for salario in salario:
    abono = salario * 0.2
    if(abono < 100):
        abono = 100.0
        totalPiso += 1
        totalAbono += abono
        if('maiorAbono' not in vars()) or (abono > maiorAbono):
            maiorAbono =  abono
            print ('R$ %.2f \tR$ %.2f' % (salario, abono))

            print('foram processado {} colaboradores'.format(salario))
            print('total gasto com abono %.2f' % totalAbono)
            print('Valor minimo pago a %d colaboradores' % totalPiso)
            print('Maior valor de abono pago: %.2f' % maiorAbono')'''