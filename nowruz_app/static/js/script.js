document.addEventListener('DOMContentLoaded', function() {
    // دکمه کپی پیام
    const copyBtn = document.getElementById('copy-btn');
    if (copyBtn) {
        copyBtn.addEventListener('click', function() {
            const messageText = document.getElementById('message-content').innerText;
            
            // کپی متن به کلیپ‌بورد
            navigator.clipboard.writeText(messageText).then(function() {
                // نمایش اعلان موفقیت
                const originalText = copyBtn.innerHTML;
                copyBtn.innerHTML = '<i class="fas fa-check"></i> کپی شد';
                
                // بازگرداندن متن اصلی دکمه بعد از 2 ثانیه
                setTimeout(function() {
                    copyBtn.innerHTML = originalText;
                }, 2000);
                
            }).catch(function(err) {
                console.error('خطا در کپی کردن متن: ', err);
            });
        });
    }
    
    // دکمه اشتراک‌گذاری
    const shareBtn = document.getElementById('share-btn');
    if (shareBtn) {
        shareBtn.addEventListener('click', function() {
            const messageText = document.getElementById('message-content').innerText;
            
            // اگر API اشتراک‌گذاری وب در مرورگر پشتیبانی می‌شود
            if (navigator.share) {
                navigator.share({
                    title: 'پیام تبریک نوروزی',
                    text: messageText
                }).then(() => {
                    console.log('پیام با موفقیت به اشتراک گذاشته شد');
                }).catch((error) => {
                    console.log('خطا در اشتراک‌گذاری', error);
                });
            } else {
                // نمایش یک اعلان برای مرورگرهایی که از API اشتراک‌گذاری پشتیبانی نمی‌کنند
                alert('متن پیام را کپی کرده و در برنامه مورد نظر خود به اشتراک بگذارید.');
            }
        });
    }
    
    // ارسال فرم با AJAX (بدون رفرش صفحه)
    const messageForm = document.getElementById('message-form');
    if (messageForm) {
        messageForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // نمایش لودینگ
            const submitBtn = document.getElementById('submit-btn');
            const originalBtnText = submitBtn.innerHTML;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> در حال ساخت پیام...';
            submitBtn.disabled = true;
            
            // گرفتن داده‌های فرم
            const formData = {
                recipient_name: document.getElementById('recipient_name').value,
                sender_name: document.getElementById('sender_name').value,
                topic: document.getElementById('topic').value
            };
            
            // ارسال درخواست به سرور
            fetch('/api/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            })
            .then(response => response.json())
            .then(data => {
                // نمایش پیام دریافتی یا خطا
                const messageBox = document.getElementById('message-box');
                const messageContent = document.getElementById('message-content');
                
                // اگر خطای محدودیت درخواست وجود داشت
                if (data.error && data.error.includes('محدودیت درخواست')) {
                    // نمایش پیام خطا
                    let errorDiv = document.querySelector('.error-message');
                    if (!errorDiv) {
                        errorDiv = document.createElement('div');
                        errorDiv.className = 'error-message';
                        messageForm.insertAdjacentElement('afterend', errorDiv);
                    }
                    errorDiv.innerHTML = `<i class="fas fa-exclamation-circle"></i> ${data.error}`;
                    
                    // اسکرول به سمت پیام خطا
                    errorDiv.scrollIntoView({ behavior: 'smooth' });
                } 
                else if (data.message) {
                    // حذف پیام خطا اگر وجود داشت
                    const errorDiv = document.querySelector('.error-message');
                    if (errorDiv) {
                        errorDiv.remove();
                    }
                    
                    // اگر پیام وجود نداشته باشد، آن را ایجاد کنیم
                    if (!messageBox.style.display || messageBox.style.display === 'none') {
                        messageBox.style.display = 'block';
                        // افزودن کلاس انیمیشن
                        messageBox.classList.add('animated');
                    }
                    
                    // به‌روزرسانی محتوای پیام
                    messageContent.textContent = data.message;
                    
                    // اسکرول به پایین صفحه برای نمایش پیام
                    messageBox.scrollIntoView({ behavior: 'smooth' });
                }
                
                // بازگرداندن وضعیت دکمه
                submitBtn.innerHTML = originalBtnText;
                submitBtn.disabled = false;
            })
            .catch(error => {
                console.error('خطا:', error);
                
                // بازگرداندن وضعیت دکمه
                submitBtn.innerHTML = originalBtnText;
                submitBtn.disabled = false;
                
                // نمایش خطا
                alert('خطا در ارتباط با سرور. لطفاً دوباره تلاش کنید.');
            });
        });
    }
});document.addEventListener('DOMContentLoaded', function() {
    // دکمه کپی پیام
    const copyBtn = document.getElementById('copy-btn');
    if (copyBtn) {
        copyBtn.addEventListener('click', function() {
            const messageText = document.getElementById('message-content').innerText;
            
            // کپی متن به کلیپ‌بورد
            navigator.clipboard.writeText(messageText).then(function() {
                // نمایش اعلان موفقیت
                const originalText = copyBtn.innerHTML;
                copyBtn.innerHTML = '<i class="fas fa-check"></i> کپی شد';
                
                // بازگرداندن متن اصلی دکمه بعد از 2 ثانیه
                setTimeout(function() {
                    copyBtn.innerHTML = originalText;
                }, 2000);
                
            }).catch(function(err) {
                console.error('خطا در کپی کردن متن: ', err);
            });
        });
    }
    
    // دکمه اشتراک‌گذاری
    const shareBtn = document.getElementById('share-btn');
    if (shareBtn) {
        shareBtn.addEventListener('click', function() {
            const messageText = document.getElementById('message-content').innerText;
            
            // اگر API اشتراک‌گذاری وب در مرورگر پشتیبانی می‌شود
            if (navigator.share) {
                navigator.share({
                    title: 'پیام تبریک نوروزی',
                    text: messageText
                }).then(() => {
                    console.log('پیام با موفقیت به اشتراک گذاشته شد');
                }).catch((error) => {
                    console.log('خطا در اشتراک‌گذاری', error);
                });
            } else {
                // نمایش یک اعلان برای مرورگرهایی که از API اشتراک‌گذاری پشتیبانی نمی‌کنند
                alert('متن پیام را کپی کرده و در برنامه مورد نظر خود به اشتراک بگذارید.');
            }
        });
    }
    
    // ارسال فرم با AJAX (بدون رفرش صفحه)
    const messageForm = document.getElementById('message-form');
    if (messageForm) {
        messageForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // نمایش لودینگ
            const submitBtn = document.getElementById('submit-btn');
            const originalBtnText = submitBtn.innerHTML;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> در حال ساخت پیام...';
            submitBtn.disabled = true;
            
            // گرفتن داده‌های فرم
            const formData = {
                recipient_name: document.getElementById('recipient_name').value,
                sender_name: document.getElementById('sender_name').value,
                topic: document.getElementById('topic').value
            };
            
            // ارسال درخواست به سرور
            fetch('/api/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            })
            .then(response => response.json())
            .then(data => {
                // نمایش پیام دریافتی
                const messageBox = document.getElementById('message-box');
                const messageContent = document.getElementById('message-content');
                
                if (data.message) {
                    // اگر پیام وجود نداشته باشد، آن را ایجاد کنیم
                    if (!messageBox.style.display || messageBox.style.display === 'none') {
                        messageBox.style.display = 'block';
                        // افزودن کلاس انیمیشن
                        messageBox.classList.add('animated');
                    }
                    
                    // به‌روزرسانی محتوای پیام
                    messageContent.textContent = data.message;
                    
                    // اسکرول به پایین صفحه برای نمایش پیام
                    messageBox.scrollIntoView({ behavior: 'smooth' });
                }
                
                // بازگرداندن وضعیت دکمه
                submitBtn.innerHTML = originalBtnText;
                submitBtn.disabled = false;
            })
            .catch(error => {
                console.error('خطا:', error);
                
                // بازگرداندن وضعیت دکمه
                submitBtn.innerHTML = originalBtnText;
                submitBtn.disabled = false;
                
                // نمایش خطا
                alert('خطا در ارتباط با سرور. لطفاً دوباره تلاش کنید.');
            });
        });
    }
});