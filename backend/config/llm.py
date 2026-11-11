import os

from agno.models.openai import OpenAIChat

DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1"
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

# Used by agents that need tools (Exa/Firecrawl, etc.); deepseek-chat keeps function calling stable
model = OpenAIChat(
    id="deepseek-chat",
    base_url=DEEPSEEK_BASE_URL,
    api_key=DEEPSEEK_API_KEY,
    temperature=0.3,
    max_tokens=8096
)

# deepseek-reasoner, for tasks that need no tools and require heavy reasoning/summarization
model2 = OpenAIChat(
    id="deepseek-reasoner",
    base_url=DEEPSEEK_BASE_URL,
    api_key=DEEPSEEK_API_KEY,
    temperature=0.1
)

model_zero = OpenAIChat(
    id="deepseek-reasoner",
    base_url=DEEPSEEK_BASE_URL,
    api_key=DEEPSEEK_API_KEY,
    temperature=0.1,
    max_tokens=8096
)