# Esta é a resolução do problema de enunciado 3
# Realizada pelo candidato de código >>002<<

import os

# Variáveis de validação
numeros = [False,False,False,False,False,False,False,False,False,False]
validadeLinha = True
validadeColuna = True
validadeQuadrantes = True
validade = True

# Variáveis de input
sudoku9 = [['*' for _ in range(9)] for _ in range(9)]

tipoinput = input(f"\nCaso queira colar todos os valores de uma só vez, digite 1\nCaso deseje colar as linhas separadamente, digite 2\nCaso deseje entrar com caracteres individualmente, digite qualquer outro valor:\n")

# Inicia o algoritmo para coletar input

if tipoinput == str(1):
    # Script para input por tabela inteira colada
    os.system('cls')
    print("\n\n")

    for linha in sudoku9:
        print(linha)

    linhacolada = input(f"\nCole a matriz de valores:")
    linhacolada = linhacolada.split()

    if len(linhacolada) != 81:
        print("Erro: Você deve digitar exatamente 81 caracteres.\n")
        print("Os valores precisam estar em uma única linha, quebras de linha causam erro.\n")

    else:
        for i in range(9):
            for j in range(9):
                sudoku9[i][j] = linhacolada[j+(i*9)]


if tipoinput == str(2):
    # Script para input por linhas coladas
    for i in range(9):
        os.system('cls')
        print("\n\n")

        for linha in sudoku9:
            print(linha)

        linhacolada = input(f"\nCole a próxima linha:")
        linhacolada = linhacolada.split()

        if len(linhacolada) != 9:
            print("Erro: Você deve digitar exatamente 9 caracteres.")

        else:
            sudoku9[i] = linhacolada

if (tipoinput != str(1)) and (tipoinput != str(2)):
    # Script para input caso input individual
    for i, linha in enumerate(sudoku9):
        for j, _ in enumerate(linha):
            while True:
                os.system('cls')
                print("\n\n")

                for linha_atual in sudoku9:
                    print(linha_atual)

                proximonum = input(f"\nDigite o número para a posição ({i + 1}, {j + 1}): \n")

                if (proximonum.isdigit() and (1 <= int(proximonum) <= 9)) or proximonum == '.':
                    sudoku9[i][j] = proximonum
                    break
                else:
                    print("Erro: Digite apenas um número entre 1 e 9 ou .")

# Verificação por linhas
for linha in sudoku9:
    if not validade:
        break
    numeros = [False, False, False, False, False, False, False, False, False, False]
    for caractere in linha:
        if not validade:
            break
        if caractere.isdigit() and (1 <= int(caractere) <= 9):
            if numeros[int(caractere)] == False:
                numeros[int(caractere)] = True
            else:
                validade = False
                validadeLinha = False
                break

# Verificação por colunas
for j in range(9):
    if not validade:
        break
    numeros = [False, False, False, False, False, False, False, False, False, False]
    for i in range(9):
        if not validade:
            break
        if sudoku9[i][j].isdigit() and (1 <= int(sudoku9[i][j]) <= 9):
            if numeros[int(sudoku9[i][j])] == False:
                numeros[int(sudoku9[i][j])] = True
            else:
                validade = False
                validadeColuna = False
                break

# Verificação por quadrantes

quadi = 0
quadj = 0

for submatrizLin in range(3):
    if (quadj == 3) or not validade:
        break
    for submatrizCol in range(3):
        if not validade:
            break
        numeros = [False, False, False, False, False, False, False, False, False, False]
        quadi = 0
        for i in range(quadi * 3, (quadi * 3) + 3):
            if not validade:
                break
            for j in range(quadj * 3, (quadj * 3) + 3):
                if not validade:
                    break
                if sudoku9[i][j].isdigit() and (1 <= int(sudoku9[i][j]) <= 9):
                    if numeros[int(sudoku9[i][j])] == False:
                        numeros[int(sudoku9[i][j])] = True
                    else:
                        validade = False
                        validadeQuadrantes = False
                        break
        quadi += 1
    quadj += 1

#Final

if(validade):
    os.system('cls')
    print("\n\n")
    for linha in sudoku9:
        print(linha)

    print("\nA matriz é valida!")
else:
    if not validadeLinha:
        print("A matriz é inválida, há uma linha com números repetidos!")
    if not validadeColuna:
        print("A matriz é inválida, há uma coluna com números repetidos!")
    if not validadeQuadrantes:
        print("A matriz é inválida, há um dos quadrantes menores com números repetidos!")
