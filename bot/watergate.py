import discord
import random
import json
import os
import time
from discord.ext import commands
from bot import client
from datetime import datetime

if not(os.environ.get("impressorabrr")):
    def print(*args): return None
    
def prinny(message):
    print('\n\n')
    print(f"::: De: {message.author.name}")
    print(f"::: {str(message.created_at)}")
    print(message.content)
    #print('*'*3, str(message), "*"*3)
    return None

@client.command(alias=['v'])
async def myvoice(ctx, *args):
    if isinstance(args[0], list): args=args[0]
    owners = {272479833341034507,   #Thales
              279432001621065735,   #Romer
              392159980016369665,   #Rise
              417713728126058498,   #Caleb É um easteregg que ele nunca descobriu
              }
    if ctx.author.id in owners:
        channel = client.get_channel(384148772826906624)
        msg=" ".join(args)
        condicoes=[len(args[0])==18, args[0].isdigit(), ctx.author.id!=417713728126058498]
        if all(condicoes):
            channel = client.get_channel(int(args[0]))
            msg=msg[18:]
        msg+=f"  ({ctx.author.id})"
        await channel.send(msg)

#770527971509141504 Sugestões do Senado, o ideal é ir para o 21 dez ou direto para o Trello
@client.command(alias=['sg'])
async def sgt(ctx, *args):
    channel = client.get_channel(770527971509141504)
    msg=f"Sugestão de {ctx.author.name}\n\n\n"
    msg+=" ".join(args)
    await channel.send(msg)
    await ctx.send("Seria de grande valor. Pode ser feito?")
    
    
@client.command(alias=['h'])
async def hw(ctx, *args):
    print(os.environ.get('chanceler'))
    counter = 0
    channel=client.get_channel(384148772826906624)
    async for message in channel.history(limit=20):
        prinny(message)
    print("Olá mundo")



@client.command(aliases=['debugging'])
async def pp(ctx, *args):
    #print(help(client.get_all_members))
    #print(dir(client.get_all_members))
    #print(list(client.get_all_members()))
    dicio=dicioMembros[1]
    print(args)
    if len(args)==1:
        args=args[0]
    else:
        args=" ".join(args)

    #print(ctx.content)
    user=(get(client.get_all_members(), name=args))
    if user:
        print(f"Ok, {user}")
    print("táqui nao")

'''
    Um dicionário ID <-> Nome poupará bastante poder computacional
'''
def dicioMembros():
    dicioIDs=dict()
    dicioNomes=dict()
    print(list(client.get_all_members()))
    #print(dict(client.get_all_members()))
    for x in (client.get_all_members()):
        print(x)
        print(x.id)
        dicioIDs[x.id] = x.name
        dicioNomes[x.name]=x.id
    print(dicioIDs)
    print('\n'*5)
    print(dicioNomes)
    return dicioIDs, dicioNomes

@client.command()
async def t1(ctx, argumento=True):
    dicioMembros()
    pass



