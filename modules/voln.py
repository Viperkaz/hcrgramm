# Type2
'''
.voln:: Анимация для текста. \n\n<b>Использование:</b> \n<code>.voln</code> ваштекст
'''

ifrom telethon import events
import asyncio

def a(client):
    @client.on(events.NewMessage(pattern=r"\.voln (.*)", outgoing=True))
    async def _(event):
        if event.fwd_from:
            return
        input_str = event.pattern_match.group(1)
        DELAY_BETWEEN_EDITS = 0.1
        await event.edit(input_str)
        await asyncio.sleep(DELAY_BETWEEN_EDITS)
        for _ in range(10):  # количество "волн"
            for i in range(len(input_str)):
                await event.edit(input_str[:i] + "🌊" + input_str[i+1:])
                await asyncio.sleep(DELAY_BETWEEN_EDITS)
            await event.edit(input_str)
            await asyncio.sleep(DELAY_BETWEEN_EDITS)

if __name__ == '__main__':
    try:
        a(client)
    except:
        pass
