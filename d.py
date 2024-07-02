tentativas = 0
while True:
    numero = input("Entre com uma senha: ")
    senha = "4321"
    
    if numero == senha:
        tentativas = + 1
        print("Senha Correta")
        print("tentativas restantes",tentativas)
        break
    
