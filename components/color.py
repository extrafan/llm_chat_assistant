import re
import logging
from colorama import Fore, Style, init

# 初始化colorama
init()

class Colored:
    """提供彩色文本输出的工具类"""
    
    @staticmethod
    def cyan(text):
        return f"{Fore.CYAN}{text}{Style.RESET_ALL}"
    
    @staticmethod
    def blue(text):
        return f"{Fore.BLUE}{text}{Style.RESET_ALL}"
    
    @staticmethod
    def red(text):
        return f"{Fore.RED}{text}{Style.RESET_ALL}"
    
    @staticmethod
    def green(text):
        return f"{Fore.GREEN}{text}{Style.RESET_ALL}"
    
    @staticmethod
    def yellow(text):
        return f"{Fore.YELLOW}{text}{Style.RESET_ALL}"
    
    @staticmethod
    def magenta(text):
        return f"{Fore.MAGENTA}{text}{Style.RESET_ALL}"
    
    @staticmethod
    def white(text):
        return f"{Fore.WHITE}{text}{Style.RESET_ALL}"
    
    @staticmethod
    def highlight(content: str, keyword: str) -> str:
        """高亮显示关键字

        Args:
            content: 原始文本
            keyword: 需要高亮的关键字

        Returns:
            str: 带有高亮效果的文本
        """
        result = ""
        positions = [
            match.start() for match in re.finditer(re.escape(keyword), content)
        ]
        start = 0

        for pos in positions:
            result = (
                result
                + Colored.green(content[start:pos])
                + Colored.white(content[pos : pos + len(keyword)])
            )
            start = pos + len(keyword)

        result += Colored.green(content[start:])
        return result


