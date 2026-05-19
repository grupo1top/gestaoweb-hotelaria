-- cria o banco de dados "HOTELARIA", que foi solicitado no NOTION.
CREATE DATABASE hotelaria;

USE hotelaria; -- seleciona o banco de dados para uso.

-- cria a tabela hospedes e segue o padrão do NOTION.
CREATE TABLE hospedes (

    -- id, unico e com auto incremento.
    id INT PRIMARY KEY AUTO_INCREMENT,
    -- nome, obrigatorio.
    nome VARCHAR(100) NOT NULL,
    -- email, não obrigatorio
    email VARCHAR(100) NULL,
    -- telefone, não obrigatorio
    telefone VARCHAR(100) NULL,
    -- cpf, unico
    cpf VARCHAR(14) UNIQUE

);

-- cria a tabela quartos e segue o padrão do NOTION.
CREATE TABLE quartos (

    -- id, unico e com auto incremento.
    id INT PRIMARY KEY AUTO_INCREMENT,
    -- numero, obrigatorio.
    numero VARCHAR(10) NOT NULL,
    -- tipo, obrigatorio.
    tipo VARCHAR(50) NOT NULL,
    -- valor da diaria, obrigatorio
    valor_diaria DECIMAL(10,2) NOT NULL,
    -- status, obrigatorio
    status VARCHAR(20) NOT NULL

);

-- cria a tabela reservas e segue o padrão do NOTION
CREATE TABLE reservas (

    -- id, unico e com auto incremento.
    id INT PRIMARY KEY AUTO_INCREMENT,
    -- hospede
    hospede_id INT,
    -- quarto
    quarto_id INT,
    -- data de entrada, obrigatoria
    data_entrada DATE NOT NULL,
    -- data de saida, obrigatoria
    data_saida DATE NOT NULL,
    
    -- vincula os id de duas tabelas diferentes
    FOREIGN KEY (hospede_id) REFERENCES hospedes(id),
    FOREIGN KEY (quarto_id) REFERENCES quartos(id)
    
);

-- insert basico para teste na tabela hospedes
INSERT INTO hospedes (nome, email, telefone, cpf) 
VALUES ('Kurachi' , 'kurachi@email.com', '11961865757', '51242090966');


-- insert basico para teste na tabela quartos
INSERT INTO quartos( numero , tipo, valor_diaria, status)
VALUES ('107', "PADRÃO", 1200.00 , 'DISPONÍVEL' );

-- insert basico para teste na tabela reservas
INSERT INTO reservas (hospede_id, quarto_id, data_entrada, data_saida)
VALUES (1, 1, '2012-12-12', '2012-12-16');


-- cria a view reservas seguindo o padrão solicitado no NOTION
CREATE VIEW view_reservas AS SELECT
    
    -- id da reserva
    r.id AS reserva_id,
    -- id do hospede
    r.hospede_id AS hospede_id,
    -- hospede
    h.nome AS hospede,
    -- quarto
    q.numero AS quarto,
    -- tipo
    q.tipo AS tipo_quarto,
    -- data entrada
    r.data_entrada,
    -- data saida
    r.data_saida,
    -- calculo de valor estimado
    DATEDIFF(r.data_saida, r.data_entrada) * q.valor_diaria AS valor_estimado
    
    -- join nas tabelas
FROM reservas r
INNER JOIN hospedes h ON r.hospede_id = h.id
INNER JOIN quartos q ON r.quarto_id = q.id;

-- cria a view do dashboard com os totais básicos do sistema
CREATE VIEW view_dashboard AS
SELECT
    -- quantidade de hóspedes
    (SELECT COUNT(*) FROM hospedes) AS total_hospedes,
    -- quantidade de quartos
    (SELECT COUNT(*) FROM quartos) AS total_quartos,
    -- reservas ativas
    (SELECT COUNT(*) FROM reservas
        WHERE DATEDIFF(data_saida, CURDATE()) >= 0
          AND DATEDIFF(CURDATE(), data_entrada) >= 0) AS total_reservas_ativas,
    -- rendimentos
    (SELECT COALESCE(SUM(DATEDIFF(r.data_saida, r.data_entrada) * q.valor_diaria), 0)
        FROM reservas r
        INNER JOIN quartos q ON r.quarto_id = q.id) AS total_rendimentos;

-- consultas avulsas apenas para testes
SELECT * FROM hospedes;
SELECT * FROM quartos;
SELECT * FROM reservas;
SELECT * FROM view_reservas;
SELECT * FROM view_dashboard;