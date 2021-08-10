CREATE DATABASE Projeto
GO

USE Projeto
GO

CREATE TABLE usuarios
(
	codigo       INT         PRIMARY KEY IDENTITY NOT NULL,
	nome         VARCHAR(50)                      NOT NULL,
	senha        VARCHAR(50)                      NOT NULL,
    status       INT         DEFAULT(1)           NOT NULL
)
GO

SELECT * FROM usuarios
GO

/*INSERT INTO usuarios(nome, senha) VALUES('Pedro', '123456')
GO
INSERT INTO usuarios(nome, senha) VALUES('admin', 'admin')
GO
INSERT INTO usuarios(nome, senha) VALUES('Alexandre Jr.', '654321')
GO
INSERT INTO usuarios(nome, senha) VALUES('Daniela', 'dani')
GO
INSERT INTO usuarios(nome, senha) VALUES('Isabela', 'fridaK')
GO
INSERT INTO usuarios(nome, senha) VALUES('Henrique', 'Babi')
GO
INSERT INTO usuarios(nome, senha) VALUES('teste', 'teste')
GO
INSERT INTO usuarios(nome, senha) VALUES('Elias u-Designer', 'html')
GO
SELECT * FROM usuarios
GO*/

DELETE FROM usuarios WHERE codigo = 9;
GO
