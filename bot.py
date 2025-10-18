import discord
import os
from keep_alive import keep_alive

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Logged in as {client.user}')

# Start the keep-alive server
keep_alive()

# Run the bot
client.run(os.getenv("DISCORD_TOKEN"))