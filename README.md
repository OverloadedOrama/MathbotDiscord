# MathbotDiscord
A simple Discord bot that does mathematical calculations. Includes basic operations like addition, subtraction, multiplication,
division and exponentation, as well as factorial calculation, Trigometrical functions like sine, cosine and tangent, Logarithms and
calculation of the Fibonacci sequence.

This was written in Python 3.6, so I cannot guarantee it will work on other versions as well. I believe versions prior to 3.5
require some tweaking to work, due to discord.py working a bit differently in these versions.

The project requires an installation of discord.py, and importing the asyncio and math libraries.

## Installing discord.py

To install the library without full voice support, you can just run the following command:

```
python3 -m pip install -U discord.py
```

Otherwise to get voice support you should run the following command:

```
python3 -m pip install -U discord.py[voice]
```

More info on https://github.com/Rapptz/discord.py
