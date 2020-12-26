#2. Tendo como dado de entrada o sexo e a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# M - Masculino: (72.7*h) - 58
# F - Feminino: (62.1*h) - 44.7

def main():
  print("Informe seu sexo: \n digite M para masculino \n digite F para feminino")
  sexo = input()
  print("Informe sua altura:")
  h = float(input())
  
  if(sexo == "f" or "F" or "feminino" or "Feminino"):
    pesoIdeal = (62.1*h) - 44.7
    print("O seu peso ideal é {}".format(pesoIdeal))
    
  elif(sexo == "m" or "M" or "masculino" or "Masculino"):
    pesoIdeal = (72.7*h) - 58
    print("O seu peso ideal é {}".format(pesoIdeal))
    
if __name__ == "__main__":
  main()
