
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder 


Menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🕕 Taqvim', callback_data='ramazon'), InlineKeyboardButton(text='☪️ Iymon', callback_data='new')],
        [InlineKeyboardButton(text="📖 Ma'lumotnoma", callback_data='kitob'),InlineKeyboardButton(text='📖 Sura va hadis', callback_data='malumot') ],
        [InlineKeyboardButton(text="Qibla 🕋", web_app=WebAppInfo(url="https://qiblafinder.withgoogle.com/intl/ru/desktop"))]
    ]
)

kitobim = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Safarda o'qiladigan duo")],
        [KeyboardButton(text="Jahldor bo'lsangiz"), KeyboardButton(text="Iymon zaiflashsa")],
        [KeyboardButton(text="Baxtsiz bo'lsangiz"), KeyboardButton(text="Gunox qilgan bo'lsangiz")],
        [KeyboardButton(text="Tashvishda bo'lsangiz"), KeyboardButton(text="🚞 ASOSIY MENYU")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
7


my_list = ["Toshkent", "Andijon", "Buxoro", "Guliston", "Samarqand", "Namangan", "Navoiy", "Jizzax", "Nukus", "Qarshi", "Qo'qon", "Xiva", "Marg'ilon"]

viloyat = InlineKeyboardBuilder()
for i in my_list:
    viloyat.add(InlineKeyboardButton(text=i,callback_data=i))
viloyat.add(InlineKeyboardButton(text='Ortga', callback_data='Ortga'))
viloyat.adjust(3)



suralar = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Fotixa surasi"), KeyboardButton(text="Qunut duosi")],
        [KeyboardButton(text="Kavsar surasi"), KeyboardButton(text="🤲 DUO")],
        [KeyboardButton(text="Azon duosi"), KeyboardButton(text='🚞 ASOSIY MENYU')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


