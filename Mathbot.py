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
                
        #Basic operations (addition, subtraction, multiplication, division, exponentation)
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

        #Factorials
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

        #Trigonometry <3
        if message.content.upper().startswith('SIN'):
                args = message.content.split(" ")
                if len(args) == 1:
                        await client.send_message(message.channel, "Please provide one number (in radians), for example: sin 3.14")
                elif len(args) > 2:
                        await client.send_message(message.channel, "You must only provide one number (in radians), for example: sin 3.14")
                else:
                        try:
                                x = float(args[1])
                        except ValueError:
                                await client.send_message(message.channel, "Input value must be a number (in radians), for example: sin 3.14")
                                return
                        
                        result = math.sin(x)
                        await client.send_message(message.channel, result)

        if message.content.upper().startswith('COS'):
                args = message.content.split(" ")
                if len(args) == 1:
                        await client.send_message(message.channel, "Please provide one number (in radians), for example: cos -6.28")
                elif len(args) > 2:
                        await client.send_message(message.channel, "You must only provide one number (in radians), for example: cos -6.28")
                else:
                        try:
                                x = float(args[1])
                        except ValueError:
                                await client.send_message(message.channel, "Input value must be a number (in radians), for example: cos -6.28")
                                return
                        
                        result = math.cos(x)
                        await client.send_message(message.channel, result)

        if message.content.upper().startswith('TAN'):
                args = message.content.split(" ")
                if len(args) == 1:
                        await client.send_message(message.channel, "Please provide one number (in radians), for example: tan 12")
                elif len(args) > 2:
                        await client.send_message(message.channel, "You must only provide one number (in radians), for example: tan 12")
                else:
                        try:
                                x = float(args[1])
                        except ValueError:
                                await client.send_message(message.channel, "Input value must be a number (in radians), for example: tan 12")
                                return
                        
                        result = math.tan(x)
                        await client.send_message(message.channel, result)

        #Logarithms
        if message.content.upper().startswith('LOG'):
                args = message.content.split(" ")
                if len(args) == 1:
                        await client.send_message(message.channel, "Please provide one positive number and a base (not needed, if you don't provide a base, default is e), for example: log 1 10")
                elif len(args) == 2:
                        try:
                                x = float(args[1])
                        except ValueError:
                                if args[1].upper() == "E":
                                        x = math.e
                                else:
                                        await client.send_message(message.channel, "Input value must be a positive number, for example: log 3")
                                        return
                        if x > 0:
                                result = math.log(x)
                                await client.send_message(message.channel, result)
                        else:
                                await client.send_message(message.channel, "Input value must be a positive number, for example: log 3")
                elif len(args) == 3:
                        try:
                                x = float(args[1])
                        except ValueError:
                                if args[1].upper() == "E":
                                        x = math.e
                                else:
                                        await client.send_message(message.channel, "Input value must be two positive numbers, for example: log 2 8")
                                        return
                        try:
                                base = float(args[2])
                        except ValueError:
                                if args[2].upper() == "E":
                                        base = math.e
                                else:
                                        await client.send_message(message.channel, "Input value must be two positive numbers, for example: log 2 8")
                                        return
                        
                        if x > 0 and base > 0:
                                result = math.log(x,base)
                                await client.send_message(message.channel, result)
                        else:
                                await client.send_message(message.channel, "Input value must be two positive numbers, for example: log 2 8")
                else:
                        await client.send_message(message.channel, "You must only provide one or two numbers (second number used as base), for example: log 1 10")

