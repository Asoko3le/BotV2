from aiogram import F, Router, types
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, Filter
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import sqlite3
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton,   InlineKeyboardMarkup)



def vidacha_dannih_first(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO users(user_id,napravlenie) VALUES (?, ?)",(user_id,'nety',))
    cursor.execute("INSERT OR IGNORE INTO professions_test (user_id) VALUES (?)", (user_id,))
    conn.commit()
    

def polychenie_slovo_napr(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor() 
    cursor.execute('SELECT napravlenie FROM users WHERE user_id = ?',(user_id,))
    result = cursor.fetchone()
    if result:
        napravlenie_code = result[0]  
        cursor.execute('SELECT name FROM directions WHERE code = ?', (napravlenie_code,))
        result = cursor.fetchone() 
        if result:
            return result[0]  
    

def zapolnenie_for_test(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR REPLACE INTO professions_test(user_id, nap, Inz, It, Mark, Him, Econ, Bot, "All", Psihoter, Ecol, Psiholog, Prep, Zhur, Adv, Buh, Fin) VALUES (?, NULL , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)',(user_id,))
    conn.commit()
    
def obzor_napr(fizmat):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM directions WHERE dop = ?',(fizmat,))
    all = cursor.fetchall()
    return all

def ochistka_lastcon(user_id, ls):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()  
    cursor.execute('INSERT OR RAPLACE INTO lastcon(user_id, lastdata) VALUES(?,?)',(user_id,ls,))
    conn.commit()


def help_obzor(user_id,uniq):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()  
    cursor.execute('INSERT OR REPLACE INTO users(user_id, napravlenie) VALUES (?,?)',(user_id,uniq,))
    cursor.execute('SELECT Descript FROM directions WHERE code = ?',(uniq,))
    opisanie = cursor.fetchone()
    conn.commit()
    return opisanie

def help_sort_test(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT user_id, Inz, It, Mark, Him, Econ, Bot, "All", Psihoter, Ecol, Psiholog, Prep, Zhur, Adv, Buh, Fin FROM professions_test WHERE user_id = ?' ,(user_id,))
    rows = cursor.fetchall()
    for row in rows:
        user_id = row[0]
        professions = {
            'F1': row[1],
            'F2': row[2],
            'G1': row[3],
            'H1': row[4],
            'F3': row[5],
            'H5': row[6],
            'H4': row[7],
            'H3': row[8],
            'H2': row[9],
            'G5': row[10],
            'G4': row[11],
            'G3': row[12],
            'G2': row[13],
            'F5': row[14],
            'F4': row[15]
    }
    sorted_professions = sorted(professions.items(), key=lambda x: x[1], reverse=True)
    
    max_nap = sorted_professions[0][0]
    max_nap2 = sorted_professions[1][0]
    return max_nap, max_nap2

def help_test_2(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    max_nap, max_nap2 = help_sort_test(user_id)
    cursor.execute('SELECT name FROM directions WHERE code = ?', (max_nap,))
    re11 = cursor.fetchone()
    result1 = re11[0]
    cursor.execute('SELECT name FROM directions WHERE code = ?', (max_nap2,))
    re22 = cursor.fetchone()
    result2 = re22[0]

    return result1,result2
    

def help_test(user_id,uniq):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()  
    if uniq == '1a':
        cursor.execute('UPDATE professions_test SET Inz = Inz + 1, It = It + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        print('+')
        text = 'vop2'
        return text
    elif uniq == '1b':
        cursor.execute('UPDATE professions_test SET Bot = Bot + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop2'
        return text
    elif uniq == '1c':
        cursor.execute('UPDATE professions_test SET Psihoter  = Psihoter + 1, Psiholog = Psiholog + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop2'
        return text
    elif uniq == '2a':
        cursor.execute('UPDATE professions_test SET Econ = Econ + 1, Fin = Fin + 1, Buh = Buh + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop3'
        return text
    elif uniq == '2b':
        cursor.execute('UPDATE professions_test SET Him = Him + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop3'
        return text
    elif uniq == '2c':
        cursor.execute('UPDATE professions_test SET Psihoter  = Psihoter + 1, Psiholog = Psiholog + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop3'
        return text
    elif uniq == '3a':
        cursor.execute('UPDATE professions_test SET Ecol = Ecol + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop4'
        return text
    elif uniq == '3b':
        cursor.execute('UPDATE professions_test SET Inz = Inz + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop4'
        return text
    elif uniq == '3c':
        cursor.execute('UPDATE professions_test SET Mark = Mark + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop4'
        return text
    elif uniq == '4a':
        cursor.execute('UPDATE professions_test SET Mark = Mark + 1, Fin = Fin + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop5'
        return text
    elif uniq == '4b':
        cursor.execute('UPDATE professions_test SET "All" = "All" + 1, Psiholog = Psiholog + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop5'
        return text
    elif uniq == '4c':
        cursor.execute('UPDATE professions_test SET Buh = Buh + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop5'
        return text
    elif uniq == '5a':
        cursor.execute('UPDATE professions_test SET Bot = Bot + 1, Him = Him + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop6'
        return text
    elif uniq == '5b':
        cursor.execute('UPDATE professions_test SET It = It + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop6'
        return text
    elif uniq == '5c':
        cursor.execute('UPDATE professions_test SET Adv = Adv + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop6'
        return text
    elif uniq == '6a':
        cursor.execute('UPDATE professions_test SET Fin = Fin + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop7'
        return text
    elif uniq == '6b':
        cursor.execute('UPDATE professions_test SET Him = Him + 1, Bot = Bot + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop7'
        return text
    elif uniq == '6c':
        cursor.execute('UPDATE professions_test SET Psihoter  = Psihoter + 1, Psiholog = Psiholog + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop7'
        return text
    elif uniq == '7a':
        cursor.execute('UPDATE professions_test SET Inz = Inz + 1, It = It + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop8'
        return text
    elif uniq == '7b':
        cursor.execute('UPDATE professions_test SET Adv = Adv + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop8'
        return text
    elif uniq == '7c':
        cursor.execute('UPDATE professions_test SET Bot = Bot + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop8'
        return text
    elif uniq == '8a':
        cursor.execute('UPDATE professions_test SET Econ = Econ + 1, Fin = Fin + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop9'
        return text
    elif uniq == '8b':
        cursor.execute('UPDATE professions_test SET Psihoter  = Psihoter + 1, Psiholog = Psiholog + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop9'
        return text
    elif uniq == '8c':
        cursor.execute('UPDATE professions_test SET Adv = Adv + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop9'
        return text
    elif uniq == '9a':
        cursor.execute('UPDATE professions_test SET Him = Him + 1, Bot = Bot + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop10'
        return text
    elif uniq == '9b':
        cursor.execute('UPDATE professions_test SET Inz = Inz + 1, It = It + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop10'
        return text
    elif uniq == '9c':
        cursor.execute('UPDATE professions_test SET Mark = Mark + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop10'
        return text
    elif uniq == '10a':
        cursor.execute('UPDATE professions_test SET Inz = Inz + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop11'
        return text
    elif uniq == '10b':
        cursor.execute('UPDATE professions_test SET Buh = Buh + 1, Fin = Fin + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop11'
        return text
    elif uniq == '10c':
        cursor.execute('UPDATE professions_test SET Psihoter  = Psihoter + 1, Psiholog = Psiholog + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop12'
        return text
    elif uniq == '11a':
        cursor.execute('UPDATE professions_test SET Econ = Econ + 1, Fin = Fin + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop12'
        return text
    elif uniq == '11b':
        cursor.execute('UPDATE professions_test SET Mark = Mark + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop12'
        return text
    elif uniq == '11c':
        cursor.execute('UPDATE professions_test SET Him = Him + 1, Bot = Bot + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop13'
        return text
    elif uniq == '12a':
        cursor.execute('UPDATE professions_test SET Psihoter  = Psihoter + 1, Psiholog = Psiholog + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop13'
        return text
    elif uniq == '12b':
        cursor.execute('UPDATE professions_test SET Him = Him + 1, Bot = Bot + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop13'
        return text
    elif uniq == '12c':
        cursor.execute('UPDATE professions_test SET It = It + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop13'
        return text
    elif uniq == '13a':
        cursor.execute('UPDATE professions_test SET Psihoter  = Psihoter + 1, Psiholog = Psiholog + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop14'
        return text
    elif uniq == '13b':
        cursor.execute('UPDATE professions_test SET Fin = Fin + 1, Econ = Econ + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop14'
        return text
    elif uniq == '13c':
        cursor.execute('UPDATE professions_test SET Adv = Adv + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop14'
        return text
    elif uniq == '14a':
        cursor.execute('UPDATE professions_test SET Inz = Inz + 1, It = It + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop15'
        return text
    elif uniq == '14b':
        cursor.execute('UPDATE professions_test SET Buh = Buh + 1, Fin = Fin + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop15'
        return text
    elif uniq == '14c':
        cursor.execute('UPDATE professions_test SET Ecol = Ecol + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        text = 'vop15'
        return text
    elif uniq == '15a':
        result1, result2 = help_test_2(user_id)
        text = 'konec'
        return text, result1, result2
    elif uniq == '15b':
        result1, result2 = help_test_2(user_id)
        text = 'konec'
        return text, result1, result2
    elif uniq == '15c':
        cursor.execute('UPDATE professions_test SET Adv = Adv + 1 WHERE user_id = ?', (user_id,))
        conn.commit()
        result1, result2 = help_test_2(user_id)
        text = 'konec'
        return text, result1, result2
    
def clear_test(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR REPLACE INTO professions_test(user_id, nap, Inz, It, Mark, Him, Econ, Bot, "All", Psihoter, Ecol, Psiholog, Prep, Zhur, Adv, Buh, Fin) VALUES (?, NULL , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)',(user_id,))
    conn.commit()
    
