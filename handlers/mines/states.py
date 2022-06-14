from aiogram.dispatcher.filters.state import State, StatesGroup


class OrderMines(StatesGroup):
    game = State()