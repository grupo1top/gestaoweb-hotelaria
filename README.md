# Sistema Web de Gestão Hoteleira

Sistema Web de Gestão Hoteleira desenvolvido com **Python**, **FastAPI**, **Jinja2** e **MySQL**, seguindo a arquitetura **MVC**.  
O projeto tem como objetivo facilitar o gerenciamento de hóspedes, quartos, reservas e hospedagens em um ambiente web simples, organizado e funcional.

---

## Objetivo

Desenvolver uma aplicação web para controle hoteleiro, permitindo o cadastro, consulta, edição, visualização e exclusão de informações relacionadas a:

- Hóspedes
- Quartos
- Reservas
- Hospedagens

A aplicação utiliza renderização de páginas HTML com **Jinja2**, rotas controladas pelo **FastAPI** e persistência de dados em banco **MySQL**.

---

## Tecnologias Utilizadas

- Python
- FastAPI
- Jinja2
- MySQL
- HTML
- CSS
- JavaScript
- Arquitetura MVC

---

## Arquitetura do Projeto

O sistema segue a arquitetura **MVC**, separando as responsabilidades da aplicação em camadas:

- **Model:** responsável pelas regras de negócio e acesso aos dados.
- **View:** responsável pela interface visual do sistema, utilizando templates Jinja2.
- **Controller:** responsável pelas rotas e controle das requisições da aplicação.

---

## Estrutura do Projeto

```bash
Projeto/
│
├── static/
│   ├── img/
│   ├── js/
│   └── css/
│
├── templates/
│   ├── index.html
│   ├── hospedes.html
│   ├── quartos.html
│   ├── reservas.html
│   ├── add_hospede.html
│   ├── edit_hospede.html
│   ├── add_quarto.html
│   ├── edit_quarto.html
│   ├── add_reserva.html
│   ├── edit_reserva.html
│   └── view_reserva.html
│
├── app.py
├── dao.py
├── model.py
├── hotelaria.sql
└── README.md