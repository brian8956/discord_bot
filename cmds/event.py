from discord_bot.core.classes import Cog_Extension
import discord
from discord.ext import commands 
import json,random
from  core.classes import Cog_Extension

from discord.ext.commands.cog import _cog_special_method 

with open('setting.json','r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class Event(Cog_Extension):
    
    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(857457726643634216)
        await channel.send(f'{member} join!')

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel =self.bot.get_channel(857457856785809438)
        await channel.send(f'{member} leave!')

    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content in jdata['keyword'] and msg.author != self.bot.user:
            await msg.channel.send('apple')

def setup(bot):
    bot.add_cog(Event(bot))