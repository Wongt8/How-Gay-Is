"""
Name : How Gay is ?
Version : 1.0
Auteur : Wongt8
"""
import discord,random,asyncio
from discord.ext import tasks
from itertools import cycle
from discord.ext import commands

TOKEN = ""

    #       rouge      orange    jaune      vert     blue      violet
cols = [0xff0000, 0xff8800, 0xfbff00, 0x43990a, 0x0028c7, 0x6d00c7]

client = commands.Bot(command_prefix = "*")

@client.event
async def on_ready():
    print("Connected as : ")
    print(f"{client.user.name}#{client.user.discriminator}")
    print(client.user.id)
    print("-----------------")
    await client.change_presence(activity=discord.Game(name='*rule for help !'))


@client.command(aliases=['gay'])
async def gayzouze(ctx,*mess):
    message = " ".join(mess)
    if "luc" in message.lower():

        embed=discord.Embed(title="Total Gayzouze", description=f"{message} est 100% Gay !",color=0xff0000)
        embed.set_thumbnail(url="https://cdn1.iconfinder.com/data/icons/major-world-flags-1/512/lgbt-gay-bisexual-transgender-lesbian-rainbow-pride-512.png")
        msg = await ctx.send(embed=embed)

        for i in range(1000):
            embed2=discord.Embed(title="Total Gayzouze", description=f"{message} est 100% Gay !",color=cols[i%len(cols)])
            embed2.set_thumbnail(url="https://cdn1.iconfinder.com/data/icons/major-world-flags-1/512/lgbt-gay-bisexual-transgender-lesbian-rainbow-pride-512.png")
            await asyncio.sleep(1)
            await msg.edit(embed=embed2)

    else :
        random.seed(message)
        embed=discord.Embed(title="Total Gayzouze", description=f"{message} est {random.randint(0,100)}% Gay !",color=random.choice(cols))
        embed.set_thumbnail(url="https://cdn1.iconfinder.com/data/icons/major-world-flags-1/512/lgbt-gay-bisexual-transgender-lesbian-rainbow-pride-512.png")
        await ctx.send(embed=embed)

@client.command(aliases=['rule'])
async def helpRule(ctx,*message):

    embed=discord.Embed(title="Pour utiliser le bot",color=0xff0000)
    embed.set_thumbnail(url="https://cdn1.iconfinder.com/data/icons/major-world-flags-1/512/lgbt-gay-bisexual-transgender-lesbian-rainbow-pride-512.png")
    embed.add_field(name=f"Calculer le % de gay", value="*gay <message>", inline=False)
    embed.set_footer(text="Bot by Wongt8")
    msg = await ctx.send(embed=embed)

    for i in range(1000):
        embed2=discord.Embed(title="Pour utiliser le bot",color=cols[i%len(cols)])
        embed2.set_thumbnail(url="https://cdn1.iconfinder.com/data/icons/major-world-flags-1/512/lgbt-gay-bisexual-transgender-lesbian-rainbow-pride-512.png")
        embed2.add_field(name=f"Calculer le % de gay", value="*gay <message>", inline=False)
        embed2.set_footer(text="Bot by Wongt8")
        await asyncio.sleep(1)
        await msg.edit(embed=embed2)


client.run(TOKEN)