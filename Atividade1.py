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


"-----Atividade 53------"

import random

saldo_disponivel = 1000  
while True:
    print("Bem vindo ao banco do BMG")
    saque = int(input("Insira um valor de saque (múltiplo de 10): "))
    
    if saque % 10 != 0:
        print("O valor inserido não é múltiplo de 10. Tente novamente.")
        continue
    
    if saque > saldo_disponivel:
        print("O valor inserido excede o saldo disponível. Tente novamente.")
        continue
    
    
    print(f"Saque de R$ {saque} realizado com sucesso!")
    saldo_disponivel -= saque  
    break


"-----Atividade 54------"
import random

condicao = True

while condicao:
    print("Bem-vindo")

    
    palavra1 = input("Insira a primeira palavra: ")
    palavra2 = input("Insira a segunda palavra: ")

    
    if len(palavra1) == len(palavra2):
        print("Parabéns! As palavras têm a mesma quantidade de caracteres!")
    else:
        print("As palavras têm quantidades diferentes de caracteres.")

    
    continuar = input("Deseja verificar outras palavras? (s/n): ")
    if continuar.lower() != 's':
        condicao = False

print("Obrigado por usar o programa!")

"---Rescrita 1---"

palavra = "Banana"
print(palavra*3)

"---Rescrita 2---"

string_entrada = input("Por favor, digite uma stering: ") # solicita ao usuario para digitar um string
print(string_entrada) # Imprime a string digitada
print("," * len(string_entrada)) # Inprime uma linha de traços com o mesmo comprimento da string digitada

"------Pratica------"

string1 = input("Por favor, digite a primeira string: ")
string2 = input("Por favor, digite a segunda string: ")

if len(string1) > len(string2):
    print(f"A string mais longa é", string1)
elif len(string2) > len(string1):
    print(f"A string mais longa é:", string2)
else:
    print("As strings são igualmente longas.")

"-----Atividade 55-----"


string_entrada = input("Por favor, digite uma stering: ") # solicita ao usuario para digitar um string
print(string_entrada) # Imprime a string digitada
print("," * len(string_entrada)) # Inprime uma linha de traços com o mesmo comprimento da string digitada


"-----Atividade 56-----"


string1 = input("Por favor, digite a primeira string: ")


while len(string1):
   print(string1)
   print("," * len(string1))
   

"-----Atividade 57-----"

string_entrada = input("Por favor, digite uma string: ")


while len(string_entrada) < 20:
    num_asteriscos = 20 - len(string_entrada)
    formatted_string = '*' * num_asteriscos + string_entrada
else:
    formatted_string = string_entrada

print(formatted_string)
print("," * len(string_entrada))

"-----Atividade 58-----"


string_entrada = input("Por favor, digite uma string: ")

largura_quadro = 40
largura_string = len(string_entrada)


espacos_lado = (largura_quadro - largura_string) // 2
espacos_direita = largura_quadro - largura_string - espacos_lado


print('*' * largura_quadro)  
print('*' + ' ' * (largura_quadro - 2) + '*')  
print('*' + ' ' * espacos_lado + string_entrada + ' ' * espacos_direita + '*')  
print('*' + ' ' * (largura_quadro - 2) + '*')  
print('*' * largura_quadro)  

"-----Colinha-----"

while True:  #inicia i, loop infinito
   numero = int(input("Por Favor, Digite um numero: "))
   if numero == 1: #Verifica se o numero digitando
      break #se for 1,Interrompe o loop

while numero > 0: #continua o loop enquanto o numero for maior que 0
   print(numero)
   numero + 1


"-----Colinha2-----"

def mensagem():
   print("Essa é a minha Função")
mensagem()


"-----Atividade1-----"

def sete_irmaos():
   print("paulo1")
   print("paulo2")
   print("paulo3")
   print("paulo4")
   print("paulo5")
   print("paulo6")
   print("paulo7")
mensagem()

"-----Atividade 2-----"

def media():
    
    n1, n2, n3 = map(int, input("Por favor, digite 3 números inteiros separados por espaço: ").split())
    
    print(f"A média aritmética é: {(n1 + n2 + n3) / 3}")


media()



"-----Atividade 3-----"

