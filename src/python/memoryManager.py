import sqlite3
import os

def get_memory_db(persona_db):
    db_Path =  f'data/memory/{persona_db}.db'
    if not os.path.exists(db_Path):
        conn = sqlite3.connect(db_Path)
        c = conn.cursor()
        c.execute('''CREATE TABLE memory
                     (id INTEGER PRIMARY KEY, memory TEXT)''')
        conn.commit()
        conn.close()
    return sqlite3.connect(db_Path)

def save_memory(persona, user_input, response):
    conn = get_memory_db(persona) 
    cursor = conn.cursor() 
    cursor.execute("INSERT INTO memory (user_input, response) VALUES (?, ?)", (user_input, response)) 
    conn.commit()
    conn.close()

def load_memory(persona):
    conn = get_memory_db(persona)
    cursor = conn.cursor()
    cursor.execute("SELECT user_input, response FROM memory")
    memories = cursor.fetchall() 
    conn.close() 
    return memories