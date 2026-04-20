from config import database

def create_table():
    conn = database.connection_db()
    cursor = conn.cursor()
    sql_table = '''
        CREATE TABLE IF NOT EXISTS llibres(
            id SERIAL PRIMARY KEY,
            titulo VARCHAR(100) NOT NULL,
            autor VARCHAR(100) NOT NULL,
            isbn INTEGER NOT NULL,
            sinopsis TEXT,
            genero VARCHAR(100) NOT NULL,
            anioPublicacion INTEGER NOT NULL,
            editorial VARCHAR(100) NOT NULL,
            numeroPaginas INTEGER,
            codigoEstanteria VARCHAR(100)
        )
    '''
    cursor.execute(sql_table)
    conn.commit()
    cursor.close()
    conn.close()
    print("Tabla creada correctamente")

async def fill_book(titulo, autor, isbn, sinopsis, genero, anioPublicacion, editorial, numeroPaginas, codigoEstanteria):
    conn = database.connection_db()
    cursor = conn.cursor()
    sql_post = "INSERT INTO llibres (titulo, autor, isbn, sinopsis, genero, anioPublicacion, editorial, numeroPaginas, codigoEstanteria) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (titulo, autor, isbn, sinopsis, genero, anioPublicacion, editorial, numeroPaginas, codigoEstanteria)
    cursor.execute(sql_post, values)
    conn.commit()
    cursor.close()
    conn.close()
    return{"mensaje": "Libro creado correctamente"}