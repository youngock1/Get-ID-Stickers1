from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

links_kb = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text='Ivan 👨‍💻', url='https://t.me/Ivan13112'),
            InlineKeyboardButton(text='TG channel 👥', url='https://t.me/IIIvan1311'),
        ],
        [
            InlineKeyboardButton(text='Alexa 👩‍💻', url='https://t.me/Dr_Alexa'),
            InlineKeyboardButton(text='TG channel 👥', url='https://t.me/restggbot')
        ]
    ]
)