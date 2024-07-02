from math import sqrt

while True:
   numero = int(input("Entre com um número inteiro: "))

   if numero < 0:
      print("Número inválido")
      break
   elif numero > 0:
      raiz_quadrada = sqrt(numero)
      print(f"A raiz quadrada de {numero} é {raiz_quadrada}")
      break
3