TOKKEN = '6399613416:AAEt-HEFC4RIiASnzSJ0KqixIxErp1vJwj8'
# Kanal_id = -1001916805357
# Majburiy azo  uchun kanal id


import requests as rq
import json as js
def malumot1(n):
    url = rq.get(f'https://islomapi.uz/api/present/day?region={n}').json()
    print(f'{url}')
    date = url['date']
    weekday = url['weekday']
    month = url['hijri_date']['month']
    day = url['hijri_date']['day']
    tong = url['times']['tong_saharlik']
    Bomdod = url['times']['quyosh']
    peshin = url['times']['peshin']
    asr = url['times']['asr']
    shom = url['times']['shom_iftor']
    hufton = url['times']['hufton']
    return f"Namoz vaqtlari <b>«{n}»</b> vaqti bo'yicha\n\nSana: <b>{date}</b>\n\nHafta kuni: <b>{weekday}</b>\n\n<b>Hijriy 1145 yil {day}-{month}</b>\n\nBomdod (saharlik): --> <b>{tong}</b>\n\nQuyosh chiqishi: --> <b>{Bomdod}</b>\n\nPeshin:  --> <b>{peshin}</b>\n\nAsr: --> <b>{asr}</b>\n\nShom (iftorlik): --> <b>{shom}</b>\n\nXufton: --> <b>{hufton}</b>"