def quadado_hashtag(tamanho):
    
    for i in range(tamanho):
        
        print("#" * tamanho)


tamanho = int(input("Por favor, digite o tamanho do lado do quadrado: "))
quadado_hashtag(tamanho)

   


"-----Atividade 4-----"

def mesaXadrez(n):
    x = 0
    while x < tamanho:
        y = 0
        while y < tamanho:
           if(x + y) % 2 == 0:
              print('1', end= '')
           else:
              print('0', end='')
              y += 1

mesaXadrez(9)

# Solicitandodoo o tamanho do tabuleiro ao usuário

"-----Atividade 5-----"

def quadradoString():
    s = input("Por favor, digite uma string: ")
    n = int(input("Por favor, digite um número inteiro para o tamanho do quadrado: "))

   
    for i in range(n):
        linha = ""
        for j in range(n):
            linha += s[(i + j) % len(s)]
        print(linha)


quadradoString()



"-----Colinha 3-----"

def cumprimentar(nome):
   print("Olá", nome)

def cumprimentar_varias_vezes(nome, vezes):
   while vezes > 0:
      cumprimentar(nome)
      vezes = 1

cumprimentar_varias_vezes("Emily", 3)
   
   
   
"-----Atividade 6-----" 

def linha(comprimento, caractere):
    
    if caractere == "":
        caractere = "*"
    else:
        caractere = caractere[0]  
    
    print(caractere * comprimento)


linha(10, "%")  
linha(9, "L")   
linha(5, "")    


"-----Atividade 7-----"

   











"-----Atividade 8-----"
def linha(caractere, quantidade):
    print(caractere * quantidade)

def triangulo(tamanho):
    for i in range(1, tamanho + 1):
        linha('#', i)


triangulo(5)


"----colinha 6----"

def minha_soma(a, b):
   return a + b

resultado = minha_soma(4, 6)
print("A soma é", resultado)


"-----Atividade 9-----"

def o_maior_numero():
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))
    if num1 > num2:
        print("O primeiro número é maior.")
    elif num1 < num2:
        print("O segundo número é maior.")
    else:
        print("Os números são iguais.")


o_maior_numero()



"-----Atividade 10-----"

def mesmo_caracter():
   palavra = input("Digite um caracter")
   palavra2 = input("Digite mais um caracter")

   if palavra1 == palavra2:
      print("True")

   else:
      print("False")

"----Pratica----"

valores = {1, 2, 3, 4 ,5}
pergunta = input("Digite um indice e um valor")






"----Colinha----"

numeros  = {}
numeros.append(5)
numeros.append(10)
numeros.append(3)
print(numeros)

"----Pratica 2 ----"


numero_de_itens = int(input("Digite o número de itens: "))
valor = input("Digite um valor: ")


array = [valor] * numero_de_itens


print("Lista criada:", array)


"----Pratica 3----"

valor = input("voce quer adicionar ou remover ")
if valor == "adicionar":
   valor = input("Digite o valor que deseja adicionar")
   lista = [1, 2, 3, 4, 5]
   lista.append(valor)
   print(lista)

else:
   valor = input("Digite o valor que deseja remover")
   lista = [1, 2, 3, 4, 5]
   lista.remove(valor)
   print(lista)


"----Colinha 5----"

minha_lista = [2, 5, 1, 2, 4]
minha_lista.sort()
print(minha_lista)

"----Colinha 6----"

original = [2, 5, 1, 2, 4]
ordenado = sorted(original)
print(ordenado)
print(original)

"-----Atividade 5------"

def cim_anagramas(palavra1, palavra2):
    
    palavra1 = palavra1.replace(" ", "").lower()
    palavra2 = palavra2.replace(" ", "").lower()
    
    
    return sorted(palavra1) == sorted(palavra2)

print(cim_anagramas("amor", "roma"))  
print(cim_anagramas("amor", "ramo"))  
print(cim_anagramas("amor", "romão")) 

"-----Atividade 6------"

def Soma_positivos():
   valor = int(input("Digite uma lista "))
   return valor
print(valor)

"------Atvididade 7-----"

def numeros_pares(numero):
    return numero % 2 == 0


print(numeros_pares(4)) 
print(numeros_pares(7))  
print(numeros_pares(0))  
print(numeros_pares(-2)) 

