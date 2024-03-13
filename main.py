
"""Admin @pragrammer_uz 
SANA: 11.03.2024 """

import logging
from aiogram import  Bot, types, Dispatcher
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram import Dispatcher, Bot, F, types
from aiogram.types import Message, CallbackQuery,InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.filters.command import Command
from tokken import TOKKEN, malumot1
from buttons import Menu,viloyat,kitobim,suralar
from kochirma import asos6, asos2, asos3, asos4, asos5, asos7 , dok, suralar1,suralar2,suralar3,suralar4,suralar5
from stes import Form
from aiogram.fsm.context import FSMContext
from read_bot import reading12
from read_botmalu import oqish
from insertmal import add_cmd
from insert import get_post
from tokken import TOKKEN
import asyncio
from aiogram.filters.command import Command

"""Admin ID"""
admin =  6678521239

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKKEN, parse_mode='HTML')

db = Dispatcher()


"""Satart buyurgini bosish bilan start bosgan insonninni id, ismi, familyasini va usernameni oladi va bazaga qoshadi"""

@db.message(Command('start'))
async def go_start(message: Message, state:FSMContext):
    bot_id = message.from_user.id
    frist_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    odi = message.from_user.first_name
    get_post(bot_id, frist_name, last_name, username)
    await message.answer_photo(photo="https://static.vecteezy.com/system/resources/previews/000/952/788/original/welcome-ramadan-kareem-vector.jpg", caption=f"Assalomu alaykum va rohmatullohi va barokatuh!\n<b>{odi} Botga xush kelipsiz😇</b>\n\n<b>Eslatma!</b>\nBotdagi hamma ma'lumotlar <b>islom.uz</b> saytidan olingan!\n\nBot yuzasidan yordam kerak bo'lsa <b>/help</b>", reply_markup=Menu)
    await state.set_state(Form.start)



@db.message(F.text == '/help')
async def yordam(message: types.Message):
    await message.answer_photo(photo = "https://cdn.create.vista.com/api/media/small/39257415/stock-vector-businessman-avatar-profile-picture",caption=f"Yordam va Xato kamchilikar uchun\nAdmin: @pragrammer_uz")
  

"""Allusers orqali botda qancha odam bor ekanligini aniqlab olishingiz mumkin faqat /allusers deb botga yuborishingiz kerak!"""

@db.message(Command('allusers'))
async def get_send(message: types.Message):
    await message.reply(f"Botdagi obunachilar soni: \n{len(reading12())}")





@db.callback_query(F.data =='ramazon', Form.start)
async def ramazon(callback: CallbackQuery,state:FSMContext):
     await callback.message.delete()
     await callback.message.answer_photo(photo="https://i1.wp.com/tj.habarho.com/wp-content/uploads/2020/04/mo-i-sharifi-ramazon-muborak.jpg?fit=1600%2C1031&ssl=1", caption="O'zingiz yashayotgan mintaqangizni tanlang🤗", reply_markup=viloyat.as_markup())
     await state.set_state(Form.viloyatlar)



@db.callback_query(Form.viloyatlar, F.data == 'Ortga')
async def get_meny(call: CallbackQuery, state: FSMContext):
        await call.message.delete()
        await call.message.answer_photo(photo = "https://i1.wp.com/tj.habarho.com/wp-content/uploads/2020/04/mo-i-sharifi-ramazon-muborak.jpg?fit=1600%2C1031&ssl=1", caption=f"Asosiy menyuga xush kelibsiz\nKerakli bo'limni tanlashingiz mumkin!", reply_markup=Menu)
        await state.set_state(Form.start)



@db.callback_query(Form.viloyatlar, F.data)
async def send_info(call: CallbackQuery):
        text = call.data
        await call.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=ec9688247f8c828b7d9d6e5241ee6052_sr-4450484-images-thumbs&n=13", caption=f"{malumot1(text)}")
        


@db.callback_query(F.data=='asosiy', Form.start)
async def asosy_menyu(callback: CallbackQuery):
    await callback.answer(cache_time=8)
    await callback.message.delete()
    await callback.message.answer_photo(photo = "https://i.ytimg.com/vi/tqe0A1A0xa8/maxresdefault.jpg",caption=f"Asosiy menyuga xush kelibsiz\nKerakli bo'limni tanlashingiz mumkin!", reply_markup=Menu)



