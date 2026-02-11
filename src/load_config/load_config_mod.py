import json
import logging
import sys
from typing import *

import keyboard
from colorama import *

from clear_screen import *

init(autoreset=True)


def load_config_mod(mod_config: str) -> str:
    """
    加载资源配置文件并提取关键参数。

    参数:
        mod_config (str): 资源配置文件的路径。

    返回:
        str: 包含资源路径的字符串。

    异常处理:
        如果在读取或解析配置文件时发生异常，程序会清屏、输出错误信息，
        等待用户按键后退出。
    """
    try:
        # 打开并读取资源配置文件，将其内容解析为字典
        with open(mod_config, 'r', encoding='utf-8') as f:
            mod_config: dict = json.load(f)

            # 从配置字典中提取资源路径
            mod_path: str = mod_config['path']

            # 记录资源加载成功的日志信息
            logging.info(f'Assets loaded successfully.')

        # 返回解析后的资源路径
        return mod_path

    except Exception as e:
        # 捕获异常，执行清理操作并提示错误信息后退出程序
        clear()
        logging.error(f'Mod config load failed: {str(e)}')
        print(f'{Fore.RED}config加载失败： {str(e)}')
        keyboard.read_key()
        clear_button()
        clear()
        sys.exit()

