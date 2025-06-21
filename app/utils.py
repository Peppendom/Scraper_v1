from datetime import datetime


def log(msg: str, level: str = "INFO"):
    print(f'{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]} UTC ― {level} ― {msg}')
