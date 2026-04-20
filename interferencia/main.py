from fastapi import FastAPI, Form
from services.user import fill_book, create_table, obtain_book

app = FastAPI()

create_table()

@app.post("/formulario/llibres", response_model=dict)
async def omplir(
        titulo: str = Form(...),
        autor: str = Form(...),
        isbn: int = Form(...),
        sinopsis: str = Form(None),
        genero: str = Form(...),
        anioPublicacion: int = Form(...),
        editorial: str = Form(...),
        numeroPaginas: int = Form(None),
        codigoEstanteria: str = Form(...),
    ):
    result = await fill_book(titulo, autor, isbn, sinopsis, genero, anioPublicacion, editorial, numeroPaginas, codigoEstanteria)
    return result

@app.get("/formualrio/llibres/{id}", response_model=dict)
async def consultar(id: int):
    result = await obtain_book(id)
    return result