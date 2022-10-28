import telebot
from telebot import types

main = telebot.types.ReplyKeyboardMarkup(True)
main.row('🎛 Меню')

otmena = telebot.types.ReplyKeyboardMarkup(True)
otmena.row('Отмена')
