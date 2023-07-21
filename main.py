from config import *
from aiogram import types , Bot, Dispatcher , executor
from aiogram.types import InputFile

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
    await bot.send_message(chat_id=OWNER_ID,text='Бот запущен <3')


main_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
proects_kb = types.KeyboardButton('📄Проекты📄')
b_games = types.KeyboardButton('🎮Игры🎮')
b_serials = types.KeyboardButton('🎦фильмы🎦')
b_streams = types.KeyboardButton('💬Cтримы💬')
main_keyboard.add(proects_kb).row(b_games,b_streams).add(b_serials)


games_kb = types.InlineKeyboardMarkup()
b_g1 = types.InlineKeyboardButton('Маинкруфт', url='https://tlauncher.org/')
b_g2 = types.InlineKeyboardButton('CSgo2', url='https://store.steampowered.com/app/730/CounterStrike_Global_Offensive/')
b_g3 = types.InlineKeyboardButton('GTA6', url='https://store.steampowered.com/app/271590/Grand_Theft_Auto_V/')
b_g4 = types.InlineKeyboardButton('PAYDAY3', url='https://store.steampowered.com/app/218620/PAYDAY_2/')
games_kb.add(b_g1).add(b_g2).add(b_g3).add(b_g4)

proects_kb = types.InlineKeyboardMarkup()
m_g1 = types.InlineKeyboardButton('shooter', callback_data='shooter')
m_g2 = types.InlineKeyboardButton('treasure_hants', callback_data='treasure_hants')
m_g3 = types.InlineKeyboardButton('ping-pong', callback_data='ping-pong')
proects_kb.add(m_g1).add(m_g2).add(m_g3)


films_kb = types.InlineKeyboardMarkup()
f_g1 = types.InlineKeyboardButton('Хорроры', callback_data='hor')
f_g2 = types.InlineKeyboardButton('Смешнявки', callback_data='smes')
films_kb.add(f_g1).add(f_g2)

horrors_kb = types.InlineKeyboardMarkup()
h_g1 = types.InlineKeyboardButton('Все части ОНО', url='https://www.kinopoisk.ru/film/453397/?utm_referrer=www.google.com')
h_g2 = types.InlineKeyboardButton('Все части крика', url='https://kinobar.vip/24704-krik.html')
h_g3 = types.InlineKeyboardButton('Все части Астрал', url='https://www.kinopoisk.ru/film/4850225/')
h_g4 = types.InlineKeyboardButton('Лунтик', url='https://www.youtube.com/watch?v=1Rqg8zmKAEU&ab_channel=%D0%9B%D1%83%D0%BD%D1%82%D0%B8%D0%BA')
horrors_kb.add(h_g1).add(h_g2).add(h_g3).add(h_g4)

smesnauvka_kb = types.InlineKeyboardMarkup()
sm_g1 = types.InlineKeyboardButton('Губкабоб', url='https://kinobar.vip/19177-gubka-bob-v-begah-v4.html')
sm_g2 = types.InlineKeyboardButton('Смешарики', url='https://www.kinopoisk.ru/film/570117/')
sm_g3 = types.InlineKeyboardButton('Машаимедведь', url='https://www.kinopoisk.ru/film/5264991/')
sm_g4 = types.InlineKeyboardButton('Барби', url='https://www.kinopoisk.ru/film/478052/')
smesnauvka_kb.add(sm_g1).add(sm_g2).add(sm_g3).add(sm_g4)


streams_kb = types.InlineKeyboardMarkup()
s_g1 = types.InlineKeyboardButton('Братишкин', url ='https://www.twitch.tv/bratishkinoff')
s_g2 = types.InlineKeyboardButton('S1mple', url='https://www.twitch.tv/s1mple')
s_g3 = types.InlineKeyboardButton('Хазяева',url ='https://www.twitch.tv/team/hazyaeva')
s_g4 = types.InlineKeyboardButton('Бустеренко', url='https://www.twitch.tv/buster')
streams_kb.add(s_g1).add(s_g2).add(s_g3).add(s_g4)



@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer('Привет!', reply_markup=main_keyboard)
    await message.answer('Выбери категорию')


@dp.message_handler()
async def main_controller(message: types.Message):
    if message.text == '🎮Игры🎮':
        await message.answer('Выбери игруху   ', reply_markup=games_kb)
    elif message.text == '📄Проекты📄':
        await message.answer('Cписок игр:', reply_markup=proects_kb)     
    elif message.text == '💬Cтримы💬':
        await message.answer('Выбери стримера: ', reply_markup=streams_kb)   
    elif message.text == '🎦фильмы🎦':
        await message.answer('Категория фильма:', reply_markup=films_kb)

@dp.callback_query_handler()
async def controller_callback(callback_query: types.CallbackQuery):
    if callback_query.data == 'shooter':
        game = InputFile('shooter_game-main.zip')
        await bot.send_document(chat_id=callback_query.from_user.id, document=game)

    elif callback_query.data == 'treasure_hants':
        game2 = InputFile('treasure_hunt-main.zip')
        await bot.send_document(chat_id=callback_query.from_user.id, document=game2)

    elif callback_query.data == 'ping-pong':
        game3 = InputFile('ping-pong-main.zip')
        await bot.send_document(chat_id=callback_query.from_user.id, document=game3)
    
    elif callback_query.data =='hor':
        await bot.send_message(chat_id=callback_query.from_user.id, text='hoorororos', reply_markup=horrors_kb)
    
    elif callback_query.data =='smes':
        await bot.send_message(chat_id=callback_query.from_user.id, text='smesnauvka', reply_markup=smesnauvka_kb)


    


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
