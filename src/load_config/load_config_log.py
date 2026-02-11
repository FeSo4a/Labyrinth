import json
import logging
import sys
from typing import *

import keyboard
from colorama import *

from clear_screen import *

init(autoreset=True)

# 日志级别映射字典，将字符串形式的日志级别映射为logging模块对应的常量
LOG_LEVEL: Final[Dict[str, int]] = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}


def load_config_log(log_config: str) -> Tuple[int, str, str, str, str]:
    """
    加载日志配置文件并解析其中的配置项。

    参数:
        log_config (str): 日志配置文件的路径。

    返回:
        Tuple[int, str, str, str, str]: 包含以下内容的元组：
            - log_level (int): 解析后的日志级别（对应logging模块的常量）。
            - log_path (str): 日志输出文件路径。
            - log_mode (str): 日志写入模式（如 'w' 或 'a'）。
            - log_format (str): 日志格式字符串。
            - log_datefmt (str): 日志日期时间格式字符串。

    异常处理:
        如果在读取或解析配置文件时发生异常，程序会清屏并打印错误信息，然后退出。
    """
    try:
        # 打开并读取日志配置文件
        with open(log_config, 'r', encoding='utf-8') as f:
            log_config: dict = json.load(f)

            # 提取配置文件中的各项参数
            log_level: str = log_config['level']
            log_path: str = log_config['path']
            log_mode: str = log_config['mode']
            log_format: str = log_config['format']
            log_datefmt: str = log_config['datefmt']

            # 将字符串形式的日志级别转换为logging模块对应的整数常量
            log_level: int = LOG_LEVEL[log_level]

        # 返回解析后的配置参数
        return log_level, log_path, log_mode, log_format, log_datefmt

    except Exception as e:
        # 捕获异常，清屏并提示错误信息后退出程序
        clear()
        print(f'{Fore.RED}config加载失败： {str(e)}')
        keyboard.read_key()
        clear_button()
        clear()
        sys.exit()
