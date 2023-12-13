1. Devuelve un listado con el primer apellido, segundo apellido y el nombre de todos los alumnos. El listado deberá estar ordenado alfabéticamente de menor a mayor por el primer apellido, segundo apellido y nombre.

    ```sql
    SELECT apellido1, apellido2, nombre FROM persona
    WHERE tipo = 'alumno'
    ORDER BY apellido1, apellido2, nombre;
    ```

2. Averigua el nombre y los dos apellidos de los alumnos que **no** han dado de alta su número de teléfono en la base de datos.

    ```sql
    SELECT nombre, apellido1, apellido2 FROM persona
    WHERE tipo = 'alumno' AND telefono is NULL;
    ```

3. Devuelve el listado de los alumnos que nacieron en `1999`.

    ```sql
    SELECT * FROM persona
    WHERE YEAR(fecha_nacimiento) = '1999' AND tipo = 'alumno';
    ```

4. Devuelve el listado de `profesores` que **no** han dado de alta su número de teléfono en la base de datos y además su nif termina en `K`.

    ```sql
    SELECT * FROM persona
    WHERE tipo = 'profesor' AND telefono IS NULL AND nif LIKE '%K';
    ```

5. Devuelve el listado de las asignaturas que se imparten en el primer cuatrimestre, en el tercer curso del grado que tiene el identificador `7`.

    ```sql
    SELECT * FROM asignatura
    WHERE cuatrimestre = 1 AND curso = 3 AND id_grado = 7;
    ```

6. Devuelve un listado con los datos de todas las **alumnas** que se han matriculado alguna vez en el `Grado en Ingeniería Informática (Plan 2015)`.

    ```sql
    SELECT DISTINCT p.nombre, apellido1, apellido2 FROM  alumno_se_matricula_asignatura am
    INNER JOIN persona p ON am.id_alumno = p.id
    INNER JOIN asignatura a ON am.id_asignatura = a.id
    WHERE p.sexo = 'M' AND a.id_grado = 4;
    ```

7. Devuelve un listado con todas las asignaturas ofertadas en el `Grado en Ingeniería Informática (Plan 2015)`.

    ```sql
    SELECT nombre FROM asignatura
    WHERE id_grado = 4;
    ```

8. Devuelve un listado de los `profesores` junto con el nombre del `departamento` al que están vinculados. El listado debe devolver cuatro columnas, `primer apellido, segundo apellido, nombre y nombre del departamento.` El resultado estará ordenado alfabéticamente de menor a mayor por los `apellidos y el nombre.`

    ```sql
    SELECT apellido1, apellido2, pe.nombre, d.nombre FROM profesor pr
    INNER JOIN persona pe ON pr.id_profesor = pe.id
    INNER JOIN departamento d ON pr.id_departamento = d.id
    ORDER BY apellido1, apellido2, pe.nombre;
    ```

9. Devuelve un listado con el nombre de las asignaturas, año de inicio y año de fin del curso escolar del alumno con nif `26902806M`.

    ```sql
    SELECT a.nombre, ce.anyo_inicio, ce.anyo_fin FROM alumno_se_matricula_asignatura am
    INNER JOIN persona pe ON am.id_alumno = pe.id
    INNER JOIN asignatura a ON am.id_asignatura = a.id
    INNER JOIN curso_escolar ce ON am.id_curso_escolar = ce.id
    WHERE pe.nif = '26902806M';
    ```

10. Devuelve un listado con el nombre de todos los departamentos que tienen profesores que imparten alguna asignatura en el `Grado en Ingeniería Informática (Plan 2015)`.

     ```sql
    SELECT DISTINCT de.nombre FROM asignatura a
    INNER JOIN profesor pr ON a.id_profesor = pr.id_profesor
    INNER JOIN departamento de ON pr.id_departamento = de.id
    WHERE a.id_grado = 4;
     ```

11. Devuelve un listado con todos los alumnos que se han matriculado en alguna asignatura durante el curso escolar 2018/2019.

     ```sql
    SELECT DISTINCT pe.nombre, apellido1, apellido2 FROM alumno_se_matricula_asignatura am
    INNER JOIN persona pe ON am.id_alumno = pe.id
    INNER JOIN curso_escolar ce ON am.id_curso_escolar = ce.id
    WHERE ce.anyo_inicio = 2018 AND ce.anyo_fin = 2019;
     ```

