import os
import sys

'''
    Parâmetros de entrada:
        -c Entra com o Chanceler, default Senador
        -l Imprime coisas no terminal 
        -s Habilita o startswith
'''
os.environ['chanceler']=' '*int('-c' in sys.argv)
os.environ['impressorabrr']=' '*int('-l' in sys.argv) #é L, não 1.
os.environ['romer']=' '*int(os.getlogin()=='lucas')
os.environ['startswith']=' '*int('-s' in sys.argv)

from dotenv import load_dotenv

from bot import client
from bot.bot import *
from bot.chess_cmds import *
from bot.level import *
#from bot.akinator_cmds import *
from bot.watergate import *

load_dotenv()


if os.environ.get("chanceler"):
    sys.stdout.write("Chanceler\n")
    client.run(os.environ.get("API_KEYc"))
    
else:
    sys.stdout.write("Senador\n")
    client.run(os.environ.get("API_KEYs"))

