from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
# 🎨 فۆنتی وشەی fancy
def fancy_fonts(text):
    plain = "abcdefghijklmnopqrstuvwxyz"
    fonts = [
        "𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏",
        "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫",
        "ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ",
        "🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩",
        "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳",
        "𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧",
        "ᵃᵇᶜᵈᵉᶠᵍʰᶤʲᵏˡᵐⁿᵒᵖᑫʳˢᵗᵘᵛʷˣʸᶻ",
        "𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟",
        "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃",
        "🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉",
        "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣",
        "ᗩᗷᑕᗪEᖴGᕼIᒍKᒪᗰᑎOᑭᑫᖇᔕTᑌᐯᗯ᙭Yᘔ",
        "₳฿₵ĐɆ₣₲ⱧłJ₭Ⱡ₥₦Ø₱QⱤ₴₮ɄV₩ӾɎⱫ"

    ]

    valid_fonts = [f for f in fonts if len(f) == len(plain)]
    return [text.lower().translate(str.maketrans(plain, style)) for style in valid_fonts]
# 📋 تۆمارکردنی بەکارهێنەر
def save_user(update: Update):
    user_id = str(update.effective_user.id)
    with open("users.txt", "a+") as f:
        f.seek(0)
        if user_id not in f.read().splitlines():
            f.write(user_id + "\n")

# 📌 /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    save_user(update)

    CHANNEL_ID =-1001867274340 # ← لێرە ID ـی چەنەڵەکەت دانێ

    try:
        member = await context.bot.get_chat_member(CHANNEL_ID, update.effective_user.id)
        if member.status not in ["member", "administrator", "creator"]:
            await update.message.reply_text("❌ بۆ بەکارهێنانی ئەم بۆتە، دەبێت یەکەم چەنەڵەکە join بکەی:\n👉 https://t.me/Bl4ck_Net")
            return
    except:
        await update.message.reply_text("❌ ناتوانم دڵنیابم ئەو چەنەڵەت join کردووە.\nتکایە دووبارە هەوڵ بدە.")
        return

    await update.message.reply_text(
        "👋 بەخێربێیت بۆ بۆتی زەخرەفە!\n📝 وشە بنێرە بۆ گۆڕینی بۆ فۆنتە جیاوازەکان."
    )
# 📌 handle text message
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    save_user(update)
    styles = fancy_fonts(update.message.text)
    await update.message.reply_text("\n".join(styles))

# 📌 /count
async def count_users(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        with open("users.txt", "r") as f:
            users = set(f.read().splitlines())
            await update.message.reply_text(f"👥 ژمارەی بەکارهێنەران: {len(users)} کەس")
    except FileNotFoundError:
        await update.message.reply_text("هیچ بەکارهێنەرێک تۆمار نەکراوە.")

# ▶️ دەستپێکردنی بۆت
def main():
    BOT_TOKEN = "8488377606:AAGe--YgYjkK8qx32jtev1TQmK3FP3DrHvQ"  # ← لێرە توکنی بۆتەکەت دانێ
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("count", count_users))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    print("✅ بۆتی زەخرەفە چالاکە...")
    app.run_polling()

main()