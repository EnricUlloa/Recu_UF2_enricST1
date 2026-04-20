def user_schema(result) -> dict:
    return{
        "id": result[0],
        "titulo": result[1],
        "autor": result[2],
        "isbn": result[3],
        "genero": result[4],
        "anioPublicacion": result[5],
        "editorial": result[6]
    }