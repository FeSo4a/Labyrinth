import logging
import sys

import keyboard
from colorama import *

from clear_screen import *

init(autoreset=True)


def load_asset_text(asset_config: str) -> str:
    """
    从指定路径加载资源文件的内容并返回其文本内容。

    参数:
        asset_config (str): 资源文件的路径。

    返回:
        str: 资源文件的文本内容。

    异常处理:
        如果文件读取失败，会记录错误日志，打印错误信息到控制台，
        等待用户按键后清屏并退出程序。
    """
    try:
        # 尝试以UTF-8编码打开并读取资源文件
        with open(asset_config, 'r', encoding='utf-8') as f:
            text: str = f.read()
            logging.info(f'Asset file loaded successfully.')
            return text
    except Exception as e:
        # 文件加载失败时的异常处理流程
        clear()
        logging.error(f'Asset file load failed: {str(e)}')
        print(f'{Fore.RED}资源文件加载失败： {str(e)}')
        keyboard.read_key()
        clear_button()
        clear()
        sys.exit()
