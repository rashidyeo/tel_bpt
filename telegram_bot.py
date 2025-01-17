from telethon import TelegramClient, events

# إعدادات الحساب
api_id = "24781147"  # أدخل API ID الخاص بك
api_hash = "abd183b2294312c52ef1fd1ac38b9b22"  # أدخل API Hash الخاص بك

# القنوات
source_channel = "t.me/almasirah2"  # اسم مستخدم القناة العامة
target_channel = "t.me/dhamarnews0"  # معرف أو اسم مستخدم القناة الهدف

# إنشاء عميل Telethon
client = TelegramClient("user_session", api_id, api_hash)

# الاستماع إلى الرسائل في القناة المصدر
@client.on(events.NewMessage(chats=source_channel))
async def forward_message(event):
    # نص الرسالة الأصلي
    original_message = event.message.message or ""

    # تعديل النص
    modified_message = modify_message(original_message)

    # إرسال الرسالة المعدلة مع الوسائط إن وجدت
    if event.message.media:
        await client.send_file(
            target_channel,
            event.message.media,  # الوسائط (الصورة/الفيديو/المستند)
            caption=modified_message,  # النص المعدل
            link_preview=False  # منع ظهور بطاقة المعاينة
        )
    else:
        # إرسال النص فقط مع تعطيل بطاقة الرابط
        await client.send_message(target_channel, modified_message, link_preview=False)

def modify_message(original_message):
    """
    دالة لتعديل نص الرسالة
    """
    # حذف كلمات معينة
    unwanted_words = ["Almasirah.net.ye", "ⓣ.me/almasirah2"]
    for word in unwanted_words:
        original_message = original_message.replace(word, "")
    # إضافة توقيع في نهاية النص
    return f"{original_message}                        #ذمار_نيوز\nhttps://t.me/dhamarnews0"

print("البوت يعمل باستخدام حساب المستخدم...")
client.start()
client.run_until_disconnected()