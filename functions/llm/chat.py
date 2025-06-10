import config
import requests
from classes.prompt import PromptRequest

def generate_code(data: PromptRequest):
    prompt = data.prompt           # 获取用户输入的提问
    session_id = data.session_id   # 获取用户传入的会话 ID
    stream = data.stream           # 获取是否流式标记（未使用）

    # 构建请求体，准备发送给 Ollama 模型
    payload = {
        "model": config.CONFIG_MODELS.OLLAMA_MODEL,
        "prompt": prompt,
        "stream": stream
    }

    try:
        # 向 Ollama 模型发送请求并获取返回结果
        response = requests.post(config.API_URL.OLLAMA_BASE_URL, json=payload)
        result = response.json()                    # 解析 JSON 响应
        answer = result.get("response", "")         # 获取模型生成的回答内容

        # 将结果返回给前端
        return {
            "success": True,
            "model": config.CONFIG_MODELS.OLLAMA_MODEL,
            "prompt": prompt,
            "response": answer
        }

    except Exception as e:
        # 如果模型请求失败，返回错误信息
        return {
            "success": False,
            "error": str(e)
        }
    