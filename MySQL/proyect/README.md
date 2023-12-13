# Proyecto Final SENA
Diego Alejandro Palacio Herrera
R4
# Parte 1 (Diagramas y creación)
## Diagrama entidad - relación
![entidad relacion](https://github.com/AlejandroP75/CampusAP75/blob/main/MySQL/entidad_relacion.png?raw=true)
## Diagrama relacional
![relacional](https://github.com/AlejandroP75/CampusAP75/blob/main/MySQL/Relacional.png?raw=true)
## Creación de la base de datos y sus tablas
Crear base de datos
~~~sql
CREATE DATABASE proyecto_sena;
~~~
Usar base de datos
~~~sql
USE proyecto_sena;
~~~
Creación de las tablas
~~~sql
CREATE TABLE Carreras(
    id_carrera INT PRIMARY KEY AUTO_INCREMENT,
    nombre_carrera VARCHAR(50)
);

CREATE TABLE Aprendices(
    id_aprendiz INT PRIMARY KEY AUTO_INCREMENT,
    nombres_aprendiz VARCHAR(100),
    apellidos_aprendiz VARCHAR(100),
    id_carrera INT,
    FOREIGN KEY (id_carrera) REFERENCES Carreras(id_carrera)
);

CREATE TABLE Rutas(
    id_ruta INT PRIMARY KEY AUTO_INCREMENT,
    nombre_ruta VARCHAR(50),
    id_carrera INT,
    FOREIGN KEY (id_carrera) REFERENCES Carreras(id_carrera)
);

CREATE TABLE Matriculas(
    id_aprendiz INT,
    id_ruta INT,
    FOREIGN KEY (id_aprendiz) REFERENCES Aprendices(id_aprendiz),
    FOREIGN KEY (id_ruta) REFERENCES Rutas(id_ruta)
);

CREATE TABLE Cursos(
    id_curso INT PRIMARY KEY AUTO_INCREMENT,
    nombre_curso VARCHAR(50)
);

CREATE TABLE Aprendiz_X_Curso(
    id_aprendiz INT,
    id_curso INT,
    FOREIGN KEY (id_aprendiz) REFERENCES Aprendices(id_aprendiz),
    FOREIGN KEY (id_curso) REFERENCES Cursos(id_curso)
);

CREATE TABLE Especialidades(
    id_especialidad INT PRIMARY KEY AUTO_INCREMENT,
    tipo_especialidad VARCHAR(50)
);

CREATE TABLE Instructores(
    id_instructor INT PRIMARY KEY AUTO_INCREMENT,
    nombres_instructor VARCHAR(100),
    apellidos_instructor VARCHAR(100),
    id_especialidad INT,
    FOREIGN KEY (id_especialidad) REFERENCES Especialidades(id_especialidad)
);

CREATE TABLE Cursos_X_Ruta(
    id_curso INT,
    id_ruta INT,
    id_instructor INT,
    FOREIGN KEY (id_curso) REFERENCES Cursos(id_curso),
    FOREIGN KEY (id_ruta) REFERENCES Rutas(id_ruta),
    FOREIGN KEY (id_instructor) REFERENCES Instructores(id_instructor)
);
~~~
- Poblar las tablas
~~~sql
INSERT INTO Carreras(nombre_carrera) VALUES
("Desarrollo de Software"),
("Electrónica"),
("Mecánica Automotriz"),
("Seguridad y Salud Ocupacional"),
("Soldadura");

INSERT INTO Aprendices(nombres_aprendiz, apellidos_aprendiz, id_carrera) VALUES
("Carlos","Saúl Gómez",1),
("Leyla María","Delgado Vargas",1),
("Juan José","Cardona",1),
("Sergio Augusto","Contreras Navas",1),
("Ana María","Velázquez Parra",1),
("Gustavo","Noriega Alzate",2),
("Pedro Nell","Gómez Díaz",2),
("Jairo Augusto","Castro Camargo",2),
("Henry","Soler Vega",2),
("Antonio","Cañate Cortés",5),
("Daniel","Simancas Junior",5);

INSERT INTO Rutas(nombre_ruta, id_carrera) VALUES
("Sistemas de Información Empresariales", 1),
("Videojuegos", 1),
("Machine Learning", 1),
("Microcontroladores", 2),
("Robótica", 2),
("Dispositivos Bio-médicos", 2),
("Motores Híbridos", 3),
("Vehículos de Uso Agrícola", 3),
("Sistemas de Gestión en Seguridad Ocupacional", 4),
("Soldadura Autógena Industrial", 5),
("Soldadura Eléctrica Industrial", 5),
("Soldadura Submarina", 5);

INSERT INTO Matriculas(id_aprendiz, id_ruta) VALUES
(1,1),
(2,1),
(3,2),
(4,2),
(5,3),
(6,4),
(7,4),
(8,5),
(9,5),
(10,11),
(11,10);

INSERT INTO Cursos(nombre_curso) VALUES
("Matemáticas Básicas"),
("Álgebra Computacional"),
("Programación Básica"),
("Inglés"),
("Electrónica Básica"),
("Motor de Cuatro Tiempos"),
("Enfermedades Laborales"),
("Higiene Postural en el Trabajo"),
("Ergonomía"),
("Legislación Laboral en Colombia"),
("Materiales de Soldadura"),
("Métodos de Soldadura"),
("Fusión de Metales"),
("Buceo 1"),
("Buceo 2"),
("Riesgo Eléctrico"),
("Bases de Datos Relacionales"),
("Bases de Datos NO Relacionales"),
("Electrónica Digital"),
("Microprocesadores");

INSERT INTO Aprendiz_X_Curso(id_aprendiz, id_curso) VALUES
(1,17),
(1,2),
(1,3),
(1,18),
(2,1),
(2,2),
(2,3),
(2,4),
(3,1),
(3,2),
(3,3),
(4,4),
(4,1),
(4,2),
(5,3),
(5,4),
(5,17),
(6,5),
(6,19),
(6,20),
(7,5),
(7,19),
(7,20),
(8,5),
(8,19),
(9,5),
(9,19),
(9,20),
(10,11),
(10,13),
(11,11),
(11,14);

INSERT INTO Especialidades(tipo_especialidad) VALUES
("Sistemas"),
("Salud Ocupacional"),
("Soldadura"),
("Mecánica"),
("Inglés"),
("Electrónica");

INSERT INTO Instructores(nombres_instructor, apellidos_instructor, id_especialidad) VALUES
("Ricardo Vicente","Jaimes", 1),
("Marinela","Narvaez", 2),
("Agustín","Parra Granados", 3),
("Nelson","Raúl Buitrago", 4),
("Roy Hernando","Llamas", 5),
("Maria Jimena","Monsalve", 6),
("Juan Carlos","Cobos", 6),
("Pedro Nell","Santamaría", 1),
("Andrea","González", 1),
("Marisela","Sevilla", 2);

INSERT INTO Cursos_X_Ruta(id_curso, id_ruta, id_instructor) VALUES
(17, 1, 2),
(2, 1, 1),
(3, 1, 3),
(18, 1, 2),
(1, 1, 4),
(2, 1, 1),
(3, 1, 3),
(4, 1, 5),
(1, 2, 4),
(2, 2, 1),
(3, 2, 3),
(4, 2, 5),
(1, 2, 4),
(2, 2, 1),
(3, 3, 3),
(4, 3, 5),
(17, 3, 2),
(5, 4, 7),
(19, 4, 6),
(20, 4, 7),
(5, 4, 7),
(19, 4, 6),
(20, 4, 7),
(5, 5, 7),
(19, 5, 6),
(5, 5, 7),
(19, 5, 6),
(20, 5, 7),
(11, 11, 3),
(13, 11, 3),
(11, 10, 3),
(14, 10, NULL);
~~~
# Parte 2 (Consultas)
### 1. Agregue un campo Estado_Matrícula a la tabla Matrícula que indique si el estudiante se encuentra “En Ejecución”, “Terminado” o “Cancelado”
~~~sql
ALTER TABLE Matriculas 
ADD COLUMN estado_matricula VARCHAR(20);

UPDATE Matriculas
SET estado_matricula = "Activo"
WHERE id_aprendiz IN (1, 2, 4, 5);

UPDATE Matriculas
SET estado_matricula = "Cancelado"
WHERE id_aprendiz IN (3, 9);

UPDATE Matriculas
SET estado_matricula = "Terminado"
WHERE id_aprendiz IN (6, 7, 8, 10, 11);
~~~

### 2. Agregue a el campo edad a la tabla de Aprendices.
~~~sql
ALTER TABLE Aprendices
ADD COLUMN edad INT;

UPDATE Aprendices
SET edad = 28;
~~~

### 3. Si suponemos que los cursos tienen una duración diferente dependiendo de la ruta que lo contenga ¿qué modificación haría a la estructura de datos ya planteada?
~~~sql
ALTER TABLE Cursos_X_Ruta
ADD COLUMN duracion INT;

UPDATE Cursos_X_Ruta
SET duracion = 60;
~~~

### 4. Seleccionar los nombres y edades de aprendices que están cursando la carrera de electrónica.
~~~sql
SELECT nombres_aprendiz, apellidos_aprendiz, edad FROM Aprendices
WHERE id_carrera = 2;
~~~
### Resultado
![4](https://github.com/AlejandroP75/CampusAP75/blob/main/MySQL/10.png?raw=true)

### 5. Seleccionar Nombres de Aprendices junto al nombre de la ruta de aprendizaje que cancelaron.
~~~sql
SELECT nombres_aprendiz, apellidos_aprendiz, nombre_ruta FROM Matriculas
INNER JOIN Aprendices ON Matriculas.id_aprendiz = Aprendices.id_aprendiz
INNER JOIN Rutas ON Matriculas.id_ruta = Rutas.id_ruta
WHERE Matriculas.estado_matricula = "Cancelado";
~~~
### Resultado
![5](https://github.com/AlejandroP75/CampusAP75/blob/main/MySQL/4.png?raw=true)

### 6. Seleccionar Nombre de los cursos que no tienen un instructor asignado.
~~~sql
SELECT nombre_curso FROM Cursos
LEFT JOIN Cursos_X_Ruta ON Cursos.id_curso = Cursos_X_Ruta.id_curso
WHERE Cursos_X_Ruta.id_instructor IS NULL;
~~~
### Resultado
![4](https://github.com/AlejandroP75/CampusAP75/blob/main/MySQL/5.png?raw=true)

### 7. Seleccionar Nombres de los instructores que dictan cursos en la ruta de aprendizaje “Sistemas de Información Empresariales”.
~~~sql
SELECT DISTINCT nombres_instructor, apellidos_instructor FROM Cursos_X_Ruta
INNER JOIN Instructores ON Cursos_X_Ruta.id_instructor = Instructores.id_instructor
WHERE Cursos_X_Ruta.id_ruta = 1;
~~~
### Resultado
![4](https://github.com/AlejandroP75/CampusAP75/blob/main/MySQL/6.png?raw=true)

### 8. Genere un listado de todos los aprendices que terminaron una Carrera mostrando el nombre del profesional, el nombre de la carrera y el énfasis de la carrera (Nombre de la Ruta de aprendizaje)
~~~sql
SELECT nombres_aprendiz, apellidos_aprendiz, nombre_carrera, nombre_ruta FROM Matriculas
INNER JOIN Aprendices ON Matriculas.id_aprendiz = Aprendices.id_aprendiz
INNER JOIN Carreras ON Aprendices.id_carrera = Carreras.id_carrera
INNER JOIN Rutas ON Matriculas.id_ruta = Rutas.id_ruta
WHERE Matriculas.estado_matricula = "Terminado";
~~~
### Resultado
![4](https://github.com/AlejandroP75/CampusAP75/blob/main/MySQL/7.png?raw=true)

### 9. Genere un listado de los aprendices matriculados en el curso “Bases de Datos Relacionales”.
~~~sql
SELECT nombres_aprendiz, apellidos_aprendiz FROM Aprendiz_X_Curso
INNER JOIN Aprendices ON Aprendiz_X_Curso.id_aprendiz = Aprendices.id_aprendiz
WHERE Aprendiz_X_Curso.id_curso = 17;
~~~
### Resultado
![4](https://github.com/AlejandroP75/CampusAP75/blob/main/MySQL/8.png?raw=true)

### 10. Nombres de Instructores que no tienen curso asignado.
~~~sql
SELECT nombres_instructor, apellidos_instructor FROM Instructores
LEFT JOIN Cursos_X_Ruta ON Instructores.id_instructor = Cursos_X_Ruta.id_instructor
WHERE Cursos_X_Ruta.id_instructor IS NULL;
~~~
### Resultado
![4](https://github.com/AlejandroP75/CampusAP75/blob/main/MySQL/9.png?raw=true)

### FIN