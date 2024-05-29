import discord
from discord.ext import commands

class Catch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='catch', help='Encounter a wild Pokemon to catch!')
    async def catch_pokemon(self, ctx):
        # Logic to randomly generate a Pokemon encounter
        pokemon = generate_random_pokemon()

        # Display the encountered Pokemon to the user
        await ctx.send(f'A wild {pokemon} appeared! Type !catch to catch it!')

    @commands.command(name='catch', help='Catch the encountered Pokemon')
    async def catch(self, ctx):
        # Logic to catch the encountered Pokemon
        pokemon = get_encountered_pokemon(ctx.author)

        # Add the caught Pokemon to the user's collection
        add_pokemon_to_collection(ctx.author, pokemon)

        await ctx.send(f'Congratulations! You caught {pokemon}!')

def setup(bot):
    bot.add_cog(Catch(bot))