import json
import logging
import sys
from typing import *

import keyboard
from colorama import *

from clear_screen import *

init(autoreset=True)


def load_config_asset(asset_config: str) -> Tuple[str, str, str, str]:
    """
    加载资源配置文件并提取关键参数。

    参数:
        asset_config (str): 资源配置文件的路径。

    返回:
        Tuple[str, str]: 包含logo路径和title路径的元组。

    异常处理:
        如果在读取或解析配置文件时发生异常，程序会清屏、输出错误信息，
        等待用户按键后退出。
    """
    try:
        # 打开并读取资源配置文件
        with open(asset_config, 'r', encoding='utf-8') as f:
            asset_config: dict = json.load(f)

            # 提取配置文件中的各项参数
            logo_path: str = asset_config['logo']
            title_path: str = asset_config['title']
            map_path: str = asset_config['map']
            menu_path: str = asset_config['menu']

            logging.info(f'Assets loaded successfully.')

        # 返回解析后的配置参数
        return logo_path, title_path, map_path, menu_path

    except Exception as e:
        # 捕获异常，清屏并提示错误信息后退出程序
        clear()
        logging.error(f'Assets config load failed: {str(e)}')
        print(f'{Fore.RED}config加载失败： {str(e)}')
        keyboard.read_key()
        clear_button()
        clear()
        sys.exit()
