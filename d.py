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