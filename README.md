# LLM Chat Assistant 🤖

一个功能强大的多模型大语言模型聊天助手，支持 OpenAI、DeepSeek 和 Ollama 本地模型的统一接入。

## ✨ 主要特性

### 🔐 安全配置管理
- **AES 加密存储**：API 密钥采用 AES 加密安全存储
- **统一配置管理**：集中管理所有 API 密钥、URL 和模型配置
- **类型安全验证**：使用 Pydantic 确保配置数据的类型安全

### 🤖 多模型支持
- **OpenAI API**：支持 GPT-4o、GPT-4o-mini、GPT-3.5 系列模型
- **DeepSeek API**：集成 DeepSeek Chat 模型
- **Ollama 本地模型**：支持本地部署的开源模型

### 🎨 用户体验优化
- **彩色日志系统**：多级别彩色日志输出，便于调试和监控
- **关键字高亮**：支持文本关键字高亮显示
- **详细错误处理**：完善的异常捕获和错误提示

### 💬 聊天功能
- **统一接口**：标准化的聊天 API 接口
- **会话管理**：支持 session_id 进行对话记忆
- **流式响应**：支持流式和非流式两种响应模式

## 🚀 快速开始

### 环境要求
- Python 3.8+
- 虚拟环境（推荐使用 `devoops` 环境）

### 安装依赖
```bash
pip install openai requests pycryptodome colorama pydantic
```

### 配置设置

1. **修改配置文件** `configs/config.json`：
   ```json
   {
     "secret": {
       "KEY": "your-aes-key",
       "IV": "your-aes-iv"
     },
     "api_key": {
       "OPENAI_API_KEY": "encrypted-openai-key",
       "DEEPSEEK_API_KEY": "encrypted-deepseek-key"
     },
     "api_url": {
       "DEEPSEEK_BASE_URL": "https://api.deepseek.com",
       "OLLAMA_BASE_URL": "http://127.0.0.1:11434/api/generate",
       "OLLAMA_CHAT_URL": "http://127.0.0.1:11434/api/chat/completions"
     }
   }
   ```

2. **初始化项目**：
   ```python
   from main import init
   init()  # 初始化环境变量和配置
   ```

## 📖 使用示例

### OpenAI API 调用
```python
import config
from openai import OpenAI
from main import init

init()  # 初始化配置

client = OpenAI()
response = client.chat.completions.create(
    model=config.CONFIG_ONLINE_MODELS.OPENAI_MODEL,
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ]
)
print(response.choices[0].message.content)
```

### DeepSeek API 调用
```python
import config
from openai import OpenAI
from main import init

init()

client = OpenAI(
    api_key=config.API_KEY.DEEPSEEK_API_KEY,
    base_url=config.API_URL.DEEPSEEK_BASE_URL
)
response = client.chat.completions.create(
    model=config.CONFIG_ONLINE_MODELS.DEEPSEEK_MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ]
)
print(response.choices[0].message.content)
```

### Ollama 本地模型调用
```python
import config
import requests
from main import init

init()

data = {
    "model": config.CONFIG_LOCAL_MODELS.DEEPSEEK_MODEL,
    "prompt": "解释一下机器学习的基本概念",
}
response = requests.post(
    config.API_URL.OLLAMA_BASE_URL,
    json=data
)
print(response.json())
```

### 使用统一聊天接口
```python
from functions.llm.chat import generate_code
from classes.prompt import PromptRequest

request = PromptRequest(
    prompt="写一个Python排序算法",
    session_id="user_001",
    stream=False
)
result = generate_code(request)
print(result)
```

## 📁 项目结构

```
llm_chat_assistant/
├── main.py                 # 项目初始化入口
├── config.py              # 配置管理模块
├── llm_chat.ipynb         # Jupyter 演示笔记本
├── configs/
│   └── config.json        # 主配置文件
├── components/
│   ├── logger.py          # 日志系统
│   └── color.py           # 颜色工具
├── tools/
│   ├── load_json.py       # JSON 配置加载
│   └── secret.py          # 加密解密工具
├── classes/
│   ├── config.py          # 配置数据模型
│   └── prompt.py          # 请求数据模型
└── functions/
    └── llm/
        └── chat.py        # 聊天功能实现
```

## 🛠 主要模块说明

### 配置管理 (`config.py`)
- 统一加载和管理所有配置项
- 自动解密 API 密钥
- 类型安全的配置验证

### 日志系统 (`components/logger.py`)
- 多级别日志支持（DEBUG、INFO、WARNING、ERROR、CRITICAL）
- 彩色终端输出
- 详细的调用位置信息

### 安全工具 (`tools/secret.py`)
- AES 加密/解密功能
- 保护敏感配置信息

### 聊天功能 (`functions/llm/chat.py`)
- 统一的模型调用接口
- 标准化的请求/响应格式
- 完整的错误处理机制

## 📋 支持的模型

### 在线模型
- **OpenAI**: GPT-4o, GPT-4o-mini, GPT-3.5-turbo 系列
- **DeepSeek**: deepseek-chat

### 本地模型 (Ollama)
- **DeepSeek**: deepseek-scaler, deepseek-r1
- 其他兼容 Ollama 的开源模型

## 🔧 高级配置

### 自定义日志级别
```python
from components.logger import get_module_logger

logger = get_module_logger("my_module")
logger.info("自定义模块日志")
```

### 密钥加密存储
```python
from tools.secret import encrypt_aes, decrypt_aes

# 加密新的 API 密钥
encrypted_key = encrypt_aes("your-api-key")
print(encrypted_key)

# 解密使用
decrypted_key = decrypt_aes(encrypted_key)
```

## 📝 开发说明

- 本项目在 macOS 环境下开发
- 推荐使用 `devoops` 虚拟环境
- 代码注释采用 JSDoc 风格
- 前端代码使用 ES6 语法标准

## 🤝 贡献指南

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

---

🌟 **如果这个项目对您有帮助，请给个 Star！**
