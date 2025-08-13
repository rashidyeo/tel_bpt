from telethon import TelegramClient, events


api_id = "24137179"  
api_hash = "1c0a5a968a4d8ca6aac4537543197fd8"  

# القنوات
source_channel = "t.me/almasirah2"  
target_channel = "t.me/dhamarnews0"  

client = TelegramClient("user_session", api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def forward_message(event):
    original_message = event.message.message or ""

    modified_message = modify_message(original_message)

    if event.message.media:
        await client.send_file(
            target_channel,
            event.message.media,  
            caption=modified_message, 
            link_preview=False  
        )
    else:
        await client.send_message(target_channel, modified_message, link_preview=False)

def modify_message(original_message):
    """
    دالة لتعديل نص الرسالة
    """

    unwanted_words = ["Almasirah.net.ye", "ⓣ.me/almasirah2"]
    for word in unwanted_words:
        original_message = original_message.replace(word, "")

    return f"{original_message}                        #ذمار_نيوز\nhttps://t.me/dhamarnews0"

print("البوت يعمل باستخدام حساب المستخدم...")
client.start()
client.run_until_disconnected()
