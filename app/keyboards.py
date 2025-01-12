from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton,   InlineKeyboardMarkup)

mainmenubeznapr = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Я знаю направление☑️', callback_data='znayu')],
    [InlineKeyboardButton(text='Пройти мини-тест📝', callback_data='StartTest')]
])
mainmenusnapr =  InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Подробнее про направление📍', callback_data='Podrobnee')],
    [InlineKeyboardButton(text='Выбрать вуз🏫', callback_data='obzor_vyzov')],
    [InlineKeyboardButton(text='Обзор всех направлений🔍', callback_data='obzor_napravleniy')],
    [InlineKeyboardButton(text='Дополнительно🖇', callback_data='Dop')]
])








vibor_first_napr = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Физ-мат🧮', callback_data='fizmat_first_vibor')],
    [InlineKeyboardButton(text='Гуманитарные✍', callback_data='gym_first_vibor')],
    [InlineKeyboardButton(text='Хим-био🧪', callback_data='himbio_first_vibor')]
])
FizMat_first_obzor = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Инженер', callback_data='DATA:F1')],
    [InlineKeyboardButton(text='IT-специалист', callback_data='DATA:F2')],
    [InlineKeyboardButton(text='Экономист', callback_data='DATA:F3')],
    [InlineKeyboardButton(text='Финансист', callback_data='DATA:F4')],
    [InlineKeyboardButton(text='Бухгалтер', callback_data='DATA:F5')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Dop')]
])
Gym_first_obzor = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Маркетолог', callback_data='DATA:G1')],
    [InlineKeyboardButton(text='Адвокат', callback_data='DATA:G2')],
    [InlineKeyboardButton(text='Журналист', callback_data='DATA:G3')],
    [InlineKeyboardButton(text='Преподаватель', callback_data='DATA:G4')],
    [InlineKeyboardButton(text='Психолог', callback_data='DATA:G5')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Dop')]
])
HimBio_first_obzor = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Химик', callback_data='DATA:H1')],
    [InlineKeyboardButton(text='Эколог', callback_data='DATA:H2')],
    [InlineKeyboardButton(text='Психотерапевт', callback_data='DATA:H3')],
    [InlineKeyboardButton(text='Аллерголог', callback_data='DATA:H4')],
    [InlineKeyboardButton(text='Ботаник', callback_data='DATA:H5')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Dop')]
])

itog_vibor = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Выбрать', callback_data='main')],
    [InlineKeyboardButton(text='Поменять', callback_data='znayu')],
    [InlineKeyboardButton(text='Пройти мини-тест', callback_data='himbio_first_vibor')]
])

stest = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Пройти!📍', callback_data='starttest')],
    [InlineKeyboardButton(text='Вернутся📌', callback_data='main')]
])

vop={}
for i in range(1,16):
    vop[f'vop{i}'] = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='А', callback_data=f'VOP:{i}a')],
    [InlineKeyboardButton(text='B', callback_data=f'VOP:{i}b')],
    [InlineKeyboardButton(text='C', callback_data=f'VOP:{i}c')]
])






obzor_vyzov = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Физ-мат🧮', callback_data='fizmat_obzor_vyzov')],
    [InlineKeyboardButton(text='Гуманитарные✍', callback_data='gym_obzor_vyzov')],
    [InlineKeyboardButton(text='Хим-био🧪', callback_data='himbio_obzor_vyzov')]
])

fizmat_obzor_vyzov = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Инженер', callback_data='VYZ:inz')],
    [InlineKeyboardButton(text='IT-специалист', callback_data='VYZ:it')],
    [InlineKeyboardButton(text='Экономист', callback_data='VYZ:econ')],
    [InlineKeyboardButton(text='Финансист', callback_data='VYZ:fin')],
    [InlineKeyboardButton(text='Бухгалтер', callback_data='VYZ:inzbuh')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])
gym_obzor_vyzov = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Маркетолог', callback_data='VYZ:mark')],
    [InlineKeyboardButton(text='Адвокат', callback_data='VYZ:adv')],
    [InlineKeyboardButton(text='Журналист', callback_data='VYZ:zhur')],
    [InlineKeyboardButton(text='Преподаватель', callback_data='VYZ:prep')],
    [InlineKeyboardButton(text='Психолог', callback_data='VYZ:psihol')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])
himbio_obzor_vyzov = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Химик', callback_data='VYZ:him')],
    [InlineKeyboardButton(text='Эколог', callback_data='VYZ:ecol')],
    [InlineKeyboardButton(text='Психотерапевт', callback_data='VYZ:psihoter')],
    [InlineKeyboardButton(text='Аллерголог', callback_data='VYZ:all')],
    [InlineKeyboardButton(text='Ботаник', callback_data='VYZ:bot')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])



obzor_napr = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Физ-мат🧮', callback_data='fizmat_obzor')],
    [InlineKeyboardButton(text='Гуманитарные✍', callback_data='gym_obzor')],
    [InlineKeyboardButton(text='Хим-био🧪', callback_data='himbio_obzor')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])

FizMat_napr = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Инженер', callback_data='OBZOR:inz')],
    [InlineKeyboardButton(text='IT-специалист', callback_data='OBZOR:it')],
    [InlineKeyboardButton(text='Экономист', callback_data='OBZOR:econ')],
    [InlineKeyboardButton(text='Финансист', callback_data='OBZOR:fin')],
    [InlineKeyboardButton(text='Бухгалтер', callback_data='OBZOR:buh')],
    [InlineKeyboardButton(text='Назад📌', callback_data='obzor_napravleniy')]
])

HimBio_napr = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Химик', callback_data='OBZOR:him')],
    [InlineKeyboardButton(text='Эколог', callback_data='OBZOR:ecol')],
    [InlineKeyboardButton(text='Психотерапевт', callback_data='OBZOR:psihoter')],
    [InlineKeyboardButton(text='Аллерголог', callback_data='OBZOR:all')],
    [InlineKeyboardButton(text='Ботаник', callback_data='OBZOR:bot')],
    [InlineKeyboardButton(text='Назад📌', callback_data='obzor_napravleniy')]
])

Gym_napr = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Маркетолог', callback_data='OBZOR:mark')],
    [InlineKeyboardButton(text='Адвокат', callback_data='OBZOR:adv')],
    [InlineKeyboardButton(text='Журналист', callback_data='OBZOR:zhur')],
    [InlineKeyboardButton(text='Преподаватель', callback_data='OBZOR:prep')],
    [InlineKeyboardButton(text='Психолог', callback_data='OBZOR:pisihol')],
    [InlineKeyboardButton(text='Назад📌', callback_data='obzor_napravleniy')]
])

Dop = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Выбрать другое направление🔍', callback_data='znayu')],
    [InlineKeyboardButton(text='Пройти тест на направление📝', callback_data='StartTest')],
    [InlineKeyboardButton(text='Бесплатные курсы📚', url = 'https://dopobr.petersburgedu.ru')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])

