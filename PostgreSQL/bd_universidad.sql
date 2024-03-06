CREATE DATABASE bd_universidad;
CREATE TYPE sexo AS ENUM ('H', 'M');
CREATE TYPE tipo_pers AS ENUM ('Alumno', 'Profesor');
CREATE TYPE tipo_asig AS ENUM ('Obligatoria', 'Optativa', 'Basica');
CREATE TABLE departamento (
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(50)
);
CREATE TABLE grado (
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(100)
);
CREATE TABLE curso_escolar (
	id SERIAL PRIMARY KEY,
	anyo_inicio INT,
	anyo_fin INT
);
CREATE TABLE profesor (
	id SERIAL PRIMARY KEY,
	id_departamento INT REFERENCES departamento(id)
);
CREATE TABLE asignatura (
	id SERIAL PRIMARY KEY,
	nombre VARCHAR(100),
	creditos DECIMAL(10, 2),
	tipo tipo_asig,
	curso SMALLINT,
	cuatrimestre SMALLINT,
	id_profesor INT REFERENCES profesor(id),
	id_grado INT REFERENCES grado(id)
);
CREATE TABLE persona (
	id SERIAL PRIMARY KEY,
	nif VARCHAR(9),
	nombre VARCHAR(25),
	apellido1 VARCHAR(50),
	apellido2 VARCHAR(50),
	ciudad VARCHAR(25),
	direccion VARCHAR(50),
	telefono VARCHAR(9),
	fecha_nacimiento DATE,
	sexo sexo,
	tipo tipo_pers
);
CREATE TABLE alumno_se_matricula_asignatura (
	id_alumno INT REFERENCES persona(id),
	id_asignatura INT REFERENCES asignatura(id),
	id_curso_escolar INT REFERENCES curso_escolar(id)
);
INSERT INTO departamento (nombre) 
VALUES 
    ('Departamento de Matemáticas'),
    ('Departamento de Física'),
    ('Departamento de Química'),
    ('Departamento de Biología'),
    ('Departamento de Ingeniería Eléctrica'),
    ('Departamento de Ingeniería Mecánica'),
    ('Departamento de Ingeniería Civil'),
    ('Departamento de Ciencias de la Computación'),
    ('Departamento de Economía'),
    ('Departamento de Psicología'),
    ('Departamento de Historia'),
    ('Departamento de Literatura'),
    ('Departamento de Idiomas Extranjeros'),
    ('Departamento de Arquitectura'),
    ('Departamento de Medicina');
INSERT INTO grado (nombre) 
VALUES 
    ('Licenciatura en Matemáticas'),
    ('Licenciatura en Física'),
    ('Licenciatura en Química'),
    ('Licenciatura en Biología'),
    ('Ingeniería Eléctrica'),
    ('Ingeniería Mecánica'),
    ('Ingeniería Civil'),
    ('Ciencias de la Computación'),
    ('Economía'),
    ('Psicología'),
    ('Historia'),
    ('Literatura'),
    ('Idiomas Extranjeros'),
    ('Arquitectura'),
    ('Medicina');
INSERT INTO curso_escolar (anyo_inicio, anyo_fin)
VALUES 
    (2020, 2021),
    (2021, 2022),
    (2022, 2023),
    (2023, 2024),
    (2024, 2025),
    (2025, 2026),
    (2026, 2027),
    (2027, 2028),
    (2028, 2029),
    (2029, 2030),
    (2030, 2031),
    (2031, 2032),
    (2032, 2033),
    (2033, 2034),
    (2034, 2035);
INSERT INTO profesor (id_departamento)
VALUES 
    (1),
    (1),
    (2),
    (2),
    (3),
    (4),
    (5),
    (5),
    (6),
    (7),
    (8),
    (9),
    (10),
    (11),
    (12);
