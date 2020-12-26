#3. Faça um programa para a leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

def main():
  print("Informe o nome do Aluno:")
  nome = input()
  
  print("Informe a nota da AV1")
  n1 = float(input())
  
  print("Informe a nota da AV2")
  n2 = float(input())  
  
  print("Informe a nota da AV3")
  n3 = float(input())
  
  calcMedia = (n1 + n2 + n3)/3

  if(calcMedia == 10):
    print("O aluno/a {0} foi APROVADO COM DISTINÇÃO com média {1}".format(nome, calcMedia))

  elif(calcMedia >= 7):
    print("O aluno/a {0} foi APROVADO com média {1}".format(nome, calcMedia))

  else:
    print("O aluno/a {0} foi REPROVADO com média {1}".format(nome, calcMedia))
    
if __name__ == "__main__":
  main()
