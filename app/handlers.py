#region /


from aiogram import F, Router, types
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, Filter
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import sqlite3
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton,   InlineKeyboardMarkup)
from app.text import * 
from app.defs import * 


import app.keyboards as kb

# роутер, для замены dp
router = Router()


conn = sqlite3.connect('users.db')
cursor = conn.cursor()
#endregion


#MAIN MENU 

@router.message(CommandStart())
async def cmd_start(message: Message):
    user_id = message.from_user.id
    if polychenie_slovo_napr(user_id) is None or polychenie_slovo_napr(user_id) == 'nety':
        await message.answer(TEXTMain["main"], reply_markup=kb.mainmenubeznapr)
        zapolnenie_for_test(user_id)
        vidacha_dannih_first(user_id)
    else:
        direction=polychenie_slovo_napr(user_id)
        zapolnenie_for_test(user_id)
        await message.answer(TEXTMain["mainwith"].format(direction=direction), reply_markup=kb.mainmenusnapr)


@router.callback_query(F.data=='main')
async def tsh(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    if polychenie_slovo_napr(user_id) is None or polychenie_slovo_napr(user_id) == 'nety':
        await callback.message.edit_text(TEXTMain["main"], reply_markup=kb.mainmenubeznapr)
        zapolnenie_for_test(user_id)
        vidacha_dannih_first(user_id)
    else:
        direction=polychenie_slovo_napr(user_id)
        zapolnenie_for_test(user_id)
        await callback.message.edit_text(TEXTMain["mainwith"].format(direction=direction), reply_markup=kb.mainmenusnapr)









@router.callback_query(F.data=='znayu')
async def tsh(callback: types.CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(TEXTvibor["znayu"],reply_markup=kb.vibor_first_napr)



@router.callback_query(F.data=='fizmat_first_vibor')
async def tsh(callback: types.CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(TEXTvibor["fizmat"],reply_markup=kb.FizMat_first_obzor)



@router.callback_query(F.data=='gym_first_vibor')
async def tsh(callback: types.CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(TEXTvibor["gym"],reply_markup=kb.Gym_first_obzor)



@router.callback_query(F.data=='himbio_first_vibor')
async def tsh(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    await callback.answer('')
    await callback.message.edit_text(TEXTvibor["himbio"],reply_markup=kb.HimBio_first_obzor)




@router.callback_query(lambda c: c.data.startswith("DATA:"))
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    unique = callback.data.split(":")[1]
    opisanie = help_obzor(user_id,unique)
    await callback.answer('')
    await callback.message.edit_text(f'{opisanie[0]}',reply_markup=kb.itog_vibor)

    
@router.callback_query(F.data=='StartTest')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    clear_test(user_id)
    await callback.answer('')
    await callback.message.edit_text(Texttest['starttest'],reply_markup=kb.stest)

@router.callback_query(F.data=='starttest')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    await callback.answer('')
    await callback.message.edit_text(Texttest['vop1'],reply_markup=kb.vop['vop1'])



@router.callback_query(lambda c: c.data.startswith("VOP:"))
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    unique = callback.data.split(":")[1]
    print(unique)
    if len(help_test(user_id,unique)) == 3:
        text, result1, result2 = help_test(user_id,unique)  
        konec = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=f'Выбрать {result1}', callback_data='s:main')],
            [InlineKeyboardButton(text=f'Выбрать {result2}', callback_data='s:2main')],
            [InlineKeyboardButton(text='Вернутся обратно', callback_data='main')]
    ])
        await callback.answer('')
        await callback.message.edit_text(Texttest[f'{text}'].format(result1=result1,result2=result2),reply_markup=konec)
    
    else:
        text = help_test(user_id,unique)
        await callback.answer('')
        await callback.message.edit_text(Texttest[f'{text}'],reply_markup=kb.vop[f'{text}'])



@router.callback_query(lambda c: c.data.startswith("s:"))
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    unique = callback.data.split(":")[1]
    if unique == 'main':
        result1, result2 = help_sort_test(user_id)
        print(result1)
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO users (user_id, napravlenie) VALUES (? , ?)", (user_id, result1))
        conn.commit()
    elif unique == '2main':
        result1, result2 = help_sort_test(user_id)
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO users (user_id, napravlenie) VALUES (? , ?)", (user_id, result2))
        conn.commit()
    direction = polychenie_slovo_napr(user_id)
    await callback.answer('')
    await callback.message.edit_text(TEXTMain["mainwith"].format(direction=direction), reply_markup=kb.mainmenusnapr)


@router.callback_query(F.data=='Podrobnee')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('SELECT napravlenie FROM users WHERE user_id = ?',(user_id,))
    nap1 = cursor.fetchone()
    nap=nap1[0]
    cursor.execute('SELECT Descript FROM directions WHERE code = ?',(nap,))
    napr1 = cursor.fetchone()
    napr=napr1[0]
    cursor.execute('SELECT Vyzteg FROM directions WHERE code = ?',(nap,))
    vyz_help = cursor.fetchone()
    vyz=vyz_help[0]
    cursor.execute('UPDATE vyzf SET gorin1 = NULL WHERE user_id = ?',(user_id,) )
    cursor.execute('UPDATE vyzf SET gorin2 = NULL WHERE user_id = ?',(user_id,) )
    cursor.execute('UPDATE vyzf SET gorin3 = NULL WHERE user_id = ?',(user_id,) )
    cursor.execute('INSERT OR IGNORE INTO vyzf(user_id) VALUES (?)',(user_id,))
    conn.commit()
    podrob = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вузы по направлению🏫', callback_data=f'VYZ:{vyz}')],
    [InlineKeyboardButton(text='Бесплатные курсы📚', url = 'https://dopobr.petersburgedu.ru')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{napr}\n',reply_markup=podrob)




@router.callback_query(F.data=='obzor_vyzov')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE vyzf SET gorin1 = NULL WHERE user_id = ?',(user_id,) )
    cursor.execute('UPDATE vyzf SET gorin2 = NULL WHERE user_id = ?',(user_id,) )
    cursor.execute('UPDATE vyzf SET gorin3 = NULL WHERE user_id = ?',(user_id,) )
    cursor.execute('INSERT OR IGNORE INTO vyzf(user_id) VALUES (?)',(user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text(TEXTobzor_vyzov['obzor_vstyplenie1'],reply_markup=kb.obzor_vyzov)



@router.callback_query(F.data=='fizmat_obzor_vyzov')
async def tsh(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(TEXTobzor_vyzov['obzor_vstyplenie2'],reply_markup=kb.fizmat_obzor_vyzov)

@router.callback_query(F.data=='gym_obzor_vyzov')
async def tsh(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(TEXTobzor_vyzov['obzor_vstyplenie2'],reply_markup=kb.gym_obzor_vyzov)

@router.callback_query(F.data=='himbio_obzor_vyzov')
async def tsh(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(TEXTobzor_vyzov['obzor_vstyplenie2'],reply_markup=kb.himbio_obzor_vyzov)



@router.callback_query(lambda c: c.data.startswith("VYZ:"))
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    unique = callback.data.split(":")[1]
    cursor.execute('SELECT napravlenie FROM users WHERE user_id = ?',(user_id,))
    napravlenie = cursor.fetchone()
    cursor.execute('INSERT OR REPLACE INTO users(user_id, napravlenie, vyzn) VALUES (?, ?, ?)',(user_id, napravlenie[0],f"{unique}",))
    conn.commit()
    cursor.execute('SELECT gorin1, gorin2, gorin3 FROM vyzf WHERE user_id = ?',(user_id,))
    vyzi = cursor.fetchone()
    
    cursor.execute(f'SELECT sokrash, vyz_sokr FROM vyz WHERE napravlenie = "{unique}" AND (gorodind = ? OR gorodind = ? OR gorodind = ?)', 
               (vyzi[0], vyzi[1], vyzi[2]))
    result = cursor.fetchall()
    unres = []
    if result == unres:
        cursor.execute(f'SELECT sokrash, vyz_sokr FROM vyz WHERE napravlenie = "{unique}"')
        result = cursor.fetchall()
    buttons = []
    
    for gg in result:
        buttons.append([InlineKeyboardButton(text=gg[0], callback_data=f'SOKRVYZ:{gg[1]}')])
    buttons.append([InlineKeyboardButton(text='Настройки поиска⚙️', callback_data='opt')])
    buttons.append([InlineKeyboardButton(text='Назад📌', callback_data='main')])
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    cursor.execute('SELECT name FROM directions WHERE code = ?',(napravlenie[0],))
    direction = cursor.fetchone()
    await callback.answer('')
    await callback.message.edit_text(TEXTobzor_vyzov['invyztext'].format(direction=direction[0]),reply_markup=keyboard)




@router.callback_query(lambda c: c.data.startswith("SOKRVYZ:"))
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    unique = callback.data.split(":")[1]
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = ?',(unique,))
    sokrdannie = cursor.fetchall()
    cursor.execute('SELECT napravlenie FROM vyz WHERE vyz_sokr = ?',(unique,))
    napravlenie = cursor.fetchone() 
    print(napravlenie[0])
    KeyBoard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{sokrdannie[0][1]}')],
    [InlineKeyboardButton(text='Что такое "Проходной бал"?', callback_data='prohodnoy')],
    [InlineKeyboardButton(text='Назад📌', callback_data=f'VYZ:{napravlenie[0]}')]
])
    cursor.execute('INSERT OR REPLACE INTO lastcon(user_id, lastdata) VALUES (?, ?)',(user_id,unique,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text(f'{sokrdannie[0][4]}\nГород - {sokrdannie[0][0]}\nПроходной бал бюджет - {sokrdannie[0][2]}\nПроходной бал платное - {sokrdannie[0][3]}',reply_markup=KeyBoard)



@router.callback_query(F.data=='prohodnoy')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('SELECT lastdata FROM lastcon WHERE user_id = ?',(user_id,))
    result = cursor.fetchone()
    KeyBoard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад📌', callback_data=f'SOKRVYZ:{result[0]}')]
])
    await callback.answer('')
    await callback.message.edit_text(TEXTobzor_vyzov['prohodnoy'],reply_markup=KeyBoard)



@router.callback_query(F.data=='opt')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id

    cursor.execute('SELECT vyzn FROM users WHERE user_id = ?',(user_id,))
    result = cursor.fetchone()
    opt2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Поиск по городу🏢', callback_data= 'optcity')],
    [InlineKeyboardButton(text='Назад📌', callback_data=f'VYZ:{result[0]}')],
])
    await callback.answer('')
    await callback.message.edit_text('Настройки поиска:',reply_markup=opt2)




@router.callback_query(F.data == 'optcity')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    

    cursor.execute('SELECT vyzn FROM users WHERE user_id = ?',(user_id,))
    result = cursor.fetchone()
   
    cursor.execute(f'SELECT DISTINCT gorod, gorodind FROM vyz WHERE napravlenie = "{result[0]}"')
    res = cursor.fetchall()

    

    buttons1 = []
    
    # Добавляем кнопки для каждой записи в res
    for gg in res:
        cursor.execute('SELECT gorin1, gorin2, gorin3 FROM vyzf WHERE user_id = ?',(user_id,))
        tot = cursor.fetchone()
        
        if tot[0] == gg[1] or tot[1] == gg[1] or tot[2] == gg[1]:
            buttons1.append([InlineKeyboardButton(text=f'{gg[0]}✅', callback_data=f'OPT:{gg[1]}')])
        else:
            buttons1.append([InlineKeyboardButton(text=f'{gg[0]}', callback_data=f'OPT:{gg[1]}')])
    buttons1.append([InlineKeyboardButton(text='Назад📌', callback_data=f'VYZ:{result[0]}')])

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons1)
    await callback.answer('')
    await callback.message.edit_text('Выберите город для поиска',reply_markup=keyboard)



    
@router.callback_query(lambda c: c.data.startswith("OPT:"))
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    unique = callback.data.split(":")[1]
    cursor.execute('SELECT vyzn FROM users WHERE user_id = ?',(user_id,))
    sik = cursor.fetchone()
    
    cursor.execute(f'SELECT DISTINCT gorod, gorodind FROM vyz WHERE napravlenie = "{sik[0]}"')
    res = cursor.fetchall()
    

    cursor.execute('SELECT gorin1, gorin2, gorin3 FROM vyzf WHERE user_id = ?',(user_id,))
    tot = cursor.fetchone()
    if tot[0] == f'{unique}':
        cursor.execute('UPDATE vyzf SET gorin1 = NULL WHERE user_id = ?',(user_id,) )
    elif tot[1] == f'{unique}':
        cursor.execute('UPDATE vyzf SET gorin2 = NULL WHERE user_id = ?',(user_id,) )
    elif tot[2] == f'{unique}':
        cursor.execute('UPDATE vyzf SET gorin3 = NULL WHERE user_id = ?',(user_id,) )
    else:
        if tot[0] is None:
            cursor.execute(f'UPDATE vyzf SET gorin1 = "{unique}" WHERE user_id = ?', (user_id,))
        elif tot[1] is None:
            cursor.execute(f'UPDATE vyzf SET gorin2 = "{unique}" WHERE user_id = ?', (user_id,))
        elif tot[2] is None:
            cursor.execute(f'UPDATE vyzf SET gorin3 = "{unique}" WHERE user_id = ?', (user_id,))


    conn.commit()
    buttons1 = []
    
    # Добавляем кнопки для каждой записи в res
    for gg in res:
        cursor.execute('SELECT gorin1, gorin2, gorin3 FROM vyzf WHERE user_id = ?',(user_id,))
        tot = cursor.fetchone()
        if tot[0] == gg[1] or tot[1] == gg[1] or tot[2] == gg[1]:
            buttons1.append([InlineKeyboardButton(text=f'{gg[0]}✅', callback_data=f'OPT:{gg[1]}')])
        else:
            buttons1.append([InlineKeyboardButton(text=f'{gg[0]}', callback_data=f'OPT:{gg[1]}')])
    buttons1.append([InlineKeyboardButton(text='Назад📌', callback_data=f'VYZ:{sik[0]}')])

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons1)
    await callback.answer('')
    await callback.message.edit_text('Выберите город для поиска',reply_markup=keyboard)




@router.callback_query(F.data=='obzor_napravleniy')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    
    await callback.answer('')
    await callback.message.edit_text(TEXTobzorall['obzor_start'],reply_markup=kb.obzor_napr)



@router.callback_query(F.data=='fizmat_obzor')
async def tsh(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(TEXTobzorall['obzor_vstyplenie1'],reply_markup=kb.FizMat_napr)

@router.callback_query(F.data=='gym_obzor')
async def tsh(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(TEXTobzorall['obzor_vstyplenie2'],reply_markup=kb.HimBio_napr)

@router.callback_query(F.data=='himbio_obzor')
async def tsh(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(TEXTobzorall['obzor_vstyplenie3'],reply_markup=kb.Gym_napr)


@router.callback_query(lambda c: c.data.startswith("OBZOR:"))
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    unique = callback.data.split(":")[1]
    cursor.execute('SELECT Descript, dop, name  FROM directions WHERE Vyzteg = ?', (unique,))
    info = cursor.fetchone()

    obzor_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Бесплатные курсы📚', url = 'https://dopobr.petersburgedu.ru')],
    [InlineKeyboardButton(text=f'Поменять направление на - {info[2]}', callback_data=f'SMENA:{info[2]}')],
    [InlineKeyboardButton(text='Вернутся назад', callback_data=f'{info[1]}_obzor')],
    [InlineKeyboardButton(text='Главная📌', callback_data='main')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{info[0]}',reply_markup=obzor_keyboard)



@router.callback_query(lambda c: c.data.startswith("SMENA:"))
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    unique = callback.data.split(":")[1]
    cursor.execute('SELECT code FROM directions WHERE name = ?',(unique,))
    result = cursor.fetchone()
    cursor.execute("INSERT OR REPLACE INTO users (user_id, napravlenie) VALUES (? , ?)", (user_id, result[0]))
    conn.commit()
    if polychenie_slovo_napr(user_id) is None or polychenie_slovo_napr(user_id) == 'nety':
        await callback.message.edit_text(TEXTMain["main"], reply_markup=kb.mainmenubeznapr)
        zapolnenie_for_test(user_id)
        vidacha_dannih_first(user_id)
    else:
        direction=polychenie_slovo_napr(user_id)
        zapolnenie_for_test(user_id)
        await callback.message.edit_text(TEXTMain["mainwith"].format(direction=direction), reply_markup=kb.mainmenusnapr)




@router.callback_query(F.data=='Dop')
async def tsh(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(TEXTdop['dop_text'],reply_markup=kb.Dop)







