#----sudoku----#

def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(str(num) if num else "." for num in linha))

def validar_entrada(x, y, num, tabuleiro):
    
    if tabuleiro[x][y] != 0:
        return False

    
    if num < 1 or num > 9:
        return False

    
    for i in range(9):
        if tabuleiro[x][i] == num or tabuleiro[i][y] == num:
            return False

    quad_x, quad_y = x // 3 * 3, y // 3 * 3
    for i in range(quad_x, quad_x + 3):
        for j in range(quad_y, quad_y + 3):
            if tabuleiro[i][j] == num:
                return False

    return True

def atualizar_tabuleiro(x, y, num, tabuleiro):
    tabuleiro[x][y] = num

def verificar_conclusao(tabuleiro):
    for linha in tabuleiro:
        if 0 in linha:
            return False
    return True

def main():
    
    tabuleiro = [[0] * 9 for _ in range(9)]

    
    tabuleiro[0][1] = 5
    tabuleiro[2][3] = 8
    

    while not verificar_conclusao(tabuleiro):
        exibir_tabuleiro(tabuleiro)
        try:
            x = int(input("Digite a posição x (0-8): "))
            y = int(input("Digite a posição y (0-8): "))
            num = int(input("Digite o número (1-9): "))
            if validar_entrada(x, y, num, tabuleiro):
                atualizar_tabuleiro(x, y, num, tabuleiro)
            else:
                print("Entrada inválida! Tente novamente.")
        except ValueError:
            print("Entrada inválida! Digite números inteiros.")

    print("Parabéns! Você vc resollveu o joginho sodokú")

if __name__ == "__main__":
    main()
