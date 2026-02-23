from aiogram.exceptions import TelegramAPIError, TelegramBadRequest, TelegramNetworkError
from handlers import user_commands, bot_messages
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import logging, sys, os
import asyncio


load_dotenv()


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')


async def main():
	
	bot = Bot(token=os.getenv("BOT_TOKEN"))
	dp = Dispatcher()
	dp.include_routers(
            user_commands.router,
            bot_messages.router
        )

	await bot.delete_webhook(drop_pending_updates=True)
	await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except TelegramNetworkError as error_network:
        logging.error(f'Ошибка в подключении: {error_network}.')
    except TelegramAPIError as error_api_connect:
        logging.error(f'Ошибка в подключении API: {error_api_connect}.')
    except TelegramBadRequest as error_bad_request:
        logging.error(f'Некорректный запрос на сервер TG: {error_bad_request}.')
    except KeyboardInterrupt:
        logging.error(f'Прекращена работа программы сочетанием клавиш Cntrl + C.')