INSERT INTO asignatura (nombre, creditos, tipo, curso, cuatrimestre, id_profesor, id_grado)
VALUES 
    ('Álgebra Lineal', 6.0, 'Obligatoria', 1, 1, 1, 1),
    ('Mecánica Clásica', 6.0, 'Obligatoria', 1, 1, 2, 2),
    ('Química Orgánica', 6.0, 'Obligatoria', 1, 2, 3, 3),
    ('Biología Celular', 6.0, 'Obligatoria', 1, 2, 4, 4),
    ('Electromagnetismo', 6.0, 'Optativa', 2, 1, 5, 5),
    ('Diseño de Máquinas', 6.0, 'Optativa', 2, 1, 6, 6),
    ('Diseño Estructural', 6.0, 'Optativa', 2, 2, 7, 7),
    ('Programación Avanzada', 6.0, 'Optativa', 2, 2, 8, 8),
    ('Microeconomía', 6.0, 'Obligatoria', 3, 1, 9, 9),
    ('Psicología del Desarrollo', 6.0, 'Obligatoria', 3, 1, 10, 10),
    ('Historia Contemporánea', 6.0, 'Obligatoria', 3, 2, 11, 11),
    ('Literatura Universal', 6.0, 'Obligatoria', 3, 2, 12, 12),
    ('Inglés Avanzado', 6.0, 'Optativa', 4, 1, 13, 13),
    ('Diseño Arquitectónico', 6.0, 'Optativa', 4, 1, 14, 14),
    ('Anatomía Humana', 6.0, 'Basica', 4, 2, 15, 15);
INSERT INTO persona (nif, nombre, apellido1, apellido2, ciudad, direccion, telefono, fecha_nacimiento, sexo, tipo)
VALUES 
    ('12345678A', 'Juan', 'Pérez', 'García', 'Madrid', 'Calle Mayor 123', '123456789', '1990-05-15', 'H', 'Alumno'),
    ('23456789B', 'María', 'López', 'Fernández', 'Barcelona', 'Avenida Diagonal 456', '234567890', '1988-08-25', 'M', 'Alumno'),
    ('34567890C', 'Pedro', 'Gómez', 'Martínez', 'Valencia', 'Calle Valencia 789', '345678901', '1995-10-10', 'H', 'Alumno'),
    ('45678901D', 'Ana', 'Ruiz', 'Sánchez', 'Sevilla', 'Avenida de la Constitución 321', '456789012', '1992-03-30', 'M', 'Alumno'),
    ('56789012E', 'David', 'Martín', 'López', 'Málaga', 'Calle Larios 234', '567890123', '1993-07-20', 'H', 'Alumno'),
    ('67890123F', 'Laura', 'Sanz', 'Díaz', 'Bilbao', 'Calle Gran Vía 567', '678901234', '1991-01-05', 'M', 'Alumno'),
    ('78901234G', 'Carlos', 'Jiménez', 'Muñoz', 'Alicante', 'Calle Postiguet 890', '789012345', '1994-12-12', 'H', 'Alumno'),
    ('89012345H', 'Sara', 'García', 'Rodríguez', 'Zaragoza', 'Paseo de la Independencia 432', '890123456', '1996-09-28', 'M', 'Alumno'),
    ('90123456I', 'Diego', 'Pérez', 'Fernández', 'Murcia', 'Calle Mayor 987', '901234567', '1997-06-18', 'H', 'Alumno'),
    ('01234567J', 'Elena', 'Martínez', 'Gómez', 'Granada', 'Calle Reyes Católicos 876', '012345678', '1998-04-03', 'M', 'Alumno'),
    ('12345678K', 'José', 'González', 'Gutiérrez', 'Toledo', 'Calle Real 765', '123456789', '1999-02-14', 'H', 'Profesor'),
    ('23456789L', 'Carmen', 'Díaz', 'Hernández', 'Valladolid', 'Plaza Mayor 654', '234567890', '1985-11-20', 'M', 'Profesor'),
    ('34567890M', 'Javier', 'Sánchez', 'Romero', 'Cádiz', 'Calle Ancha 543', '345678901', '1980-07-08', 'H', 'Profesor'),
    ('45678901N', 'Isabel', 'López', 'Martínez', 'Salamanca', 'Calle Mayor 432', '456789012', '1983-09-16', 'M', 'Profesor'),
    ('56789012O', 'Manuel', 'Fernández', 'García', 'León', 'Paseo de la Condesa 321', '567890123', '1978-12-05', 'H', 'Profesor');
INSERT INTO alumno_se_matricula_asignatura (id_alumno, id_asignatura, id_curso_escolar)
VALUES 
    (1, 1, 1),
    (2, 2, 1),
    (3, 3, 2),
    (4, 4, 2),
    (5, 5, 3),
    (6, 6, 3),
    (7, 7, 4),
    (8, 8, 4),
    (9, 9, 5),
    (10, 10, 5),
    (1, 11, 6),
    (2, 12, 6),
    (3, 13, 7),
    (4, 14, 7),
    (5, 15, 8);
