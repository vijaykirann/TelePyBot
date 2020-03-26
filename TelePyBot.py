#!/usr/bin/env python
from telethon import TelegramClient
import asyncio
import os
import time
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import InputMessagesFilterDocument

client = TelegramClient('vijaykirann', '1385776', '87b3a6e5afba70b1c0e9263f9988cec3')
client.start()

async def main():
    download_path = 'C:\\Users\\Vicky\\Documents\\Python_Projects\\testdata'
    channel_name = 'books_and_magazines'
    msg_limit = 11
    #channel = await client.get_entity(channel_link)
    #print(channel)
    message = await client.get_messages(channel_name, msg_limit, filter=InputMessagesFilterDocument)
    #print(message)
    #print(message[0].media.document.attributes[0].file_name)
    for curr_msg in message:
        print (curr_msg.media.document.attributes[0].file_name)
        destfile=os.path.join(download_path, curr_msg.media.document.attributes[0].file_name)
        if not os.path.isfile(destfile):
            await curr_msg.download_media(destfile)
            print('Downloaded')
        else:
            print('Download_Skipped_File_Exits')

with client:
    client.loop.run_until_complete(main())