import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.lower() == "hello":
        await message.channel.send(f"Hello {message.author.name}! 👋")
    await bot.process_commands(message)

keep_alive()
bot.run('YOUR_DISCORD_BOT_TOKEN')  # Replace in Railway secrets later
