import sqlite3

def init_db():
    conn = sqlite3.connect("chat_history.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS chats 
                      (session_id TEXT, message TEXT, response TEXT)''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
