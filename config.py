import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# AI API Configuration
AVALAI_API_KEY = os.getenv("AVALAI_API_KEY", "aa-OIK6fjtJytf8zV5lcsdge2OefR38jQF8INNtNbs120am3fm6")
AVALAI_API_BASE_URL = os.getenv("AVALAI_API_BASE_URL", "https://api.avalai.ir/v1")

# App Configuration
APP_NAME = "پیام تبریک نوروزی"
APP_DESCRIPTION = "ساخت پیام‌های تبریک نوروزی شخصی‌سازی شده با هوش مصنوعی"
DEFAULT_MODEL = "gpt-4o-mini-2024-07-18"

# For production deployment set to False
DEBUG = True