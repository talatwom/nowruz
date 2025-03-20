from flask import Flask, render_template, request, jsonify
from modules.ai_service import setup_ai_service
from modules.generator import generate_greeting
from modules.rate_limiter import rate_limiter
from modules.telegram_service import send_telegram_notification
from config import AVALAI_API_KEY, AVALAI_API_BASE_URL
import os
import datetime

# Initialize Flask app
app = Flask(__name__)

# Setup AI service
llm = setup_ai_service(AVALAI_API_KEY, AVALAI_API_BASE_URL)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    if request.method == 'POST':
        recipient_name = request.form.get('recipient_name')
        sender_name = request.form.get('sender_name')
        topic = request.form.get('topic')
        message_length = request.form.get('message_length', 'short')
        
        # بررسی محدودیت درخواست
        client_ip = request.remote_addr
        is_allowed, wait_time = rate_limiter.is_allowed(client_ip)
        
        if not is_allowed:
            return render_template('index.html', error=f"لطفاً {wait_time} ثانیه صبر کنید و دوباره تلاش کنید.")
        
        if recipient_name and sender_name:
            message = generate_greeting(llm, recipient_name, sender_name, topic, message_length)
            
            # ارسال به تلگرام
            user_data = {
                'recipient_name': recipient_name,
                'sender_name': sender_name,
                'topic': topic,
                'message_length': message_length,
                'message': message,
                'ip_address': client_ip,
                'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            send_telegram_notification(user_data)
    
    return render_template('index.html', message=message)

@app.route('/api/generate', methods=['POST'])
def api_generate():
    data = request.json
    recipient_name = data.get('recipient_name')
    sender_name = data.get('sender_name')
    topic = data.get('topic')
    message_length = data.get('message_length', 'short')
    
    # بررسی محدودیت درخواست
    client_ip = request.remote_addr
    is_allowed, wait_time = rate_limiter.is_allowed(client_ip)
    
    if not is_allowed:
        return jsonify({
            'error': f"محدودیت درخواست: لطفاً {wait_time} ثانیه صبر کنید و دوباره تلاش کنید."
        }), 429
    
    if not recipient_name or not sender_name:
        return jsonify({'error': 'نام گیرنده و فرستنده الزامی است'}), 400
    
    message = generate_greeting(llm, recipient_name, sender_name, topic, message_length)
    
    # ارسال به تلگرام
    user_data = {
        'recipient_name': recipient_name,
        'sender_name': sender_name,
        'topic': topic,
        'message_length': message_length,
        'message': message,
        'ip_address': client_ip,
        'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    send_telegram_notification(user_data)
    
    return jsonify({'message': message})

if __name__ == '__main__':
    # Make sure necessary directories exist
    for dir_path in ['static/css', 'static/js', 'templates']:
        os.makedirs(dir_path, exist_ok=True)
    
    app.run(debug=True)