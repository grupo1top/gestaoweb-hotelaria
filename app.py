from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Form
from fastapi.responses import RedirectResponse
from typing import Annotated
from fastapi.staticfiles import StaticFiles

from model import *

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")



#listagem de alunos

@app.get("/")
async def consultar_hospede(request:Request): 

    consulta = consulta_hospedes()
    quartos = consulta_quartos()
    reservas = consulta_reservas()

    return templates.TemplateResponse(
    request=request, 
    name="index.html", 
    context={

       "tabela1": consulta,
       "tabela2": quartos,
       "tabela3": reservas
    }) 

#visualizar alunos

@app.get("/hospede")
async def consultar_hospede(request:Request):
    return templates.TemplateResponse(
    request=request, 
    name="hospedes.html", 
    context={"context":consulta_hospede_id()}) 

#cadastrar aluno

@app.get("/add_hospede")
async def cadastrar_hospede(request=Request):
    return templates.TemplateResponse(
    request=request, 
    name="add_hospedes.html", 
    context={"context":add_hospede()}) 

@app.post("/add_hospede")
async def cadastrar_hospede():
    return add_hospede()

#edição de alunos

@app.get("/edit_hospede/{id}")
async def editar_hospede(request:Request):
    return templates.TemplateResponse(
    request=request, 
    name="edit_hospede.html", 
    context={"context":update_hospede()}) 

@app.post("/edit_hospede/{id}")
async def editar_alunos():
    return update_hospede()

#exclusão de alunos 

@app.get("/delete_hospede/{id}")
async def deletar_hospede(request: Request):
    return templates.TemplateResponse(
    request=request, 
    name="delete_hospedes.html", 
    context={"context":delete_hospede()}) 

#listagem de cursos

@app.post("/delete_hospede/{id}")
async def deletar_hospede():
   return delete_hospede()

# @app.get("/cursos")
# async def listar_cursos(request:Request):
#     return templates.TemplateResponse(
#     request=request, 
#     name="edit.html", 
#     context={"context":lista_cursos()}) 

@app.get("/quartos")
async def consultar_quartos(request:Request): 
    return templates.TemplateResponse(
    request=request, 
    name="quartos.html", 
    context={"context":consulta_quartos_id()}) 

#cadastrar aluno

@app.get("/add_quarto")
async def adicionar_quarto(request=Request):
    return templates.TemplateResponse(
    request=request, 
    name="add_quarto.html", 
    context={"context":add_quarto()}) 

@app.post("/add_quarto")
async def adicionar_quarto():
    return add_quarto()

#edição de alunos

@app.get("/edit_quarto/{id}")
async def editar_quarto(request:Request):
    return templates.TemplateResponse(
    request=request, 
    name="edit_quarto.html", 
    context={"context":update_quarto()}) 

@app.post("/edit_quarto/{id}")
async def editar_quarto():
    return update_quarto()

#exclusão de alunos 

@app.get("/delete_quarto/{id}")
async def deletar_quarto(request: Request):
    return templates.TemplateResponse(
    request=request, 
    name="delete_quarto.html", 
    context={"context":delete_quarto()}) 

#listagem de cursos

@app.post("/delete_quarto/{id}")
async def deletar_quarto():
   return delete_quarto()

@app.get("/reservas")
async def consultar_reserva(request:Request):
    return templates.TemplateResponse(
    request=request, 
    name="reservas.html", 
    context={"context":consulta_reservas()}) 

@app.get("/reservas/{id}")
async def consultar_reserva(request:Request):
    return templates.TemplateResponse(
    request=request, 
    name="reservas.html", 
    context={"context":consulta_reserva_id()}) 

#cadastrar aluno

@app.get("/add_reserva")
async def adicionar_reserva(request=Request):
    return templates.TemplateResponse(
    request=request, 
    name="add_reserva.html", 
    context={"context":add_reserva()}) 

@app.post("/add_reserva")
async def adicionar_reserva():
    return add_reserva()

#edição de alunos

@app.get("/edit_reserva/{id}")
async def editar_hospede(request:Request):
    return templates.TemplateResponse(
    request=request, 
    name="edit_reserva.html", 
    context={"context":update_reserva()}) 

@app.post("/edit_reserva/{id}")
async def editar_reserva():
    return update_reserva()

#exclusão de alunos 

@app.get("/delete_reserva/{id}")
async def deletar_reserva(request: Request):
    return templates.TemplateResponse(
    request=request, 
    name="delete_reserva.html", 
    context={"context":delete_reserva()}) 

#listagem de cursos

@app.post("/delete_reserva/{id}")
async def deletar_reserva():
   return delete_reserva()
