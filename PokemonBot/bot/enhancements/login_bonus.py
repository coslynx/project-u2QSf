import discord
from discord.ext import commands
import random

class LoginBonus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Login Bonus cog is ready')

    @commands.command(name='daily_login')
    async def daily_login_bonus(self, ctx):
        user = ctx.author
        # Add logic here to give daily login bonus to user
        await ctx.send(f'{user.mention}, you have received your daily login bonus!')

def setup(bot):
    bot.add_cog(LoginBonus(bot))