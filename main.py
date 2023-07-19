from config import *
from aiogram import types , Bot, Dispatcher , executor

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
    await bot.send_message(chat_id=OWNER_ID,text='Бот запущен <3')

main_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
b_music = types.KeyboardButton('🎶Музыка🎶')
b_games = types.KeyboardButton('🎮Игры🎮')
b_serials = types.KeyboardButton('🎦Сериалы🎦')
b_streams = types.KeyboardButton('💬Cтримы💬')
main_keyboard.add(b_music).row(b_games,b_streams).add(b_serials)


games_kb = types.InlineKeyboardMarkup()
b_g1 = types.InlineKeyboardButton('Маинкруфт', url='https://tlauncher.org/')
b_g2 = types.InlineKeyboardButton('CSgo2', url='https://store.steampowered.com/app/730/CounterStrike_Global_Offensive/')
b_g3 = types.InlineKeyboardButton('GTA6', url='https://store.steampowered.com/app/271590/Grand_Theft_Auto_V/')
b_g4 = types.InlineKeyboardButton('PAYDAY3', url='https://store.steampowered.com/app/218620/PAYDAY_2/')
games_kb.add(b_g1).add(b_g2).add(b_g3).add(b_g4)

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer('Привет!', reply_markup=main_keyboard)
    await message.answer('Выбери категорию')


@dp.message_handler()
async def main_controller(message: types.Message):
    if message.text == '🎮Игры🎮':
        await message.answer('Выбери игруху         ', reply_markup=games_kb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)