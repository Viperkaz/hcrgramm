# Type2
'''
.oi:: Анимация для текста. \n\n<b>Использование:</b> \n<code>.oi</code> ваштекст
'''

from telethon import events
import asyncio
import math

def a(client):
    @client.on(events.NewMessage(pattern=r"\.oi (.*)", outgoing=True))
    async def _(event):
        if event.fwd_from:
            return
        input_str = event.pattern_match.group(1)
        typing_symbol = "<"
        DELAY_BETWEEN_EDITS = 0.1
        previous_text = ""
        await event.edit(typing_symbol)
        await asyncio.sleep(DELAY_BETWEEN_EDITS)
        for character in input_str:
            previous_text = previous_text + "" + character
            typing_text = previous_text + "" + typing_symbol
            animated_text = ""
            for i in range(len(typing_text)):
                space = " " * i
                animated_text += space + typing_text[i:]
            await event.edit(f'<b>{animated_text}</b>', parse_mode='html')
            await asyncio.sleep(DELAY_BETWEEN_EDITS)

if __name__ == '__main__':
    try:
        a(client)
    except:
        pass
