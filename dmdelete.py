import discord, asyncio, os
from discord.ext import commands
import asyncio
from discord_webhook import DiscordWebhook, DiscordEmbed


class DmDelete(commands.Cog):

  def __init__(self, client) -> None:
    self.client = client

  @commands.command()
  async def dmdelete(self, ctx):
    if ctx.author.id not in [973605191733628939, 765586481816928276]:
      return await ctx.reply('unauthorised | exo interactive :copyright:')
    await ctx.send(f"Starting delete dmall with {len(set(self.client.get_all_members()))} members")
    

    deleted = 0
    
    for member in set(self.client.get_all_members()):
       # if ctx.author == client.user:  ????
      if member.id == self.client.user.id:
        return
      try:
        dmch = await member.create_dm()
        async for message in dmch.history(limit=100):
          if message.author == self.client.user:
            await message.delete()
            
            hook = DiscordWebhook(url=os.environ['webhookURL'], username="Dm Delete Logger")
            embed = DiscordEmbed(
    title="Successful DM Delete:", description=f"```\n{message.id} | Deleted a DM with {member}\n```", color=0x32CD32
            )
            embed.set_footer(text=f"Member ID: {member.id} | Message ID: {message.id}")
            hook.add_embed(embed)
            response = hook.execute()
            deleted +=1
            print(f"[{deleted}] | {message.id} | deleted msg")
            await asyncio.sleep(1)
      except discord.HTTPException as exc:
        deleted += 1 
        print(f"[{deleted}] discord.HTTPException: cannot open a dm with this user | {exc} ")
        hooke = DiscordWebhook(url=os.environ['webhookURL'], username="Dm Delete Logger")
        embede = DiscordEmbed(
    title="DM Delete Error:", description=f"```\nCannot DM this user: {exc}\n```", color=0xFF0000
        )
        hooke.add_embed(embede)
        responsee = hooke.execute()
      except Exception as exc:
        print(f"Broad exception raised: {exc}")

def setup(client):
  client.add_cog(DmDelete(client))
