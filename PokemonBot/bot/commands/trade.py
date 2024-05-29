import discord
from discord.ext import commands

class Trade(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='trade', help='Initiate a trade with another user')
    async def trade(self, ctx, user: discord.User):
        # Logic for initiating a trade with another user
        await ctx.send(f'Trade initiated with {user.name}')

    @commands.command(name='confirm_trade', help='Confirm a trade with another user')
    async def confirm_trade(self, ctx, user: discord.User):
        # Logic for confirming a trade with another user
        await ctx.send(f'Trade confirmed with {user.name}')

    @commands.command(name='cancel_trade', help='Cancel an ongoing trade')
    async def cancel_trade(self, ctx):
        # Logic for canceling an ongoing trade
        await ctx.send('Trade canceled')

def setup(bot):
    bot.add_cog(Trade(bot))