from math import sqrt
import re
import ramdom

print(sqrt)(9)
"Atividade 6"
numero = numero = float(input("Digite um número: "))


resultado = numero * 5

print(f"O resultado de {numero} multiplicado por 5 é {resultado}")


"Atividade 7"


nome = input("Qual seu nome? ")


data_nascimento = int(input("Qual o seu ano de nascimento? "))


ano_atual = 2024


idade = ano_atual - data_nascimento

print(f"Olá {nome}, você fará {idade} anos no final de 2024.")

"Atividade 8"

Preço_produto = float(input("Digite um Preço de um produto "))
desconto = 10
Preço_produto = Preço_produto - desconto
print("ficou",Preço_produto)

"Atividade 9"

Valor_conta = input("digite o valor da conta")
gorjeta = input("Digite o valor da gorjeta")
total = Valor_conta - gorjeta
print("Ficou",total)

"Atividade 10"


taxa_cambio = 4.85  


valor_reais = float(input("Digite o valor em reais: R$ "))


valor_dolares = valor_reais / taxa_cambio


print(f"O valor de R$ {valor_reais} convertido para dólares é $ {valor_dolares}")


"Atividade 12"

numero1 = input("Digite um numero")
numero2 = input("Digite outro numero")
numero3 = input("Digite mais um numero")

media = numero1 + numero2 + numero3 / 3 
print("A media dos numeros é ",media)

"Atividade 13"

largura = input("Digite a largura")
altura = input("Digite a altura")
area = (largura * altura)
perimetro = (largura + altura) * 2

print("area é ",area, "perimetro",perimetro)

"Atividade 14"


temperatura_celsius = float(input("Digite uma temperatura em graus Celsius: "))


temperatura_fahrenheit = temperatura_celsius * 9/5 + 32


print(f"{temperatura_celsius} graus Celsius é igual a {temperatura_fahrenheit} graus Fahrenheit.")


principal = float(input("Digite o valor principal (em R$): "))
taxa_juros = float(input("Digite a taxa de juros ao ano (%): "))
tempo = int(input("Digite o tempo de aplicação (em anos): "))


juros = principal * (taxa_juros / 100) * tempo


montante = principal + juros


print(f"Após {tempo} anos, com uma taxa de juros de {taxa_juros}%, o montante total será de R$ {montante:.2f}.")

"Atividade 15"

"3" #SolicitO  ao usuário que digite uma nota e apresentamos uma série de etapas para calcular a média de várias notas."

notas = input("Entre com uma nota")



print("-Reunir todas as notas")
print("-Anotar",notas)
print("-Soma das notas")
print("-Calculo da media")
print("-Divisão pela quantidade de notas")


"4" #Pedi ao usuário para digitar um número e verificamos se ele é par ou ímpar.

numero = int(input("Digite um número: "))



if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")


"5"


numero5 = int(input("Digite um número: "))
numero6 = int(input("Digite outro número: "))



if numero5 > numero6:
    print(f"O número {numero5} é maior")
else:
    print(f"O número {numero5} é menor")


"""11"""


nome = input("Digite o nome do funcionário: ")
salario_base = float(input("Digite o salário base: "))
horas_extras = float(input("Digite o valor total das horas extras: "))
bonus = float(input("Digite o valor do bônus: "))
descontos = float(input("Digite o valor total dos descontos: "))


salario_liquido = salario_base + horas_extras + bonus - descontos

print("\nResumo do Cálculo do Salário:")
print("Nome do Funcionário:", nome)
print("Salário Base: R$", salario_base)
print("Total de Horas Extras: R$", horas_extras)
print("Bônus: R$", bonus)
print("Descontos: R$", descontos)
print("Salário Líquido: R$", salario_liquido)
print("Algoritmo feito com sucesso! 👍")


"-------------------------------------------------------------------------------------"

numero = int(input)("Entre com um numero")

if numero < 0:
    print("Numero é negativo")


    if numero > 0:
        print("Numero é positivo")


        if numero == 0:
            print("o numero é ")


"-------------------------------------------------------------------------------------"


numero10 = int(input)("Digite um numero")

if numero10 == 1984:
    print("Orwell")


"-----Atividade 16------"

