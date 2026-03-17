IF OBJECT_ID('dbo.clientes') IS NULL
BEGIN
    CREATE TABLE dbo.clientes (
        id INT IDENTITY(1,1) PRIMARY KEY,
        nome VARCHAR(150) NOT NULL,
        email VARCHAR(150),
        data_cadastro DATETIME DEFAULT GETDATE()
    );
END
GO