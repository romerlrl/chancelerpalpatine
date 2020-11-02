import discord
import random
import json
import os
import time
from discord.ext import commands

    
@client.event
async def sugestao():
    pass


'''
O arquivo deve ter esse nome para não dar conflito com a biblioteca que importamos
A ideia do trelloBot era
1. .p!sugerir: permitir que as sugestões fossem automaticamente para a caixa de sugestões do trello
(não automaticamente, a staff do bot precisaria dar um joinha para evitar flood.
2. .p!sugestoes: Exibir a lista de sugestões quando solicitado 
Usaríamos a biblioteca trello (obtida via pip install py-trello) para isso, são
necessárias duas chaves para usá-las, que são explicadas aqui:
https://medium.com/@rafael.dourado/utilizando-a-api-do-trello-com-python-740583e6ab27
e aqui
http://devblog.drall.com.br/como-obter-a-key-e-token-de-um-usuario-no-trello
Não seria necessário despejar atualizações do Trello no Discord, um webhook daria conta disso.


A documentação da API se encontra em
https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/#boards

Os dados da listas e do board podem ser obtidos nesse json:
https://trello.com/1/boards/5f5a5b6819f2a8470276a5ed/lists

Uma dúvida bem parecida o item 1.
https://stackoverflow.com/questions/58156721/how-do-you-use-the-trello-api-to-add-a-new-card-in-python

O problema que me fez parar o trabalho foi:
AttributeError: 'str' object has no attribute 'fetch_json'
O erro subia no meio da execução de quase todos os métodos de Board. Sem condições para
prosseguir.

Solução temporária possível é fazer um sugestões como um p!myvoice qe irá jogar para um CANAL EXCLUSIVO
para sugestões no Senado ou outro server. Podendo ou não exigir aprovação prévia antes de ser encaminhado. 
Uma planilha ou doc no google drive também seriam eficiente, mas sabedoRISEmente, Rise não compartilha
seu email conosco.
'''


TRELLO_APP_KEY = os.environ.get(API_KeyTrello)     #your trello key
TOKEN = os.environ.get(TokenTrello)                #your api token
print(GET /1/members/me/boards)
'''listID = ""             #the id for your list 
cardPos = "top"         #'top', 'bottom', or a number

trello = TrelloApi(TRELLO_APP_KEY, TOKEN)
newCard = trello.cards.new("My Card", idList=listID, desc="my card description", pos=cardPos)

print(newCard)    #above returns json details of the card just created
'''
