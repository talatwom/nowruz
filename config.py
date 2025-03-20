import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# AI API Configuration
AVALAI_API_KEY = os.getenv("AVALAI_API_KEY", "aa-OIK6fjtJytf8zV5lcsdge2OefR38jQF8INNtNbs120am3fm6")
AVALAI_API_BASE_URL = os.getenv("AVALAI_API_BASE_URL", "https://api.avalai.ir/v1")

# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "7742069500:AAGTw5q861HwZiU2eZ8UPVpfbs-fvy1cn6U")
TELEGRAM_ADMIN_ID = os.getenv("TELEGRAM_ADMIN_ID", "86551786")  # Replace with your Telegram user ID

# App Configuration
APP_NAME = "پیام تبریک نوروز ۱۴۰۴"
APP_DESCRIPTION = "ساخت پیام‌های تبریک نوروزی شخصی‌سازی شده با هوش مصنوعی"
DEFAULT_MODEL = "gpt-4o-mini-2024-07-18"

# For production deployment set to False
DEBUG = True