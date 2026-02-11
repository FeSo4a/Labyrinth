from clear_screen import *
from typing import *
import keyboard

ABOUT: Final[str] = """
作者：FeSo4a
Github: https://github.com/FeSo4a
Bilibili: https://space.bilibili.com/3546674548967510
"""


def print_about() -> None:
    clear()
    print(ABOUT)
    keyboard.read_key()
    clear_button()
    clear()
