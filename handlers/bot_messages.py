from aiogram.types import Message
from aiogram import Router, F
import inline
import emoji


router = Router()


@router.message(F.sticker)
async def sticker_handler(message: Message):
	await message.answer(f"<b>Получен стикер 📍</b>\n\n"
						f"<b>Для размещения в TG ботах:</b>\n\n"
						f"<b>ID:</b><code>{message.sticker.file_id}</code>\n\n"
						f"<b>Обратная связь:</b> @Ivan13112, @Dr_Alexa",
						parse_mode='html')


@router.message(F.photo)
async def photo_handler(message: Message):
	await message.answer(f"<b>Получено фото 📍</b>\n\n"
						f"<b>Для размещения в TG ботах:</b>\n\n"
						f"<b>ID:</b><code>{message.photo[-1].file_id}</code>\n\n"
						f"<b>Обратная связь:</b> @Ivan13112, @Dr_Alexa",
						parse_mode='html')


@router.message(F.animation)
async def gif_handlers(message: Message):
	await message.answer(f"<b>Получено GIF 📍</b>\n\n"
						f"<b>Для размещения в TG ботах:</b>\n\n"
						f"<b>ID:</b><code>{message.animation.file_id}</code>\n\n"
						f"<b>Обратная связь:</b> @Ivan13112, @Dr_Alexa",
						parse_mode='html')


@router.message(F.text)
async def emoji_handler(message: Message):
	emoji_text = message.text
	if emoji.is_emoji(emoji_text):
		await message.answer(f"<b>Получено Emoji 📍</b>\n\n"
							f"<b>Для размещения в TG ботах:</b>\n\n"
							f"<b>ID:</b> <code>{emoji_text}</code>\n\n"
							f"<b>Обратная связь:</b> @Ivan13112, @Dr_Alexa",
							parse_mode='html')
	else:
		await message.answer(f"Для получения идентификатора stickers/photo/GIF, отправьте их соотвественно в чат с ботом."
						f"<b>Обратная связь:</b> @Ivan13112, @Dr_Alexa",
						parse_mode='html',
						reply_markup=inline.links_kb)

@router.message()
async def anything_handler(message: Message):
	await message.answer(f"Для получения идентификатора stickers/photo/GIF, отправьте их соотвественно в чат с ботом."
						f"<b>Обратная связь:</b> @Ivan13112, @Dr_Alexa",
						parse_mode='html',
						reply_markup=inline.links_kb)
