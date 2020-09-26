'''
/tabs
:hash:	:one:	:two:	:three:	:hash:
:regional_indicator_a:	:negative_squared_cross_mark:	:o2:	:negative_squared_cross_mark:	:regional_indicator_a:
:regional_indicator_b:	:negative_squared_cross_mark:	:o2:	:o2:	:regional_indicator_a:
:regional_indicator_c:	:negative_squared_cross_mark:	:negative_squared_cross_mark:	:o2:	:regional_indicator_c:
:hash:	:one:	:two:	:three:	:hash:
'''

def imprimeMatriz(matriz):
    abc=":hash::regional_indicator_a::regional_indicator_b::regional_indicator_c::hash:"
    num=(":one:", ":two:", ":three:")
    #abc="* A B C *"
    #num=("1", "2", "3")
    strMatriz=abc
    strMatriz+='\n'
    for x, emoji in enumerate(num):
        strMatriz+=emoji
        for y in range(3):
            strMatriz+=f'{matriz[x][y]}'
        strMatriz+=emoji
        strMatriz+='\n'
    strMatriz+=abc
    return strMatriz

def EhFimDeJogo(col, lin, matriz, player):
    EhIgual=bool()
    #Testando diagonais
    if col==lin:
        eixo=all([matriz[linha][linha]==player for linha in range(3)])
        if eixo:
            return True
    elif col+lin==2:
        eixo=all([matriz[linha][2-linha]==player for linha in range(3)])
        if eixo:
            return True        
    eixo=all([matriz[linha][col]==player for linha in range(3)])
    if eixo:
        return True
    eixo=all([matriz[coluna][lin]==player for coluna in range(3)])
    if eixo:
        return True
    


def leentrada(matriz, player):
    print("vez do ", player[1])
    BotaPeça=input()
    invalido=str("Jogada Inválida: ")
    if len(BotaPeça)>1:
        if (BotaPeça[0].lower() in 'abc') and ('0'<BotaPeça[1]<'4'):
            lin=ord(BotaPeça[0].lower())-97
            col=int(BotaPeça[1])-1
            print(col, lin)
            if matriz[col][lin]==nulo:
                matriz[col][lin]=player[0]
                venceu=(EhFimDeJogo(col, lin, matriz, player[0]))
                invalido=False
            else:
                invalido+='Essa casa já está ocupada'
            
        else:
            invalido+='Entrada incorreta, declare sua casa como: a1'
    else:
        invalido+="É necessário 2 caracteres no mínimo"
    if invalido:
        print(invalido);
        invalido=(invalido)
        venceu=False
    return (matriz, venceu, invalido) 
            
nulo=':blue_square:'
nulo='_'
matriz=[[nulo, nulo, nulo], [nulo, nulo, nulo], [nulo, nulo, nulo]]
imprimeMatriz(matriz)
segue_o_jogo=9
jogadores=[('o', "Ana"), ('x', 'Bia')]
while segue_o_jogo:
    jogador=jogadores[segue_o_jogo%2]
    matriz, vitoria, invalido=leentrada(matriz, jogador)
    if not(invalido):
        segue_o_jogo-=1
    if vitoria:
        segue_o_jogo=False
        print('*'*15)
        print(f'jogador {jogador[1]} venceu')
        print('*'*15)
    elif not(segue_o_jogo):
        print("Deu velha")    
    print(imprimeMatriz(matriz))

'''No fim de cada lance, deve ser armazendo um json com
    JogadorBola: id
    JogadorXiss: id
    VezDaBola: booleano
    partida : lista
    
    
    
    
