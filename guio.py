#size = int
#returns list (str)
def novaPartida(size):
    linha1 = ['.'] * (size - 1) + ['2']
    linha2 = ['1'] + ['.'] * (size - 1)
    tabuleiro = [linha1, linha2]   #lista
    i = 1
    while i < size - 1:
        tabuleiro.insert(i, ['.'] * size) #adicionar pontos ao resto 
        i += 1
    return tabuleiro

#jogada = par de coordenadas
#partida é imutavel
#partida: size e jogadas
def imprimir(partida):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    abc_lst = []
    for char in abc:
        abc_lst.append(char)
    i = 0
    res = ''
    while i < len(partida):
        index = len(partida) - i    #indice da linha (numeraçao)
        linha = ' '.join(partida[i])  #insert space in between each char, concatenate, each line of partida[]
        res += (f'{index:<2}' if index >= 10 else f' {index}') + '│' + linha + '\n' 
        i += 1
    res += '  └' + '─' * len(linha) + '\n' + '  '  #estrutura do grafico, espaço por causa das abc
    i = 0
    while i < len(partida):
        res += ' ' + abc_lst[i]  #escrever abc no eixo, apenas ate à largura requerida
        i += 1
    return res + '\n'

#valid jogada
def eValida(partida, jogada):
    x1, y = jogada
    x = len(partida) - x1 - 1
    p = partida
    trig = 0
    if (x) >= len(partida) or y >= len(partida):
        return False
    if partida[x][y] != '.':
        return False
    for _, row in enumerate(partida):
        for _, element in enumerate(row):
            if element == '0' or element == '#':
                trig = 1
                break ;
    if trig == 0:
        return True
    if (    #check if it is between bounds, and if it is a possible path
        (x + 1 < len(p) and p[x + 1][y] == 'O') or
        (x + 1 < len(p) and y - 1 >= 0 and p[x + 1][y - 1] == 'O') or 
        (x - 1 >= 0 and y - 1 >= 0 and p[x - 1][y - 1] == 'O') or 
        (x + 1 < len(p) and y + 1 < len(p) and p[x + 1][y + 1] == 'O') or
        (x - 1 >= 0 and y + 1 < len(p) and p[x - 1][y + 1] == 'O') or
        (x - 1 >= 0 and p[x - 1][y] == 'O') or
        (y - 1 >= 0 and p[x][y - 1] == 'O') or
        (y + 1 < len(p) and p[x][y + 1] == 'O')
        
    ):
        return True # anda para a frente para o lado ou na diagonal
    return False

def fazerJogada(partida, jogada):
    for row_index, row in enumerate(partida):
        for col_index, element in enumerate(row):
            if element == 'O':
                partida[row_index][col_index] = '#'
    x, y = jogada
    partida[len(partida) - x - 1][y] = 'O'
    return partida

def imprimirLances(partida):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    jogadas = [[] for _ in range(10)]
    res = ''
    count = 0
    line_number = 1
    for x, row in enumerate(partida):
        for y, element in enumerate(row):
            if element == '#':
                count += 1
    if count > 1:
        for x, row in enumerate(partida):
            for y, element in enumerate(row):
                if element == '#':
                    jogada = abc[y] + str(len(partida) - x)
                    jogada = f'{line_number:>3}. {jogada:<3}'
                    jogadas[(line_number - 1) % 10].append(jogada)
                    line_number += 1  #increment line number for valid moves
    for x, row in enumerate(partida):
        for y, element in enumerate(row):
            if element == 'O':
                jogada = abc[y] + str(len(partida) - x)
                jogada = f'{line_number:>3}. {jogada:<3}'
                jogadas[(line_number - 1) % 10].append(jogada)
                line_number += 1
    jogadas = [x for x in jogadas if x]
    for linha in jogadas:
        res += ' '.join(linha) + '\n'
    return res

#check valid next jogadas
def proximasJogadas(partida):
    res = []
    for x, row in enumerate(partida):
        for y, element in enumerate(row):
            if element == 'O':
                if (x,y) == (0,6) or (x,y) == (6,0):
                    return res    #empty since the game is over
    for x in range(len(partida)):
        for y in range(len(partida)):
            if eValida(partida, (x, y)):
                res.append((x,y))
    return res

def eFim(partida):
    return proximasJogadas(partida) == [] #game ends when theres no possible path

def vencedor(partida):
    count = 0
    for _, row in enumerate(partida):
        for _, element in enumerate(row):
            if element == '#':
                count += 1
    if count % 2 == 0:
        return 1
    return 2

#Testes
partida = novaPartida(8)

#Print the initial tabuleiro
#print(imprimir(partida))
print(imprimir(partida))
print('\n')
#Make a move
partida = fazerJogada(partida, (4, 4))

partida = fazerJogada(partida, (3, 3))

# partida = fazerJogada(partida, (2, 3))

# partida = fazerJogada(partida, (3, 2))

# partida = fazerJogada(partida, (2, 2))

# partida = fazerJogada(partida, (1, 1))

# partida = fazerJogada(partida, (0, 1))

# partida = fazerJogada(partida, (0, 2))

# partida = fazerJogada(partida, (0, 3))

# partida = fazerJogada(partida, (0, 4))

# partida = fazerJogada(partida, (1, 5))

# partida = fazerJogada(partida, (1, 6))

# partida = fazerJogada(partida, (2, 6))

# partida = fazerJogada(partida, (3, 5))

# partida = fazerJogada(partida, (3, 4))

# partida = fazerJogada(partida, (4, 3))

# partida = fazerJogada(partida, (5, 3))

# partida = fazerJogada(partida, (6, 2))

# partida = fazerJogada(partida, (6, 3))

# partida = fazerJogada(partida, (6, 4))

# partida = fazerJogada(partida, (6, 5))

# partida = fazerJogada(partida, (6, 6))

print(imprimir(partida))

# print (eValida(partida, (3,2)))
# print (eValida(partida, (3,3)))
# print (eValida(partida, (2,5)))
# print (eValida(partida, (3,2)))
# print (eValida(partida, (3,3)))
# print (eValida(partida, (2,5)))

# print(sorted(proximasJogadas(partida)))
#Print the updated board
#print(imprimir(partida))

# Print the moves
print('\n')
print(imprimirLances(partida))

#print(vencedor(partida))

# 