import random
import discord
from discord.ext import commands

# 봇 기본 설정 (프리픽스: !)
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# 봇이 켜졌을 때 실행되는 이벤트
@bot.event
async def on_ready():
    print(f'{bot.user.name} 봇이 성공적으로 온라인이 되었습니다!')

# 1. '!안녕' 명령어
@bot.command(name='안녕')
async def hello(ctx):
    await ctx.send('안녕하세요!')

# 2. '!핑' 명령어
@bot.command(name='핑')
async def ping(ctx):
    await ctx.send('퐁!')

# 3. '!주사위' 명령어
@bot.command(name='주사위')
async def dice(ctx):
    number = random.randint(1, 6)
    await ctx.send(f'🎲 주사위를 던져서 **{number}**가 나왔습니다!')

# 토큰 분할 설정 (줄바꿈 에러 방지)
t1 = 'MTU2NzUzMjQzMzU5ODA1ODQ5Ng.GXHW_c.'
t2 = 'aCdVkJw0moS8coWT3pEDlXLd1K1jVSayPr0ODo'

bot.run(t1 + t2)
