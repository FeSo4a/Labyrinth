import logging
from typing import *

import keyboard
from colorama import *

from clear_screen import *
from game import *
from gui import *
from load_mod import load_mod_level

init(autoreset=True)


def game_loop(mod_path: str, mod_name: str, file: str, color_dict: dict, all_color: dict) -> str:
    """
    主游戏循环函数，根据选择的地图路径和关卡索引执行游戏逻辑。

    参数:
        choose (int): 关卡选择索引，用于从 LEVEL 列表中获取对应关卡名称。
        map_path (str): 地图文件的基础路径，与关卡名称拼接后构成完整地图文件路径。

    返回:
        str: 游戏执行结果，可能的返回值包括：
             - 'finish': 表示游戏完成（胜利或返回上一级）。
             - 'no_finish': 表示需要重新加载当前关卡。
    """
    while True:
        # 读取指定关卡的地图数据
        # noinspection PyTypeHints
        map_data: dict = read_map(f'{mod_path}{mod_name}/map/{file}')

        # 执行当前地图的游戏循环逻辑
        result: str = map_loop(map_data, color_dict, all_color)

        # 根据游戏循环的结果决定下一步操作
        if result == 'win':
            # 胜利时结束当前关卡并返回完成状态
            clear()
            print('恭喜过关！')
            keyboard.read_key()
            clear_button()
            clear()
            return 'finish'
        elif result == 'reload':
            # 需要重新加载当前关卡，返回未完成状态
            return 'no_finish'
        elif result == 'back':
            # 返回上一级菜单或关卡，视为完成状态
            return 'finish'


def trigger_game_choose(mod_path: str, mod_name: str, file: str, color_dict: dict, all_color: dict) -> Optional[bool]:
    """
    触发游戏选择逻辑，根据用户选择执行游戏循环直到满足退出条件。

    参数:
        choose (int): 用户的选择，用于决定游戏行为。如果等于QUIT，则函数直接返回。
        map_path (str): 地图文件路径，传递给游戏循环使用。

    返回值:
        None: 该函数不返回任何值。
    """
    # 进入主循环，持续处理游戏逻辑直到满足退出条件
    while True:

        # 调用游戏循环函数，传入用户选择和地图路径，并获取返回状态
        cond: str = game_loop(mod_path, mod_name, file, color_dict, all_color)

        # 根据游戏循环的返回状态决定下一步操作
        if cond == 'finish':
            # 如果返回状态为'finish'，表示游戏完成，跳出循环
            return True
        elif cond == 'no_finish':
            # 如果返回状态为'no_finish'，表示游戏未完成，继续下一轮循环
            continue


def start_game(mod_path: str, mod_name: str, file: str, color_dict: dict, all_color: dict) -> None:
    """
    启动游戏主循环，显示菜单并根据用户选择触发相应操作。

    参数:
        menu_path (str): 主菜单配置文件的路径前缀。
        map_path (str): 地图文件的路径。

    返回值:
        None: 该函数无返回值。
    """
    while True:

        if_break: bool = trigger_game_choose(mod_path, mod_name, file, color_dict, all_color)
        if if_break:
            break


def level_menu(mod_path: str, mod_name: str, path: str, color_dict: dict, all_color: dict) -> None:
    """
    显示并处理关卡选择菜单，允许用户选择并启动特定关卡。

    参数:
        mod_path (str): 模组路径，用于定位模组资源。
        path (str): 关卡数据文件的路径。
        color_dict (dict): 当前使用的颜色配置字典。
        all_color (dict): 所有可用的颜色配置字典。

    返回值:
        None: 该函数无返回值。
    """
    # 加载模组关卡数据
    result = load_mod_level(mod_path, path, all_color)
    if result is None:
        logging.error("Failed to load mod level data.")
        return
    level_menu_, level_id = result

    # 验证加载的数据类型是否正确
    if not isinstance(level_menu_, list) or not isinstance(level_id, list):
        logging.error("Invalid level_menu or level_id type.")
        return

    while True:
        # 进入菜单循环，获取用户选择
        choose: int = menu_loop(level_menu_)

        # 如果用户选择退出菜单（通常为最后一个选项），则跳出循环
        if choose + 1 == len(level_menu_):
            break

        try:
            # 根据用户选择获取对应的关卡文件名
            file = level_id[choose]
            if not isinstance(file, str):
                logging.error("Invalid file type in level_id.")
                continue
            # 启动游戏并加载选定的关卡
            start_game(mod_path, mod_name, file, color_dict, all_color)
        except Exception as e:
            # 处理异常情况：清屏、记录错误日志并提示用户
            clear()
            logging.error(f"Mod load error: {e}")
            print(f"{Fore.RED}地图加载失败： {e}")
            keyboard.read_key()
            clear_button()
            clear()
            return

