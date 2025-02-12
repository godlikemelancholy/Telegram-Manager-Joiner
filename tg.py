from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon import functions
import asyncio
import os


class Telegram:
    def __init__(self, key_file):
        with open(key_file) as kf:
            key = kf.read()
        self.__session = TelegramClient(StringSession(key), 17463049, "bd4bbac77f54cd096ede52dd2e8e2e50", system_version="4.16.30-vxCUSTOM")
        self.__peer = 777000

    async def join_channel(self, url):
        await self.__session.connect()
        result = await self.__session(functions.channels.JoinChannelRequest(
            channel=url
        ))
