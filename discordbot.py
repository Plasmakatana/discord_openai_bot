import openai
import discord
from discord.ext import commands
openai.api_key = "openai api key"
bot = commands.Bot(command_prefix='!',
                   intents=discord.Intents.all())
@bot.command()
async def chat(ctx, *, prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2048,
        temperature=0.5,
        timeout=2000,
        n=1
    )
    text = response.choices[0].text
    if len(text) > 1500:
        messages = [text[i:i + 1500] for i in range(0, len(text), 1500)]
    else:
        messages = [text]
        # Send the response messages to the Discord channel
    for text in messages:
        await ctx.send("```" + text + "```")
    #for i in range(0,5):
    #    discord.Embed(await ctx.send(response.choices[i].text))
bot.run("discord bot key")

