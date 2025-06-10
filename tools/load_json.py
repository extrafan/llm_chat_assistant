import json
from components.logger import logger

def load_json(path, desc, default=None):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        logger.info(f"{desc}加载成功: {path}")
        return data
    except FileNotFoundError:
        logger.critical(f"{desc}未找到: {path}")
        return default if default is not None else {}
    except json.JSONDecodeError as e:
        logger.critical(f"{desc}解析失败: {e}")
        return default if default is not None else {}