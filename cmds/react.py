from discord_bot.core.classes import Cog_Extension
import discord
from discord.ext import commands 
from core.classes import Cog_Extension
import random,json 
with open('setting.json','r',encoding='utf8') as jfile:
    jdata=json.load(jfile)


class React(Cog_Extension):
    @commands.command()
    async def IDK(self,ctx):
        random_pic=random.choice(jdata['pic_WTM'])
        pic_wtm= discord.File(random_pic)
        await ctx.send(file=pic_wtm)

def setup(bot):
    bot.add_cog(React(bot))