12. Devuelve un listado con los nombres de **todos** los profesores y los departamentos que tienen vinculados. El listado también debe mostrar aquellos profesores que no tienen ningún departamento asociado. El listado debe devolver cuatro columnas, nombre del departamento, primer apellido, segundo apellido y nombre del profesor. El resultado estará ordenado alfabéticamente de menor a mayor por el nombre del departamento, apellidos y el nombre.

     ```sql
    SELECT de.nombre, apellido1, apellido2, pe.nombre FROM profesor pr
    INNER JOIN persona pe ON pr.id_profesor = pe.id
    INNER JOIN departamento de ON pr.id_departamento = de.id
    ORDER BY de.nombre, apellido1, apellido2, pe.nombre;
     ```

13. Devuelve un listado con los profesores que no están asociados a un departamento.Devuelve un listado con los departamentos que no tienen profesores asociados.

     ```sql
    SELECT de.nombre FROM profesor pr
    RIGHT JOIN departamento de ON pr.id_departamento = de.id
    WHERE id_profesor IS NULL;

    SELECT pe.nombre FROM persona pe
    RIGHT JOIN profesor pr on pr.id_profesor = pe.id
    WHERE id_departamento is NULL;
     ```

14. Devuelve un listado con los profesores que no imparten ninguna asignatura.

     ```sql
    SELECT pr.id_profesor, pe.nombre, apellido1, apellido2 FROM asignatura a
    RIGHT JOIN profesor pr ON a.id_profesor = pr.id_profesor
    INNER JOIN persona pe ON pr.id_profesor = pe.id
    WHERE a.id IS NULL;
     ```

15. Devuelve un listado con las asignaturas que no tienen un profesor asignado.

     ```sql
    SELECT nombre FROM asignatura
    WHERE id_profesor IS NULL;
     ```

16. Devuelve un listado con todos los departamentos que tienen alguna asignatura que no se haya impartido en ningún curso escolar. El resultado debe mostrar el nombre del departamento y el nombre de la asignatura que no se haya impartido nunca.

     ```sql
    SELECT de.nombre, a.nombre FROM asignatura a
    LEFT JOIN alumno_se_matricula_asignatura am ON a.id = am.id_asignatura
    INNER JOIN profesor pr ON a.id_profesor = pr.id_profesor
    INNER JOIN departamento de ON pr.id_departamento = de.id
    WHERE am.id_curso_escolar IS NULL;
     ```

17. Devuelve el número total de **alumnas** que hay.

     ```sql
    SELECT COUNT(id) FROM persona
    WHERE sexo = 'M' AND tipo = 'alumno'
     ```

18. Calcula cuántos alumnos nacieron en `1999`.

     ```sql
    SELECT COUNT(id) FROM persona
    WHERE tipo = 'alumno' AND YEAR(fecha_nacimiento) = '1999';
     ```

19. Calcula cuántos profesores hay en cada departamento. El resultado sólo debe mostrar dos columnas, una con el nombre del departamento y otra con el número de profesores que hay en ese departamento. El resultado sólo debe incluir los departamentos que tienen profesores asociados y deberá estar ordenado de mayor a menor por el número de profesores.

     ```sql
    SELECT nombre, COUNT(nombre) FROM departamento de
    INNER JOIN profesor pr ON de.id = pr.id_departamento
    GROUP BY nombre
    ORDER BY COUNT(nombre) DESC;
     ```

20. Devuelve un listado con todos los departamentos y el número de profesores que hay en cada uno de ellos. Tenga en cuenta que pueden existir departamentos que no tienen profesores asociados. Estos departamentos también tienen que aparecer en el listado.

     ```sql
    SELECT COUNT(id_profesor) FROM departamento de
    LEFT JOIN profesor pr ON de.id = pr.id_departamento
    GROUP BY(nombre);
     ```

21. Devuelve un listado con el nombre de todos los grados existentes en la base de datos y el número de asignaturas que tiene cada uno. Tenga en cuenta que pueden existir grados que no tienen asignaturas asociadas. Estos grados también tienen que aparecer en el listado. El resultado deberá estar ordenado de mayor a menor por el número de asignaturas.

     ```sql
    SELECT gr.nombre, COUNT(a.id) AS Numero_asignaturas FROM grado gr
    LEFT JOIN asignatura a ON gr.id = a.id_grado
    GROUP BY gr.nombre
    ORDER BY Numero_asignaturas DESC;
     ```

