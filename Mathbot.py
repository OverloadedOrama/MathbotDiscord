import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

Client = discord.Client()
client = commands.Bot(command_prefix = "")

@client.event
async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')
        
@client.event
async def on_message(message):
        if message.author == client.user: #if the bot itself sent the message, ignore it and return
                return
                
        if message.content.upper().startswith('ADD'):
                args = message.content.split(" ")
                result = 0
                for arg in args[1:]: #starts from the second element of the list, because the first is 'add'
                        arg_f = float(arg) #convert every argument from string to float
                        result += arg_f
                await client.send_message(message.channel, result)

        if message.content.upper().startswith('SUBTRACT'):
                args = message.content.split(" ")
                result = float(args[1]) #we can't use 0, because it would yield wrong results.
                for arg in args[2:]:
                        arg_f = float(arg)
                        result -= arg_f
                await client.send_message(message.channel, result)

        if message.content.upper().startswith('MULTIPLY'):
                args = message.content.split(" ")
                result = 1
                for arg in args[1:]:
                        arg_f = float(arg)
                        result *= arg_f
                await client.send_message(message.channel, result)

        if message.content.upper().startswith('DIVIDE'):
                args = message.content.split(" ")
                result = float(args[1]) #we can't use 1, because it would yield wrong results.
                for arg in args[2:]:
                        arg_f = float(arg)
                        if arg_f == 0:
                                await client.send_message(message.channel, "You can't divide by zero")
                                return
                        else:
                                result /= arg_f
                await client.send_message(message.channel, result)

        if message.content.upper().startswith('POWER'):
                #Power goes from right to left, so it's x^(y^(z^w)) etc
                args = message.content.split(" ")
                result = float(args[-1]) #get the last element of the list
                for arg in reversed(args[1:-1]): #start from the second-to-last number, to the first
                        arg_f = float(arg)
                        result = arg_f**result
                await client.send_message(message.channel, result)

client.run("INSERTTOKENHERE")