"------Atvididade 8------"

def lista_soma(lista1, lista2):
    
    if len(lista1) != len(lista2):
        raise ValueError("As listas devem ter o mesmo número de itens.")
    
    
    soma_lista = [lista1[i] + lista2[i] for i in range(len(lista1))]
    return soma_lista


lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
print(lista_soma(lista1, lista2))  

lista1 = [7, -3, 0]
lista2 = [3, 6, 2]
print(lista_soma(lista1, lista2))  


"----exemplos 1----"

minha_string = "quantas madeiras um esquilo poderia empilhar se um esquilo pudesse empilhar madeira"
print(minha_string.count("ma"))

minha_lista = [1,2,3,1,4,5,1,6]
print(minha_lista.count(1))

"----exemplos 2----"

minha_string = "01"
minha_string = minha_string.replace("01", "Olá")
print(minha_string)



"----Patrica----"

def mais_caracteres(s):
    
    contador = {}
    
    
    for char in s:
        contador[char] = contador.get(char, 0) + 1
    
   
    max_ocorrencias = 0
    caractere_mais_frequente = ''
    
    for char in s:
        if contador[char] > max_ocorrencias:
            max_ocorrencias = contador[char]
            caractere_mais_frequente = char
    
    return caractere_mais_frequente


print(mais_caracteres("abracadabra"))  
print(mais_caracteres("aabbcc"))       
print(mais_caracteres("opa minecraft")) 

"-----Atividade 9----"

def sem_vogal():
    argumento = input("Digite um argumento: ")
    vogais = "aeiou"
    resultado = ""
    index = 0
    tamanho = len(argumento)
    
    while index < tamanho:
        if argumento[index] in vogais:
            index += 1
        elif argumento[index] not in vogais:
            resultado += argumento[index]
            index += 1
        else:
            index += 1

    return resultado


print(sem_vogal())

"----Rescrita matriz-----"

minha_lista = [[5,2,3], [2,2,5,1]]
print(minha_lista)
print(minha_lista[1])
print(minha_lista[1][0])


pessoas = [["Bety", 10, 1,37], ["pedro",7, 1.25], ["Emily", 32, 1.64], ["Alan", 39, 1.78]]
for pessoa in pessoas:
   nome = pessoa[0]
   idade = pessoa[1]
   altura = pessoa[2]

"----Rescrita matriz 2-----"

minha_matriz = [[1,2,3], [3,2,1], [4,5,6]]

print(minha_matriz[0][1])
minha_matriz[1][0] = 10
print(minha_matriz)


"----Pratica-----"
def conta_elementos(minha_matriz: list, elemento: int):
   pessoas = [["Bety", 10, 1,37], ["pedro",7, 1.25], ["Emily", 32, 1.64], ["Alan", 39, 1.78]]
   print(minha_matriz)



"----Pratica sudoku-----"

sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [0, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [0, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

for item in sudoku:
   for itens in item:
      if itens == 0:
         print('-',end='')
      else:
         print(itens, end='')
         print("")
   
"----Atividade 10-----"

velha = [
  [9, 0, 0,] 
  [0, 0, 0,]
  [0, 2, 0,]

]

def jogue_o_jogo():
    
    mesa = [['-' for _ in range(3)] for _ in range(3)]
    jogador_atual = 'X'
    
    while True:
        
        for linha in mesa:
            print(" ".join(linha))
        
        try:
            
            x = int(input(f"Jogador {jogador_atual}, insira a coordenada X (0-2): "))
            y = int(input(f"Jogador {jogador_atual}, insira a coordenada Y (0-2): "))
            
            
            if 0 <= x <= 2 and 0 <= y <= 2:
                if mesa[x][y] == '-':
                    mesa[x][y] = jogador_atual
                else:
                    print("Posição já ocupada! Escolha outra.")
                    continue
            else:
                print("Coordenadas fora dos limites! Tente novamente.")
                continue

            
            jogador_atual = 'O' if jogador_atual == 'X' else 'X'
            
        except ValueError:
            print("Entrada inválida! Por favor, insira números inteiros para as coordenadas.")
        
        print()


jogue_o_jogo()
