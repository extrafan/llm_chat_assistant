import logging
from components.color import Colored

class CustomFormatter(logging.Formatter):
    """自定义日志格式化器，为不同级别设置不同格式"""
    
    def __init__(self, use_color=True):
        super().__init__()
        # 通过参数控制是否使用彩色输出
        self.use_color = use_color
        
        # 定义不同级别的普通格式（无颜色）
        self.plain_formatters = {
            logging.DEBUG: logging.Formatter(
                '%(asctime)s [%(name)s] [DEBUG] %(message)s [%(filename)s:%(lineno)d]'
            ),
            logging.INFO: logging.Formatter(
                '%(asctime)s [%(name)s] [INFO] %(message)s [%(filename)s:%(lineno)d]'
            ),
            logging.WARNING: logging.Formatter(
                '%(asctime)s [%(name)s] [WARNING] %(message)s [%(filename)s:%(lineno)d]'
            ),
            logging.ERROR: logging.Formatter(
                '%(asctime)s [%(name)s] [ERROR] %(message)s [%(filename)s:%(lineno)d]'
            ),
            logging.CRITICAL: logging.Formatter(
                '%(asctime)s [%(name)s] [CRITICAL] %(message)s [%(filename)s:%(lineno)d] !!!'
            )
        }
        
        # 定义不同级别的彩色格式
        self.color_formatters = {
            logging.DEBUG: logging.Formatter(
                Colored.cyan('%(asctime)s') + ' ' + 
                Colored.blue('%(name)s') + ' ' + 
                Colored.magenta('DEBUG') + ' ' + 
                Colored.white('%(message)s') + ' ' + 
                Colored.yellow('[%(filename)s:%(lineno)d]')
            ),
            logging.INFO: logging.Formatter(
                Colored.cyan('%(asctime)s') + ' ' + 
                Colored.blue('%(name)s') + ' ' + 
                Colored.green('INFO') + ' ' + 
                Colored.green('%(message)s') + ' ' + 
                Colored.yellow('[%(filename)s:%(lineno)d]')
            ),
            logging.WARNING: logging.Formatter(
                Colored.cyan('%(asctime)s') + ' ' + 
                Colored.blue('%(name)s') + ' ' + 
                Colored.yellow('WARNING') + ' ' + 
                Colored.yellow('%(message)s') + ' ' + 
                Colored.yellow('[%(filename)s:%(lineno)d]')
            ),
            logging.ERROR: logging.Formatter(
                Colored.cyan('%(asctime)s') + ' ' + 
                Colored.blue('%(name)s') + ' ' + 
                Colored.red('ERROR') + ' ' + 
                Colored.red('%(message)s') + ' ' + 
                Colored.yellow('[%(filename)s:%(lineno)d]')
            ),
            logging.CRITICAL: logging.Formatter(
                Colored.cyan('%(asctime)s') + ' ' + 
                Colored.blue('%(name)s') + ' ' + 
                Colored.red('CRITICAL') + ' ' + 
                Colored.red('%(message)s') + ' ' + 
                Colored.yellow('[%(filename)s:%(lineno)d]') + ' !!!'
            )
        }

    def format(self, record):
        if self.use_color:
            formatter = self.color_formatters.get(record.levelno)
        else:
            formatter = self.plain_formatters.get(record.levelno)
        
        if formatter is None:
            formatter = self.plain_formatters[logging.DEBUG]
        
        return formatter.format(record)

def setup_logger():
    """
    配置并返回全局日志记录器
    
    特性:
    - 彩色输出: 不同日志级别和信息使用不同颜色
    - 格式化输出: 时间、模块名、级别、消息和位置信息
    - 防止重复: 确保只添加一次处理器
    - 日志轮转: 按天创建新日志文件，保留30天的历史日志
    
    返回:
        logging.Logger: 配置好的全局日志记录器
    """
    
    # 获取根日志记录器
    logger = logging.getLogger()
    
    # 如果没有处理器，添加处理器
    if not logger.handlers:
        # 创建控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(CustomFormatter())
        logger.addHandler(console_handler)
        
        # 创建日志目录
        # log_dir = 'logs'
        # if not os.path.exists(log_dir):
        #     os.makedirs(log_dir)
        
        # 创建按天轮转的文件处理器
        # when='midnight'表示每天午夜创建新日志文件
        # backupCount=30表示保留30天的日志文件
        # file_handler = TimedRotatingFileHandler(
        #     os.path.join(log_dir, 'general.log'),
        #     when='midnight',
        #     interval=1,
        #     backupCount=30,
        #     encoding='utf-8'
        # )
        
        # # 设置日志文件命名格式为'app.log.YYYY-MM-DD'
        # file_handler.suffix = '%Y-%m-%d'
        
        # file_handler.setFormatter(
        #     logging.Formatter(
        #         '%(asctime)s [%(name)s] [%(levelname)s] %(message)s [%(filename)s:%(lineno)d]'
        #     )
        # )
        # logger.addHandler(file_handler)
    
    # 设置日志级别
    logger.setLevel(logging.INFO)
    
    return logger

def get_module_logger(module_name):
    """
    获取模块专属的logger
    
    Args:
        module_name: 模块名称
    
    Returns:
        logging.Logger: 模块专属的logger
    """
    logger = logging.getLogger(module_name)
    
    if not logger.handlers:  # 如果该模块logger没有处理器
        # 创建控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(CustomFormatter())
        logger.addHandler(console_handler)
    
    return logger

# 全局默认logger保持不变
logger = setup_logger()