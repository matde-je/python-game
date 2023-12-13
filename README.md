# pyhton
Game in python

Um tabuleiro. Sabemos que o tabuleiro é sempre um quadrado, mas a dimensão do mesmo pode variar. No documento das regras vemos um tabuleiro 7x7, mas poderia ser 15x15 ou 8x8, etc. A dimensão mínima é 5x5 e a máxima é 26x26.
Uma sequência de jogadas que definem o decorrer de uma partida.
Determinamos que uma jogada é um par de coordenadas (linha, coluna), começando no índice zero, que identifica uma jogada da bola.
Vamos convencionar que a primeira jogada da sequência de jogadas representa a posição inicial da bola. Isto significa que, na nossa implementação, podemos escolher a posição inicial da bola (ao contrário das regras oficiais onde a bola começa sempre no mesmo sítio). Assim, esta primeira «jogada» não corresponde ainda aos movimentos dos jogadores.
A última jogada na sequência representa a posição atual da bola.
Uma partida tem de incluir a dimensão do tabuleiro e a sequência de jogadas efetuadas até ao momento.
Um requisito a cumprir é que as partidas devem ser consideradas valores imutáveis. Qualquer função que pretenda alterar a partida dada, tem de devolver uma cópia dessa partida onde a alteração ocorre.
Uma vez decidida as representações, queremos implementar as seguintes funções:

novaPartida, recebe um inteiro positivo, que representa o tamanho do tabuleiro quadrado, e devolve uma partida de Rastros ainda sem jogadas.
imprimir, recebe uma partida, e retorna numa string o estado atual do tabuleiro. A formatação deve ser a mesma do exemplo mostrado acima: cada linha do tabuleiro numa linha distinta (um espaço a separar cada casa, nenhum espaço antes ou depois, e terminando cada linha com uma mudança de linha).
Uma casa vazia é representada por um ponto, uma casa ocupada por um hashtag, e a bola por um ó maiúsculo.
Os cantos opostos para onde a bola se deve dirigir devem mostrar o 1 para a casa do 1º jogador -- corresponde à coordenada (0,0) --, e um 2 para a casa do 2º jogador -- que corresponde à coordenada (size-1, size-1), sendo size o tamanho do tabuleiro.
Devem incluir as coordenadas de linhas e colunas, como nos tabuleiros do Xadrez.
Os números das linhas ocupam dois espaços (justificado à direita).
As letras das colunas são separadas por um espaço, havendo três espaços à esquerda do 'a'.
Para fazer as linhas dos traços usar os caracteres │ ─ └ (façam copy-paste destes, não usem os | e - do teclado)
Há uma mudança de linha também na última linha, i.e., a linha que tem as coordenadas das colunas.
eValida, recebe uma partida e uma jogada, e verifica se a jogada dada é válida de efetuar na partida dada, de acordo com as regras do jogo.
fazerJogada, recebe uma partida e uma jogada válida, e produz uma nova partida que decorre de jogar a jogada dada na partida dada.
imprimirLances, dada uma partida, retorna numa string as jogadas usando coordenadas como no xadrez (a coluna é dada por letras começando no 'a', a linha por números começando no '1').
As jogadas devem ser apresentadas em grupos de 10, cada grupo numa coluna.
Cada jogada deve ser apresentada no formato num. jogada, onde num é o número da jogada e ocupa três espaços (justificado à direita), um espaço a seguir ao ponto, e jogada é a coordenada da respetiva jogada e ocupa três espaços (justificado à esquerda).
Deve haver um espaço extra de separação entre cada par de colunas.
A primeira jogada, que representa a posição inicial da bola, não deve ser mostrada.
Conferir os exemplos dados nos testes para esclarecimento destes requisitos.
proximasJogadas, dada uma partida, retorna uma lista com as jogadas válidas que se podem realizar.
eFim, dada uma partida verifica se esta terminou, de acordo com as regras do jogo
vencedor, dada uma partida terminada, retorna 1 se ganhou o primeiro jogador, ou 2 se ganhou o segundo jogador.
