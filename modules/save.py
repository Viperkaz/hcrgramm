import re
import pytz
import random
import logging
import asyncio
import os
from datetime import datetime

from .. import utils, loader

logger = logging.getLogger(__name__)

day_to_weekday = {
    "mon": 0,
    "tue": 1,
    "wed": 2,
    "thu": 3,
    "fri": 4,
    "sat": 5,
    "sun": 6,
    "пн": 0,
    "вт": 1,
    "ср": 2,
    "чт": 3,
    "пт": 4,
    "сб": 5,
    "вс": 6,
}


@loader.tds
class AlarmMod(loader.Module):
    """Alarm module for remind you about something"""

    strings = {
        # ... остальные строки
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
            # ... остальные конфигурации
        )

    async def save_file(self, content, file_name):
        path_to_save = "/путь/к/папке/для/сохранения/"  # Замените на свой путь
        try:
            with open(os.path.join(path_to_save, file_name), "w", encoding="utf-8") as file:
                file.write(content)
            return os.path.join(path_to_save, file_name)
        except Exception as e:
            logger.error(f"Error saving file: {e}")
            return None

    # Остальной код без изменений
    # ...

    async def off_alarm(self, call, id_):
        alarms = self.get("alarms", {})
        for day, alarm in alarms.items():
            if alarm["id"] == id_:
                alarm["status"] = "off"
                self.set("alarms", alarms)
                await call.edit(self.strings("turned_off"))
                return False
        await call.answer("Не найдено!")
