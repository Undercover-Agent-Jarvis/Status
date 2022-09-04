import discord
from discord.ext import commands
import asyncio
import time
import _thread
import datetime
from math import floor
# from webserver import keep_alive

guildID = 972404362242560020
roleID = 1013877648298086481
vanity = ("/Linux-HQ")
Vanity_Name = ("Linux-HQ")
Server_Name = ("Jarvis")
footer_text = ("© 2022 Made by Your's Jarvis#1906 with ❤")

UserJarvis = ("https://discord.com/users/899961311771897877")
Jarvis_Banner = "https://media.discordapp.net/attachments/936162957648351233/957608674472366110/20220327_172425.png"
Jarvis_Avatar = "https://media.discordapp.net/attachments/936162957648351233/959705984304046100/Avatar_Link.gif?width=1500&height=1500"

dot = "<:dc_event_1:972211708250718238>"
gold_event = "<:event_1:972160502883057725>"
green_event = "<:dot:972204227009065060>"
success = "<:successful:981231271722229810>"
error = "<a:wrong:962646000969863188>"
support = "<:test_2:972160504594300958>"

b = commands.Bot(command_prefix='..', intents=discord.Intents.all())
c = discord.Client()
import os


@b.event
async def on_ready():
    await b.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name="Jarvis"))
    print("Bot Ready")

    async def threading():
        total_seconds_wait = 5
        fg = 0
        while total_seconds_wait:
            guil = b.get_guild(guildID)
            memberList = guil.members
            for user in memberList:
                fla = 0
                for s in user.activities:
                    fla = 1
                    if isinstance(s, discord.CustomActivity):
                        if str(s).find(vanity) != -1:
                            r = user.guild.get_role(roleID)
                            if r in user.roles:
                                continue
                            else:  # User adding vanity in status
                              
                                embed = discord.Embed(title="send", description="1", colour=000000)
                                # embed.set_author(name=f"", url="", icon_url="")
                                # embed.set_thumbnail(url=f"")
                                # embed.add_field(name="", value="")
                                # embed.add_field(name="", value="")
                                # embed.add_field(name="", value="")
                                # # embed.set_image(url="")
                                embed.timestamp = datetime.datetime.utcnow()
                                # embed.set_image(url="")

                                asyncio.run_coroutine_threadsafe(
                                    user.add_roles(r), c.loop).result()
                                print(user)
                                try:
                                    asyncio.run_coroutine_threadsafe(
                                        user.send(embed=embed),
                                        c.loop).result()
                                    print('SENT')
                                except:
                                    continue
                        else:
                            r = user.guild.get_role(roleID)
                            if r in user.roles:  # embed remove
                                embed = discord.Embed(title="remove", description="remove 2", colour=000000)
                                # embed.set_author(name=f"", url="", icon_url="")
                                # embed.set_thumbnail(url=f"")
                                # embed.add_field(name="", value="")
                                # embed.add_field(name="", value="")
                                # embed.add_field(name="", value="")
                                # # embed.set_image(url="")
                                embed.timestamp = datetime.datetime.utcnow()
                                # embed.set_footer(text=f"", icon_url="")

                                asyncio.run_coroutine_threadsafe(
                                    user.remove_roles(r), c.loop).result()
                                print(user)
                                try:
                                    asyncio.run_coroutine_threadsafe(
                                        user.send(embed=embed),
                                        c.loop).result()
                                    print('DEL SENT')
                                except:
                                    continue
                if fla == 0:
                    k = user.guild.get_role(roleID)
                    if k in user.roles:
                        flaggg = 0
                        if isinstance(s, discord.CustomActivity):
                            #print('u have status')
                            flaggg = 1
                        if flaggg == 0:
                            print('u do not have status')  # Embed remove
                            embed = discord.Embed(title="remove 3", description="remove 3", colour=000000)
                            # embed.set_author(name=f"", url="", icon_url="")
                            # embed.set_thumbnail(url=f"")
                            # embed.add_field(name="", value="")
                            # embed.add_field(name="", value="")
                            # embed.add_field(name="", value="")
                            # # embed.set_image(url="")
                            embed.timestamp = datetime.datetime.utcnow()
                            # embed.set_footer(text=f"", icon_url="")

                            asyncio.run_coroutine_threadsafe(
                                user.remove_roles(k), c.loop).result()
                            print(user)
                            try:
                                asyncio.run_coroutine_threadsafe(
                                    user.send(embed=embed), c.loop).result()
                                print('DEL SENT')
                            except:
                                continue
            if (fg == 0):
                now = floor(time.time())
                fg = 1
            if (now + 1 <= floor(time.time())):
                fg = 0
                total_seconds_wait -= 1
            if (total_seconds_wait == 0):
                total_seconds_wait = 5

    def between_callback():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(threading())
        loop.close()

    _thread.start_new_thread(between_callback, ())


# keep_alive()
my_secret = os.environ['TOKEN']
b.run(my_secret)
