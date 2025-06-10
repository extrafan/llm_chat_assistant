import os
import config
from components.logger import logger
from tools.secret import decrypt_aes

def generate_env():
    os.environ['OPENAI_API_KEY'] = config.API_KEY.OPENAI_API_KEY

def init():
    generate_env()

if __name__ == "__main__":
    init()
    logger.info("初始化完成")

