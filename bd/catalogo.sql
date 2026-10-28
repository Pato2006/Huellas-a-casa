USE huellas_a_casa;

-- Catalogo usuario (catalogo.html)
SELECT id, nombre, ruta_img
FROM mascotas;

-- Catalogo admin (catalogo_admin.html)
-- estado: Adoptado si tiene una adopcion Aceptada
SELECT mascotas.id, mascotas.nombre, mascotas.ruta_img, IF(adopciones.id IS NULL, 'En adopción', 'Adoptado') AS estado
FROM mascotas
LEFT JOIN adopciones
ON adopciones.mascota_id = mascotas.id AND adopciones.estado = 'Aceptado';

-- Catalogo usuario con filtros (ejemplo)
-- Edad 0-4: edad < 4 | Tamaño mediano: peso entre 10 y 25
SELECT id, nombre, ruta_img
FROM mascotas
WHERE tipo = 'Perro' AND genero = 'Hembra' AND edad < 4 AND peso BETWEEN 10 AND 25 AND nombre LIKE '%lu%';

-- Catalogo admin con filtros (ejemplo)
SELECT mascotas.id, mascotas.nombre, mascotas.ruta_img, IF(adopciones.id IS NULL, 'En adopción', 'Adoptado') AS estado
FROM mascotas
LEFT JOIN adopciones
ON adopciones.mascota_id = mascotas.id AND adopciones.estado = 'Aceptado'
WHERE mascotas.tipo = 'Perro' AND mascotas.genero = 'Hembra' AND mascotas.edad < 4 AND mascotas.peso BETWEEN 10 AND 25 AND mascotas.nombre LIKE '%lu%';

-- Perro exacto usuario (detalle.html)
SELECT id, nombre, edad, peso, personalidad, descripcion, ruta_img
FROM mascotas
WHERE id = 5;

-- Perro exacto admin (detalle_modificar_admin.html)
SELECT mascotas.id, mascotas.nombre, mascotas.edad, mascotas.peso, mascotas.personalidad, mascotas.descripcion, mascotas.castrado, mascotas.tipo, mascotas.genero, mascotas.ruta_img, IF(adopciones.id IS NULL, 'En adopción', 'Adoptado') AS estado
FROM mascotas
LEFT JOIN adopciones
ON adopciones.mascota_id = mascotas.id AND adopciones.estado = 'Aceptado'
WHERE mascotas.id = 5;

-- Editar perro admin
-- castrado: si = 1, no = 0
UPDATE mascotas
SET nombre = 'Terry', edad = 5, peso = 18.5, personalidad = 'Cariñosa', descripcion = 'Buena con las personas', castrado = 1, tipo = 'Perro'
WHERE id = 5;