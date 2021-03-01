import discord

client = discord.Client()

@client.event
async def on_connect():
    print("nigga")


@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        if message.content == 'nigga123':
            for channel in client.private_channels:
                print(channel)
                async for msg in channel.history(limit=None):
                    if msg.author == client.user:
                        try:
                            await msg.delete()
                        except:
                            pass
                    
client.run("NzMzMDA2MDI0ODYwMTA2ODMy.X5Ly8A.C4aNguWSPxQ-8mE_LYdAALRt8Ag", bot=False)
