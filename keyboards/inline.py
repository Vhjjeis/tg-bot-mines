from aiogram import types


def get_keyboard_game(field):
    keyboard = types.InlineKeyboardMarkup()
    for row in field:
        buttons = tuple()
        for value in row:
            text = '✅' if value == 'c' else '⬜️'
            buttons += (types.InlineKeyboardButton(text=text, callback_data=value), )
        keyboard.add(*buttons)
    keyboard.add(types.InlineKeyboardButton(text='close', callback_data='close'))
    return keyboard


def get_keyboard_close_game(field):
    keyboard = types.InlineKeyboardMarkup()
    for row in field:
        buttons = tuple()
        for value in row:
            text = '✅' if value == 'c' else ('💣' if value == 'm' else '⬜️')
            buttons += (types.InlineKeyboardButton(text=text, callback_data='not'), )
        keyboard.add(*buttons)
    return keyboard