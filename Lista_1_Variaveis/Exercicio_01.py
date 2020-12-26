#1. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

def conv(F, C):
  C = 5 * ((F-32) / 9)
  return C

def main():
  print("\nInforme a temperatura em graus Fahrenheit:")
  F = int(input())
  C = 0

  C = conv(F, C)
  print("Resultado da transformação em graus celsius é {:.2f}".format(C))

if __name__ == "__main__":
  main()
