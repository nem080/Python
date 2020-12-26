# Faça uma função que retorne o reverso de um número inteiro informado. Obs: utilizar uma função recursiva

def input_valores():
  print("\n")
  numero = str(input("Informe o número que deseja inverter:\n"))
  while (numero.isnumeric() == False):
    numero = str(input("Informe um número inteiro:\n"))
  if(numero=="0"):
    print("\n")
    print("Obrigado.")
  else:
    print(inverte_valor(numero))
    input_valores()

def inverte_valor(numero):
  if len(numero)==0:
    return numero
  else:
    return inverte_valor(numero[1:])+numero[0]

if __name__ == '__main__':
  print("Olá, bem vindo ao módulo de inversão de inteiros.")
  print("Para encerrar o inversor digite 0.\n")
  input_valores()