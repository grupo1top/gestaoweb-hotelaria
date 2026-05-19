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

    dashboard = dashboard_index()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "dashboard": dashboard,
        },
    )

#visualizar alunos

@app.get("/hospede")
async def consultar_hospede(request:Request):
    return templates.TemplateResponse(
    request=request, 
    name="hospedes.html",   
    context={"context":consulta_hospedes()}) 
   
   

#cadastrar aluno

@app.get("/add_hospede")
async def cadastrar_hospede(request:Request):
    return templates.TemplateResponse(
    request=request, 
    name="add_hospede.html", 
    )

@app.post("/add_hospede")
async def cadastrar_hospede(

    request: Request,

    nome: str = Form(...),
    email: str = Form(...),
    telefone: str = Form(...),
    cpf: str = Form(...)

):
    add_hospede(nome, email, telefone, cpf)

    return RedirectResponse("/hospede", status_code=303)  

#edição de alunos

@app.get("/edit_hospede/{id}")
async def editar_hospede(request:Request, id:int):
    hospede = consulta_hospede_id(id)

    return templates.TemplateResponse(
    request=request, 
    name="edit_hospede.html",
    context={"hospede": hospede})



@app.post("/edit_hospede/{id}")
async def editar_hospede(
    request: Request,
    id :int,
    nome: str = Form(...),
    email: str = Form(...),
    telefone: str = Form(...),
    cpf: str = Form(...)
):
    update_hospede(id, nome, email, telefone, cpf)
    return RedirectResponse("/hospede", status_code=303)

#exclusão de alunos 

@app.get("/delete_hospede/{id}")
async def deletar_hospede(request: Request, id:int):
    hospede = consulta_hospede_id(id)

    return templates.TemplateResponse(
    request=request, 
    name="hospedes.html", 
    context={"hospede":hospede}) 



@app.post("/delete_hospede/{id}")
async def deletar_hospede(id: int):

    delete_hospede(id)

    return RedirectResponse("/hospede", status_code=303)
   

@app.get("/quartos")
async def consultar_quartos(request:Request): 
    return templates.TemplateResponse(
    request=request, 
    name="quartos.html", 
    context={"context":consulta_quartos()}) 

#cadastrar aluno

@app.get("/add_quarto")
async def adicionar_quarto(request: Request):
    return templates.TemplateResponse(
    request=request,
    name="add_quarto.html")

@app.post("/add_quarto")
async def adicionar_quarto(

    request: Request,

    numero: str = Form(...),
    tipo: str = Form(...),
    valor_diaria: str = Form(...),
    status: str = Form(...)

):
    add_quarto(numero, tipo, valor_diaria, status)

    return RedirectResponse("/quartos", status_code=303)  
#edição de alunos

@app.get("/edit_quarto/{id}")
async def editar_quarto(request:Request, id:int):

    quarto = consulta_quartos_id(id)

    return templates.TemplateResponse(
    request=request, 
    name="edit_quarto.html", 
    context={"quartos":quarto}) 

@app.post("/edit_quarto/{id}")
async def editar_quarto(
    request: Request,

    id: int,
    numero: str = Form(...),
    tipo: str = Form(...),
    valor_diaria: str = Form(...),
    status: str = Form(...)

):
    update_quarto(id, numero, tipo, valor_diaria, status)

    return RedirectResponse("/quartos", status_code=303)  

#exclusão de alunos 

@app.get("/delete_quarto/{id}")
async def deletar_quarto(request: Request, id:int):

    quarto = consulta_quartos_id(id)

    return templates.TemplateResponse(
    request=request, 
    name="quartos.html", 
    context={"quartos": quarto}) 

#listagem de cursos

@app.post("/delete_quarto/{id}")
async def deletar_quarto(id: int):

    delete_quarto(id)

    return RedirectResponse("/quartos", status_code=303)  



@app.get("/reservas")
async def consultar_reserva(request:Request):
    return templates.TemplateResponse(
    request=request, 
    name="reservas.html", 
    context={"context":consulta_reservas()}) 

@app.get("/reservas/{id}")
async def consultar_reserva(request:Request, id:int):
    return templates.TemplateResponse(
    request=request, 
    name="view_reserva.html", 
    context={"context":view_reserva(id), "hospede_id": id}) 

#cadastrar aluno

@app.get("/add_reserva")
async def adicionar_reserva(request: Request):
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
