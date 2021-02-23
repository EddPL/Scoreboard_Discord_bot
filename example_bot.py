import discord
import os

from discord.ext import commands
intents = discord.Intents().all()

bot = commands.Bot(command_prefix="$",intents=intents)

valid_users = [176866082307440640,274306047420923906,183351979873927168,352599288926175247,200753518682832897,291354881715863553,692433973950808184,277261629941350400,339607828442513419,291595988353679370,211610922492362752,431953383612481537,382679971631464450]
team1 = []
team2 = []
score = {}

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def vendredi(ctx):
    global score
    await ctx.channel.send("Voyons voir qui a perdu le plus de vendredi fou...")

    sorted_score = {}
    sorted_keys = sorted(score,key=score.get)

    for w in sorted_keys:
        sorted_score[w] = score[w]
        
    score = sorted_score
    for name in score:
        await ctx.channel.send(name+" : "+str(score[name]))

@bot.command()
async def logout(ctx):
    await ctx.channel.send("C'est off bye.")
    await bot.logout()

@bot.command()
async def maketeams(ctx):
    global team1
    global team2

    voice1 = bot.get_channel(461400620515983360)
    voice2 = bot.get_channel(461400745288400946)

    team1 = []
    team2 = []

    m1 = voice1.members
    m2 = voice2.members

    for member in m1:
        team1.append(member.id)
    
    for member in m2:
        team2.append(member.id)

@bot.command()
async def addplayer(ctx,arg):
    if arg not in valid_users:   
        valid_users.append(arg)

@bot.command()
async def showplayers(ctx):
    global valid_users

    for user_id in valid_users:
        await ctx.channel.send(bot.get_user(user_id).name)

@bot.command()
async def showteams(ctx):
    global team1
    global team2 

    await ctx.channel.send("Team 1 :")
    for player in team1:
        await ctx.channel.send(bot.get_user(player).name)
    await ctx.channel.send("Team 2 :")
    for player in team2:
        await ctx.channel.send(bot.get_user(player).name)
    
@bot.command()
async def win(ctx,team):
    global team1
    global team2

    if team in ["team1","1","Team1"]:
        await ctx.channel.send("Victoire de team 1")
        for user_id in team1:
            if bot.get_user(user_id).name not in score:
                score[bot.get_user(user_id).name] = 1
            else:
                score[bot.get_user(user_id).name] += 1

    if team in ["team2","2","Team2"]:
        await ctx.channel.send("Victoire de team 2")
        for user_id in team2:
            if bot.get_user(user_id).name not in score:
                score[bot.get_user(user_id).name] = 1
            else:
                score[bot.get_user(user_id).name] += 1

bot.run('ODEzNTMzMDIzMDU5MzEyNjQy.YDQrqw.cnHqG-zsDu3wvnemPsqkh3FRljU')