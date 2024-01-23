import discord
from discord.ext import commands



bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user.name}")

@bot.command()
async def send_alert(ctx, message):
    channel = bot.get_channel(YOUR_CHANNEL_ID)
    await channel.send(f"Recycling Alert: {message}")

# Run the bot
bot.run("YOUR_BOT_TOKEN")
