import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

from bot.chess.chess import Chess
    
load_dotenv()

client = discord.Client()

prefixo= 'sp!'
if os.environ['chanceler']:
    prefixo= 'cp!'
client = commands.Bot(command_prefix = prefixo)

chess_bot = Chess()
chess_bot.load_games()
