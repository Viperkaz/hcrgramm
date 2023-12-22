python
Copy code
from pyrogram import Client, filters, types
from utils.misc import modules_help, prefix
from utils.scripts import (
    with_reply,
    interact_with,
    interact_with_to_delete,
    format_exc,
    resize_image,
)

.sticer:: Анимация \n\n<b>Использование</b>: \n<code>.sticer</code>

@Client.on_message(filters.command("kang", prefix) & filters.me)
@with_reply
async def kang(client: Client, message: types.Message):
    await message.edit("<b>Please wait...</b>")
    # ... (остальной код функции kang)

@Client.on_message(
    filters.command(["stp", "s2p", "stick2png"], prefix) & filters.me
)
@with_reply
async def stick2png(client: Client, message: types.Message):
    try:
        await message.edit("<b>Downloading...</b>")
        # ... (остальной код функции stick2png)
    except Exception as e:
        await message.edit(format_exc(e))
    else:
        await message.delete()

@Client.on_message(filters.command(["resize"], prefix) & filters.me)
@with_reply
async def resize_cmd(client: Client, message: types.Message):
    try:
        await message.edit("<b>Downloading...</b>")
        # ... (остальной код функции resize_cmd)
    except Exception as e:
        await message.edit(format_exc(e))
    else:
        await message.delete()

def a(client):
    @client.on(events.NewMessage(pattern=r"\.lv", outgoing=True))
    async def lv_animation(event):
        # ... (код функции lv_animation)

if __name__ == '__main__':
    try:
        client = Client("my_session")
        client.start()
        a(client)
        client.run()
    except:
        pass
