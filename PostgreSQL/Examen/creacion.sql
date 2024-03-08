DROP DATABASE IF EXISTS ventas;
CREATE DATABASE ventas;
CREATE TABLE cliente(
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(100) NOT NULL,
	apellido1 VARCHAR(100) NOT NULL,
	apellido2 VARCHAR(100),
	ciudad VARCHAR(100),
	categoria INT
);
CREATE TABLE comercial(
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(100) NOT NULL,
	apellido1 VARCHAR(100) NOT NULL,
	apellido2 VARCHAR(100),
	comision DECIMAL(10, 2)
);
CREATE TABLE pedido(
	id SERIAL PRIMARY KEY,
	total DOUBLE PRECISION NOT NULL,
	fecha DATE,
	id_cliente INT REFERENCES cliente(id),
	id_comercial INT REFERENCES comercial(id)
);