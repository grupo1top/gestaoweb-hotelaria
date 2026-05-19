CREATE DATABASE hotelaria;

USE hotelaria;

CREATE TABLE hospedes (

	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NULL,
    telefone VARCHAR(100) NULL,
    cpf VARCHAR(14) UNIQUE

);

CREATE TABLE quartos (

	id INT PRIMARY KEY AUTO_INCREMENT,
    numero VARCHAR(10) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    valor_diaria DECIMAL(10,2) NOT NULL,
    status VARCHAR(20) NOT NULL

);

CREATE TABLE reservas (
	
    id INT PRIMARY KEY AUTO_INCREMENT,
    hospede_id INT,
    quarto_id INT,
    data_entrada DATE NOT NULL,
    data_saida DATE NOT NULL,
    
    FOREIGN KEY (hospede_id) REFERENCES hospedes(id),
    FOREIGN KEY (quarto_id) REFERENCES quartos(id)
    
);

INSERT INTO hospedes (nome, email, telefone, cpf) 
VALUES ('Kurachi' , 'kurachi@email.com', '11961865757', '51242090966');


INSERT INTO quartos( numero , tipo, valor_diaria, status)
VALUES ('107', "PADRÃO", 1200.00 , 'DISPONÍVEL' );

INSERT INTO reservas (hospede_id, quarto_id, data_entrada, data_saida)
VALUES (1, 1, '2012-12-12', '2012-12-16');

CREATE VIEW view_reservas AS SELECT
    
    r.id AS reserva_id,
    h.nome AS hospede,
    q.numero AS quarto,
    q.tipo AS tipo_quarto,
    r.data_entrada,
    r.data_saida,
    DATEDIFF(r.data_saida, r.data_entrada) * q.valor_diaria AS valor_estimado
    
FROM reservas r
INNER JOIN hospedes h ON r.hospede_id = h.id
INNER JOIN quartos q ON r.quarto_id = q.id;

SELECT * FROM hospedes;
SELECT * FROM quartos;
SELECT * FROM reservas;
SELECT * FROM view_reservas;