numeroint = int(input)("Digite um numero inteiro")

if numeroint <= 0:
   if numeroint * -1:
       print("Numero é negativo")

if numeroint > 0 :
    print("Numero é positivo")


"-----Atividade 17------"

numero11 = input("Digite seu nome")

if numero11 == "jerry":
    print("Nome é jerry")

print("o preço da porção unica é 5,90")
porçoes = int(input)("Digite um numero de porçoes")

if porçoes == 1:
   print("O preço fica 5,90")
    
"-----Atividade 18------"

numeroint2 = int(input)("Digite um numero inteiro")

##Solicito ao usuário para digitar um número inteiroo
numero = int(input("Digite um número inteiro: "))


# Verifica a magnitude do numero
if numero < 1000:
    print("Este número é menor que 1000. Obrigado!")

if numero < 100:
    print("Este número é menor que 100.")

if numero < 10:
    print("Este número é menor que 10. Obrigado!")

print("Obrigado")

"-----Atividade 19------"

nome = "Paulo"
cidade = "Curitiba"
estado = "Paraná"
cep = "81"

peça = int(input)("Digite Seu nome")

if nome == peça :
    print("Nome correto:",cidade,estado,cep)

else:
    print("este usuario não existe em nossas bases de dados")

"----------------------------------------------------------------"

a = 3 
condicao = a < 5
print(condicao)
if condicao:
    print("A é menor que 5")

"----------------------------------------------------------------"


"-----Atividade 20------"


print("Operações disponiveis: * - + / ")
op = int(input)("Digite uma operação 1 2 3 ou 4")

if op == 1:
    print("Voce escolheu vezes")
    entrada1 = int(input)("Dgitite um numero")
    entrada2 = int(input)("Digite outro numero")
    media1 = (entrada1 * entrada2)
    print("o resultado deu",media)

    if op == 2:
         print("Voce escolheu subtração")
         entrada1 = int(input)("Dgitite um numero")
         entrada2 = int(input)("Digite outro numero")
         media2 = (entrada1 - entrada2)
         print("o resultado deu",media2)


         if op == 3:
            print("Voce escolheu +")
            entrada1 = int(input)("Dgitite um numero")
            entrada2 = int(input)("Digite outro numero")
            media3 = (entrada1 + entrada2)
            print("o resultado deu",media3)


            if op == 3:
                print("Voce escolheu divisão")
                entrada1 = int(input)("Dgitite um numero")
                entrada2 = int(input)("Digite outro numero")
                media4 = (entrada1 / entrada2)
                print("o resultado deu",media4)


         
        
"-----Atividade 21------"


op = int(input)("Coloque uma temperatura em graus Fahrenheit")

temperatura_celsius = op * 1/8 + 32

if temperatura_celsius < 0:
    print("brr! esta frio aqui")


print(f"{op} graus Fahrenheit é igual a {temperatura_celsius} graus celsius.")


"-----Atividade 22------"

op = int(input)("Digite seu salario por hora")
op2 = int(input)("Digite suas horas trabalhadas exceto comingo")
op3 = int(input)("e o dia da semana")

media = op * op2

print("o salario diario é",media)

"-----Atividade 23------"

pontos = int(input)("Digite a quantidade de pontos no cartão fidelidade")

if pontos == 100:
    print("10% de desconto")

else:
    print("15% De desconto")


"-----Atividade 24------"

atividade24 = int(input)("Digite a previsão do tempo para amanhã")
atividade24 = int(input)("vai chover (sim ou não?)")

if atividade24 >= 20:
    print("Use jeans e camiseta")

    if atividade24  <=10:
       print("Use uma jeans e uma camiseta com um casaco se possivel")



"-----Atividade 25,26------"

pergunta = input("Notas")
pergunta2 = input("Notas")
media = (pergunta + pergunta2) / 2

if media >= 7:
    print("Aprovado")

    if media <7:
        print("Reprovado")


"-----Atividade 27------"


atividade27 = int(input)("Digite o preço do produto")

if atividade27 <=50:
    print("Categoria economica")

    if atividade27 >50  >=100:
       print("Categoria Intermediaria")

    else:
        print("Premium")


"-----Atividade 28------"

idade1 = int(input)("Qual sua idade?")

