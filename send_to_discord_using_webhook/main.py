#! /usr/bin/python3

from discordwebhook import Discord

discord = Discord(url="<ウェブフックurl>")
discord.post(content=input())