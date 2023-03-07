import sqlite3
import time, random
import telebot
from telebot import types
import datetime

from Data.config import *



bot = telebot.TeleBot(":)")

connect = sqlite3.connect('info_players.db', check_same_thread=False)
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS info_users(id BIGINT, nik_name VARCHAR, cash BIGINT)""")
connect.commit()


def init(message, choose):
    id = message.from_user.id
    if choose == 'id':
        return id

    if choose == 'cash':
        cursor.execute(f"SELECT cash FROM info_users WHERE id = {id}")
        cash = cursor.fetchone()[0]
        return cash

    if choose == 'nik':
        cursor.execute(f"SELECT nik_name FROM info_users WHERE id = {id}")
        nik = cursor.fetchone()[0]
        return nik


def check_registration(message):
    id = message.from_user.id

    cursor.execute(f"SELECT id FROM info_users WHERE id = {id}")
    if cursor.fetchone() is None:
        return False

    else:
        print(121232)
        return True


def qty_mess(qty):     #Функция для изменения кол-ва сообщений у пользователя
    itog = qty + 1
    return itog
