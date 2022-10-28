
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types.reply_keyboard import ReplyKeyboardRemove
from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from telethon import TelegramClient
from telethon.errors import rpcerrorlist
from datetime import date, datetime
import re
import sqlite3

sessions = {}
logging.basicConfig(level=logging.INFO)

API_TOKEN = '1968892175:AAFx6uMy-36K5r01N0Q1PpNljMOGDKWSkQg'
api_id = 988074
api_hash = "a5ec8b7b6dbeedc2514ca7e4ba200c13"
admin = 1806310962

bot = Bot(token=API_TOKEN)

# For example use simple MemoryStorage for Dispatcher.
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

Ssilka = InlineKeyboardMarkup()
Ssilka.add(InlineKeyboardButton('⬅️ Назад', url='https://t.me/3225235'))

proooooo = InlineKeyboardMarkup()
proooooo.add(InlineKeyboardButton('📜 Инструкция', url='https://telegra.ph/Dobavlyaem-proksi-06-28'))
proooooo.add(InlineKeyboardButton('➕ Купить прокси', url='https://www.proxy.house/?r=65634'))

# States
class Form(StatesGroup):
    phone = State()  # Will be represented in storage as 'Form:name'
    proxy = State()  # Will be represented in storage as 'Form:age'
    isGood = State()
    code = State()
    password = State()



@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    state = dp.current_state(user=message.from_user.id)
    if not state is None:
        await state.reset_state()
    # Set state
    await Form.phone.set()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Отмена")
    await message.answer("📱 Введите номер от аккаунта Telegram (Без + и пробелов):", reply_markup=markup)


# You can use state '*' if you need to handle all states
@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='Отмена', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    phone = ""
    async with state.proxy() as data:
        if data.__contains__("phone"):
            phone = data["phone"]
    if phone != "":
        if sessions.__contains__(phone):
            await sessions[phone].disconnect()
    current_state = await state.get_state()
    if current_state is None:
        return
    logging.info('Cancelling state %r', current_state)
    await state.reset_state()
    await message.answer('Отменено. Для создания сессии нажмите /start', reply_markup=types.ReplyKeyboardRemove())

# Check age. Age gotta be digit
@dp.message_handler(lambda message: len(re.findall(r'^[+]?\d+$',message.text))==0, state=Form.phone)
async def process_phone_invalid(message: types.Message):
    return await message.answer("Неправильный формат!")

@dp.message_handler(state=Form.phone)
async def process_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    await Form.next()
    await message.answer('''ℹ️ Введите прокси в формате: login:password@ip:port (SOCKS)''', reply_markup=proooooo)


@dp.message_handler(lambda message: len(message.text.split("@")) != 2 or len(message.text.split(":")) != 3, state=Form.proxy)
async def process_age_invalid(message: types.Message):
    return await message.answer("✖️ Неверный формат!")


@dp.message_handler(lambda message: message.text != None, state=Form.proxy)
async def process_proxy(message: types.Message, state: FSMContext):
    # Update state and data
    await state.update_data(proxy=message.text)
    txt = message.text
    IPpr = txt.split("@")[1].split(":")[0]
    portpr = txt.split("@")[1].split(":")[1]
    loginpr = txt.split("@")[0].split(":")[0]
    paspr = txt.split("@")[0].split(":")[1]
    print(message.chat.id)
    async with state.proxy() as data:
        text = "📱 Номер: <code>{0}</code>\n🌐 Прокси:\n-IP: <code>{1}</code>\n-LOGIN: <code>{2}</code>\n-PASSWORD: <code>{3}</code>\n-PORT: <code>{4}</code>".format(data["phone"], IPpr,loginpr, paspr, portpr)  
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("✔️Все верно, добавить")
    markup.add("Отмена")
    await Form.next()
    await message.answer(text,parse_mode="HTML", reply_markup=markup)


