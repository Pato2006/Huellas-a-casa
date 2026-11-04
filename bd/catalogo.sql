USE huellas_a_casa;
SELECT * FROM mascotas;

SELECT * FROM mascotas WHERE id=2;
SELECT * FROM mascotas WHERE id=3;
SELECT * FROM mascotas WHERE id=5;

SELECT * FROM mascotas WHERE edad<=2 AND peso BETWEEN 2 AND 10 AND genero="Hembra";

UPDATE mascotas SET edad=5, peso=4.5, genero="Macho" WHERE id="5";

SELECT * FROM mascotas WHERE tipo="Perro" AND genero="Macho";

SELECT * FROM mascotas WHERE tipo="Gato" AND castrado=0;

SELECT * FROM mascotas WHERE edad>=5 AND peso>10;

SELECT * FROM mascotas WHERE personalidad LIKE "%juguetona%";

SELECT nombre, edad, tipo, genero, ruta_img FROM mascotas ORDER BY edad ASC;

SELECT * FROM mascotas
WHERE id NOT IN (SELECT mascota_id FROM adopciones WHERE estado="Aceptado");

UPDATE mascotas SET castrado=1 WHERE id=4;

UPDATE mascotas SET peso=13.2, edad=4 WHERE id=1;