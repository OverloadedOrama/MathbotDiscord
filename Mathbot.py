import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import math

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
                if len(args) > 1:
                        result = 0
                        for arg in args[1:]: #starts from the second element of the list, because the first is 'add'
                                try:
                                        arg_f = float(arg) #convert every argument from string to float
                                except ValueError:
                                        await client.send_message(message.channel, "Please provide numbers, for example: add 3 3")
                                        return
                                result += arg_f
                        await client.send_message(message.channel, result)
                else:
                        await client.send_message(message.channel, "Please provide numbers, for example: add 3 3")

        if message.content.upper().startswith('SUBTRACT'):
                args = message.content.split(" ")
                if len(args) > 1:
                        try:
                                result = float(args[1]) #we can't use 0, because it would yield wrong results.
                        except ValueError:
                                await client.send_message(message.channel, "Please provide numbers, for example: subtract 8.2 12")
                                return
                        for arg in args[2:]:
                                try:
                                        arg_f = float(arg) #convert every argument from string to float
                                except ValueError:
                                        await client.send_message(message.channel, "Please provide numbers, for example: subtract 8.2 12")
                                        return
                                result -= arg_f
                        await client.send_message(message.channel, result)
                else:
                        await client.send_message(message.channel, "Please provide numbers, for example: subtract 8.2 12")

        if message.content.upper().startswith('MULTIPLY'):
                args = message.content.split(" ")
                if len(args) > 1:
                        result = 1
                        for arg in args[1:]: #starts from the second element of the list, because the first is 'add'
                                try:
                                        arg_f = float(arg) #convert every argument from string to float
                                except ValueError:
                                        await client.send_message(message.channel, "Please provide numbers, for example: multiply -42 2.3")
                                        return
                                result *= arg_f
                        await client.send_message(message.channel, result)
                else:
                        await client.send_message(message.channel, "Please provide numbers, for example: multiply -42 2.3")

        if message.content.upper().startswith('DIVIDE'):
                args = message.content.split(" ")
                if len(args) > 1:
                        try:
                                result = float(args[1]) #we can't use 0, because it would yield wrong results.
                        except ValueError:
                                await client.send_message(message.channel, "Please provide numbers, for example: divide 0 2 -12")
                                return
                        for arg in args[2:]:
                                try:
                                        arg_f = float(arg) #convert every argument from string to float
                                except ValueError:
                                        await client.send_message(message.channel, "Please provide numbers, for example: divide 0 2 -12")
                                        return
                                if arg_f != 0:
                                        result /= arg_f
                                else:
                                        await client.send_message(message.channel, "You can't divide by zero.")
                                        return
                        await client.send_message(message.channel, result)
                else:
                        await client.send_message(message.channel, "Please provide numbers, for example: divide 0 2 -12")

        if message.content.upper().startswith('POWER'):
                #Power goes from right to left, so it's x^(y^(z^w)) etc
                args = message.content.split(" ")
                if len(args) > 1:
                        try:
                                result = float(args[-1]) #get the last element of the list
                        except ValueError:
                                await client.send_message(message.channel, "Please provide numbers, for example: power 2 3")
                                return
                        for arg in reversed(args[1:-1]): #start from the second-to-last number, to the first
                                try:
                                        arg_f = float(arg)
                                except ValueError:
                                        await client.send_message(message.channel, "Please provide numbers, for example: power 2 3")
                                        return
                                result = arg_f**result
                        await client.send_message(message.channel, result)
                else:
                        await client.send_message(message.channel, "Please provide numbers, for example: power 2 3")

        if message.content.upper().startswith('FACTORIAL'):
                args = message.content.split(" ")
                if len(args) == 1:
                        await client.send_message(message.channel, "Please provide one non-negative integer, for example: factorial 5")
                elif len(args) > 2:
                        await client.send_message(message.channel, "You must only provide one number, for example: factorial 5")
                else:
                        try:
                                x = int(args[1])
                        except ValueError:
                                await client.send_message(message.channel, "Number must be an integer, for example: factorial 5")
                                return
                        if x >= 0:
                                result = math.factorial(x)
                                await client.send_message(message.channel, result)
                        else:
                                await client.send_message(message.channel, "Number must not be negative, for example: factorial 5")

client.run("INSERTTOKENHERE")
