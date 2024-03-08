/*1) Consultas sobre una tabla*/
/*1*/
SELECT * FROM pedido
ORDER BY fecha DESC;

/*2*/
SELECT * FROM pedido
ORDER BY total DESC
LIMIT 2;

/*3*/
SELECT DISTINCT id_cliente FROM pedido;

/*4*/
SELECT * FROM pedido
WHERE EXTRACT(YEAR FROM fecha) = 2017 AND total > 500;

/*5*/
SELECT nombre, apellido1, apellido2, comision FROM comercial
WHERE comision >= 0.05 AND comision <= 0.11;

/*6*/
SELECT MAX(comision) FROM comercial;

/*7*/
SELECT id, nombre, apellido1 FROM cliente
WHERE apellido2 IS NOT NULL
ORDER BY apellido1, apellido2, nombre;

/*8*/
SELECT nombre FROM cliente
WHERE nombre LIKE 'A%n' OR nombre LIKE 'P%'
ORDER BY nombre;

/*9*/
SELECT nombre FROM cliente
WHERE nombre NOT LIKE 'A%'
ORDER BY nombre;

/*10*/
SELECT DISTINCT nombre FROM comercial
WHERE nombre LIKE '%el' OR nombre LIKE '%o';

/*2) Consultas multitabla (Composición interna)*/
/*1*/
SELECT DISTINCT cl.id, cl.nombre, cl.apellido1, cl.apellido2 FROM pedido pe
JOIN cliente cl ON cl.id = pe.id_cliente;

/*2*/
SELECT * FROM cliente cl
JOIN pedido pe ON cl.id = pe.id_cliente
ORDER BY cl.nombre;

/*3*/
SELECT * FROM pedido pe
JOIN comercial co ON pe.id_comercial = co.id
ORDER BY co.nombre, co.apellido1, co.apellido2;

/*4*/
SELECT * FROM cliente cl
JOIN pedido pe ON cl.id = pe.id_cliente
JOIN comercial co ON pe.id_comercial = co.id
ORDER BY cl.nombre;

/*5*/
SELECT cl.nombre, cl.apellido1 FROM pedido pe
JOIN cliente cl ON cl.id = pe.id_cliente
WHERE EXTRACT(YEAR FROM pe.fecha) = 2017 AND total >= 300 AND total <= 1000;

/*6*/
SELECT DISTINCT co.nombre, co.apellido1, co.apellido2 FROM pedido pe
JOIN cliente cl ON cl.id = pe.id_cliente
JOIN comercial co ON co.id = pe.id_comercial
WHERE cl.nombre = 'María' AND cl.apellido1 = 'Santana' AND cl.apellido2 = 'Moreno';

/*7*/
SELECT DISTINCT cl.nombre, cl.apellido1, cl.apellido2 FROM pedido pe
JOIN cliente cl ON cl.id = pe.id_cliente
JOIN comercial co ON co.id = pe.id_comercial
WHERE co.nombre = 'Daniel' AND co.apellido1 = 'Sáez' AND co.apellido2 = 'Vega';

/*3) Consultas multitabla (Composición externa)*/
/*1*/
SELECT DISTINCT cl.apellido1, cl.apellido2, cl.nombre, pe.* FROM cliente cl
LEFT JOIN pedido pe ON pe.id_cliente = cl.id
ORDER BY cl.apellido1, cl.apellido2, cl.nombre;

/*2*/
SELECT DISTINCT co.apellido1, co.apellido2, co.nombre, pe.* FROM comercial co
LEFT JOIN pedido pe ON pe.id_comercial = co.id
ORDER BY co.apellido1, co.apellido2, co.nombre;

/*3*/
SELECT * FROM cliente cl
LEFT JOIN pedido pe ON pe.id_cliente = cl.id
WHERE pe.id IS NULL;

/*4*/
SELECT * FROM comercial co
LEFT JOIN pedido pe ON pe.id_comercial = co.id
WHERE pe.id IS NULL;

/*5*/
SELECT 'Cliente' AS tipo, cl.nombre, cl.apellido1, cl.apellido2
FROM cliente cl
LEFT JOIN pedido pe ON cl.id = pe.id_cliente
WHERE pe.id IS NULL

UNION ALL

SELECT 'Comercial' AS tipo, co.nombre, co.apellido1, co.apellido2
FROM comercial co
LEFT JOIN pedido pe ON co.id = pe.id_comercial
WHERE pe.id IS NULL
ORDER BY apellido1, apellido2, nombre;

/*6*/
/*Lo que hacen los natural es enlazar directamento dos tablas por el nombre de sus 
columnas, considero que se pueden usar en algunas pero en otras darian resultados
innesperados asi que considero que es mejor no usarlos.

/*4) Consultas resumen*/
/*1*/
SELECT SUM(total) AS cantidad_total_pedidos FROM pedido;

/*2*/
SELECT AVG(total) AS media_pedidos FROM pedido;

/*3*/
SELECT COUNT(DISTINCT id_comercial) AS numero_comerciales FROM pedido;

/*4*/
SELECT COUNT(id) AS numero_clientes FROM cliente;

/*5*/
SELECT MAX(total) AS mayor_cantidad FROM pedido;

/*6*/
SELECT MIN(total) AS mayor_cantidad FROM pedido;

/*7*/
SELECT ciudad, MAX(categoria) FROM cliente
GROUP BY ciudad;

/*8*/
SELECT id_cliente, nombre, apellido1, apellido2, fecha, total
FROM (
    SELECT 
        id_cliente,
        nombre,
        apellido1,
        apellido2,
        fecha,
        total,
        ROW_NUMBER() OVER (PARTITION BY id_cliente, fecha ORDER BY total DESC) AS rn
    FROM pedido
    JOIN cliente ON pedido.id_cliente = cliente.id
) AS ranked
WHERE rn = 1;

/*9*/


/*10*/


/*11*/


/*12*/


/*13*/


/*14*/


/*15*/


/*5) Con operadores básicos de comparación*/
/*1*/


/*2*/


/*3*/


/*4*/


/*5*/


/*6) Subconsultas con ALL y ANY*/
/*1*/


/*2*/


/*3*/


/*7) Subconsultas con IN y NOT IN*/
/*1*/


/*2*/


/*8) Subconsultas con EXISTS y NOT EXISTS*/
/*1*/


/*2*/
