# Love
'''
.ut:: Анимация \n\n<b>Использование</b>: \n<code>.ut</code>
'''
import asyncio
from telethon import events
from asyncio import sleep
import random

def a(client):
    @client.on(events.NewMessage(pattern=r"\.ut", outgoing=True))
    async def moving_wave_animation(event):
        message = event
        if message.sender_id == (await message.client.get_me()).id:
            wave_symbols = ["🌊", "⬜️"]
            h = "⬜️"
            
            for _ in range(4):
                await message.edit("".join([wave_symbols[0]*9, "\n", wave_symbols[0]*2, h, wave_symbols[0]*2, h*2, "\n", h, wave_symbols[0]*7, h, "\n", h, wave_symbols[0]*7, h, "\n", h, wave_symbols[0]*7, h, "\n", h*2, wave_symbols[0]*5, h*2, "\n", h*3, wave_symbols[0]*3, h*3, "\n", h*4, wave_symbols[0], h*4]))
                await sleep(0.3)
                await message.edit("".join([wave_symbols[1]*9, "\n", wave_symbols[1]*2, h, wave_symbols[1]*2, h*2, "\n", h, wave_symbols[1]*7, h, "\n", h, wave_symbols[1]*7, h, "\n", h, wave_symbols[1]*7, h, "\n", h*2, wave_symbols[1]*5, h*2, "\n", h*3, wave_symbols[1]*3, h*3, "\n", h*4, wave_symbols[1], h*4]))
                await sleep(0.3)

            for _ in range(8):
                await message.edit((wave_symbols[0]*(8-_)+wave_symbols[1]*_+"\n")*(8-_))
                await sleep(0.4)

            for i in range(10):
                for _ in range(7):
                    await message.edit((wave_symbols[0]*(8-_)+wave_symbols[1]*_+"\n")*(8-_))
                    await sleep(0.2)
                    await message.edit((wave_symbols[1]*(8-_)+wave_symbols[0]*_+"\n")*(8-_))
                    await sleep(0.2)

            for i in ["🌞", "🏄‍♂️", "🌴", "🌺"]:
                await message.edit(f"<b>{i}</b>", parse_mode='html')
                await sleep(0.5)

if __name__ == '__main__':
    try:
        a(client)
    except:
        pass
