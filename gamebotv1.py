# bot.py
import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='.')

@bot.command(name='create', help='Create a Character.')
async def create_char(ctx):
    char_tot_stats = 0
    while char_tot_stats < 20:
        char_hp = random.choice(range(1, 6)) + 6
        char_atk = random.choice(range(1, 6))
        char_def = random.choice(range(1, 6))
        char_spd = random.choice(range(1, 6))
        char_rcv = random.choice(range(1, 6))
        char_tot_stats = char_hp + char_atk + char_def + char_spd + char_rcv

    file = open("files/charstats/charstats.csv", "w")
    writeToFile = file.write(str(char_hp) + "," + str(char_atk) + "," + str(char_def) + "," + str(char_spd) + "," + str(char_rcv))
    file.close()

    await ctx.send(
        'HP: ' + str(char_hp) +
        '\nAtk: ' + str(char_atk) + '\tDef: ' + str(char_def) +
        '\nSpd: ' + str(char_spd) + '\tRCV: ' + str(char_rcv)
    )

@bot.command(name='checkstats')
async def checkstats(ctx):
    file = open("files/charstats/charstats.csv", "r")
    content = file.read()
    list = content.split(",")
    if int(list[0]) + int(list[1]) + int(list[2]) + int(list[3]) + int(list[4]) < 45:
        villagerText = str("You weak ass bitch.")
    else:
        villagerText = str("What a strong Hero!")
    await ctx.send(
        'HP: ' + str(list[0]) +
        '\nAtk: ' + str(list[1]) + '\tDef: ' + str(list[2]) +
        '\nSpd: ' + str(list[3]) + '\tRCV: ' + str(list[4]) +
        '\n' + villagerText
    )


@bot.command(name='eat')
async def eat(ctx):

    file = open("files/charstats/charstats.csv", "r")
    readHealthStat = file.read()
    cStat = readHealthStat.split(",")
    healthStat = int(cStat[0])
    newHealthStat = healthStat + 2
    file.close()

    file = open("files/charstats/charstats.csv", "w")
    upgradeHealthStat = file.write(str(newHealthStat) + "," + str(cStat[1]) + "," + str(cStat[2]) + "," + str(cStat[3]) + "," + str(cStat[4]))
    file.close()

    file = open("files/charstats/charstats.csv", "r")
    readTheFile = file.read()
    newStats = readTheFile.split(",")
    await ctx.send(
        'You ate a hearty meal. +2 to HP.\n'
        'HP: ' + str(newStats[0]) +
        '\nAtk: ' + str(newStats[1]) + '\tDef: ' + str(newStats[2]) +
        '\nSpd: ' + str(newStats[3]) + '\tRCV: ' + str(newStats[4])
    )

@bot.command(name='lift')
async def lift(ctx):

    file = open("files/charstats/charstats.csv", "r")
    readAttackStat = file.read()
    cStat = readAttackStat.split(",")
    attackStat = int(cStat[1])
    newAttackStat = attackStat + 1
    file.close()

    file = open("files/charstats/charstats.csv", "w")
    upgradeAttackStat = file.write(str(cStat[0]) + "," + str(newAttackStat) + "," + str(cStat[2]) + "," + str(cStat[3]) + "," + str(cStat[4]))
    file.close()

    file = open("files/charstats/charstats.csv", "r")
    readTheFile = file.read()
    newStats = readTheFile.split(",")
    await ctx.send(
        'You lift some weights. +1 to Atk.\n'
        'HP: ' + str(newStats[0]) +
        '\nAtk: ' + str(newStats[1]) + '\tDef: ' + str(newStats[2]) +
        '\nSpd: ' + str(newStats[3]) + '\tRCV: ' + str(newStats[4])
    )


@bot.command(name='rocks')
async def rocks(ctx):

    file = open("files/charstats/charstats.csv", "r")
    readDefenseStat = file.read()
    cStat = readDefenseStat.split(",")
    defenseStat = int(cStat[2])
    newDefenseStat = defenseStat + 1
    file.close()

    file = open("files/charstats/charstats.csv", "w")
    upgradeDefenseStat = file.write(str(cStat[0]) + "," + str(cStat[1]) + "," + str(newDefenseStat) + "," + str(cStat[3]) + "," + str(cStat[4]))
    file.close()

    file = open("files/charstats/charstats.csv", "r")
    readTheFile = file.read()
    newStats = readTheFile.split(",")
    await ctx.send(
        'You throw rocks at yourself. +1 to Def.\n'
        'HP: ' + str(newStats[0]) +
        '\nAtk: ' + str(newStats[1]) + '\tDef: ' + str(newStats[2]) +
        '\nSpd: ' + str(newStats[3]) + '\tRCV: ' + str(newStats[4])
    )

@bot.command(name='run')
async def run(ctx):

    file = open("files/charstats/charstats.csv", "r")
    readSpeedStat = file.read()
    cStat = readSpeedStat.split(",")
    speedStat = int(cStat[3])
    newSpeedStat = speedStat + 1
    file.close()

    file = open("files/charstats/charstats.csv", "w")
    upgradeSpeedStat = file.write(str(cStat[0]) + "," + str(cStat[1]) + "," + str(cStat[2]) + "," + str(newSpeedStat) + "," + str(cStat[4]))
    file.close()

    file = open("files/charstats/charstats.csv", "r")
    readTheFile = file.read()
    newStats = readTheFile.split(",")
    await ctx.send(
        'You run a mile. +1 to Spd.\n'
        'HP: ' + str(newStats[0]) +
        '\nAtk: ' + str(newStats[1]) + '\tDef: ' + str(newStats[2]) +
        '\nSpd: ' + str(newStats[3]) + '\tRCV: ' + str(newStats[4])
    )

@bot.command(name='heal')
async def heal(ctx):

    file = open("files/charstats/charstats.csv", "r")
    readRecoveryStat = file.read()
    cStat = readRecoveryStat.split(",")
    recoveryStat = int(cStat[4])
    newRecoveryStat = recoveryStat + 1
    file.close()

    file = open("files/charstats/charstats.csv", "w")
    upgradeRecoveryStat = file.write(str(cStat[0]) + "," + str(cStat[1]) + "," + str(cStat[2]) + "," + str(cStat[3]) + "," + str(newRecoveryStat))
    file.close()

    file = open("files/charstats/charstats.csv", "r")
    readTheFile = file.read()
    newStats = readTheFile.split(",")
    await ctx.send(
        'You help out at the local hospital. +1 to RCV.\n'
        'HP: ' + str(newStats[0]) +
        '\nAtk: ' + str(newStats[1]) + '\tDef: ' + str(newStats[2]) +
        '\nSpd: ' + str(newStats[3]) + '\tRCV: ' + str(newStats[4])
    )
bot.run(TOKEN)