if idade1 >=16:
    print("Pode votar")

else:
    print("Não pode votar")

"-----Atividade 29------"

mes1 = int(input)("Digite um mes")

if mes1 == 1:
    print("janeiro")

    if mes1 == 2:
      print("Fevereiro")

    if mes1 == 3:
      print("março")

    if mes1 == 4:
      print("abril")

    if mes1 == 5:
      print("maio")

    if mes1 == 6:
      print("junho")

    if mes1 == 7:
      print("julho")

    if mes1 == 8:
      print("agosto")

    if mes1 == 9:
      print("setembro")

    if mes1 == 10:
      print("outubro")

    if mes1 == 11:
      print("novembro")

    if mes1 == 12:
      print("dezembro")

"-----Rescrevendo slide------"

gol_casa = int(input("Pontuação de casa:"))
gol_fora = int(input("Pontuação de fora"))

if gol_casa > gol_fora:
   print("O time de casa venceu")

elif gol_fora > gol_casa:
   print("O time de fora é campeao")

else:
   print("Empate")

"-----Atividade 30------"

um = int(input("Digite um numero inteiro"))
dois = int(input("Digite mais um "))

if um > dois:
   print("O primeiro numero é maior que o segundo")

elif dois > um:
    print("O segundo numero é maior que o primeiro")


"-----Atividade 31------"

nome1 = int(input)("Digite seu nome")
idade1 = int(input)("Digite sua idade")

nome2 = int(input)("Digite seu nome")
idade2 = int(input)("Digite sua idade")

if idade1 > idade2:
   print("O",nome1,"é idoso")

elif idade2 > idade1:
  print("O",nome2,"é idoso" )

else:
   print("Ninguem é idoso")

"-----Atividade exemplo------"

numero = int(input)("Entre com um numero")
if numero >= 5 and numero <= 8:
   print("O numero está entre 5 e 8")

numero = int(input)("Entre com um numero")
if numero >= 5 or numero <= 8:
   print("O numero está entre 5 e 8")


"-----Atividade 33------"

idade1 = int(input)("Digite sua idade")

if idade1 < 5 and idade1 >100:
   print("Voce nao é humano, idade não plausivel")

elif idade1 >5 and idade1<=100:
   print("voce é humano, idade plausivel")

"-----Atividade 34------"

nome11 = input("Digite seu nome")

if nome11 == "Zezinho" and "Huginho" and "Luisinho":
   print("Voce é sobrinho do pato donault")

elif nome11 == "Chuquinho" and "Francisquinho":
   print("Sobrinhos do Mikey Mouse")

"-----Atividade 35------"

nome12 = input("Digite seus pontos")

if nome12 <0:
   print("Impossivel")

elif nome12 >= 0 and nome12 <=49:
   print("Falhar miseravelmente")


elif nome12 >=50 and nome12<=59:
   print("1")

elif nome12 >=60 and nome12<=69:
   print("2")

elif nome12 >=70 and nome12<=79:
   print("3")

elif nome12 >=80 and nome12<=89:
   print("4")

elif nome12 >=90 and nome12<=100:
   print("5")
   
elif nome12 >100:
   print("Impossivel")

"-----Atividade 36------"

numberone = input("Digite numero inteiro tropa")

if numberone /3:
   print("Divisivel por 3")

else:
   print("Não é divisivel por 3, rebola pos crias papai kkkkkkkk")

"-----Atividade Especial 37------"

def eh_ano_bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                print("verdadeiro")
            else:
                print("falso")
        else:
            print("verdadeiro")
    else:
        print("falso")

ano = int(input("Digite um ano: "))

if eh_ano_bissexto(ano):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")


"-----Rescrevendo a estrutura de repetição------"

while True:
   numero = int(input)("Entre com um numero: ou digite -1 para parar:")

   if numero == -1:
      break
   
   print(numero ** 2)

   print("Programa encerrado, Obrigado(a)")

"-----Rescrevendo a estrutura de repetição 2------"

while True:
   codigo = input("Por favor, insira o PIN:")
   if codigo == "1234":
      break
   print("Errado!... tente de novo")

print("PIN correto! Obrigado.")

"-----Atividade 38------"

