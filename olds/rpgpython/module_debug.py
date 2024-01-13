"""module for debug"""
from icecream import ic


def output_to_file(text) -> None:
    """write debug in a file"""
    with open('debug_log.txt', 'a', encoding="utf-8") as file:
        file.write(text + '\r')


ic.configureOutput(
    prefix='Debug| ', outputFunction=output_to_file, includeContext=True)
