import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesion con {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un {bot.user} y fui creado para dar consejos de la contaminacion!')
consejos = [
    'Usa bolsas reutilizables para tus compras',
    'Evita los productos de un solo uso como sorbetes y cubiertos de plastico',
    'Evita quemar la basura',
    'Usa botellas retornables',
    'Usa bicicletas o camina para reducir la produccion del dioxido de carbono y otros gases nocivos',
    'Usa residuos organicos como fertilizante para las plantas',
    'Reduce el consumo de energia en tu casa',
    'Planta arboles para ayudar al ecosistema'
]

@bot.command()
async def imagen(ctx):
    todas_las_imagenes = os.listdir("contaminacion_img")
    img_name = random.choice(todas_las_imagenes)
    with open(f'contaminacion_img/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def consejodeldia(ctx):
    consejo = random.choice(consejos)
    await ctx.send(consejo)

# Funcion que explica que es la contaminacion
@bot.command()
async def contaminacion(ctx):
    definicion = "La contaminación ambiental es la presencia de componentes nocivos, bien sean de naturaleza biológica, química o de otra clase, en el medioambiente, de modo que supongan un perjuicio para los seres vivos que habitan un espacio."
    await ctx.send(definicion)

#bot.run("token here")
