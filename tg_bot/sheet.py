import datetime

import gspread
from aiogram import types

scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

service_acc = gspread.service_account('tg_bot/creds.json', scopes=scope)
#
# # for local use
# service_acc = gspread.service_account('creds.json', scopes=scope)

CONFIG_SHEET_NAME = "CONFIG_MAIN_DEV"
USERS_INFO_SHEET_NAME = "USERS_INFO_DEV"

config_sheet = service_acc.open(CONFIG_SHEET_NAME).get_worksheet(0)
offices = service_acc.open(CONFIG_SHEET_NAME).get_worksheet(1)
info_sheet = service_acc.open(USERS_INFO_SHEET_NAME).get_worksheet(0)


def get_offices():
    """функиця получает все офисы из табличек"""
    return offices.col_values(1)[1:]


def get_whole_config():
    """Берет все значения отфильтровывает и возвращает их как словарь"""
    all_records = config_sheet.get_all_records()
    sorted_records = {}
    for record in all_records:
        values = record["value"].replace(r"\n", "\n") if isinstance(record["value"], str) else record["value"]
        sorted_records[record['key']] = values
    return sorted_records


async def write_user_info(message: types.Message):
    """
    функция получает обьект message и извлекает оттуда информацию о пользователе
    после чего записывает все в табличку
    A = full name
    B = username
    C = id
    D = office
    E = last interaction
    """
    fullname = message.from_user.full_name
    username = message.from_user.username
    user_id = message.from_user.id
    office = message.text

    # получет все ид пользователей
    users = info_sheet.col_values(3)
    row = len(users) + 1
    info_sheet.update(f"A{row}", fullname)
    info_sheet.update(f"B{row}", username)
    info_sheet.update(f"C{row}", user_id)
    info_sheet.update(f"D{row}", office)
    info_sheet.format(f"A{row + 1}:D{row + 1}", {"horizontalAlignment": 'LEFT'})


async def get_users_list():
    return info_sheet.col_values(3)[1:]