@dp.message_handler(lambda message: message.text not in ["✔️Все верно, добавить", "Отмена"], state=Form.isGood)
async def process_isgood_invalid(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("✔️Все верно, добавить")
    markup.add("Отмена")
    return await message.answer("Воспользуйтесь клавитатурой!",reply_markup=markup)


@dp.message_handler(lambda message: message.text == "✔️Все верно, добавить",state=Form.isGood)
async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['isGood'] = True
        phone = data['phone']
        txt = data['proxy']
    IPpr = txt.split("@")[1].split(":")[0]
    portpr = txt.split("@")[1].split(":")[1]
    loginpr = txt.split("@")[0].split(":")[0]
    paspr = txt.split("@")[0].split(":")[1]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Отмена")
    sessions[phone] = TelegramClient(phone, api_id, api_hash, device_model="Ids bot", system_version="6.12.0", app_version="10 P (28)", proxy=("socks5", str(IPpr), int(portpr), True, str(loginpr), str(paspr)))
    try:
        await sessions[phone].connect()
    except ConnectionError:
        await Form.previous()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        markup.add("Отмена")
        return await message.answer("Прокси невалидны, введите заново!", reply_markup=markup)
    except rpcerrorlist.FloodWaitError:
        current_state = await state.get_state()
        logging.info('Cancelling state %r', current_state)
        await state.reset_state()
        sessions.pop(phone)
        await message.answer('Лимит авторизаций!\n Для создания сессии нажмите /start', reply_markup=types.ReplyKeyboardRemove())

    if not await sessions[phone].is_user_authorized():
        await sessions[phone].sign_in(phone)
        await Form.next()
        await message.answer("💬 Введите полученный код:", reply_markup=markup)
    else:
        current_state = await state.get_state()
        logging.info('Cancelling state %r', current_state)
        await state.reset_state()
        await sessions[phone].disconnect()
        connection = sqlite3.connect('spam_baza.sqlite')
        q = connection.cursor()
        print(message.chat.id)
        colvo_akk = q.execute(f"SELECT COUNT(id) FROM akk where user = '{message.chat.id}'").fetchone()[0]
        print(colvo_akk)
        user_zakaz = q.execute(f"SELECT colvo FROM ugc_users where id = '{message.chat.id}'").fetchone()[0]
        if user_zakaz > colvo_akk:
            q.execute("INSERT INTO akk (id,user,name,proxi) VALUES ('%s','%s','%s','%s')"%(data['phone'],message.chat.id,data['phone'],data['proxy']))
            connection.commit()

        await message.answer('✔️ Аккаунт уже добавлен. Для создания сессии нажмите /start', reply_markup=types.ReplyKeyboardRemove())
        

@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.code)
async def process_isgood_invalid(message: types.Message):
    return await message.answer("✖️ Неверный формат кода, повторите код!")

@dp.message_handler(state=Form.code)
async def process_gender(message: types.Message, state: FSMContext):
    code = message.text
    async with state.proxy() as data:
        data["code"] = code
        phone = data['phone']
    try:
        s = await sessions[phone].sign_in(phone, code)
        current_state = await state.get_state()
        logging.info('Finishing state %r', current_state)
        await state.reset_state()
        await sessions[phone].disconnect()
        connection = sqlite3.connect('spam_baza.sqlite')
        q = connection.cursor()
        print(message.chat.id)
        q.execute("INSERT INTO akk (id,user,name,proxi) VALUES ('%s','%s','%s','%s')"%(data['phone'],message.chat.id,data['phone'],data['proxy']))
        connection.commit()
        await message.answer("✔️ Аккаунт успешно добавлен", reply_markup=Ssilka)

    except rpcerrorlist.SessionPasswordNeededError:
        await message.answer("🔐 Введите пароль!")
        Form.next()
    except rpcerrorlist.PhoneCodeInvalidError:
        return await message.answer("✖️ Неверный код!")
    except rpcerrorlist.PhoneCodeExpiredError:
        await Form.previous()
        return await message.answer("✖️ Код истек или вы используете аккаунт на который приходит подтверждение !")

@dp.message_handler(state=Form.password)
async def process_gender(message: types.Message, state: FSMContext):
    pas = message.text
    async with state.proxy() as data:
        data["password"] = pas
        phone = data['phone']
    try:
        await sessions[phone].sign_in(password=pas)
        connection = sqlite3.connect('spam_baza.sqlite')
        q = connection.cursor()
        q.execute("INSERT INTO akk (id,user,name,proxi) VALUES ('%s','%s','%s','%s')"%(data['phone'],message.chat.id,data['phone'],data['proxy']))
        connection.commit()
        await message.answer("✔️ Аккаунт успешно добавлен", reply_markup=Ssilka)
        state.reset_state()
        await sessions[phone].disconnect()
        sessions.pop(phone)

    except rpcerrorlist.PasswordHashInvalidError:
        return await message.answer("✖️ Неверный пароль!")

async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)