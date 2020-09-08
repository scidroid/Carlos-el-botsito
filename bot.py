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

Frases = ['Te quiero mucho', 'La teoria de la gravedad de Einstein', 'Yo no soy senior, ni mid, ni junior yo soy ingeniero', '¿Todo bien en casa?', 'Mis mods son simps', 'Coño *Inserte persona del chat*']

@bot.command(name="frase")
async def Frase(ctx):
    await ctx.channel.send(random.choice(Frases) + '-Freddy 2020')

@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat.'
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



if __name__ == "__main__":
    bot.run()