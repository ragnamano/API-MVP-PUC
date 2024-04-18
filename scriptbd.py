import mysql.connector
from mysql.connector import errorcode

def CriarDB():
        
        print("Conectanto...")
        try:
            conn = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password="admin"
            )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('usuario ou senha incorreto')
            else:
                print(err)

        cursor = conn.cursor()
        cursor.execute("DROP DATABASE IF EXISTS Coleção;")
        cursor.execute("CREATE DATABASE Coleção;")
        cursor.execute("USE Coleção;")

        TABLES = {}
        TABLES['livros'] = ("""
                CREATE TABLE livros (
                    id int(11) NOT NULL AUTO_INCREMENT,
                    titulo varchar(50) NOT NULL,
                    autor varchar(40) NOT NULL,
                    genero varchar(20) NOT NULL,
                    PRIMARY KEY (id)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;""")

        for tabela_nome in TABLES:
            tabela_sql = TABLES[tabela_nome]
            try:
                print('Criando tabela {}:'.format(tabela_nome), end=' ')
                cursor.execute(tabela_sql)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print('Já existe')
                else:
                    print(err.msg)
            else:
                print('OK')

        livros_sql = 'INSERT INTO livros (titulo, autor, genero) values (%s, %s, %s)'
        livros = [
            ('Senhor dos Aneis', 'J. R. R. Tolkien', 'Fantasia Medieval'),
            ('A Culpa É das Estrelas', 'John Green', 'Romance'),
        ]

        cursor.executemany(livros_sql, livros)
        conn.commit()
        cursor.close()