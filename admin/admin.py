import discord

from discord.ext import commands

class Admin(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.command(hidden=True)
	@commands.is_owner()
	async def load(self, ctx, extension):
		self.bot.load_extension(f"cogs.{extension}")
		embed = discord.Embed(color=discord.Color.blurple())
		embed.add_field(name=":inbox_tray: `Input`", value=f"`Requested for loading cogs.{extension}`", inline=True)
		embed.add_field(name=":outbox_tray: `Output`", value=f"`Successfully loaded cogs.{extension}`", inline=True)
		await ctx.send(embed=embed)
	
	@commands.command(hidden=True)
	@commands.is_owner()
	async def unload(self, ctx, extension):
		self.bot.unload_extension(f"cogs.{extension}")
		embed = discord.Embed(color=discord.Color.blurple())
		embed.add_field(name=":inbox_tray: `Input`", value=f"`Requested for unloading cogs.{extension}`", inline=True)
		embed.add_field(name=":outbox_tray: `Output`", value=f"`Successfully unloaded cogs.{extension}`", inline=True)
		await ctx.send(embed=embed)
		
	@commands.command(hidden=True)
	@commands.is_owner()
	async def reload(self, ctx, extension):
		self.bot.unload_extension(f"cogs.{extension}")
		self.bot.load_extension(f"cogs.{extension}")
		embed = discord.Embed(color=discord.Color.blurple())
		embed.add_field(name=":inbox_tray: `Input`", value=f"`Requested for re-loading cogs.{extension}`", inline=True)
		embed.add_field(name=":outbox_tray: `Output`", value=f"`Successfully re-loaded cogs.{extension}`", inline=True)
		await ctx.send(embed=embed)
					
def setup(bot):
	bot.add_cog(Admin(bot))