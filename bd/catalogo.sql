USE huellas_a_casa;
SELECT * FROM mascotas;

SELECT * FROM mascotas WHERE id=2;
SELECT * FROM mascotas WHERE id=3;
SELECT * FROM mascotas WHERE id=5;

SELECT * FROM mascotas WHERE edad<=2 AND peso BETWEEN 2 AND 10 AND genero="Hembra";

UPDATE mascotas SET nombre="Cleo", edad=5, peso=4.5, personalidad="Independiente y afectuosa", descripcion="Blanca con manchas grises en el", castrado=1, genero="Macho" WHERE id="5";