#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. 

#A saída deve ser conforme o exemplo abaixo:
#Tabuada de 5:
#5 X 1 = 5
#5 X 2 = 10
#...
#5 X 10 = 50


def main():
  print("\nGerador de Tabuadas\n \nInforme um numero inteiro de 0 a 10 para gerar a tabuada:\n")
  n1 = int(input())

  t0 = n1 * 0
  t1 = n1 * 1
  t2 = n1 * 2
  t3 = n1 * 3
  t4 = n1 * 4
  t5 = n1 * 5
  t6 = n1 * 6
  t7 = n1 * 7
  t8 = n1 * 8
  t9 = n1 * 9
  t10 = n1 * 10
  
  print("\n {0} x 0 = {0} \n {0} x 1 = {1}\n {0} x 2 = {2}\n {0} x 3 = {3}\n {0} x 4 = {4}\n {0} x 5 = {5}\n {0} x 6 = {6}\n {0} x 7 = {7}\n {0} x 8 = {8}\n {0} x 9 = {9}\n {0} x 10 = {10}".format(n1, t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10))
    
if __name__ == "__main__":
  main()
