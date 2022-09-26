import discord, os, asyncio, json, sys, logging
from discord.ext import commands
from keep_alive import keep_alive
from discord_webhook import DiscordWebhook, DiscordEmbed


#For Unverified Bots.
#client = commands.Bot(command_prefix = "$", intents = discord.Intents.all())



#For Verified Bots:
_i = discord.Intents.default()
_i.members = True
#_i.presences = True
#Only enable above if you have it enabled.
#client = commands.Bot(command_prefix = commands.when_mentioned, intents = _i)
client = commands.AutoShardedBot(command_prefix = commands.when_mentioned, intents = _i, shard_count = 1)
#Only enable above and remove existing client if your bot needs sharding, and then add the appropriate shard count needed. 3k servers = 3 shards, 4k servers = 4 shards, etc.





client.load_extension("dmdelete")
print("Loaded dmall cog")


@client.event
async def on_connect(): 
  logging.info('[INFO] [Connected to the API.]')

@client.event
async def on_ready():
  await client.change_presence(status= discord.Status.online, activity = discord.Game(name="Distributing Gifts"))
  print(f"[INFO] {client.user} is online.")
  hookel = DiscordWebhook(url=os.environ['connectionWebhookURL'], username="Connection Status")
  embedel = DiscordEmbed(
    title="Connection Valid:", description=f"```\nSuccessfully logged in as {client.user}\n```", color=0x32CD32
  )
  embedel.set_footer(text=f"Bot ID: {client.user.id}")
  hookel.add_embed(embedel)
  responseel = hookel.execute()

@client.command()
async def reload(ctx):
  if ctx.author.id != 765586481816928276:
    return await ctx.send("unauthorised | exo interactive :copyright:")

  client.unload_extension("dmdelete")
  client.load_extension("dmdelete")
  await ctx.send("reloaded dmDelete.DmDeleteCommand")



keep_alive()
client.run(os.environ['botToken'])