@db.callback_query(F.data =='kitob', Form.start)
async def kitob(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer_photo(photo="https://bronk.club/uploads/posts/2023-02/1676943419_bronk-club-p-otkritki-s-ramazanom-krasivo-60.jpg", caption=f"O'zingizni tashvishga solgan savolga javob olishingizga ishonamiz 🤲",reply_markup=kitobim)
    await state.set_state(Form.kitob)



@db.callback_query(Form.start,F.data=='new')
async def read_cmdm(call:CallbackQuery,state:FSMContext):
    await call.message.delete()
    name_cars = InlineKeyboardBuilder()
    for i in oqish():
        name_cars.add(InlineKeyboardButton(text=i[0],callback_data=i[0]))
    name_cars.add(InlineKeyboardButton(text='Ortga',callback_data='Ortga'))
    name_cars.adjust(4)
    await call.message.answer_photo(photo="https://yt3.googleusercontent.com/mRakxC38uR936_DTml_dXOjeBVwxsN5Qb4qra9u9FUQlAojVTJf4fw6Fm6uMpKQ19RzdAwYP=s900-c-k-c0x00ffffff-no-rj" , caption="Kerakli bo'limni tanlashingiz mumkin.\n\nEslatma!\nXamma ma'lumotlar islom.uz sahifasidan olingan! ", reply_markup=name_cars.as_markup())
    await state.set_state(Form.start1)


@db.callback_query(Form.start1,F.data=='Ortga')
async def nazad(call:CallbackQuery,state:FSMContext):
    await call.message.answer(f"Bosh sahifaga xush kelipsiz\n\nYana o'zingizga kerakli bo'lgan bo'limni tanlashingiz mumkin!\n/help",reply_markup=Menu)
    await state.set_state(Form.start)



@db.callback_query(Form.start1,F.data)
async def send(call:CallbackQuery):
    text=call.data
    for i in oqish():
        if text ==i[0]:
            await call.message.answer(f'{i[0]}\n{i[1]}\n\n\n<b>Malumotlar  islom.uz saytidan olindi!</b>')




@db.message(F.text == '🚞 ASOSIY MENYU')
async def get_menyu(message: Message, state: FSMContext):
    await message.answer_photo(photo = "https://i1.wp.com/tj.habarho.com/wp-content/uploads/2020/04/mo-i-sharifi-ramazon-muborak.jpg?fit=1600%2C1031&ssl=1", caption=f"Asosiy menyuga xush kelibsiz", reply_markup=Menu)
    await state.set_state(Form.start)



@db.callback_query(F.data =='malumot', Form.start)
async def namoz_vaqt(call: CallbackQuery, state:FSMContext):
    await call.answer(cache_time=10)
    await call.message.delete()
    await call.message.answer(" 🤲 SURALAR", reply_markup=suralar)
    await state.set_state(Form.malumotlarrr)



@db.message(Form.kitob, F.text == "Gunox qilgan bo'lsangiz")
async def mat(message: Message):
    G = asos6
    await message.answer_photo(photo="https://ramadany.org/wp-content/uploads/2020/03/Ramadan-Slide.jpg",caption=f"{G}")


@db.message(Form.kitob, F.text == "Jahldor bo'lsangiz")
async def mativ(message: Message):
    G = asos7
    await message.answer_photo(photo="https://ramadany.org/wp-content/uploads/2020/03/Ramadan-Slide.jpg",caption=f"{G}")

@db.message(Form.kitob, F.text == "Baxtsiz bo'lsangiz")
async def mativa(message: Message):
    G = asos4
    await message.answer_photo(photo="https://ramadany.org/wp-content/uploads/2020/03/Ramadan-Slide.jpg",caption=f"{G}")

@db.message(Form.kitob, F.text == "Tashvishda bo'lsangiz")
async def mativat(message: Message):
    G = asos5
    await message.answer_photo(photo="https://ramadany.org/wp-content/uploads/2020/03/Ramadan-Slide.jpg",caption=f"{G}")

@db.message(Form.kitob, F.text == "Iymon zaiflashsa")
async def mativats(message: Message):
    G = asos3
    await message.answer_photo(photo="https://ramadany.org/wp-content/uploads/2020/03/Ramadan-Slide.jpg",caption=f"{G}")

@db.message(Form.kitob, F.text == "Safarda o'qiladigan duo")
async def mativatsiya(message: Message):
    G = asos2
    await message.answer_photo(photo="https://ramadany.org/wp-content/uploads/2020/03/Ramadan-Slide.jpg",caption=f"{G}")



@db.message(Form.malumotlarrr ,F.text == "🤲 duolar")
async def duolar(message: Message):
    await message.answer(f"{dok}")

@db.message(Form.malumotlarrr ,F.text == "Fotixa surasi")
async def fotixa(message: Message):
    mad = suralar1
    await message.answer(f"{mad}")


@db.message(Form.malumotlarrr , F.text == "Qunut duosi")
async def qunt(message: Message):
    mad = suralar2
    await message.answer(f"{mad}")

@db.message(Form.malumotlarrr ,F.text == "Kavsar surasi")
async def kavsar(message: Message):
    mad = suralar3
    await message.answer(f"{mad}")

@db.message(Form.malumotlarrr , F.text == "🤲 DUO")
async def duo(message: Message):
    mad = suralar4
    await message.answer(f"{mad}")

@db.message(Form.malumotlarrr , F.text == "Azon duosi")
async def Azon(message:  Message):
    mad = suralar5
    await message.answer(f"{mad}")


"""Exo bot yani siz botga nima yuborsangiz xam bot sizga shu xabarni yana yuboradi"""
@db.message()
async def echo_handler(message: types.Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")



async def main():
    await db.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot ish faolyatini tugatdi!")
