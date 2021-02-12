import discord
import os
import config_helper
import google_search
import persistent_store

client = discord.Client()
@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'hi':
        return await message.channel.send("<@{0}> Hey".format(message.author.id))
    if message.content.startswith('!google'):
        search_text = message.content.split("!google")
        if len(search_text) > 1:
            persistent_store.add_search(search_text[1],message.author.id)
            search_response = google_search.search(search_text[1])
            return await message.channel.send("<@{0}> {1}".format(message.author.id,search_response))
    if message.content.startswith('!recent'):
        search_text = message.content.split("!recent")
        if len(search_text) > 1:
            recent_response = persistent_store.find_search_term(search_text[1],message.author.id)
            return await message.channel.send("<@{0}> {1}".format(message.author.id,recent_response))

client.run(config_helper.get_discord_token())