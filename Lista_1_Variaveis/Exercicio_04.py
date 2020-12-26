# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.

# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5%

# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

def main():
  print("Informe o nome do Funcionário:")
  nome = input()
  
  print("Informe o salário atual")
  salario = float(input())
  
  if(salario <= 280.00):
    salarioMaisAumento = salario * 1.2
    valorAumento = (salarioMaisAumento - salario)
    print("Calculo de salário do/a funcionario/a: {0} \n Salário atual: R$ {1}\n Salário reajustado R$ {2}\n Valor do aumento {3}\nPercentual de reajuste 20%".format(nome, salario, salarioMaisAumento, valorAumento))

  elif(salario > 280.00 and salario < 700.00):
    salarioMaisAumento = salario * 1.15
    valorAumento = (salarioMaisAumento - salario)
    print("Calculo de salário do/a funcionario/a: {0} \n Salário atual: R$ {1}\n Salário reajustado R$ {2}\n Valor do aumento {3}\nPercentual de reajuste 15%".format(nome, salario, salarioMaisAumento, valorAumento))
  
  elif(salario > 700.00 and salario < 1500.00):
    salarioMaisAumento = salario * 1.10
    valorAumento = (salarioMaisAumento - salario)
    print("Calculo de salário do/a funcionario/a: {0} \n Salário atual: R$ {1}\n Salário reajustado R$ {2}\n Valor do aumento {3}\nPercentual de reajuste 10%".format(nome, salario, salarioMaisAumento, valorAumento))

  else:
    salarioMaisAumento = salario * 1.05
    valorAumento = (salarioMaisAumento - salario)
    print("Calculo de salário do/a funcionario/a: {0} \n Salário atual: R$ {1}\n Salário reajustado R$ {2}\n Valor do aumento {3}\nPercentual de reajuste 5%".format(nome, salario, salarioMaisAumento, valorAumento))
    
if __name__ == "__main__":
  main()
