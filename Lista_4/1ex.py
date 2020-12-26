# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

def input_horario():
  print("\n")
  hora = int(input("Poderia me informar que horas são? "))
  minutos = int(input("... e quantos minutos? "))
  verifica_horario(hora,minutos)

def verifica_horario(hora,minutos):
  if(hora<0 or hora>23):
    print("Desculpe, não entendi...")
    print("Poderia repetir?")
    input_horario()
  elif(minutos<0 or minutos>60):
    print("Desculpe, não entendi...")
    print("Poderia repetir?")
    input_horario()
  else:
    converte12(hora,minutos)

def converte12(hora,minutos):
  if(hora<12):
    h=hora
    m=minutos
    xm="AM"
    printhorario(h,m,xm)
  else:
    h=hora-12
    m=minutos
    xm="PM"
    printhorario(h,m,xm)

def printhorario(h,m,xm):
  if(xm=="AM" and h>4):
    print(f"Agora são {h}:{m} {xm}")
    print("Bom dia!")
    input_horario()
  elif(xm=="PM" and h<6):
    print(f"Agora são {h}:{m} {xm}")
    print("Boa tarde!")
    input_horario()
  else:
    print(f"Agora são {h}:{m} {xm}")
    print("Boa noite!")
    input_horario()

if __name__ == '__main__':
  print("Olá.")
  input_horario()