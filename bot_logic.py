import discord
from discord.ext import commands
from utilis import gen_pass
from Emoji import gen_emodji


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def generate_password(ctx, length: int):
    try:
        password = gen_pass(length)
        await ctx.send(f'Generated password: {password}')
    except Exception as e:
        await ctx.send(f'Error: {e}')

@bot.command()
async def gen_emoji(ctx, length: int):
    emoji_sequence = gen_emodji(length)
    await ctx.send(f'This is your emoji sequence: {emoji_sequence}')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("heh" * count_heh)

bot.run("token va aqui") 
