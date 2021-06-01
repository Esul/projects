import discord
import commands

TOKEN = 'aq-iqneboda-tqveni-tokeni'

bot = discord.Client()


@bot.event
async def on_message(message):
    # Prevent bot from replying to himself
    if message.author == bot.user:
        return

    if message.content.startswith("!hello"):
        msg = 'Oh, hi Mark!'
        await message.channel.send(msg)

    if message.content.startswith("!temp"):
        command = message.content.split()
        current_temp = commands.get_temp(command[1])
        msg = 'Current temperature in {} is {}°C'.format(
            str(command[1].lower().capitalize()), str(current_temp))
        await message.channel.send(msg)

    if message.content.startswith("!cat"):
        cat_fact = commands.random_cat_fact()
        await message.channel.send(cat_fact)

    if message.content.startswith("!bored"):
        activity = commands.bored()
        msg = "You can try to: " + activity
        await message.channel.send(msg)

    if message.content.startswith('!price'):
        command = message.content.split()
        value = commands.get_crypto_value(command[1].lower())
        msg = "Currently the price of {} is {}$.\n\n Powered by CoinGecko API".format(
            command[1].capitalize(), value)
        await message.channel.send(msg)

    if message.content.startswith('!ip'):
        msg = "Server ip address: loopebistye.ddns.net"
        await message.channel.send(msg)

    if message.content.startswith('!help'):
        msg = "\n!temp {ქალაქი.}\n\!price {cryptocurrency.}\n!cat\n!ip\n!bored"
        await message.channel.send(msg)

    if message.content.startswith('!gegi'):
        msg = "momshordi"
        await message.channel.send(msg)

print("Chveni Dzma has woken up.")

bot.run(TOKEN)

print("Going back to sleep.")
