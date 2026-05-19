from dao import connection

def consulta_hospedes():
    conn = connection()
    cursor = conn.cursor(dictionary=True) # cria quem irá executar os comandos no banco / deixa os resultados em fora de dicionario

    cursor.execute(

        '''
            SELECT *
                FROM 
            hospedes
        '''

    )

    dados = cursor.fetchall() # pega os registros retornados pela query
    conn.close()
    return dados 

def consulta_hospede_id(id_user):
    conn = connection()
    cursor = conn.cursor(dictionary=True) 

    cursor.execute(
        '''
            SELECT  *
            FROM hospedes
            WHERE id = %s     
        ''',
        (id_user,) 
    )
        
    dados = cursor.fetchone() # pega os registros retornados pela query
    conn.close()
    return dados


def add_hospede(nome, email, telefone, cpf):
    conn = connection()
    cursor = conn.cursor()

    query = '''
            insert into hospedes (nome, email, telefone, cpf) values (%s, %s, %s, %s)
            '''
    
    cursor.execute(query , (nome,email, telefone, cpf))

    conn.commit()
    conn.close()

def update_hospede(id_user, nome, email, telefone, cpf):
    conn = connection() 
    cursor = conn.cursor()

    cursor.execute(
        '''
        UPDATE hospedes
        SET nome = %s, email = %s, telefone = %s, cpf = %s
        WHERE id = %s
        ''',
        (nome, email, telefone, cpf, id_user)
    )

    conn.commit()
    conn.close()

def delete_hospede(id_user):
    conn = connection()
    cursor = conn.cursor()

    cursor.execute(
        '''
        DELETE FROM hospedes
        where id = %s
        ''',
        (id_user,)
    )

    conn.commit()
    conn.close()

# def lista_cursos():
#     conn = connection()
#     cursor = conn.cursor(dictionary=True)

#     cursor.execute(
#         '''
#         SELECT * FROM cursos
#         '''
#     )

#     dados = cursor.fetchall() # pega os registros retornados pela query
#     conn.close()

#     resposta = {} # cria um novo dicionário que salva as informações encontradas

#     for item in dados:
#         resposta[f"{len(resposta)+1}"] = item["nome"]

#     return resposta


def consulta_quartos():
    conn = connection()
    cursor = conn.cursor(dictionary=True) # cria quem irá executar os comandos no banco / deixa os resultados em fora de dicionario

    cursor.execute(

        '''
            SELECT *
                FROM 
            quartos
        '''

    )

    dados = cursor.fetchall() # pega os registros retornados pela query
    conn.close()
    return dados


def consulta_quartos_id(id_user):
    conn = connection()
    cursor = conn.cursor(dictionary=True) 

    cursor.execute(
        '''
            SELECT  *
            FROM quartos
            WHERE id = %s     
        ''',
        (id_user,) 
    )
        
    dados = cursor.fetchone() # pega os registros retornados pela query
    conn.close()
    return dados



def add_quarto(numero, tipo, valor_diaria, status):
    conn = connection()
    cursor = conn.cursor()

    query = '''
            insert into quartos (numero, tipo, valor_diaria, status) values (%s, %s, %s, %s)
            '''
    
    cursor.execute(query , (numero, tipo, valor_diaria, status))

    conn.commit()
    conn.close()

def update_quarto(id_user, numero, tipo, valor_diaria, status):
    conn = connection()
    cursor = conn.cursor()

    cursor.execute(
        '''
        UPDATE quartos
        SET numero = %s, tipo = %s, valor_diaria = %s, status = %s
        WHERE id = %s
        ''',
        (numero, tipo, valor_diaria, status, id_user)
    )

    conn.commit()
    conn.close()

def delete_quarto(id_user):
    conn = connection()
    cursor = conn.cursor()

    cursor.execute(
        '''
        DELETE FROM quartos
        where id = %s
        ''',
        (id_user,)
    )

    conn.commit()
    conn.close()


def consulta_reservas():
    conn = connection()
    cursor = conn.cursor(dictionary=True) # cria quem irá executar os comandos no banco / deixa os resultados em fora de dicionario

    cursor.execute(

        '''
        SELECT 
            reservas.id,
            hospedes.nome AS nome_hospede,
            quartos.numero AS numero_quarto,
            reservas.data_entrada,
            reservas.data_saida
        FROM reservas
        JOIN hospedes 
            ON reservas.hospede_id = hospedes.id
        JOIN quartos 
            ON reservas.quarto_id = quartos.id;
        '''

    )

    dados = cursor.fetchall() # pega os registros retornados pela query
    conn.close()
    return dados


def consulta_reserva_id(id_user):
    conn = connection()
    cursor = conn.cursor(dictionary=True) 

    cursor.execute(
        '''
            SELECT  *
            FROM reservas
            WHERE id = %s     
        ''',
        (id_user,) 
    )
        
    dados = cursor.fetchall() # pega os registros retornados pela query
    conn.close()

    return dados
    

def add_reserva(hospede_id, quarto_id, data_entrada, data_saida):
    conn = connection()
    cursor = conn.cursor()

    query = '''
            insert into alunos (numero, tipo, valor_diaria, status) values (%s, %s, %s, %s)
            '''
    
    cursor.execute(query , (hospede_id, quarto_id, data_entrada, data_saida))

    conn.commit()
    conn.close()

def update_reserva(id_user, hospede_id, quarto_id, data_entrada, data_saida):
    conn = connection()
    cursor = conn.cursor()

    cursor.execute(
        '''
        UPDATE reservas
        SET hospede_id= %s, quarto_id = %s, data_entrada = %s, data_saida = %s
        WHERE id = %s
        ''',
        (hospede_id, quarto_id, data_entrada, data_saida, id_user)
    )

    conn.commit()
    conn.close()

def delete_reserva(id_user):
    conn = connection()
    cursor = conn.cursor()

    cursor.execute(
        '''
        DELETE FROM reservas
        where id = %s
        ''',
        (id_user,)
    )

    conn.commit()
    conn.close()
