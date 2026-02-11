import logging
import os
import sys
from typing import *

import keyboard
from colorama import *

from clear_screen import *

init(autoreset=True)


def load_log(config_log: Tuple[int, str, str, str, str]) -> None:
    """
    初始化日志配置并创建日志文件。

    参数:
        config_log (Tuple[int, str, str, str, str]): 包含日志配置的元组，具体含义如下：
            - config_log[0] (int): 日志级别（如 logging.DEBUG, logging.INFO 等）。
            - config_log[1] (str): 日志文件存储路径。
            - config_log[2] (str): 日志文件写入模式（如 'w' 覆盖写入，'a' 追加写入）。
            - config_log[3] (str): 日志格式字符串。
            - config_log[4] (str): 日志时间格式字符串。

    返回值:
        None: 该函数无返回值。

    功能说明:
        1. 根据传入的日志配置初始化 Python 的 logging 模块。
        2. 创建指定路径的日志目录（如果不存在）。
        3. 配置日志的基本信息，包括日志级别、文件路径、写入模式、格式和时间格式。
        4. 在日志中记录初始化成功的信息。
        5. 如果初始化过程中发生异常，则清屏并输出错误信息，等待用户按键后退出程序。
    """
    log_level = config_log[0]
    log_path = config_log[1]
    log_mode = config_log[2]
    log_format = config_log[3]
    log_datefmt = config_log[4]

    os.makedirs(log_path, exist_ok=True)  # 创建日志目录

    try:
        # 配置日志基本信息
        logging.basicConfig(
            level=log_level,
            filename=f'{log_path}/log.log',
            filemode=log_mode,
            format=log_format,
            datefmt=log_datefmt
        )
    except Exception as e:
        # 处理日志初始化失败的情况
        clear()
        print(f'{Fore.RED}Log初始化失败： {str(e)}')
        keyboard.read_key()
        clear_button()
        sys.exit()

    # 记录日志初始化成功地相关信息
    logging.info('From FeSo4a')
    logging.info('-----------------------------------')
    logging.info(f'Log path: {log_path}/log.log')
    logging.info(f'Log mode: {log_mode}')
    logging.info(f'Log format: {log_format}')
    logging.info(f'Log datefmt: {log_datefmt}')
    logging.info('-----------------------------------')
    logging.info('Log initialized successfully.')
