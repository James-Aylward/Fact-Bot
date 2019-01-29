import discord
from discord.ext import commands
import requests

bot = commands.Bot(command_prefix='+', description="Fact bot!")

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""


@bot.event
async def on_ready():
    print('Logged in as')
    print(discord.__version__)
    print(bot.user.name)
    print(bot.user.id)
    print('-------------')


@bot.command()
async def halp(ctx):
    embed = discord.Embed(title="Fact Bot", description="Learn stuff by getting off-topic!", color=0xeee657)

    embed.add_field(name="+fact", value="Learn something!", inline=False)
    embed.add_field(name="+info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="+halp", value="Gives this message", inline=False)

    await ctx.send(embed=embed)


@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Fact Bot", description="Learn stuff by getting off-topic!", color=0xeee657)
    embed.add_field(name="Author", value="James Aylward")
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")
    embed.add_field(name="Invite", value="[Invite link](https://discordapp.com/api/oauth2/authorize?client_id=440403009076199426&permissions=8&scope=bot)")

    await ctx.send(embed=embed)


@bot.command()  # Adds two numbers together
async def fact(ctx):
    page = requests.get("http://randomfactgenerator.net")
   
    start = "id=\'z\'>"
    end = "<br/>"
    
    fact = find_between(page.text, start, end)
    print(fact)
    await ctx.send(fact);


bot.run("TOKENHERE"); # Token
