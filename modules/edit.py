# Edit
'''
.edit:: Анимация для текста. \n\n<b>Использование:</b> \n<code>.type</code> ваштекст
'''

from telethon import events
import asyncio

@events.register(events.NewMessage(pattern='.edit'))
async def _(event):
    message = event.text[6:]
    typing_symbol = "|"

    if message:
        msg = ""
        for letter in message:
            msg += letter
            if letter != " ":
                msg += typing_symbol
            await event.respond(msg)
            await asyncio.sleep(0.10)  # задержка между каждым символом
            msg = msg[:-1]
        await event.respond(message)
    else:
        await event.respond("Пожалуйста, введите текст после `.edit`.")

if __name__ == '__main__':
    try:
        a(client)
    except:
        pass
