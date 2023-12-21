#Police
'''
.police:: Полицейская анимация \n\n<b>Использование</b>: \n<code>.police</code>
'''
import asyncio
from telethon import events
from asyncio import sleep
import random


def police_animation(client):
    @client.on(events.NewMessage(pattern=r"\.police", outgoing=True))
    async def police_animate(event):
        message = event
        if message.sender_id == (await message.client.get_me()).id:
            arr = ["🔵", "🚨", "🔴", "🚨"]
            h = "⬜️"
            first = ""
            for i in range(8):
                await message.edit((arr[i % 2] * 9 + "\n") * 4)
                await sleep(0.3)

            for _ in range(5):
                rand = random.choice(arr)
                await message.edit("".join([h * 9, "\n", h * 2, rand * 5, h * 2, "\n", h * 3, rand * 3, h * 3, "\n",
                                            h * 4, rand, h * 4, "\n", h * 9]))
                await sleep(0.3)

            for i in range(8):
                await message.edit((arr[i % 2] * 9 + "\n") * 4)
                await sleep(0.3)

            await sleep(0.5)

            for i in range(8):
                await message.edit((arr[(i + 1) % 2] * 9 + "\n") * 4)
                await sleep(0.3)

            await sleep(0.5)

            for i in range(8):
                await message.edit((arr[i % 2] * 9 + "\n") * 4)
                await sleep(0.3)


if __name__ == '__main__':
    try:
        police_animation(client)
    except:
        pass
