# 用于请求体验证的 Pydantic 基类
from pydantic import BaseModel
from enum import Enum

class LocalModel(Enum):
    DEEPSEEK_SCALER = "deepseek-scaler:latest"
    DEEPSEEK_R1_1_DOT_5 = "deepseek-r1:1.5b"
    
class OnlineModel(Enum):
    DEEPSEEK_CHAT = "deepseek-chat"
    GPT_4O = "gpt-4o"
    GPT_4O_MINI = "gpt-4o-mini"
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_3_5_TURBO_MINI = "gpt-3.5-turbo-mini"
    GPT_3_5_TURBO_1106 = "gpt-3.5-turbo-1106"
    GPT_3_5_TURBO_1106_MINI = "gpt-3.5-turbo-1106-mini"

class Secret(BaseModel):
    KEY: str
    IV: str

class ApiKey(BaseModel):
    OPENAI_API_KEY: str
    DEEPSEEK_API_KEY: str

class ApiUrl(BaseModel):
    DEEPSEEK_BASE_URL: str
    OLLAMA_BASE_URL: str
    OLLAMA_CHAT_URL: str

class Models(BaseModel):
    LOCAL_MODEL: LocalModel
    ONLINE_MODEL: OnlineModel

class ConfigOnlineModels(BaseModel):
    DEEPSEEK_MODEL: str
    OPENAI_MODEL: str

class ConfigLocalModels(BaseModel):
    DEEPSEEK_MODEL: str
