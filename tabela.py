import sqlite3
import os

# Verificar se o diretório existe ou criá-lo se necessário
db_database = 'db'
if not os.path.exists(db_database):
    os.makedirs(db_database)

# Conectar ao banco de dados
conn = sqlite3.connect(os.path.join(db_database, 'database.db'), check_same_thread=False)

def criar_tabela():
    try:
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS atleta 
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nome TEXT, 
            idade TEXT, 
            modalidade TEXT,
            id_usuario INTEGER,      
            FOREIGN KEY (id_usuario) REFERENCES aulas (id))""")
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro SQLite durante a criação da tabela: {e}")

def aulas():
    try:
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS aulas 
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nome_aula TEXT  
            )""")
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro SQLite durante a criação da tabela: {e}")


criar_tabela()
aulas()