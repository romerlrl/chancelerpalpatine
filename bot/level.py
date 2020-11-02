import discord
import random
import json
import os
import time
from discord.ext import commands
from bot import client
from bot.utils import IdParaNome

@client.event
async def on_member_join(member):
    with open('users.json', 'r') as f:
        users = json.load(f)

        await update_data(users, member)

    with open('users.json', 'w') as f:
        json.dump(users, f)

@client.event
async def on_message(message):
    if message.content.lower().startswith('odeio'):
        await message.channel.send('Sim, deixe o ódio fluir por você... <:sheev:735473486046298173>')

    if message.content.lower().startswith('ban'):
        await message.channel.send('Mate-o, mate-o agora...')

    if message.content.lower().startswith('i shouldnt'):
        await message.channel.send('DEW IT!')

    if message.content.lower().startswith('i shouldn\'t'):
        await message.channel.send('DEW IT!')

    if message.content.lower().startswith('-poll'):
        await message.channel.send('Eu amo democracia!')

    if message.content.lower().startswith('votação'):
        await message.channel.send('Eu amo democracia!')

    if message.content.lower().startswith('voto'):
        await message.channel.send('Eu amo democracia!')

    if message.content.lower().startswith('democracia'):
        await message.channel.send('Eu amo democracia!')

    if message.content.lower().startswith('estou muito fraco'):
        await message.channel.send('PODER ILIMITADOOOOOO!')

    if message.content.lower().startswith('você é muito sábio'):
        await message.channel.send('Já ouviu a tragédia de Darth Plagueis, o sábio?')

    if message.content.lower().startswith('tão sábio'):
        await message.channel.send('Já ouviu a tragédia de Darth Plagueis, o sábio?')

    if message.content.lower().startswith('sábio'):
        await message.channel.send('Já ouviu a tragédia de Darth Plagueis, o sábio?')

    with open('users.json', 'r') as f:
        users = json.load(f)

        if message.author.bot:
            return

        else:

            await update_data(users, message.author)
            exp = random.randint(5, 15)
            await add_xp(users, message.author, exp)
            await level_up(users, message.author, message.channel)

        with open('users.json', 'w') as f:
            json.dump(users, f)

        await client.process_commands(message)

async def update_data(users, user):
    if not str(user.id) in users:
        users[str(user.id)] = {}
        users[str(user.id)]['experiencia'] = 0
        users[str(user.id)]['level'] = 1
        users[str(user.id)]['ultima_mesg'] = 0
        users[str(user.id)]['id'] = user.id

async def add_xp(users, user, xp):
    if time.time() - users[str(user.id)].get('ultima_mesg', 0) > 40:
        users[str(user.id)]['experiencia'] += xp
        users[str(user.id)]['ultima_mesg'] = time.time()
    else:
        return

async def level_up(users, user, channel):
    experiencia = users[str(user.id)]['experiencia']
    level_start = users[str(user.id)]['level']
    level_end = int(experiencia **(1/4))

    if level_start < level_end:
        if os.environ.get("chanceler"):
            await channel.send('{} subiu ao nível {}! Assistiremos sua carreira com grande interesse.'.format(user.mention, level_end))
        users[str(user.id)]['level'] = level_end


@client.command(aliases=['nivel'])
async def level(ctx, argumento):
    #O IdParaNome supostamente deveria validar a entrada do usuário.
    #Não tá funcionando.
    user_id = IdParaNome(argumento)
    if user_id == "Fulcrum":
        user_id = str(ctx.author.id)
    else:
        user_id = int(argumento)
    '''if len(message.content)!=8:
        new_id=message.content[9:]
        if not(new_id.isdigit()):
            new_id=messsage.mentions[0]
            #Abre condicional para caso o valor em mention seja None não der ruim.
            if isinstance(new_id, Member):
                new_id=str(new_id.id)
            else:
                #Mais para frente, vamos tentar mexer no querry para
                #pegar alguém com nome parecido caso ninguém tenha sido
                #mencionado. Por enquanto, retorna "foo".
                new_id="foo"
        
        if new_id in users:
            user_id = new_id
            '''
    
    '''if argumento.isdigit():
        user_id = str(argumento)'''
    with open('users.json', 'r') as f:
        users = json.load(f)
        try:
            descricao=f'{users[str(user_id)]["nome"]} se encontra atualmente no nível {users[str(user_id)]["level"]} com {users[str(user_id)]["experiencia"]}'
        except:
            descricao=f'{ctx.author.mention} se encontra atualmente no nível {users[str(ctx.author.id)]["level"]} com {users[str(ctx.author.id)]["experiencia"]}'
        levelbed = discord.Embed(title='Nível', description=descricao, colour=discord.Color.red(), timestamp=ctx.message.created_at)
        levelbed.set_thumbnail(url='https://cdn.discordapp.com/attachments/676574583083499532/752314249610657932/1280px-Flag_of_the_Galactic_Republic.png')
        await ctx.send(embed=levelbed)

                                 
@client.command(aliases=['board','rrank'])
async def rank(ctx, pagina=0):
    user_id = str(ctx.author.id)
    with open('users.json', 'r') as f:
        users = json.load(f)
    pos_do_solicitante=-1
    if user_id in users:
        pos_do_solicitante=0
    rank = [(value['experiencia'], key) for key, value in users.items()]
    rank.sort(reverse=True)
    #msg = '\n '.join([str(x[1]['experiencia']) for x in rank]) Muito bonito, mas não entendi nada.
    #print(rank)
    
    if pos_do_solicitante+1:
        while rank[pos_do_solicitante][1]!=user_id:
            pos_do_solicitante+=1
    msg= f'\n::: Posição de {ctx.author.name} é {pos_do_solicitante+1} :::\n'    
    msg+='::: Ranking do Palpatine :::```'
    for totXp, pessoa in rank[pagina*5:(pagina+1)*5]:
        msg+='\n'+IdParaNome(pessoa).ljust(40)+str(totXp).rjust(15)
    msg+='```'
    if msg.endswith('``````'):
        msg=msg[:-6] #Para quando acessarem uma página sem elementos.
    await ctx.send(msg)
