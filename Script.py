class script(object):
    START_TXT = """<blockquote>👋🏻 Hᴇʟʟᴏ {}.</blockquote>
𝖨’𝗆 𝖺𝗇 𝖺𝗎𝗍𝗈 𝖿𝗂𝗅𝗍𝖾𝗋 𝖻𝗈𝗍 𝗍𝗁𝖺𝗍 𝖼𝖺𝗇 𝗉𝗋𝗈𝗏𝗂𝖽𝖾 𝗆𝗈𝗏𝗂𝖾𝗌 𝗂𝗇 𝗒𝗈𝗎𝗋 𝗍𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝗀𝗋𝗈𝗎𝗉𝗌.

➕ 𝖠𝖽𝖽 𝗆𝖾 𝗍𝗈 𝗒𝗈𝗎𝗋 𝗀𝗋𝗈𝗎𝗉  
🛡️ 𝖯𝗋𝗈𝗆𝗈𝗍𝖾 𝗆𝖾 𝖺𝗌 𝖺𝗇 𝖠𝖽𝗆𝗂𝗇

🚀 𝖠𝗇𝖽 𝗂’𝗅𝗅 𝗍𝖺𝗄𝖾 𝗂𝗍 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾𝗋𝖾!

<blockquote>©️ Maintained by <a href="https://t.me/im_goutham_josh">Sa</a></blockquote>"""

    HELP_TXT = """
🙋🏻‍♂️ Hᴇʟʟᴏ {}! 🤓

<blockquote>📌 Aᴠᴀɪʟᴀʙʟᴇ Cᴏᴍᴍᴀɴᴅs:</blockquote>

🔹 /start – Check if I’m alive  
🔹 /ping – Check bot response time  
🔹 /usage – How to use the bot  
🔹 /status – Bot system status  
🔹 /info – Your user info  
🔹 /id – Get your Telegram ID  
🔹 /stats – Database stats  
🔹 /broadcast – Broadcast message (Owner only)

<blockquote>📙 Nᴏᴛɪᴄᴇ:</blockquote>
⚠️ Pʟᴇᴀsᴇ ᴅᴏɴ’ᴛ sᴘᴀᴍ ᴛʜᴇ ʙᴏᴛ. 🙂
"""
    ABOUT_TXT = """<b>
<blockquote>🤖 Nᴀᴍᴇ: Rᴀꜱʜᴍɪᴋᴀ Mᴀɴᴅᴀɴɴᴀ™</blockquote>

👨‍💻 Cʀᴇᴀᴛᴏʀ: <a href="https://t.me/Sandalwood_Man">Goutham SER</a>  
💬 Lᴀɴɢᴜᴀɢᴇ: Pʏᴛʜᴏɴ 3  
🗄️ Dᴀᴛᴀʙᴀsᴇ: Mᴏɴɢᴏ DB  
🌐 Sᴇʀᴠᴇʀ: KᴏYᴇʙ
</b>"""
    SOURCE_TXT = """<b>📢 NOTE:</b>
<blockquote>ᴋᴜᴛᴛᴜ ʙᴏᴛ™ is an open source project.</blockquote>

🔗 <b>Source Code:</b> <a href="https://github.com/GouthamSER">Click Here 😂</a>

<b>👨‍💻 DEVS:</b>  
<blockquote><a href="https://t.me/wudixh12">Gᴏᴜᴛʜᴀᴍ Josh ✅</a></blockquote>
"""

    MANUALFILTER_TXT = """<b>❓ Help: Filters</b>

Filters allow users to set automated replies for specific keywords. Whenever a message contains a keyword, EvaMaria will automatically respond with the preset message.

<b>🔒 NOTE:</b>
1. The bot must have <b>admin privileges</b> in the chat.  
2. Only <b>admins</b> can add or manage filters.  
3. <b>Alert buttons</b> have a character limit of 64.

<b>⚙️ Commands & Usage:</b>
• <code>/filter</code> – Add a filter to the chat  
• <code>/filters</code> – List all filters in the chat  
• <code>/del</code> – Delete a specific filter  
• <code>/delall</code> – Delete all filters (Chat Owner only)
"""

    BUTTON_TXT = """<b>❓ Help: Buttons</b>

This bot supports both URL and alert inline buttons.

<b>🔒 NOTE:</b>
1. Telegram does not allow sending buttons without content; content is mandatory.  
2. Buttons are supported with any Telegram media type.  
3. Buttons must be properly formatted using Markdown syntax.

<b>🌐 URL Buttons:</b>
<code>[Button Text](buttonurl:https://t.me/sources_cods)</code>

<b>⚠️ Alert Buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>
"""
    AUTOFILTER_TXT = """<b>❓ Help: Auto Filter</b>

<b>⚠️ NOTE:</b>
1. Please make me an admin of your channel if it is private.  
2. Ensure your channel does not contain camrips, porn, or fake files.  
3. Forward the last message to me with quotes.  
   I will add all the files from that channel to my database.
"""
    CONNECTION_TXT = """<b>❓ Help: Connections</b>

- Used to connect the bot to your PM for managing filters.  
- Helps to avoid spamming in groups.

<b>⚠️ NOTE:</b>
1. Only admins can add a connection.  
2. Send <code>/connect</code> to connect me to your PM.

<b>⚙️ Commands & Usage:</b>
• <code>/connect</code> – Connect a particular chat to your PM.  
• <code>/disconnect</code> – Disconnect from a chat.  
• <code>/connections</code> – List all your connections.
"""
    EXTRAMOD_TXT = """<b>❓ Help: Extra Modules</b>

<b>⚠️ NOTE:</b>
These are additional features of Eva Maria.

<b>⚙️ Commands & Usage:</b>
• <code>/id</code> – Get the ID of a specified user.  
• <code>/info</code> – Get information about a user.  
• <code>/imdb</code> – Get film information from IMDb.  
• <code>/search</code> – Get film information from various sources.
"""
    ADMIN_TXT = """<b>❓ Help: Admin Mods</b>

<b>⚠️ NOTE:</b>  
This module only works for my admins.

<b>⚙️ Commands & Usage:</b>
• <code>/logs</code> – Get recent errors.  
• <code>/stats</code> – Get status of files in the database.  
• <code>/delete</code> – Delete a specific file from the database.  
• <code>/users</code> – Get list of users and their IDs.  
• <code>/chats</code> – Get list of chats and their IDs.  
• <code>/leave</code> – Leave a chat.  
• <code>/disable</code> – Disable a chat.  
• <code>/ban</code> – Ban a user.  
• <code>/unban</code> – Unban a user.  
• <code>/channel</code> – Get list of connected channels.  
• <code>/broadcast</code> – Broadcast a message to all users.
"""
    STATUS_TXT = """📁 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
👥 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
💬 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
💾 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code>
📦 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code>
"""
    LOG_TEXT_G = """#NewGroup
👥 Group: {} (<code>{}</code>)
👤 Total Members: <code>{}</code>
➕ Added By: {}
"""
    RESULT_TXT = """<b>🎉 Yay! I dug through my database and found this for you:</b>
<blockquote>{}</blockquote>"""

    CUSTOM_FILE_CAPTION = """<blockquote><b>📁 Fɪʟᴇ Nᴀᴍᴇ: 📄 <code>{file_name}</code>

📦 Fɪʟᴇ Sɪᴢᴇ: 💾 <code>{file_size}</code>

🔗 [⚡ Jᴏɪɴ Eʟᴅᴏʀᴀᴅᴏ ⚡](https://t.me/+53lB8qzQaGFlNDll)</b></blockquote>"""
    
    RESTART_GC_TXT = """
<b>🔄 𝖡𝗈𝗍 𝖱𝖾𝗌𝗍𝖺𝗋𝗍𝖾𝖽!</b>
Kuttu Bot  
<a href="https://t.me/im_goutham_josh">@im_goutham_josh</a>

📅 𝖣𝖺𝗍𝖾 : <code>{}</code>  
⏰ 𝖳𝗂𝗆𝖾 : <code>{}</code>  
🌐 𝖳𝗂𝗆𝖾𝗓𝗈𝗇𝖾 : <code>Asia/Kolkata</code>  
🛠️ 𝖡𝗎𝗂𝗅𝖽 𝖲𝗍𝖺𝗍𝗎𝗌 : <code>𝗏1 [ 𝖲𝗍able 😁 ]</code>
"""
    
    LOG_TEXT_P = """#NewUser
🆔 ID: <code>{}</code>
👤 Name: {}
"""

    SPOLL_NOT_FND = """<blockquote>Oops! 🤖</blockquote>
No matches found for your request. 😵‍💫  
Take a peek at the instructions below and let’s try again! 👇🏼
"""
#SPELL CHECK LANGUAGES TO KNOW callback
    ENG_SPELL = """Please Note 📓

1️⃣ Ask using correct spelling.  
2️⃣ Don’t ask for movies that are not released on OTT platforms.   
"""
    MAL_SPELL = """ദയവായി താഴെ ശ്രദ്ധിക്കുക📓

1️⃣ ശരിയായ അക്ഷരവിന്യാസത്തിൽ ചോദിക്കുക.  
2️⃣ OTT പ്ലാറ്റ്‌ഫോമുകളിൽ റിലീസ് ചെയ്യാത്ത സിനിമകൾ ചോദിക്കരുത്.  
"""
    HIN_SPELL = """कृपया नीचे ध्यान दें📓

1️⃣ सही वर्तनी में पूछें।  
2️⃣ उन फिल्मों के बारे में न पूछें जो ओटीटी प्लेटफॉर्म पर रिलीज़ नहीं हुई हैं।  
"""
    TAM_SPELL = """கீழே கவனிக்கவும்📓

1️⃣ சரியான எழுத்துப்பிழையில் கேளுங்கள்.  
2️⃣ வெளியாகாத திரைப்படங்களை கேட்காதீர்கள்.   
"""

    CHK_MOV_ALRT = "♻️ Eᴅᴀᴀ Mᴏɴᴇʜ ᴄʜᴇᴄᴋɪɴɢ ꜰɪʟᴇ ᴏɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ... ♻️"

    OLD_MES = "Eᴅᴀᴀ Mᴏɴᴇʜ, 𝐘𝐨𝐮 𝐚𝐫𝐞 𝐮𝐬𝐢𝐧𝐠 𝐨𝐧𝐞 𝐨𝐟 𝐦𝐲 𝐨𝐥𝐝 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬 🤔. 𝐏𝐥𝐞𝐚𝐬𝐞 𝐬𝐞𝐧𝐝 𝐭𝐡𝐞 𝐫𝐞𝐪𝐮𝐞𝐬𝐭 𝐚𝐠𝐚𝐢𝐧."

    MOV_NT_FND = """<b>Eᴅᴀᴀ Mᴏɴᴇʜ, Tʜɪs Mᴏᴠɪᴇ ɪs Nᴏᴛ Yᴇᴛ Rᴇʟᴇᴀsᴇᴅ ᴏʀ Aᴅᴅᴇᴅ Tᴏ ᴅᴀᴛᴀʙᴀsᴇ.</b>
<blockquote>Report To ADMIN - <a href="https://t.me/im_goutham_josh">@im_goutham_josh</a></blockquote>
"""

    RESTART_TXT = """<b><u>𝖡𝗈𝗍 𝖱𝖾𝗌𝗍𝖺𝗋𝗍𝖾𝖽 ✅
Kuttu Bot ¹ 💓</u></b>"""
    DMCA_TXT = """<b><u>This Telegram bot is designed to operate within the guidelines of the Digital Millennium Copyright Act (DMCA) and respects intellectual property rights. We are committed to responding to any valid DMCA takedown notices promptly.</u></b>

<blockquote>Please send your DMCA takedown notice to dmcarexie@proton.me</blockquote>
"""



