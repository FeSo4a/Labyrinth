import keyboard


def clear_button() -> None:
    max_attempts = 100  # 限制最大尝试次数
    for _ in range(max_attempts):
        if not keyboard.is_pressed(keyboard.read_key()):
            break
