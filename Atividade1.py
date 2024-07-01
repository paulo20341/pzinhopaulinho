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

media = (op * op2)

print("o salario diario é",media)


