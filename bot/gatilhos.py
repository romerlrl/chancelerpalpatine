import discord
import json
import os
from discord.ext import commands
from bot import client

async def inicio(message):
    #print(message) #nada demais, só diz quem e onde.
    for key, value in referencias.items():
        if message.content.lower().startswith(key):
            await message.channel.send(value)
            return None
    return None

''' Esses são os primeiros passos de deshardcodar o bot,
    Isso não está nem pert de estar pronto, o json de
    gatilhos ainda não existe, deverá ser criado um filtro
    interno por servidor e mais um monte de coisa que eu
    nem pensei a respeito.

'''
#@client.command(aliases=[])
#@commands.has_permissions(manage_messages=True)
async def adicionaGatilho(ctx, *args):
    if False:
        frase=" ".join(args)
        gatilho=frase.find(':')
        chave, valor = frase[:gatilho], frase[gatilho:]
        with open('gatilhos.json', 'r') as f:
            triggerr = json.load(f)
            triggerr[chave]=valor
        with open('gatilhos.json', 'w') as f:
            json.dump(triggerr, f)

#@client.command(aliases=[])
#@commands.has_permissions(manage_messages=True)
async def removeGatilho(ctx, *args):
    if False:
        frase=" ".join(args)
        with open('gatilhos.json', 'r') as f:
            triggerr = json.load(f)
            if frase in triggerr:
                triggerr.pop(frase)
        with open('gatilhos.json', 'w') as f:
            json.dump(triggerr, f)
    


referencias={
    'odeio':'Sim, deixe o ódio fluir por você... <:sheev:735473486046298173>', 
    'ban':'Mate-o, mate-o agora', 
    'i shouldnt':'DEW IT!', 
    'i shouldn\'t':'DEW IT!', 
    '-poll':'Eu amo a democracia', 
    'votacao':'Eu amo a democracia', 
    'voto':'Eu amo a democracia', 
    'democracia':'Eu amo a democracia', 
    'estou muito fraco':'PODER ILIMITADO', 
    'voce é muito sábio':'Já ouviu a tragédia de Darth Plagueis, o sábio?', 
    'tão sabio':'Já ouviu a tragédia de Darth Plagueis, o sábio?' , 
    'sabio':'Já ouviu a tragédia de Darth Plagueis, o sábio?'
    }

