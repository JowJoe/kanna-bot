import discord
import asyncio
client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="Bola de fogo"))

@client.event
async def on_message(message):
    if message.content.startswith('@flood'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Deixa eu ver aqui...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'Você floodou {} vezes.'.format(counter))
    elif message.content.startswith('!dormir'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Não durma!')


client.run('MzkyMzIxMTAyNzAzMDk5OTM1.DRlhdA.eCRUyDOfbOv0N5nNBo104WizpkI')
