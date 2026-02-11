from typing import *

import keyboard

from clear_screen import *
from gui import *

LEVEL: Final[List] = [
    'test.json'
]
QUIT: Final[int] = 1


def game_loop(choose: int, map_path: str, color_dict: dict, all_color: dict) -> str:
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
        map_data: dict = read_map(f'{map_path}{LEVEL[choose]}')

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


def trigger_game_choose(choose: int, map_path: str, color_dict: dict, all_color: dict) -> Optional[bool]:
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
        # 如果用户选择退出（choose等于QUIT），则直接结束函数
        if choose == QUIT:
            return True

        # 调用游戏循环函数，传入用户选择和地图路径，并获取返回状态
        cond: str = game_loop(choose, map_path, color_dict, all_color)

        # 根据游戏循环的返回状态决定下一步操作
        if cond == 'finish':
            # 如果返回状态为'finish'，表示游戏完成，跳出循环
            break
        elif cond == 'no_finish':
            # 如果返回状态为'no_finish'，表示游戏未完成，继续下一轮循环
            continue


def start_game(menu_path: str, map_path: str, color_dict: dict, all_color: dict) -> None:
    """
    启动游戏主循环，显示菜单并根据用户选择触发相应操作。

    参数:
        menu_path (str): 主菜单配置文件的路径前缀。
        map_path (str): 地图文件的路径。

    返回值:
        None: 该函数无返回值。
    """
    while True:
        # 读取主菜单配置文件
        menu_: list = read_menu(f'{menu_path}start_game_menu.json')
        # 显示菜单并获取用户选择
        choose: int = menu_loop(menu_)

        if_break: bool = trigger_game_choose(choose, map_path, color_dict, all_color)
        if if_break:
            break
