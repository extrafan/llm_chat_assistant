from tools.load_json import load_json
from tools.secret import decrypt_aes
from classes.config import Secret, ApiKey, ApiUrl, ConfigOnlineModels, ConfigLocalModels

CONFIG_PATH = "./configs/config.json"
CMD_MAP_PATH = "./configs/commands.json"
JSON_CONFIGS = load_json(CONFIG_PATH, "主配置")
SECRET = Secret(**JSON_CONFIGS["secret"])
API_KEY = ApiKey(**{k: decrypt_aes(v) for k, v in JSON_CONFIGS["api_key"].items()})
API_URL = ApiUrl(**JSON_CONFIGS["api_url"])
CONFIG_ONLINE_MODELS = ConfigOnlineModels(**JSON_CONFIGS["online_models"])
CONFIG_LOCAL_MODELS = ConfigLocalModels(**JSON_CONFIGS["local_models"])