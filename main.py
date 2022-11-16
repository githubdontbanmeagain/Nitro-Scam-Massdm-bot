import discord # py -3 -m pip install -U discord.py
from discord.ext import commands
import json, os

class util:
    def get_config():
        with open("config.json") as f:
            return json.load(f)

    def load():
        os.system("cls")
        os.system("title github.com/githubdontbanmeagain")


config = util.get_config()

intents=discord.Intents.default()
intents.message_content=True
intents.members=True

bot=commands.Bot(command_prefix=config["bot prefix"], intents=intents, help_command=None)

async def dmall(ctx, emoji):
    print(f"/ | {len(ctx.guild.members)} members fetched")
    for member in ctx.guild.members:
        if not member.bot:
            message=config["dm message"]
            if config["mention in dm"].lower()=="yes":
                message=message+f"||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||{member.mention}"

            view=discord.ui.View()
            view.add_item(item=discord.ui.Button(style=discord.ButtonStyle.gray, label=config["button text"], url=config["site link"], emoji=emoji))
            try:
                await member.send(content=message, file=discord.File(config["image path"]), view=view)
                print(f"+ | {member.name}")
            except discord.HTTPException:
                print(f"- | {member.name}")

@bot.command()
async def setup(ctx, key):
    await ctx.message.delete()
    if key == config["command key"]:
        with open(config["emoji path"], "rb") as f:
            emoji_bytes=f.read()
        await ctx.guild.create_custom_emoji(name="nitro0emoji", image=emoji_bytes)

@bot.command()
async def start(ctx, key):
    await ctx.message.delete()
    if key == config["command key"]:
        for emoji in ctx.guild.emojis:
            if emoji.name == "nitro0emoji":
                print("/ | Starting...")
                await dmall(ctx, emoji)
                return
        print(f"/ | Run {config['bot prefix']}setup {config['command key']} first")
    
@bot.listen("on_connect")
async def ready():
    util.load()
    print("Bot is online, commands:")
    for command in bot.commands:
        print(f"    {config['bot prefix']}{command.name} {config['command key']}")

if __name__ == "__main__":
    bot.run(config["bot token"])
