"""
سرویس هوش مصنوعی برای تولید پیام‌های تبریک نوروزی
"""
from langchain_openai import ChatOpenAI
import openai
from config import DEFAULT_MODEL

def setup_ai_service(api_key, api_base_url):
    """
    راه‌اندازی سرویس هوش مصنوعی
    
    پارامترها:
    api_key (str): کلید API
    api_base_url (str): آدرس پایه API
    
    خروجی:
    ChatOpenAI: نمونه مدل LangChain
    """
    # تنظیم کلاینت OpenAI
    openai.api_key = api_key
    openai.api_base = api_base_url
    
    # ساخت و برگرداندن مدل LangChain
    return ChatOpenAI(
        model_name=DEFAULT_MODEL,
        openai_api_key=api_key,
        openai_api_base=api_base_url
    )