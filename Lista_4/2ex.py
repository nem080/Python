# Faça um programa que tenha uma função chamada valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 5% de multa, mais 1% de juros por dia de atraso.

def valorDivida(vp, da):
        if da < 1:
                valor = vp
                print(valor)
                return valor
        else:
                valor = (vp + vp * 0.05 + 0.01 * da)
                print(valor)
                return valor

valor = []
vp = 0
da = 0
qp = 0
valortotal = 0

while True:
        qp += 1
        vp = float(input('Qual o valor da prestacao?(digite 0 para sair) '))
        if vp != 0:
                break
        da = int(input('Quantos dias esta em atraso? '))
        valor.append(valorDivida(vp, da))

qp -= 1
for i in range(qp):
    valortotal += valor[i]

    print('Relatorio do dia, foram pagas %d prestacoes no valor: ' %qp, valor)
print('Valor total de prestacoes pagas: ', valortotal) 