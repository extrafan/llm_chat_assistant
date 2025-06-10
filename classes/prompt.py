# 用于请求体验证的 Pydantic 基类
from pydantic import BaseModel

# 定义客户端请求的格式
class PromptRequest(BaseModel):
    prompt: str                 # 用户输入的提问/指令
    session_id: str = "default" # 会话ID，用于对话记忆
    stream: bool = False        # 是否流式返回，默认关闭