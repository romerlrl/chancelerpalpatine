import inspect
import discord
import random
import json
import os
import time
from discord.ext import commands
from bot import client, chess_bot


'''
/tabs
:hash:	:one:	:two:	:three:	:hash:
:regional_indicator_a:	:negative_squared_cross_mark:	:o2:	:negative_squared_cross_mark:	:regional_indicator_a:
:regional_indicator_b:	:negative_squared_cross_mark:	:o2:	:o2:	:regional_indicator_a:
:regional_indicator_c:	:negative_squared_cross_mark:	:negative_squared_cross_mark:	:o2:	:regional_indicator_c:
:hash:	:one:	:two:	:three:	:hash:
'''

def imprimeMatriz(matriz, online):
    abc=":hash::regional_indicator_a::regional_indicator_b::regional_indicator_c::hash:"
    num=(":one:", ":two:", ":three:")
    possibilidades=['blue_square', 'regional_indicator_x',  'regional_indicator_o']
    #abc="* A B C *"
    #num=("1", "2", "3")
    strMatriz=abc
    strMatriz+='\n'
    for x, emoji in enumerate(num):
        strMatriz+=emoji
        for y in range(3):
            strMatriz+=f'{possibilidades[matriz[x][y]]}'
        strMatriz+=emoji
        strMatriz+='\n'
    strMatriz+=abc
    if online:
        M= discord.Embed(title='Tabuleiro', description=strMatriz, colour=discord.Color.blurple(), timestamp=ctx.message.created_at)
        ctx.send(embed=M)
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
    


def leentrada(matriz, player, movimento=None):
    print("vez do ", player[1])
    BotaPeça=input()
    if not(movimento):
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
            

 
@client.command()
async def imprimeTabuleiroJogoDaVelha(ctx):
    foo=imprimeMatriz([[':blue_square:', ':blue_square:', ':blue_square:'], [':blue_square:', ':blue_square:', ':blue_square:'], [':blue_square:', ':blue_square:', ':blue_square:']])
    M= discord.Embed(title='Tabuleiro', description=foo, colour=discord.Color.blurple(), timestamp=ctx.message.created_at)
    await ctx.send(embed=M)       

@client.command()
async def jv(ctx, movimento):
    with open('velha.json', 'r') as f:
        if ctx.author.id in f['jogadores']:
            numero_do_jogo=f['jogadores'][ctx.author.id]
            raw_matriz=f['jogos']['numero_do_jogo']['matriz']
            turno= int(f['jogos']['numero_do_jogo']['turno'])*2-1
            turno=(turno, ctx.author.name)
            matriz, vitoria, invalido=leentrada(matriz, jogador, movimento)
            if vitoria:
                ctx.send(f"Parabéns, <@{ctx.author.id}> venceu")
            elif invalido:
                ctx.send(invalido)
            else:
                turno2=((f['jogos']['numero_do_jogo']['turno'])+1)%2
                f['jogos']['numero_do_jogo']['turno']=turno2
                imprimeMatriz(matriz, 1)
            
                
            
            
        f['jogadores'][ctx.author.id]=numero_do_jogo
        f['jogos'][numero_do_jogo]={"matriz":[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
				"canal":ctx.channel.id,
				"jogador1":str(ctx.author.id),
                
				"jogador2":"", 
                "aberto":1,
				"turno":"0",
				"hora":"0"}

        with open('velha.json', 'w') as f:
            json.dump(velha, f)
    ctx.send(f"Para aceitar o jogo "cp!AceitaConvite {numero_do_jogo}")

    

@client.command()
async def CriaConvite(ctx):
    #Cria um tabuleiro em branco no json e registra o jogador 1.
    
    with open('velha.json', 'r') as f:
        numero_do_jogo=max(f['jogos'])+1
        f['jogadores'][ctx.author.id]=numero_do_jogo
        f['jogos'][numero_do_jogo]={"matriz":[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
				"canal":ctx.channel.id,
				"jogador1":str(ctx.author.id),
                
				"jogador2":"", 
                "aberto":1
				"turno":"0",
				"hora":"0"}

        with open('velha.json', 'w') as f:
            json.dump(velha, f)
    ctx.send(f"Para aceitar o jogo "cp!AceitaConvite {numero_do_jogo}")

    pass
    
@client.command()
async def AceitaConvite(ctx, numero_do_jogo):
    with open('velha.json', 'r') as f:
        if numero_do_jogo in f['jogos'] and f['jogos'][numero_do_jogo]['aberto']:
            f['jogos'][numero_do_jogo]['aberto']=0
            f['jogos'][numero_do_jogo]['jogador2']=str(ctx.author.id)
            f['jogadores'][ctx.author.id]=numero_do_jogo
            ctx.send(f"Desafio aceito, <@{f['jogos'][numero_do_jogo]['jogador2']}>")
        else:
            ctx.send("Jogo não disponível")
            
        numero_do_jogo=max(f['jogos'])+1
        f['jogadores'][ctx.author.id]=numero_do_jogo
        f['jogos'][numero_do_jogo]={"matriz":[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
				"canal":ctx.channel.id,
				"jogador1":str(ctx.author.id),
				"jogador2":"", 
                "aberto":1
				"turno":"0",
				"hora":"0"}

        with open('velha.json', 'w') as f:
            json.dump(velha, f)
    ctx.send(f"Para aceitar o jogo "cp!AceitaConvite {numero_do_jogo}")



    
if __name__ == '__main__':
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
        partida : lista'''
