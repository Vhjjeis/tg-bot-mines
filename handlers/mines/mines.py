from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from loader import dp
from .funcs import *
from .states import *
from .texts import *
from keyboards import *
from config import QUANTITY_MINES, QUANTITY_CELLS




@dp.message_handler(commands='mines')
async def start_mines_handler(message: types.Message):
    field = func_get_new_field(QUANTITY_CELLS, QUANTITY_MINES)
    await OrderMines.game.set()
    state = Dispatcher.get_current().current_state()
    await state.update_data(field=field)
    await message.answer('game', reply_markup=get_keyboard_game(field))


@dp.callback_query_handler(state=OrderMines.game)
async def game_handler(call: types.CallbackQuery, state: FSMContext):
    value = call.data
    data = await state.get_data()
    field = data['field']
    score = sum([row.count("c") for row in field])
    if value == 'c':
        # clear cell
        await call.answer(TEXT_OLD_CELL)
    elif value == 'm':
        # loss game
        await state.finish()
        await call.message.edit_text(TEXT_LOSS_GAME.format(score=score), reply_markup=get_keyboard_close_game(field))
    elif value == 'close':
        # close game
        await state.finish()
        await call.message.edit_text(TEXT_CLOSE_GAME.format(score=score))
    elif value == 'not':
        # old cell
        await call.answer()
    else:
        field[int(value) // QUANTITY_CELLS][int(value) % QUANTITY_CELLS] = 'c'
        score += 1
        # win
        if score == QUANTITY_CELLS * QUANTITY_CELLS - QUANTITY_MINES:
            await state.finish()
            await call.message.edit_text(TEXT_WIN_GAME.format(score=score), reply_markup=get_keyboard_close_game(field))
        # game
        else:
            await state.update_data(field=field)
            await call.message.edit_text(TEXT_GAME.format(score=score), reply_markup=get_keyboard_game(field))


@dp.message_handler()
async def default_handler(message: types.Message):
    await message.answer(TEXT_START)
