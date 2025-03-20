"""
ماژول ارسال اطلاعات به بات تلگرام
"""
import requests
import json
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_ADMIN_ID

def send_telegram_notification(user_data):
    """
    ارسال پیام به بات تلگرام با اطلاعات کاربر و پیام تولید شده
    
    پارامترها:
    user_data (dict): اطلاعات کاربر شامل نام، موضوع، پیام و آدرس IP
    
    خروجی:
    bool: وضعیت موفقیت ارسال پیام
    """
    try:
        # ساخت پیام قالب‌بندی شده
        message = f"""
🌷 *اطلاعات پیام تبریک جدید* 🌷

👤 *گیرنده:* {user_data.get('recipient_name')}
🙋‍♂️ *فرستنده:* {user_data.get('sender_name')}
🔖 *موضوع:* {user_data.get('topic') or 'تعیین نشده'}
📏 *نوع پیام:* {'کوتاه' if user_data.get('message_length') == 'short' else 'مفصل'}
🌐 *آی‌پی:* `{user_data.get('ip_address')}`
⏰ *زمان:* {user_data.get('timestamp')}

📝 *متن پیام:*
```
{user_data.get('message')}
```
"""
        
        # ارسال به تلگرام
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": TELEGRAM_ADMIN_ID,
            "text": message,
            "parse_mode": "Markdown"
        }
        
        response = requests.post(url, json=payload)
        result = response.json()
        
        # بررسی وضعیت ارسال
        if result.get("ok"):
            return True
        else:
            print(f"خطا در ارسال پیام به تلگرام: {result.get('description')}")
            return False
            
    except Exception as e:
        print(f"خطا در ارسال اطلاعات به تلگرام: {str(e)}")
        return False