while True:
    codigo = input("Por favor, insira o PIN:")
    if codigo == "1234":
      break
    print("Errado!..., Voce quer continuar? (s/n) ")
    codigo2 = input("Por favor, insira a opção desejada:(sim/não)")
    if codigo2 == "Não":
       break

print("PIN correto! Obrigado.")


"-----Atividade 39------"

while True:
   numero = int(input("Entre com um número inteiro: "))

   if numero < 0:
      print("Número inválido")
      break
   elif numero > 0:
      raiz_quadrada = sqrt(numero)
      print(f"A raiz quadrada de {numero} é {raiz_quadrada}")
      break

"-----Atividade 40------"
while True:
   numero = 5
   print("Contando")

   print(numero)
   numero = numero -1
   if numero > 0:
      break
   
print("fall")

"-----Atividade 41------"

while True:
    numero = input("Entre com uma senha: ")
    senha = "1234"
    
    if numero == senha:
        print("Senha Correta")
        break
    else:
        print("Senha incorreta")


"-----Rescrita------"

tentativas = 0
while True:
   codigo = input("Por favor, digite seu PIN:")
   tentativas = 1
   if codigo == "1234":
     sucesso = True
     break

   if tentativas == 3:
    sucesso = False
    break
   
   print("Incorreto...tente novamente")
if sucesso:
   print("PIN correto inserido!")

else:
   print("Muitas tentativas...")

"-----Atividade 42------"

tentativas = 0
while True:
    numero = input("Entre com uma senha: ")
    senha = "4321"
    
    if numero == senha:
        tentativas = + 1
        print("Senha Correta")
        print("tentativas restantes",tentativas)
        break
    
"-----Atividade 43------"


ano = int(input("Digite um ano: "))

while True:
    ano += 1
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"O próximo ano bissexto após {ano - 1} é {ano}.")
        break

"-----Rescrita------"

numero = int(input("Por favor,Digite um numero"))

while numero < 10:
   print(numero)
   numero += 1

print("Execução Finalizada")

"-----Atividade 44------"

numero = 2
while numero <= 30:
    print(numero)
    numero += 2

"-----Atividade 45------"

numero = int(input("por favor, digite um numero:"))

while numero == 0:
   print("Voce está pronto?")
   print("Agora!!")
   print(numero)

"-----Atividade 46------"

numero = int(input("Por favor,Digite um numero"))

if numero % 2 == 0 and numero > 0:
      print(numero)
     
"-----Atividade 47------"
while True:

  numero = int(input("Por favor,Digite um Limite superior"))

  if numero == 8:
   print(" 1 ")
   print(" 2 ")
   print(" 4 ")
   print(" 8 ")

   break
   
"-----Atividade 48------"


while True:

  numero = int(input("Por favor,Digite um Limite superior"))

  if numero == 8:
   print(" 1 ")
   print(" 2 ")
   print(" 4 ")
   print(" 8 ")

   break

"-----Bibliotecas------"

print(re.searsh("[A-Z])", "Senha"))
print(re.searsh("[a-z])", "Senha"))
print(re.searsh("[0-9])", "Senha"))

"-----Bibliotecas 2 ------"

numero_secreto = random.randint(1,100)

print(numero_secreto)

"-----Atividade 50------"

soma = 0

while soma <= 100:
    numero = int(input("Por favor, digite um número: "))
    soma += numero

print(f"A soma total é {soma}.")

"-----Atividade 51------"

import re

while condicao:
    senha = input("Digite uma senha que tenha pelo menos 8 caracteres, uma letra maiúscula, uma letra minúscula e um número: ")

    if (len(senha) >= 8 and 
        re.search("[A-Z]", senha) and 
        re.search("[a-z]", senha) and 
        re.search("[0-9]", senha)):
        
        print("Senha válida!")
        break
    else:
        print("A senha não atende aos requisitos. Tente novamente.")

print("Senha aceita:", senha)

"-----Atividade 52------"
import random

while condicao:
    print("Bem vindo ao jogo de advinhação")
    Advinha = int(input("Digite um Numero entre 1 a 100: "))
    
    numero_secreto = 6
    
    if Advinha == numero_secreto:
        print("Parabéns, você acertou!")
        break
    elif Advinha < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")


