
from telethon import events
from asyncio import sleep
import random

async def animate_cat(message):
    cat_frames = [
        r" /\_/\ ",
        r"( o.o )",
        r"> ^ <"
    ]

    for frame in cat_frames:
        await message.edit(frame)
        await sleep(0.5)

async def animate_animal(client, command, frames):
    @client.on(events.NewMessage(pattern=command, outgoing=True))
    async def watcher(event):
        message = event
        if message.sender_id == (await message.client.get_me()).id:
            for frame in frames:
                await message.edit(frame)
                await sleep(0.5)
if __name__ == '__main__':
	try:
		a(client)
	except:
		pass