22. Devuelve un listado con el nombre de todos los grados existentes en la base de datos y el número de asignaturas que tiene cada uno, de los grados que tengan más de `40` asignaturas asociadas.

     ```sql
    SELECT gr.nombre, COUNT(a.id) AS Numero_asignaturas FROM grado gr
    LEFT JOIN asignatura a ON gr.id = a.id_grado
    GROUP BY gr.nombre
    HAVING Numero_asignaturas > 40
    ORDER BY Numero_asignaturas DESC;
     ```

23. Devuelve un listado que muestre el nombre de los grados y la suma del número total de créditos que hay para cada tipo de asignatura. El resultado debe tener tres columnas: nombre del grado, tipo de asignatura y la suma de los créditos de todas las asignaturas que hay de ese tipo. Ordene el resultado de mayor a menor por el número total de crédidos.

     ```sql
    SELECT gr.nombre, tipo, sum(creditos) AS total_creditos FROM grado gr
    INNER JOIN asignatura a ON gr.id = a.id_grado
    GROUP BY gr.nombre, a.tipo
    ORDER BY total_creditos DESC;
     ```

24. Devuelve un listado que muestre cuántos alumnos se han matriculado de alguna asignatura en cada uno de los cursos escolares. El resultado deberá mostrar dos columnas, una columna con el año de inicio del curso escolar y otra con el número de alumnos matriculados.

     ```sql
    SELECT ce.anyo_inicio, COUNT(am.id_alumno) FROM alumno_se_matricula_asignatura am
    INNER JOIN curso_escolar ce ON am.id_curso_escolar = ce.id
    GROUP BY ce.id;
     ```

25. Devuelve un listado con el número de asignaturas que imparte cada profesor. El listado debe tener en cuenta aquellos profesores que no imparten ninguna asignatura. El resultado mostrará cinco columnas: id, nombre, primer apellido, segundo apellido y número de asignaturas. El resultado estará ordenado de mayor a menor por el número de asignaturas.

     ```sql
    SELECT pr.id_profesor, pe.nombre, pe.apellido1, pe.apellido2, COUNT(a.id) AS asignaturas_que_imparte FROM asignatura a
    INNER JOIN profesor pr ON a.id_profesor = pr.id_profesor
    INNER JOIN persona pe ON pr.id_profesor = pe.id
    GROUP BY pr.id_profesor;
     ```

26. Devuelve todos los datos del alumno más joven.

     ```sql
    SELECT * FROM persona
    WHERE tipo = 'alumno'
    ORDER BY fecha_nacimiento DESC
    LIMIT 1;
     ```

27. Devuelve un listado con los profesores que no están asociados a un departamento.

     ```sql
    SELECT * FROM persona pe 
    LEFT JOIN profesor pr ON pe.id = pr.id_profesor 
    WHERE tipo = 'profesor' and pr.id_departamento IS NULL;
     ```

28. Devuelve un listado con los departamentos que no tienen profesores asociados.

     ```sql
    SELECT id, nombre FROM departamento de
    LEFT JOIN profesor pr ON de.id = pr.id_departamento
    WHERE id_profesor is NULL;
     ```

29. Devuelve un listado con los profesores que tienen un departamento asociado y que no imparten ninguna asignatura.

     ```sql
    SELECT pr.id_profesor, de.nombre FROM departamento de
    INNER JOIN profesor pr ON de.id = pr.id_departamento
    LEFT JOIN asignatura a ON pr.id_profesor = a.id_profesor
    WHERE a.id IS NULL
    ORDER BY id_profesor;
     ```

30. Devuelve un listado con las asignaturas que no tienen un profesor asignado.

     ```sql
    SELECT id, nombre FROM asignatura
    WHERE id_profesor IS NULL;
     ```

31. Devuelve un listado con todos los departamentos que no han impartido asignaturas en ningún curso escolar.

     ```sql
    SELECT DISTINCT de.id, de.nombre FROM departamento de
    LEFT JOIN profesor pr ON de.id = pr.id_departamento
    LEFT JOIN asignatura a ON pr.id_profesor = a.id_profesor
    LEFT JOIN alumno_se_matricula_asignatura am ON a.id= am.id_asignatura
    WHERE am.id_curso_escolar IS NULL AND a.id IS NULL;
     ```