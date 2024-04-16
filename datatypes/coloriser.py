from typing import Optional
import datetime as dt
import colorama
colorama.init(autoreset=True)
log_format = "[%H:%M:%S.%f] {}\n"


def log(text: str, to_file: Optional[str] = None):
    if to_file is None:
        to_file = text

    with open(dt.datetime.now().date().strftime('logs\\%B_%e.log'), "a") as f:
        f.write(dt.datetime.now().strftime(log_format).format(to_file))
    print(dt.datetime.now().strftime(log_format).format(text))


def red(text: str):
    log(colorama.Fore.RED + text, text)


def green(text: str):
    log(colorama.Fore.GREEN + text, text)


def blue(text: str):
    log(colorama.Fore.BLUE + text, text)
