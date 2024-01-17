__version__ = (1, 0, 0)

import contextlib

"""
    █▀▄▀█ █▀█ █▀█ █ █▀ █ █ █▀▄▀█ █▀▄▀█ █▀▀ █▀█
    █ ▀ █ █▄█ █▀▄ █ ▄█ █▄█ █ ▀ █ █ ▀ █ ██▄ █▀▄
    Авторское право 2022 t.me/morisummermods
    Лицензировано по лицензии Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
"""
# мета разработчик: @morisummermods
# мета баннер: https://i.imgur.com/H1vPM6U.jpg

from telethon.tl.types import Message
import requests
import logging
import re

from .. import loader, utils  # noqa

logger = logging.getLogger(__name__)


@loader.tds
class ChatGPT(loader.Module):
    """Взаимодействие с API ChatGPT"""

    strings = {
        "name": "ChatGPT",
        "no_args": (
            "<emoji document_id=5312526098750252863>🚫</emoji> <b>Не указаны"
            " аргументы</b>"
        ),
        "question": (
            "<emoji document_id=5974038293120027938>👤</emoji> <b>Вопрос:</b>"
            " {question}\n"
        ),
        "answer": (
            "<emoji document_id=5199682846729449178>🤖</emoji> <b>Ответ:</b> {answer}"
        ),
        "loading": "<code>Загрузка...</code>",
        "no_api_key": (
            "<b>🚫 Не указан API ключ</b>\n<i><emoji"
            " document_id=5199682846729449178>ℹ️</emoji> Получите его на официальном"
            " сайте OpenAI и добавьте в конфиг</i>"
        ),
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            "API_KEY", None, "Ключ API для доступа к ChatGPT"
        )

    @loader.unrestricted
    @loader.ratelimit
    async def chatgptcmd(self, message: Message):
        """Задайте вопрос ChatGPT"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings("no_args", message))
            return
        if not self.config["API_KEY"]:
            await utils.answer(message, self.strings("no_api_key", message))
            return
        await utils.answer(message, self.strings("loading", message))
        try:
            response = requests.post(
                "https://api.openai.com/v1/engines/chatgpt-ru/completions",
                headers={"Authorization": f"sk-{self.config['API_KEY']}"},
                json={
                    "prompt": f"Q: {args}\nA:",
                    "max_tokens": 50,
                    "temperature": 0.9,
                    "top_p": 1,
                    "frequency_penalty": 0,
                    "presence_penalty": 0.6,
                    "stop": "\n
