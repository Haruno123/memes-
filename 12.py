import discord
from discord.ext import commands
import random
import asyncio
import os
import requests
import json

url = 'https://kitsu.io/api/edge/anime?filter[text]=tokyo'
response = requests.get(url)
data = response.json()

print(json.dumps(data, indent=4))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Tu bot está en linea: {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    imagen = random.choice(os.listdir('imagenes'))
    with open(f'imagenes/{imagen}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_TOKIO_image_url():
    url1 = 'https://kitsu.io/api/edge/anime?filter[text]=tokyo'
    res = requests.get(url1)
    data = res.json()
    # Seleccionar una imagen aleatoria de los resultados
    random_anime = random.choice(data['data'])
    return random_anime['attributes']['posterImage']['original']

@bot.command(name='TOKIO')
async def TOKIO(ctx):
    image_url1 = get_TOKIO_image_url()
    await ctx.send(image_url1)

# Función para seleccionar un meme con rareza
def select_meme_with_rarity(meme_list):
    weighted_memes = []
    for meme in meme_list:
        rarity = 1  # Cambiar a 2, 3, etc. para aumentar la rareza de ciertos memes
        weighted_memes.extend([meme] * rarity)
    return random.choice(weighted_memes)

# Comando para memes temáticos
@bot.command(name='animales')
async def animales(ctx):
    imagenes = os.listdir('imagenesanimales')
    meme = select_meme_with_rarity(imagenes)
    with open(f'imagenesanimales/{meme}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command(name='memes_clasicos')
async def memes_clasicos(ctx):
    imagenes = os.listdir('imagenesmemes_clasicos')
    meme = select_meme_with_rarity(imagenes)
    with open(f'imagenesmemes_clasicos/{meme}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def guess(ctx):
    await ctx.send('Guess a number between 1 and 10.')

    def is_correct(m):
        return m.author == ctx.author and m.content.isdigit()

    answer = random.randint(1, 10)

    try:
        guess = await bot.wait_for('message', check=is_correct, timeout=5.0)
    except asyncio.TimeoutError:
        return await ctx.send(f'Sorry, you took too long it was {answer}.')

    if int(guess.content) == answer:
        await ctx.send('You are right!')
    else:
        await ctx.send(f'Oops. It is actually {answer}.')



bot.run("token")