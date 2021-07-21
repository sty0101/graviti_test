from typing import Callable


def init(params: dict) -> Callable:
    return None


def run(data: dict, filter_fun: Callable = None) -> bool:
    if data.get('objectPath', '').endswith('.png'):
        return True
    return False
