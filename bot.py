import os
from twitchio.ext import commands
import random
import time

bot = commands.Bot(
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

@bot.event
async def event_ready():
    'El Bot ha sido llamado'
    print(f"{os.environ['BOT_NICK']} llego al chat!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me llego al chat!")


@bot.event
async def event_message(ctx):
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower() or ctx.author.name.lower() == 'Nightbot'.lower():
        return

    await bot.handle_commands(ctx)

    # await ctx.channel.send(ctx.content)

    if 'hola' in ctx.content.lower():
        await ctx.channel.send(f"Hola, @{ctx.author.name} bienvenido al MEJOR STREAM 2020 espero te la pases bien!!!")

    if 'chakaflus' in ctx.content.lower():
        await ctx.channel.send("chakaflus")

    if 'juan-carlos' in ctx.content.lower():
        await ctx.channel.send("La mejor combinacion 2020")

    if 'discord' in ctx.content.lower() and 'sigue a nuestro npc favorito en todas sus redes sociales' not in ctx.content.lower():
        await ctx.channel.send("Unete al discord mas cool, discord.gg/TWuEDzT ")
    
    if '?' in ctx.content.lower() and 'youtube.com' not in ctx.content.lower():
        await ctx.channel.send("Contrata a mario")

    true = 'yes'

    while true == 'yes':
        await ctx.channel.send("Hey, ya sigues a Freddy en todas sus redes? no, no lo hiciste, pues te llevas un puño en tu boca")
        time.sleep(1800) 


@bot.command(name="frase")
async def Frase(ctx):
    await ctx.channel.send(random.choice('Te quiero mucho', 'La teoria de la gravedad de Einstein', 'Yo no soy senior, ni mid, ni junior yo soy ingeniero', '¿Todo bien en casa?', 'Mis mods son simps', 'Coño *Inserte persona del chat*') + ' -Freddy 2020.')

@bot.command(name='Source')
async def Source(ctx):
    await ctx.channel.send('Mira como funciono por dentro, https://github.com/scidroid/carlos-el-botsito')
    
uno= 0

dos= 0

tres= 0

cuatro= 0

cinco= 0

@bot.event
async def event_message(ctx):
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower() or ctx.author.name.lower() == 'Nightbot'.lower():
        return

    await bot.handle_commands(ctx)

    # await ctx.channel.send(ctx.content)

    if ctx.content.lower() == 1:
        uno += 1

    if ctx.content.lower() == 2:
        dos += 1

    if ctx.content.lower() == 3:
        tres += 1

    if ctx.content.lower() == 4:
        cuatro += 1

    if ctx.content.lower() == 5:
        cinco += 1


@bot.command(name="resultados")
async def resultados(ctx):
    await ctx.channel.send(f"1 tiene {uno} votos, 2 tiene {dos} votos, 3 tiene {tres} votos, 4 tiene {cuatro} votos, 5 tiene {cinco} votos.")



@bot.command(name="resetvots")
async def resetvots(ctx):
    uno = 0
    dos = 0
    tres = 0
    cuatro = 0
    cinco = 0


if __name__ == "__main__":
    bot.run()