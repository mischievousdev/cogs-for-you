import discord
import requests

from discord.ext import commands
from discord import Embed

class Animals(commands.Cog):
	"""Commands related to animals"""
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command()
	async def image(self, ctx, *, animal):
		"""Gives you the random image of different animals"""
		try:
			animals = ("cat", "dog", "fox", "koala", "panda", "birb", "racoon", "kangaroo", "whale")
			if not animal in animals:
				await ctx.send(f"{animal} is not a valid animal\nValid animals are: cat, dog, fox, koala, panda, birb, racoon, kangaroo, whale")
			
			r = requests.get(f"https://some-random-api.ml/img/{animal}")
			data = r.json()
			url = data["link"]
			embed = Embed()
			if animal == "panda":
				embed.title = ":panda_face: ~panda~"
			elif animal == "racoon":
				embed.title = ":raccoon: ~racoon~"
			else:
				embed.title = f":{animal}: ~{animal}~"
			embed.set_image(url=url)
			await ctx.send(embed=embed)
			
		except Exception:
			pass
			
	@commands.command()
	async def facts(self, ctx, *, animal):
		"""Gives you the facts of different animals"""
		try:
			animals = ("cat", "dog", "fox", "koala", "panda", "bird", "racoon", "kangaroo", "elephant", "giraffe", "whale")
			if not animal in animals:
				await ctx.send(f"{animal} is not a valid animal\nValid animals are: cat, dog, fox, koala, panda, bird, racoon, kangaroo, elephant, giraffe, whale")
				
			r = requests.get(f"https://some-random-api.ml/facts/{animal}")
			f = r.json()
			cont = f["fact"]
			embed = discord.Embed(color=discord.Color.blurple(),description=cont)
			if animal == "panda":
				embed.title = f":panda_face: panda fact"
			elif animal == "racoon":
				embed.title = f":raccoon: racoon fact"
			else:
				embed.title = f":{animal}: {animal} fact"
			await ctx.send(embed=embed)
		except Exception:
			pass
		
def setup(bot):
	bot.add_cog(Animals(bot))