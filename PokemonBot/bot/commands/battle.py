import discord

from discord.ext import commands

class Battle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='battle', help='Initiate a battle with another user')
    async def battle(self, ctx, opponent: discord.Member):
        # Logic for initiating a battle with the specified opponent
        await ctx.send(f'{ctx.author.mention} has initiated a battle with {opponent.mention}')

    @commands.Cog.listener()
    async def on_battle_win(self, ctx, winner: discord.Member, loser: discord.Member):
        # Logic for handling events after a battle is won
        await ctx.send(f'{winner.mention} has won the battle against {loser.mention}')

def setup(bot):
    bot.add_cog(Battle(bot))