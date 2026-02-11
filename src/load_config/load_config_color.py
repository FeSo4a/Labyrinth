import json
import logging
import sys

import keyboard
from colorama import *

from clear_screen import *


def read_color(path) -> dict:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            color: dict = json.load(f)
            return color
    except Exception as e:
        clear()
        logging.error(f'Color load error: {e}')
        print(f'{Fore.RED}颜色解析时错误： {e}')
        keyboard.read_key()
        clear_button()
        sys.exit(0)
