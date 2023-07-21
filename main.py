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

music_kb = types.InlineKeyboardMarkup()
m_g1 = types.InlineKeyboardButton('Фонк')
m_g2 = types.InlineKeyboardButton('Не фонк')
music_kb.add(m_g1).add(m_g2)

phonk_kb= types.InlineKeyboardMarkup()
ph1 = types.InlineKeyboardButton('xxxmanera', url='https://genius.com/artists/Xxxmanera')
ph2 = types.InlineKeyboardButton('Freddie Dredd', url='https://now.morsmusic.org/artist/8154')
phonk_kb(ph1).add(ph2)

dont_phonk_kb = types.InlineKeyboardMarkup()
dph1 = types.InlineKeyboardButton('neznyia', url='https://neznai/artist/')
dph2 = types.InlineKeyboardButton('Krid', url='https://sefon.pro/artist/89-egor-krid/')
dont_phonk_kb(dph1).add(dph2)

films_kb = types.InlineKeyboardMarkup()
f_g1 = types.InlineKeyboardButton('Хорроры')
f_g2 = types.InlineKeyboardButton('Смешнявки')
films_kb.add(f_g1).add(f_g2)

horrors_kb = types.InlineKeyboardMarkup()
h_g1 = types.InlineKeyboardButton('Все части ОНО', url='https://www.kinopoisk.ru/film/453397/?utm_referrer=www.google.com')
h_g2 = types.InlineKeyboardButton('Все части крика', url='https://kinobar.vip/24704-krik.html')
h_g3 = types.InlineKeyboardButton('Все части Астрал', url='https://www.kinopoisk.ru/film/4850225/')
h_g4 = types.InlineKeyboardButton('Лунтик', url='https://www.youtube.com/watch?v=1Rqg8zmKAEU&ab_channel=%D0%9B%D1%83%D0%BD%D1%82%D0%B8%D0%BA')
horrors_kb(h_g1).add(h_g2).add(h_g3).add(h_g4)

smesnauvka_kb = types.InlineKeyboardMarkup()
sm_g1 = types.InlineKeyboardButton('Губкабоб', url='https://kinobar.vip/19177-gubka-bob-v-begah-v4.html')
sm_g2 = types.InlineKeyboardButton('Смешарики', url='https://www.kinopoisk.ru/film/570117/')
sm_g3 = types.InlineKeyboardButton('Машаимедведь', url='https://www.kinopoisk.ru/film/5264991/')
sm_g4 = types.InlineKeyboardButton('Барби', url='https://www.kinopoisk.ru/film/478052/')
smesnauvka_kb(sm_g1).add(sm_g2).add(sm_g3).add(sm_g4)


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
        await message.answer('Выбери игруху         ', reply_markup=games_kb)
    elif message.text == '🎶Музыка🎶':
        await message.answer('Категория музыки', reply_markup=music_kb)     
    elif message.text == '💬Cтримы💬':
        await message.answer('Выбери стримера ', reply_markup=streams_kb)   


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
