# Faça um programa que carregue uma lista com modelos de carros (exemplo de mod- elos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Para finalizar o cadastro, o usuário deve escrever "listar" como nome de veículo.
# Calcule e mostre:
# a) O modelo do carro mais econômico;
# b) Quantos litros de combustível cada um dos carros cadastrados consome para per- correr uma distância de 1000 quilômetros; c) Quanto custará para percorrer os 1000 quilômetros, considerando um que a gasolina custe R$ 4,25 o litro.

print('-'*27)
print('Comparativo de Combustivel')
print('-'*27)
lisCarro = []
lisConsumo = []

while len(lisCarro) < 5:
    lisCarro.append(input('\nInsira o nome do carro: '))
    lisConsumo.append(float(input('Qual o consumo do carro (km por litro): ')))
    print('Informe novos dados... \n')

results = ''
vlr_gas = 4.25
total_km = 1000
for l, c in enumerate(lisCarro):
    print('Veiculo {}'.format(l+1))
    print('Nome: {}'.format(c))
    print('Km por litro: {}\n'.format(lisConsumo[l]))
    print('-'*27)
    consumo_l = round(total_km/lisConsumo[l], 2)
    results += 'O carro {} consume {}L e custará $R{} quando fizer {}km\n'.format(c, consumo_l, round(consumo_l * vlr_gas, 2), total_km)
print('\nRelatorio final\n')
print('O carro mais económico é o {}\n'.format(lisCarro[lisConsumo.index(max(lisConsumo))])) 
print(results) 

