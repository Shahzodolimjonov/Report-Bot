from aiogram import Router, types, Bot, F
from aiogram.filters import CommandStart

from config import MAIN_CHAT_ID, BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
router = Router()


@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer("Salom! bot ishga tushdi.")


@router.message(F.text)
async def handle_bot_message(message: types.Message):
    print(message)

    if message.chat.type in {"group", "supergroup"}:
        group_name = message.chat.title
        chat_info = await bot.get_chat(message.chat.id)
        group_link = (
            chat_info.invite_link if chat_info.invite_link
            else f"https://t.me/{chat_info.username}" if chat_info.username
            else "#"
        )
        chat_type = "Guruh"
    elif message.chat.type == "channel":
        group_name = message.chat.title
        chat_info = await bot.get_chat(message.chat.id)
        group_link = (
            chat_info.invite_link if chat_info.invite_link
            else f"https://t.me/{chat_info.username}" if chat_info.username
            else "#"
        )
        chat_type = "Kanal"
        print(f"Kanal ID: {message.chat.id}")
    else:
        group_name = "Shaxsiy Chat"
        group_link = "#"
        chat_type = "Shaxsiy Chat"

    pass_message = (
        f"**Manba**: {chat_type}\n"
        f"**Nomi**: [{group_name}]({group_link})\n"
        f"**Xabar**: {message.text}\n"
    )

    await bot.send_message(MAIN_CHAT_ID, pass_message, parse_mode="Markdown", disable_web_page_preview=True)
