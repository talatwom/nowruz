"""
ماژول محدودیت درخواست‌ها (Rate Limiter)
برای محدود کردن تعداد درخواست‌های ارسالی به هوش مصنوعی در هر دقیقه
"""
import time
from collections import defaultdict, deque
from threading import Lock

class RateLimiter:
    """
    کلاس محدودیت درخواست‌ها
    تعداد درخواست‌های مجاز در هر دقیقه را کنترل می‌کند
    """
    def __init__(self, max_requests_per_minute=3):
        """
        سازنده کلاس محدودیت درخواست‌ها
        
        پارامترها:
        max_requests_per_minute (int): حداکثر تعداد درخواست‌های مجاز در هر دقیقه
        """
        self.max_requests = max_requests_per_minute
        self.window_size = 60  # بازه زمانی: ۶۰ ثانیه (یک دقیقه)
        self.requests = defaultdict(deque)  # برای هر IP، صف زمان‌های درخواست‌ها
        self.lock = Lock()  # قفل برای اطمینان از thread-safety
    
    def is_allowed(self, ip_address):
        """
        بررسی می‌کند که آیا IP مورد نظر اجازه ارسال درخواست جدید دارد یا خیر
        
        پارامترها:
        ip_address (str): آدرس IP کاربر
        
        خروجی:
        bool: True اگر درخواست مجاز باشد، False در غیر این صورت
        int: زمان باقی‌مانده (به ثانیه) تا مجاز شدن درخواست بعدی، یا 0 اگر مجاز باشد
        """
        with self.lock:
            current_time = time.time()
            
            # حذف درخواست‌های قدیمی‌تر از یک دقیقه
            while self.requests[ip_address] and self.requests[ip_address][0] < current_time - self.window_size:
                self.requests[ip_address].popleft()
            
            # بررسی تعداد درخواست‌های فعلی
            if len(self.requests[ip_address]) < self.max_requests:
                self.requests[ip_address].append(current_time)
                return True, 0
            
            # محاسبه زمان باقی‌مانده تا آزاد شدن یک اسلات درخواست
            time_to_wait = int(self.window_size - (current_time - self.requests[ip_address][0])) + 1
            return False, time_to_wait

# ساخت یک نمونه از محدودکننده درخواست
rate_limiter = RateLimiter(max_requests_per_minute=3)