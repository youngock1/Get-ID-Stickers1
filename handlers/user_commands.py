from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram import Router
import inline
import time


router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
	user_id = message.from_user.id
	user_name = message.from_user.first_name
	await message.reply(f'<b>Добро пожаловать, {user_name}!</b>\n\n' 
						'Это бот <b>"Get ID Sickers, Photo and GIF"</b>\n'
					    'Здесь ты можешь получить ID любого стикера, GIF, Emoji или фото просто отправив его в чат с ботом.',
					    parse_mode='html')


@router.message(Command("help"))
async def help_command(message: Message):
	await message.answer('Не понимаешь, в чем суть? Сейчас расскажу!\n' 
						 'Отправляй в чат бота <b>Sticker, GIF, Photo and Emoji</b> и бот покажет их ID идентификатор.\n'
						 'И вуа-ля! <b>Забирай свой ID ✅</b>\n\n',
						 parse_mode='html')


@router.message(Command('community'))
async def our_com(message: Message):
	await message.answer('<b>Мы и наши соцсети</b> 👇', 
						 parse_mode='html',
						 reply_markup=inline.links_kb)


@router.message(Command("sticker"))
async def sticker_command(message: Message):
	sticker = message.text.split()[-1]
	if sticker != '/sticker':
		try:
			await message.answer_sticker(sticker)
		except:
			await message.answer("Некорректный sticker file_id")		
	else:
		await message.answer("Вы не передали стикер в качестве аргумента команды.")


@router.message(Command("photo"))
async def photo_command(message: Message):
	photo = message.text.split()[-1]
	if photo != '/photo':
		try:
			await message.answer_photo(photo)
		except:
			await message.answer("Некорректный photo file_id")
	else:
		await message.answer("Вы не передали фото в качестве аргумента команды.")


@router.message(Command('gif'))
async def gif_command(message: Message):
	gif = message.text.split()[-1]
	if gif != '/gif':
		try:
			await message.answer_animation(gif)
		except:
			await message.answer('Некорректный gif file_id')
	else:
		await message.answer("Вы не передали gif в качестве аргумента команды.")
