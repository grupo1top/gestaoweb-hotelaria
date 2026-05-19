# app.py: rotas e páginas da aplicação usando FastAPI
# Importa o que é necessário do FastAPI e do módulo de dados
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Form
from fastapi.responses import RedirectResponse
from typing import Annotated
from fastapi.staticfiles import StaticFiles
from mysql.connector.errors import IntegrityError # para tratamento de erros no banco de dados 

from model import *

app = FastAPI()
# Serve arquivos na pasta static em /static
app.mount("/static", StaticFiles(directory="static"), name="static")
# Configura o diretório dos templates HTML
templates = Jinja2Templates(directory="templates")




# Página inicial que mostra o painel de controle

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


# Lista todos os hóspedes cadastrados

@app.get("/hospede")
async def consultar_hospede(request:Request):
    return templates.TemplateResponse(
    request=request, 
    name="hospedes.html",   
    context={"context":consulta_hospedes()}) 
   
   

# Exibe o formulário para incluir um novo hóspede

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


# Exibe o formulário de edição de um hóspede pelo id

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


# Mostra os dados para confirmar a exclusão

@app.get("/delete_hospede/{id}")
async def deletar_hospede(request: Request, id:int):
    hospede = consulta_hospede_id(id)

    return templates.TemplateResponse(
    request=request, 
    name="hospedes.html", 
    context={"hospede":hospede}) 



@app.post("/delete_hospede/{id}")
async def deletar_hospede(request: Request, id: int):
    try: # tenta adicionar um hóspede 
        delete_hospede(id)
        return RedirectResponse("/hospede", status_code=303)
    except IntegrityError: # em caso de erro exibe uma mensagem informando o possível erro vindo do banco de dados s
        return templates.TemplateResponse(
            request=request,
            name="hospedes.html",
            context={
                "context": consulta_hospedes(),
                "error_message": "Não é possível remover um hóspede que possuí uma reserva cadastrada.", # mensagem de erro 
            },
            status_code=400,
        )
   

@app.get("/quartos")
async def consultar_quartos(request:Request): 
    return templates.TemplateResponse(
    request=request, 
    name="quartos.html", 
    context={"context":consulta_quartos()}) 

#cadastrar quarto
# Exibe o formulário para inserir um novo quarto

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

# exibe formulário de edição de quarto 
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

# exclui um quarto

@app.get("/delete_quarto/{id}")
async def deletar_quarto(request: Request, id:int):

    quarto = consulta_quartos_id(id)

    return templates.TemplateResponse(
    request=request, 
    name="quartos.html", 
    context={"quarto": quarto}) 



@app.post("/delete_quarto/{id}")
async def deletar_quarto(id: int):

    delete_quarto(id)

    return RedirectResponse("/quartos", status_code=303)  

#visualizar reservas
# Lista todas as reservas e mostra a página de detalhes

@app.get("/reservas")
async def consultar_reserva(request:Request):
    return templates.TemplateResponse(
    request=request, 
    name="reservas.html", 
    context={"context":consulta_reservas()}) 


# busca reserva pelo id do hospede 
@app.get("/reservas/{id}")
async def consultar_reserva(request:Request, id:int):
    return templates.TemplateResponse(
    request=request, 
    name="view_reserva.html", 
    context={"context":view_reserva(id), "hospede_id": id}) 


# formulario para adicionar uma reserva 
@app.get("/add_reserva")
async def adicionar_reserva(request: Request):
    return templates.TemplateResponse(
    request=request, 
    name="add_reserva.html", 
    )

@app.post("/add_reserva")
async def adicionar_reserva(
    request: Request,

    id_hospede: str = Form(...),
    id_quarto: str = Form(...),
    data_entrada: str = Form(...),
    data_saida: str = Form(...)

):
    add_reserva(id_hospede, id_quarto, data_entrada, data_saida)

    return RedirectResponse("/reservas", status_code=303)  

# formulario de edição de reserva 
@app.get("/edit_reserva/{id}")
async def editar_hospede(request:Request, id:int):

    reserva = consulta_reserva_id(id)

    return templates.TemplateResponse(
    request=request, 
    name="edit_reserva.html", 
    context={"reserva": reserva}) 

@app.post("/edit_reserva/{id}")
async def editar_reserva(
    request: Request,

    id: int,
    id_hospede: str = Form(...),
    id_quarto: str = Form(...),
    data_entrada: str = Form(...),
    data_saida: str = Form(...)

):
    update_reserva(id, id_hospede, id_quarto, data_entrada, data_saida)

    return RedirectResponse("/reservas", status_code=303)  

# exclui uma reserva 


@app.post("/delete_reserva/{id}")
async def deletar_reserva(id:int):
    delete_reserva(id)

    return RedirectResponse("/reservas", status_code=303)  